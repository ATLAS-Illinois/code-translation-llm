from llama_index import SimpleDirectoryReader, GPTListIndex

class DocumentationIndexer:
    def __init__(self, cpp_docs_path, python_docs_path):
        self.cpp_docs = SimpleDirectoryReader(cpp_docs_path).load_data()
        self.python_docs = SimpleDirectoryReader(python_docs_path).load_data()
        self.index = GPTListIndex(self.cpp_docs + self.python_docs)

    def retrieve_docs(self, query):
        return self.index.query(query)