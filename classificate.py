import numpy as np
from text_to_array import text_to_array

def classificate(text: str, perceptrons, languages):
    vector = text_to_array(text)
    vector_np = np.array(list(vector[0].values()))
    outputs = [p.compute(vector_np) for p in perceptrons]
    # print("outputs: " +str(outputs))
    # print(languages[np.argmax(outputs)])
    return languages[np.argmax(outputs)]