import numpy as np
from perceptron import Perceptron
import statistics

def train_perceptrons(languages, training_data, alpha=0.1, max_epochs=10000):
    perceptrons = []
    for l in languages:
        perceptrons.append(Perceptron(theta=0.05))


    for epoch in range(1, max_epochs+1):
        total_error = 0
        epoch_avg_list = []

        lang_avg_list = []
        for lang_idx, lang_examples in enumerate(training_data):
            # print(lang_idx, lang_examples)



            for example in lang_examples:
                # print("example: "+ str(example))
                avg_error = 0

                input_vector = np.array(list(example[0].values()))
                # print(input_vector)

                input_vector = input_vector / np.linalg.norm(input_vector)
                # print(input_vector)

                outputs = [p.compute(input_vector) for p in perceptrons]
                # print("outputs: " + str(outputs))

                targets = [-1] * len(languages)
                # print("targets: " + str(targets))
                targets[lang_idx] = 1
                # print("targets: " + str(targets))

                for p, target, output in zip(perceptrons, targets, outputs):
                    p.learn(input_vector, target, alpha)

                example_error = 0
                # print("\n--- Nowy przykład ---")
                # print(f"Oczekiwane wyjścia (targets): {targets}")
                # print(f"Rzeczywiste wyjścia (outputs): {outputs}")

                total_for_avg = 0
                counter = 0
                for i, (t, o) in enumerate(zip(targets, outputs)):
                    counter = i+1
                    difference = t - o
                    abs_difference = abs(difference)
                    example_error += abs_difference
                    total_for_avg += difference

                    # print(f"\nPerceptron {i} (język: {languages[i]}):")
                    # print(f"  Oczekiwano: {t}, Otrzymano: {o}")
                    # print(f"  Różnica: {t} - {o} = {difference}")
                    # print(f"  Błąd bezwzględny: |{difference}| = {abs_difference}")
                    # print(f"  Suma błędów po tym kroku: {example_error}")

                total_error += example_error
                avg_error = (avg_error + total_for_avg/counter)
                # print(counter)
                # print(avg_error)
                lang_avg_list.append(avg_error)
                # print(f"\nCałkowity błąd dla tego przykładu: {example_error}")
                # print(f"Suma wszystkich błędów (total_error): {total_error}")

            # print("lang_avg_list: " + str(lang_avg_list))
            # print("lang_avg: " + str(statistics.mean(lang_avg_list)))
            epoch_avg_list.append(statistics.mean(lang_avg_list))



        # avg_error = total_error / len(languages)*len(outputs)
        # print("epoch_avg_list: " + str(epoch_avg_list))
        # print("epoch_avg: " + str(statistics.mean(epoch_avg_list)))
        print("Epoch " + str(epoch) +", Avg error: "+ str(abs(statistics.mean(epoch_avg_list))))

        if abs(statistics.mean(epoch_avg_list)) < 0.01:
            print("Learning finished!")
            break

    return perceptrons