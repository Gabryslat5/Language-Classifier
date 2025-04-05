import os
from text_to_array import text_to_array

def load_data(file_path: str):
    with open(file_path, encoding='utf-8') as f:
        return [text_to_array(f.read())]