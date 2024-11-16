from llama_index import VectorStoreIndex, SimpleDirectoryReader
from embedder import CustomHFEmbedding
import markdown2

class DocumentationIndexer:
    def __init__(self, cpp_docs_path, python_docs_path):
        self.cpp_docs = self.load_and_process_docs(cpp_docs_path)
        self.python_docs = self.load_and_process_docs(python_docs_path)
        self.embedding_model = CustomHFEmbedding()

        self.index = VectorStoreIndex.from_documents(
            self.cpp_docs + self.python_docs,
            embed_model=self.embedding_model
        )
    
    def load_and_process_docs(self, path):
        docs = []
        reader = SimpleDirectoryReader(path, recursive=True)
        for doc in reader.load_data():
            if doc.file_name.endswith('.md'):
                doc.text = markdown2.markdown(doc.text, extras=["strip"])
            docs.append(doc)
        return docs

    def retrieve_docs(self, query):
        query_engine = self.index.as_query_engine()
        return query_engine.query(query)