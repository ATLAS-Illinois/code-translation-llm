# Code Translation LLM

## Overview

This project is a sophisticated code translation tool that leverages AI to translate C++ code to Python, utilizing advanced indexing and remote model generation techniques.

## Project Structure

```
.
├── backend/
│   ├── index_storage
│   ├── __init__.py
│   ├── indexer.py
│   ├── main.py
│   ├── model.py
│   ├── test_api.py
│   └── translate.py
├── data/
│   ├── cpp_docs
│   └── python_docs
├── .env
├── .gitignore
├── READMD.md
└── requirements.txt
```

## Components

### Backend Components

1. **indexer.py**: 
   - Manages document indexing using `llama_index`
   - Creates a vector store index for C++ and Python documentation
   - Supports document retrieval and indexing

2. **translate.py**:
   - Handles code translation from C++ to Python
   - Utilizes a remote model and documentation indexer
   - Generates translation prompts with specific guidelines

3. **model.py**:
   - Manages remote model interactions
   - Loads environment variables for authentication
   - Sends translation requests to a remote LLM service

4. **main.py**:
   - Demonstrates the translation workflow
   - Provides an example of translating C++ code to Python

## Key Features

- AI-powered code translation
- Vector-based document indexing
- Flexible translation system
- Support for C++ and Python documentation

## Prerequisites

- Python 3.8+
- Required libraries:
  - llama_index
  - requests
  - python-dotenv
  - huggingface transformers

## Setup and Installation

1. Clone the repository
2. Create a `.env` file with the following variables:
   ```
   LLM_URL=your_llm_service_url
   LLM_USERNAME=your_username
   LLM_PASSWORD=your_password
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage Example

```python
from translate import CodeTranslator

translator = CodeTranslator()
cpp_code = '''your C++ code here'''
python_code = translator.translate_cpp_to_python(cpp_code)
print(python_code)
```

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

Distributed under the MIT License. See `LICENSE` for more information.