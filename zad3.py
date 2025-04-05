import string

def calculate_letter(text):
    letter_counts = {letter: 0 for letter in string.ascii_lowercase}
    # print(letter_counts)
    total_letters = 0

    for char in text.lower():
        # print(char)
        if char in letter_counts:
            letter_counts[char] += 1
            total_letters += 1

    # frequencies = []
    # if total_letters > 0:
    #     for letter in string.ascii_lowercase]:
    #         frequencies.append(letter_counts[letter] / total_letters)
    #     else:


    if total_letters > 0:
        frequencies = [letter_counts[letter] / total_letters for letter in string.ascii_lowercase]
    else:
        frequencies = [0.0]

    return frequencies


def main():
    file_path = "tekst.txt"

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()

        # print(content)

        line = [p.strip() for p in content]

        print(line)


        full_text = ' '.join(line)
        # print(full_text)

        counter = calculate_letter(full_text)

        for letter, freq in zip(string.ascii_lowercase, counter):
            print(letter +": "+ str(freq))

    except FileNotFoundError:
        print("error")
    except Exception as e:
        print("error")


if __name__ == "__main__":
    main()