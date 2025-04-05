from collections import Counter
import numpy as np
import re


def text_to_array(text: str) -> list:
    text = re.sub(r'[^a-zA-Z]', '', text.lower())
    letter_counts = Counter(text)
    total_letters = sum(letter_counts.values())

    letter_frequencies = {}

    for i in range(ord('a'), ord('z') + 1):
        char = chr(i)
        count = letter_counts.get(char, 0)

        if total_letters > 0:
            frequency = count / total_letters
        else:
            frequency = 0

        letter_frequencies[char] = frequency

    return [letter_frequencies]