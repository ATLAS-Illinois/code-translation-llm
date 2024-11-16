from translate import CodeTranslator

def main():
    translator = CodeTranslator()
    cpp_code = "int add(int a, int b) { return a + b; }"

    python_translation = translator.translate_cpp_to_python(cpp_code)
    print("Python Translation:\n", python_translation)

if __name__ == "__main__":
    main()
