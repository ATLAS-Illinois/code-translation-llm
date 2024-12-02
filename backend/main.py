from translate import CodeTranslator

def main():
    translator = CodeTranslator()
    cpp_code = '''
    ```cpp
    #include <iostream>
    #include <memory> // For smart pointers

    class Animal {
    public:
        virtual void makeSound() const { 
            std::cout << "Some generic animal sound!" << std::endl; 
        }
        virtual ~Animal() = default; // Virtual destructor
    };

    class Dog : public Animal {
    public:
        void makeSound() const override { 
            std::cout << "Woof! Woof!" << std::endl; 
        }
    };

    class Cat : public Animal {
    public:
        void makeSound() const override { 
            std::cout << "Meow!" << std::endl; 
        }
    };

    int main() {
        std::unique_ptr<Animal> animal1 = std::make_unique<Dog>();
        std::unique_ptr<Animal> animal2 = std::make_unique<Cat>();

        animal1->makeSound(); // Polymorphic call
        animal2->makeSound(); // Polymorphic call

        return 0;
    }

    '''

    python_translation = translator.translate_cpp_to_python(cpp_code)
    print("Python Translation:\n", python_translation)

if __name__ == "__main__":
    main()
