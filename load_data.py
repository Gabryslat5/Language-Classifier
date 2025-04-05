import os
from text_to_array import text_to_array

def load_data(base_path: str):
    languages = []
    lang_dict = []
    for lang in os.listdir(base_path):
        # print(lang)
        lang_path = os.path.join(base_path, lang)
        if os.path.isdir(lang_path):
            languages.append(lang)
            text_dict = []
            for file in os.listdir(lang_path):
                with open(os.path.join(lang_path, file), encoding='utf-8') as f:
                    text_dict.append(text_to_array(f.read()))
            lang_dict.append(text_dict)
    # print("--- END TRAIN FILES ---")
    return languages, lang_dict