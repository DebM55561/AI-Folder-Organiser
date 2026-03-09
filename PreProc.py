import re
from pathlib import Path

import nltk
import torch
import torchvision.models as models
import torchvision.transforms as transforms
from PIL import Image
import numpy as np
from nltk.corpus import stopwords


class PreProc:
    def __init__(self, folder_path):
        # Download stopwords if not already present
        self.folder_path = folder_path
        self.base_model = models.resnet50(weights=models.ResNet50_Weights.DEFAULT)
        self.feature_extractor = torch.nn.Sequential(*list(self.base_model.children())[:-1])
        self.feature_extractor.eval()
        self.transform = transforms.Compose([transforms.Resize(256), transforms.CenterCrop(224), transforms.ToTensor(),
                                             transforms.Normalize((0.485, 0.456, 0.406), (0.229, 0.224, 0.225))])
        try:
            nltk.data.find('corpora/stopwords')
        except LookupError:
            nltk.download('stopwords')

        self.stopword_set = set(stopwords.words('english'))




    def  text_process(self, text):

        # Convert to lowercase
        text = str(text).lower()

        # Remove punctuation and special characters
        text = re.sub(r'[^\w\s]', ' ', text)

        # Remove numbers
        text = re.sub(r'\d+', '', text)

        # Tokenize and remove stopwords
        words = text.split()
        filtered_words = [w for w in words if w not in self.stopword_set]
        return " ".join(filtered_words)



    def get_vector(self, img):
        tensor = self.transform(img).unsqueeze(0)
        with torch.no_grad():
            vec = self.feature_extractor(tensor).flatten().numpy()
        return vec



    def preprocessing(self, data_list):
        """
        Processes a list of strings (filenames or file content).
        """
        processed_list = []

        for file in data_list:
            if isinstance(file, tuple):
                filename, img = file
                image_path = Path(self.folder_path)/filename
                image = Image.open(image_path).convert('RGB')
                transformed_image = self.get_vector(image)
                processed_list.append(str(transformed_image))

            if isinstance(file, str):
                clean_text = self.text_process(file)
                processed_list.append(clean_text)

        return processed_list
