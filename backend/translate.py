from model import RemoteModelLoader
from indexer import DocumentationIndexer

class CodeTranslator:
    def __init__(self):
        self.model_loader = RemoteModelLoader()
        self.indexer = DocumentationIndexer("../data/cpp_docs", "../data/python_docs")

    def create_system_prompt(self):
        return """
            
            You are a code translation assistant. Your only task is to translate C++ code into Python code.
            IMPORTANT RULES:
            - Output ONLY the translated Python code
            - Do not include any explanations
            - Do not include any comments unless they were present in the original code
            - Do not include code fence markers (```)
            - Do not include any text before or after the code
            - Preserve the original indentation style where possible
            - Maintain any existing comments from the source code
            - If the code cannot be translated, output only 'TRANSLATION_ERROR'
            
            """


    def translate_cpp_to_python(self, cpp_code):
        docs = self.indexer.retrieve_docs(f"Translate this C++ code to Python: {cpp_code}")
        system_prompt = self.create_system_prompt()

        prompt = f"{system_prompt}\n\n{docs}\n\nTranslate the following C++ code to Python:\n{cpp_code}"
        
        python_code = self.model_loader.generate_code(prompt)
        return python_code