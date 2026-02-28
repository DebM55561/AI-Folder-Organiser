# AI-Folder-Organiser

An intelligent desktop application that uses **Natural Language Processing (NLP)** and **Machine Learning** to automatically sort unorganized files into meaningful clusters based on their actual content.

---

## Project Structure

| File | Description |
| :--- | :--- |
| **`front.py`** | The **Tkinter GUI**; the main entry point for the application. |
| **`filemanager.py`** | Handles local I/O, file discovery, and text extraction logic for `.txt` and `.pdf` files. |
| **`model.py`** | The AI engine; handles **embeddings**, **PCA reduction**, and **K-Means clustering**. |
| **`PreProc.py`** | Cleans text by removing stop words, numbers, and special characters. |
| **`folderscript.py`** | A utility to generate hundreds of themed test files (Legal, School, Office, etc.). |
| **`main.py`** | A CLI-based script for testing backend logic without the GUI. |

---

## Getting Started

### 1. Install Dependencies
Ensure you have Python installed, then run the following command to install the required libraries:

```bash
pip install nltk spacy scikit-learn sentence-transformers PyMuPDF reportlab python-docx joblib
```
### 2. How to run

```bash
python front.py

