from pathlib import Path
import joblib
from fs.path import combine
from sklearn.cluster import KMeans
from sentence_transformers import SentenceTransformer
from sklearn.decomposition import PCA
from torch.nn.functional import embedding
import numpy as np


class ModelHandler:
    def __init__(self, model_path):
        self.model_path = Path(model_path)
        # pca_path = self.model_path/"pca_model.pkl"
        self.pca_path = self.model_path / "pca_model.joblib"
        self.kmeans_path = self.model_path / "kmeans_model.joblib"
        self.data = None
        self.kmeans_obj = None
        self.pca_obj = None
        self.max_comp = 10

    def save_model(self):
        if self.pca_obj and self.kmeans_obj:
            joblib.dump(self.pca_obj, self.pca_path)
            joblib.dump(self.kmeans_obj, self.kmeans_path)
            print("Model Saved Successfully")
        else:
            print("No model objects found to save.")

    def filemodel(self):
        if not self.data or len(self.data) == 0:
            return []

        emb = self.data

        # PCA Reduction (ensure components <= samples)
        n_comp = min(len(self.data), self.max_comp)

        if not self.pca_obj:
            self.pca_obj = PCA(n_components=n_comp)
            print("pca created")
            x_reduced = self.pca_obj.fit_transform(emb)
        else:
            x_reduced = self.pca_obj.transform(emb)

        # KMeans Clustering (ensure clusters <= samples)
        n_clust = min(len(self.data), 5)
        if  not self.kmeans_obj:
            self.kmeans_obj = KMeans(n_clusters=n_clust, n_init='auto')
            print("kmeans created")
            clusters = self.kmeans_obj.fit_predict(x_reduced)
        else:
            clusters = self.kmeans_obj.predict(x_reduced)

        return clusters
