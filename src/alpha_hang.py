import numpy as np
from node import *

ALPHABET_NUM = 26

INPUT = 0
CONV = 1
POOLING = 2
HIDDEN = 3
OUTPUT = 5


class AlphaHang():
    def __init__(self):
        self.nodes = [[] for x in range(OUTPUT + 1)]

        self.nodes[INPUT].append(Node(None, "CUR_WORD"))
        self.nodes[INPUT].append(Node(None, "FAIL_ALPHABETS"))

        self.nodes[CONV].append(Node(None, "CONV_CUR_WORD"))

        self.nodes[POOLING].append(Node(None, "POOL_CUR_WORD"))

        for i in range(0, OUTPUT - HIDDEN):
            for j in range(0, 3):
                self.nodes[HIDDEN + i].append(Node(None, "HIDDEN_" + str(i) + "-" + str(j)))

        self.nodes[OUTPUT].append(Node(None, "OUTPUT"))

        # connect nodes
        self.getNodeByName('CUR_WORD').outputs = self.getNodeByName('CONV_CUR_WORD')
        self.getNodeByName('CONV_CUR_WORD').outputs = self.getNodeByName('POOL_CUR_WORD')
        self.getNodeByName('POOL_CUR_WORD').outputs = self.nodes[HIDDEN]

        self.getNodeByName('FAIL_ALPHABETS').outputs = self.nodes[HIDDEN]

        for i in range(OUTPUT - HIDDEN):
            for j in range(len(self.nodes[HIDDEN + i])):
                self.nodes[HIDDEN + i][j].outputs = self.nodes[HIDDEN + i + 1]

    def perceive(self, _cur_word, _fail_alphabets):
        self.getNodeByName('CUR_WORD').x = np.array(np.zeros((len(_cur_word), ALPHABET_NUM), dtype=float))

        self.getNodeByName('FAIL_ALPHABETS').x = np.array(np.zeros((1, ALPHABET_NUM), dtype=float))
        for i in _fail_alphabets:
            self.getNodeByName('FAIL_ALPHABETS').x[0, (ALPHABET_NUM - 1) - (ord('z') - ord(i))] = 1

        for i in range(len(_cur_word)):
            if _cur_word[i].isalpha():
                self.getNodeByName('CUR_WORD').x[i, (ALPHABET_NUM - 1) - (ord('z') - ord(_cur_word[i]))] = 1

    def getNodeByName(self, _name):
        for i in range(len(self.nodes)):
            for j in range(len(self.nodes[i])):
                if self.nodes[i][j].name == _name:
                    return self.nodes[i][j]

        print('No node named: ' + _name)
