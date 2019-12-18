import numpy as np


class Layer(object):  # fully connected Layer
    def __init__(self, _node_num, _name):
        self.x = np.zeros((_node_num, 26), dtype=float)
        self.w = np.zeros((_node_num, 26), dtype=float)
        self.b = np.zeros((_node_num, 26), dtype=float)

        self.name = _name

    def __str__(self):
        return 'Name: ' + self.name + '\nX: ' + str(self.x) + '\nW: ' + str(self.w) + '\nB: ' + str(self.b)

    def randWeightBias(self):
        self.w = np.random.randn(self.w.shape[0], self.w.shape[1])
        self.b = np.random.randn(self.b.shape[0], self.b.shape[1])
        #self.roundWeightBias()

    def roundWeightBias(self):
        for i in range(self.w.shape[0]):
            for j in range(self.w.shape[1]):
                self.w[i, j] = round(self.w[i, j], 5)
                self.b[i, j] = round(self.b[i, j], 5)