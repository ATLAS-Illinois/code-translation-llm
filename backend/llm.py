from translate import CodeTranslator

class LLMIntegration:
    def __init__(self):
        self.translator = CodeTranslator()

    def translate_code_with_retrieval(self, cpp_code):
        return self.translator.translate_cpp_to_python(cpp_code)
