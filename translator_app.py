import PySimpleGUI as sg
from transformers import MarianMTModel, MarianTokenizer
import asyncio
import logging

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Dictionary to hold models and tokenizers for each language pair
models = {}
tokenizers = {}

# List of available language pairs
language_pairs = {
    'English to Albanian': 'Helsinki-NLP/opus-mt-en-sq',
    'English to Arabic': 'Helsinki-NLP/opus-mt-en-ar',
    'English to Armenian': 'Helsinki-NLP/opus-mt-en-hy',
    'English to Azerbaijani': 'Helsinki-NLP/opus-mt-en-az',
    'English to Bulgarian': 'Helsinki-NLP/opus-mt-en-bg',
    'English to Chinese': 'Helsinki-NLP/opus-mt-en-zh',
    'English to Czech': 'Helsinki-NLP/opus-mt-en-cs',
    'English to Danish': 'Helsinki-NLP/opus-mt-en-da',
    'English to Dutch': 'Helsinki-NLP/opus-mt-en-nl',
    'English to Filipino': 'Helsinki-NLP/opus-mt-en-tl',
    'English to Finnish': 'Helsinki-NLP/opus-mt-en-fi',
    'English to French': 'Helsinki-NLP/opus-mt-en-fr',
    'English to German': 'Helsinki-NLP/opus-mt-en-de',
    'English to Greek': 'Helsinki-NLP/opus-mt-en-el',
    'English to Hindi': 'Helsinki-NLP/opus-mt-en-hi',
    'English to Hungarian': 'Helsinki-NLP/opus-mt-en-hu',
    'English to Icelandic': 'Helsinki-NLP/opus-mt-en-is',
    'English to Indonesian': 'Helsinki-NLP/opus-mt-en-id',
    'English to Irish': 'Helsinki-NLP/opus-mt-en-ga',
    'English to Italian': 'Helsinki-NLP/opus-mt-en-it',
    'English to Kinyarwanda': 'Helsinki-NLP/opus-mt-en-rw',
    'English to Konkani': 'Helsinki-NLP/opus-mt-en-gom',
    'English to Lingala': 'Helsinki-NLP/opus-mt-en-ln',
    'English to Macedonian': 'Helsinki-NLP/opus-mt-en-mk',
    'English to Maltese': 'Helsinki-NLP/opus-mt-en-mt',
    'English to Romanian': 'Helsinki-NLP/opus-mt-en-ro',
    'English to Russian': 'Helsinki-NLP/opus-mt-en-ru',
    'English to Spanish': 'Helsinki-NLP/opus-mt-en-es',
    'English to Swedish': 'Helsinki-NLP/opus-mt-en-sv',
    'English to Ukrainian': 'Helsinki-NLP/opus-mt-en-uk',
    'English to Vietnamese': 'Helsinki-NLP/opus-mt-en-vi',
    'English to Welsh': 'Helsinki-NLP/opus-mt-en-cy',
    'English to Xhosa': 'Helsinki-NLP/opus-mt-en-xh',
    'Albanian to English': 'Helsinki-NLP/opus-mt-sq-en',
    'Arabic to English': 'Helsinki-NLP/opus-mt-ar-en',
    'Armenian to English': 'Helsinki-NLP/opus-mt-hy-en',
    'Azerbaijani to English': 'Helsinki-NLP/opus-mt-az-en',
    'French to English': 'Helsinki-NLP/opus-mt-fr-en',
    'Spanish to English': 'Helsinki-NLP/opus-mt-es-en',
    'Italian to English': 'Helsinki-NLP/opus-mt-it-en',
    'German to English': 'Helsinki-NLP/opus-mt-de-en',
    'Chinese to English': 'Helsinki-NLP/opus-mt-zh-en',
    'Greek to English': 'Helsinki-NLP/opus-mt-el-en',
    # Add more pairs as needed
}

# Load models and tokenizers on demand
async def load_model_and_tokenizer(pair, model_name):
    try:
        tokenizers[pair] = MarianTokenizer.from_pretrained(model_name)
        models[pair] = MarianMTModel.from_pretrained(model_name)
        logging.info(f"Successfully loaded model and tokenizer for {pair}")
    except Exception as e:
        logging.error(f"Failed to load model {model_name}: {str(e)}")

def translate_text(text, source_language, target_language):
    try:
        language_pair = f"{source_language} to {target_language}"
        if language_pair not in models:
            raise ValueError("Model not loaded")

        tokenizer = tokenizers[language_pair]
        model = models[language_pair]

        tokenized_text = tokenizer([text], return_tensors='pt', padding=True)
        translation = model.generate(**tokenized_text)
        translated_text = tokenizer.batch_decode(translation, skip_special_tokens=True)[0]

        return translated_text

    except KeyError:
        return "Translation not supported for the selected language pair."
    except Exception as e:
        logging.error(f"Error during translation: {str(e)}")
        return f"Error during translation: {str(e)}"

async def translate_gui():
    sg.theme('DarkBlue3')

    layout = [
        [sg.Text('Select source language'), sg.Combo(
            ['English', 'French', 'Spanish', 'Italian', 'German', 'Chinese', 'Greek', 'Arabic', 'Azerbaijani', 'Hindi', 'Irish', 'Russian', 'Bulgarian', 'Danish', 'Dutch', 'Filipino', 'Indonesian', 'Hungarian', 'Icelandic', 'Macedonian', 'Romanian', 'Swedish', 'Albanian', 'Armenian', 'Czech', 'Finnish', 'Kinyarwanda', 'Konkani', 'Lingala', 'Maltese', 'Ukrainian', 'Welsh', 'Xhosa', 'Vietnamese'], default_value='English', key='source_language')],
        [sg.Text('Select target language'), sg.Combo(
            ['French', 'Spanish', 'Italian', 'German', 'English', 'Chinese', 'Greek', 'Arabic', 'Azerbaijani', 'Hindi', 'Irish', 'Russian', 'Bulgarian', 'Danish', 'Dutch', 'Filipino', 'Indonesian', 'Hungarian', 'Icelandic', 'Macedonian', 'Romanian', 'Swedish', 'Albanian', 'Armenian', 'Czech', 'Finnish', 'Kinyarwanda', 'Konkani', 'Lingala', 'Maltese', 'Ukrainian', 'Welsh', 'Xhosa', 'Vietnamese'], default_value='French', key='target_language')],
        [sg.Text('Enter text to translate')],
        [sg.Multiline(size=(50, 10), key='input_text')],
        [sg.Button('Translate')],
        [sg.Text('Translated text')],
        [sg.Multiline(size=(50, 10), key='output_text', disabled=True)]
    ]

    window = sg.Window('Translator App', layout)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        if event == 'Translate':
            input_text = values['input_text']
            source_language = values['source_language']
            target_language = values['target_language']
            language_pair = f"{source_language} to {target_language}"

            if language_pair not in models:
                await load_model_and_tokenizer(language_pair, language_pairs[language_pair])

            translated_text = translate_text(input_text, source_language, target_language)
            window['output_text'].update(translated_text)

    window.close()

if __name__ == '__main__':
    asyncio.run(translate_gui())




