import numpy as np

class Perceptron:
    def __init__(self, theta: float):
        self.theta = theta
        self.weights = np.random.rand(26)

    def compute(self, inputs: np.ndarray) -> float:
        net = sum(w * i for w, i in zip(self.weights, inputs))
        return max(-1, min(1, net / (1 + abs(net))))

    def learn(self, inputs: np.ndarray, right_decision: int, alpha: float) -> None:
        delta = right_decision - self.compute(inputs)
        self.weights = self.weights + alpha * delta * inputs
        # self.weights /= np.linalg.norm(self.weights)