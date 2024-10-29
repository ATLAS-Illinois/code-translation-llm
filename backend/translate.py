from hf_model import HFModelLoader
from indexer import DocumentationIndexer

class CodeTranslator:
    def __init__(self, model_name="Qwen/CodeQwen-7B-Chat"):
        self.model_loader = HFModelLoader(model_name)
        self.indexer = DocumentationIndexer("data/cpp_docs", "data/python_docs")

    def translate_cpp_to_python(self, cpp_code):
        docs = self.indexer.retrieve_docs(f"Translate this C++ code to Python: {cpp_code}")
    
        prompt = f"{docs}\n\nTranslate the following C++ code to Python:\n{cpp_code}"
        
        python_code = self.model_loader.generate_code(prompt)
        return python_code

if __name__ == "__main__":
    # translator = CodeTranslator()
    # cpp_code = "int add(int a, int b) { return a + b; }"  # Sample C++ code
    # python_translation = translator.translate_cpp_to_python(cpp_code)
    # print("Python Translation:\n", python_translation)
    print("Can add the translation items here")