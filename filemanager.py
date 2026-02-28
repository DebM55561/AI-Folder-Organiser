import shutil
from pathlib import Path
import fitz  # PyMuPDF


class Filemanager:
    def __init__(self, path, destination):
        self.path = Path(path)
        self.destination = Path(destination)
        self.fileList = []
        self.filesum = []

    def getFiles(self):
        """Retrieves a list of filenames from the source directory."""
        files = []
        # iterdir() allows us to check if each item is a file
        for f in self.path.iterdir():
            if f.is_file():
                files.append(f.name)
        self.fileList = files
        return self.fileList

    def moveFilesToCluster(self, clusterList, dryrun=False):
        """Moves files into subfolders named after their cluster ID."""
        for i in range(len(self.fileList)):
            folderID = clusterList[i]
            filename = self.fileList[i]

            # Define the destination subfolder
            clusterfolder = self.destination / f"{folderID}"

            if not dryrun:
                clusterfolder.mkdir(parents=True, exist_ok=True)

            sourcefile = self.path / filename
            destLoc = clusterfolder / filename

            if dryrun:
                print(f"DRY RUN: Moving {filename} to {destLoc}")
            else:
                shutil.move(sourcefile, destLoc)

    def getSummary(self):
        """Extracts the first 500 characters of text from supported files for AI processing."""
        self.filesum = []  # Reset the list to avoid duplicates on multiple calls

        for filename in self.fileList:
            # Create a full Path object for the specific file
            file_path = self.path / filename
            ext = file_path.suffix.lower()  # Correctly check the file's extension
            content = ""

            try:
                if ext == ".txt":
                    # errors='ignore' prevents crashes on non-UTF-8 characters
                    content = file_path.read_text(errors='ignore')[:500]

                elif ext == ".pdf":
                    with fitz.open(file_path) as doc:
                        if doc.page_count > 0:
                            # Extract text from the first page using PyMuPDF
                            content = doc[0].get_text()[:500]

                # Check if file was empty or unsupported
                if not content or content.strip() == "":
                    content = f"empty or binary file: {filename}"

                self.filesum.append(content)

            except Exception as e:
                print(f"Error reading {filename}: {e}")
                self.filesum.append(f"Error reading file content for {filename}")

        return self.filesum