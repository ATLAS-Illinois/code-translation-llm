from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, Settings
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
import logging


class DocumentationIndexer:
    def __init__(self, cpp_docs_path, python_docs_path):
        logging.basicConfig(level=logging.INFO)
        logging.info("Initializing DocumentationIndexer")
        Settings.llm = None
        Settings.embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-small-en-v1.5")

        self.cpp_docs = self.load_and_process_docs(cpp_docs_path)
        self.python_docs = self.load_and_process_docs(python_docs_path)
        self.index = None

    def load_and_process_docs(self, path):
        logging.info(f"Loading documents from {path}")
        reader = SimpleDirectoryReader(path, recursive=True)
        return reader.load_data()

    def create_index(self):
        logging.info("Creating the index")
        self.index = VectorStoreIndex.from_documents(self.cpp_docs + self.python_docs)
        self.index.storage_context.persist(persist_dir="./index_storage")
        logging.info("Index created and persisted to './index_storage'")

    def retrieve_docs(self, query):
        logging.info(f"Retrieving documents for query: {query}")
        if not self.index:
            raise ValueError("Index is not initialized. Call create_index() first.")
        query_engine = self.index.as_query_engine()
        return query_engine.query(query)