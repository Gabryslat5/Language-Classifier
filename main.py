from classificate import classificate
from load_data import load_data
from train_perceptrons import train_perceptrons
from test import test
from tkinter import *

if __name__ == "__main__":

    print("Hello from Jan B.")
    train_path = "texts"
    test_path = "texts_test"
    languages, training_data = load_data(train_path)
    print(training_data)
    perceptrons = train_perceptrons(languages, training_data)
    test(test_path, perceptrons, languages)

    # while True:
    #     text = input("Enter text to classify: ")
    #     if text.lower() == 'q!':
    #         break
    #     print("Language:", classificate(text, perceptrons, languages))

    def classify_text():
        text = text_input.get("1.0", "end-1c")
        if text.strip():
            language = classificate(text, perceptrons, languages)
            result_label.config(text=f"Language: {language}")
        else:
            result_label.config(text="Please enter some text")

    root = Tk()
    root.title("Language Classifier")
    root.geometry("450x380")

    instruction_label = Label(root, text="Enter text to classify:", font=('Arial', 12))
    instruction_label.pack(pady=10)

    text_input = Text(root, height=10, width=50, font=('Arial', 11))
    text_input.pack(pady=10)

    classify_button = Button(root, text="Classify", command=classify_text, font=('Arial', 12))
    classify_button.pack(pady=5)

    result_label = Label(root, text="Language: ", font=('Arial', 12, 'bold'))
    result_label.pack(pady=10)

    exit_button = Button(root, text="Exit", command=root.quit, font=('Arial', 12))
    exit_button.pack(pady=5)

    root.mainloop()