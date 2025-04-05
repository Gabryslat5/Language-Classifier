import os
from classificate import classificate

def test(test_path, perceptrons, languages):
    correct = 0
    total = 0
    for lang in os.listdir(test_path):
        lang_path = os.path.join(test_path, lang)
        if os.path.isdir(lang_path):
            for filename in os.listdir(lang_path):
                with open(os.path.join(lang_path, filename), 'r', encoding='utf-8') as f:
                    predicted_lang = classificate(f.read(), perceptrons, languages)
                    if predicted_lang == lang:
                        correct += 1
                    total += 1
    accuracy = correct / total * 100
    print("Good answers: " + str(correct))
    print("Bad answers: " + str(total - correct))
    print("Accuracy: " + str(accuracy)+"%")