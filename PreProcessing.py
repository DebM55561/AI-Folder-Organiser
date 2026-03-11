import torch
from PIL import Image
from sentence_transformers import SentenceTransformer
from pathlib import Path


class PreProcessing:
    def __init__(self, source_path):
        self.source_path = Path(source_path)
        # CLIP-ViT-B-32 outputs 512-dimensional embeddings
        self.base_model = SentenceTransformer('clip-ViT-B-32')
        self.embedding_dim = 512

    def processing_files(self, item_list, batch_size=32):
        """
        Processes a mixed list of text and image filenames efficiently using batching.
        """
        texts = []
        text_indices = []
        images = []
        image_indices = []
        failed_indices = []

        # 1. Categorize and prepare all items
        for i, item in enumerate(item_list):
            try:
                is_image = False
                if isinstance(item, str) and len(item) < 255:
                    file = self.source_path / item
                    # Safely check if it's a valid image file
                    if file.is_file() and file.suffix.lower() in [".jpg", ".jpeg", ".png"]:
                        img = Image.open(file).convert('RGB')
                        images.append(img)
                        image_indices.append(i)
                        is_image = True

                # If it wasn't successfully flagged as an image, treat it as text
                if not is_image:
                    texts.append(str(item))
                    text_indices.append(i)

            except Exception as e:
                print(f"Error preparing item '{item}': {e}")
                failed_indices.append(i)

        # Create an empty list of the correct size to hold our results in order
        processed_items = [None] * len(item_list)

        # 2. Batch encode texts (if any exist)
        if texts:
            try:
                text_embeddings = self.base_model.encode(texts, batch_size=batch_size, show_progress_bar=False)
                for idx, emb in zip(text_indices, text_embeddings):
                    processed_items[idx] = emb
            except Exception as e:
                print(f"Error during text batch encoding: {e}")
                # Fallback to zero vectors if the whole batch fails
                for idx in text_indices:
                    processed_items[idx] = torch.zeros(self.embedding_dim).numpy()

        # 3. Batch encode images (if any exist)
        if images:
            try:
                image_embeddings = self.base_model.encode(images, batch_size=batch_size, show_progress_bar=False)
                for idx, emb in zip(image_indices, image_embeddings):
                    processed_items[idx] = emb
            except Exception as e:
                print(f"Error during image batch encoding: {e}")
                for idx in image_indices:
                    processed_items[idx] = torch.zeros(self.embedding_dim).numpy()
            finally:
                # Free memory by closing PIL images after encoding
                for img in images:
                    img.close()

        # 4. Fill in any failed items with zero vectors
        for idx in failed_indices:
            processed_items[idx] = torch.zeros(self.embedding_dim).numpy()

        return processed_items
