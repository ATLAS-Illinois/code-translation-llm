from llama_index.core.embeddings import BaseEmbedding
from model import RemoteModelLoader

class CustomHFEmbedding(BaseEmbedding):
    def __init__(self):
        self.model_loader = RemoteModelLoader()

    def get_text_embedding(self, text: str) -> list[float]:
        return self.model_loader.get_embeddings(text)

    def get_query_embedding(self, query: str) -> list[float]:
        return self.model_loader.get_embeddings(query)