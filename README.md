# Translator App
- This Python application allows users to translate text between various languages using pre-trained machine translation models from the Hugging Face's transformers library.
- It features a graphical user interface built with PySimpleGUI for ease of use.

## Features
- Supported Languages: Translates text between a wide range of languages including Albanian, Arabic, Armenian, Azerbaijani, Bulgarian, Chinese, Czech, Danish, Dutch, Filipino, Finnish, French, German, Greek, Hindi, Hungarian, Icelandic, Indonesian, Irish, Italian, Kinyarwanda, Konkani, Lingala, Macedonian, Maltese, Romanian, Russian, Spanish, Swedish, Ukrainian, Vietnamese, Welsh, and Xhosa.
- Graphical Interface: Provides a user-friendly interface for selecting source and target languages, entering text to translate, and displaying the translated output.
- On-Demand Model Loading: Models and tokenizers are loaded asynchronously on demand, ensuring efficient resource management.
- Error Handling: Handles errors gracefully, including cases where the requested translation pair is not supported by the loaded models.

## Requirements
- Python 3.7 or higher
- PySimpleGUI
- Transformers library from Hugging Face
- asyncio (for asynchronous operations)

### Installation
1. Clone the repository:
- git clone https://github.com/your/repository.git
- cd repository_name
3. Install dependencies: pip install -r requirements.txt
4. Run the application: python translator_app.py

### Notes
- Unsupported Languages: Turkish, Korean, Japanese, Bengali, Latvian, Norwegian, Persian, Thai, Polish, Lithuanian, Malay, Nepali, Turkmen, Kazakh, Kannada, Lao, Portuguese, Tamil, Tatar, Uzbek, Belarusian, Bosnian, Hawaiian, Georgian, Khmer, Latin, Maithili, Tajik, Telugu, Yoruba, and Zulu are currently not supported due to unavailable models or resources.
- Error Handling: If you encounter a "Model not loaded" error during translation, please ensure your internet connection is active and retry. Contact the developer for further assistance if the issue persists.
### Contributing
- Contributions are welcome! Please fork the repository and submit pull requests with your enhancements.
