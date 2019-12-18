import numpy as np
from layer import *
import math

ALPHABET_NUM = 26
MAX_LEN = 12


class AlphaHang():
    def __init__(self, _word_len):
        self.layers = [
            Layer(MAX_LEN + 1, 'Input'),
            Layer(MAX_LEN + 2, 'Hidden_0'),
            Layer(MAX_LEN + 2, 'Hidden_1'),
            Layer(MAX_LEN + 2, 'Hidden_1'),
            Layer(MAX_LEN + 2, 'Hidden_1'),
            Layer((MAX_LEN + 2) // 2, 'Hidden_4'),
            Layer((MAX_LEN + 2) // 2, 'Hidden_4'),
            Layer((MAX_LEN + 2) // 2, 'Hidden_4'),
            Layer((MAX_LEN + 2) // 2, 'Hidden_4'),
            Layer((MAX_LEN + 2) // 3, 'Hidden_4'),
            Layer((MAX_LEN + 2) // 3, 'Hidden_4'),
            Layer((MAX_LEN + 2) // 3, 'Hidden_4'),
            Layer((MAX_LEN + 2) // 3, 'Hidden_4'),
            Layer((MAX_LEN + 2) // 4, 'Hidden_6'),
            Layer((MAX_LEN + 2) // 4, 'Hidden_6'),
            Layer((MAX_LEN + 2) // 4, 'Hidden_6'),
            Layer((MAX_LEN + 2) // 4, 'Hidden_6'),
            Layer(1, 'Output')
        ]

    def perceive(self, _cur_word, _fail_alphabets):
        for i in range(MAX_LEN):
            if i < len(_cur_word) and _cur_word[i] != '_':
                self.getLayerByName('Input').x[i, ord(_cur_word[i]) - ord('a')] = 1

        for i in _fail_alphabets:
            self.getLayerByName('Input').x[self.getLayerByName('Input').x.shape[0] - 1, ord(i) - ord('a')] = 1

    def evaluate(self):
        for i in range(1, len(self.layers)):
            for j in range(self.layers[i].x.shape[0]):
                self.layers[i].x[j] = np.sum(self.layers[i].x * self.layers[i].w + self.layers[i].b, axis=0)

            self.layers[i].x = self.sigmoid(self.layers[i].x)

        # self.printLayers()
        # self.guess()

    def interpretOutput(self):
        percent = np.zeros(ALPHABET_NUM, dtype=float)
        sum = self.getLayerByName('Output').x.sum()

        for i in range(ALPHABET_NUM):
            percent[i] = self.getLayerByName('Output').x[0, i] / sum * 100

        return percent

    def guess(self, is_print=True):
        interp_output = self.interpretOutput()

        if is_print:
            str_perc = ''
            for i in range(len(interp_output)):
                str_perc += chr(ord('a') + i) + ': ' + str(round(interp_output[i], 2)) + '%, '

            print("AlphaHang Guessed: " + chr(ord('a') + interp_output.argmax()) + ' ---by ' + str(
                round(interp_output.max(), 5)) + '% ----------' + str_perc)

        return chr(ord('a') + interp_output.argmax())  # return guessed alphabet

    def getLayerByName(self, _name):
        for i in self.layers:
            if i.name == _name:
                return i

        print('No layer named ' + _name)
        return None

    def printLayers(self):
        for i in self.layers:
            print(i)

    def createGene(self):
        for i in self.layers:
            i.randWeightBias()

    def readGene(self):
        for i in range(len(self.layers)):
            self.layers[i].w = np.loadtxt('genes/gene_master_' + str(i) + 'w.txt')
            self.layers[i].b = np.loadtxt('genes/gene_master_' + str(i) + 'b.txt')

    def writeGene(self):
        for i in range(len(self.layers)):
            np.savetxt('genes/gene_master_' + str(i) + 'w.txt', self.layers[i].w)
            np.savetxt('genes/gene_master_' + str(i) + 'b.txt', self.layers[i].b)

    def relu(self, _ndarr):
        for i in range(_ndarr.shape[0]):
            for j in range(_ndarr.shape[1]):
                _ndarr[i, j] = np.maximum(0.0, _ndarr[i, j])
        return _ndarr

    def sigmoid(self, _x):
        _x = 1 / (1 + np.exp(-_x))
        return _x
