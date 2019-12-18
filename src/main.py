from alpha_hang import *
from word import *


class Manager(object):
    def __init__(self):
        self.generation = -1
        self.goal = 10000
        self.check = 100

        self.word = Word('words.txt')
        self.secret_word = ''

        self.alpha_list = []
        self.alpha = None

        self.cur_word = ''
        self.fail_alphabets = []

        self.words_gene = []
        self.fail_gene = []

        self.fitness = np.zeros(10, dtype=int)
        self.mutant_rate = 1

    def makeAlphaByFile(self):
        self.alpha = AlphaHang(self.secret_word)
        self.alpha.readGene()

        self.secret_word = self.word.randFromDB([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
        print('Secret: ' + self.secret_word)
        self.cur_word = ''.join(['_' for x in range(len(self.secret_word))])
        self.fail_alphabets = []

        for cnt in range(len(self.secret_word)):
            self.alpha.perceive(self.cur_word, self.fail_alphabets)
            self.alpha.evaluate()
            guessed = self.alpha.guess(True)

            if guessed in self.fail_alphabets or guessed in self.cur_word:
                self.fail_alphabets.append(guessed)
            elif guessed in self.secret_word:
                for j in range(len(self.secret_word)):
                    if self.secret_word[j] == guessed:
                        self.cur_word = self.cur_word[:j] + guessed + self.cur_word[j + 1:]
            else:
                self.fail_alphabets.append(guessed)

            print('Cur word: ' + self.cur_word)
            print('Failed: ' + ''.join(self.fail_alphabets))

    def makeGeneration(self):
        self.generation += 1

        self.secret_word = self.word.randFromDB([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

        if self.generation == self.goal:
            print('Secret Word: ' + self.secret_word)

        self.cur_word = ''.join(['_' for x in range(len(self.secret_word))])
        self.fail_alphabets = []

        for i in range(10):
            if self.generation == 0:
                self.alpha_list.append(AlphaHang(len(self.secret_word)))
                self.alpha_list[i].createGene()
            else:
                parents_index = self.getParentsIndex()
                self.alpha_list.append(
                    self.crossover([self.alpha_list[parents_index[0]], self.alpha_list[parents_index[1]]],
                                   len(self.secret_word)))
        if self.generation != 0:
            self.alpha_list = self.alpha_list[10:]

    def runGeneration(self):
        self.fitness = np.zeros(10, dtype=int)
        self.words_gene = []
        self.fail_gene = []

        for i in range(10):
            if self.generation == self.goal:
                print('Gene ' + str(i))

            self.cur_word = ''.join(['_' for x in range(len(self.secret_word))])
            self.fail_alphabets = []

            for cnt in range(len(self.secret_word)):
                self.alpha_list[i].perceive(self.cur_word, self.fail_alphabets)
                self.alpha_list[i].evaluate()
                guessed = self.alpha_list[i].guess(self.generation == self.goal)

                if (guessed in self.cur_word) or (guessed in self.fail_alphabets):
                    self.fitness[i] -= 10000
                elif guessed in self.secret_word:
                    for j in range(len(self.secret_word)):
                        if self.secret_word[j] == guessed:
                            self.cur_word = self.cur_word[:j] + guessed + self.cur_word[j + 1:]
                            self.fitness[i] += 100
                else:
                    self.fitness[i] -= 50
                    self.fail_alphabets.append(guessed)

            self.words_gene.append(self.cur_word)
            self.fail_gene.append(self.fail_alphabets)

    def getParentsIndex(self):
        rank = self.fitness.argsort()[::-1]

        return rank[0], rank[1]

    def crossover(self, _parents, _word_len):
        alpha_ret = AlphaHang(_word_len)

        for i in range(len(alpha_ret.layers)):
            row_point = np.random.randint(0, alpha_ret.layers[i].w.shape[0])
            col_point = np.random.randint(0, alpha_ret.layers[i].w.shape[1])

            w_0 = _parents[np.random.randint(0, 2)].layers[i].w[:row_point, :col_point]
            w_1 = _parents[np.random.randint(0, 2)].layers[i].w[:row_point, col_point:]
            w_2 = _parents[np.random.randint(0, 2)].layers[i].w[row_point:, :col_point]
            w_3 = _parents[np.random.randint(0, 2)].layers[i].w[row_point:, col_point:]

            b_0 = _parents[np.random.randint(0, 2)].layers[i].b[:row_point, :col_point]
            b_1 = _parents[np.random.randint(0, 2)].layers[i].b[:row_point, col_point:]
            b_2 = _parents[np.random.randint(0, 2)].layers[i].b[row_point:, :col_point]
            b_3 = _parents[np.random.randint(0, 2)].layers[i].b[row_point:, col_point:]

            alpha_ret.layers[i].w = np.concatenate(
                (np.concatenate((w_0, w_1), axis=1), np.concatenate((w_2, w_3), axis=1)), axis=0)
            alpha_ret.layers[i].b = np.concatenate(
                (np.concatenate((b_0, b_1), axis=1), np.concatenate((b_2, b_3), axis=1)), axis=0)

            alpha_ret.layers[i].w += np.random.rand() * self.mutant_rate * (1 if np.random.rand() > 0.5 else -1)
            alpha_ret.layers[i].b += np.random.rand() * self.mutant_rate * (1 if np.random.rand() > 0.5 else -1)

        return alpha_ret


mng = Manager()


max_fitness = -9999999
for i in range(mng.goal + 1):
    mng.makeGeneration()
    mng.runGeneration()
    if mng.generation % mng.check == 0:
        print('G' + str(mng.generation) + ' Best: ' + str(mng.fitness.max()) +
              ' Word: ' + mng.words_gene[mng.getParentsIndex()[0]] + ' Failed: ' + ''.join(mng.fail_gene[mng.getParentsIndex()[0]]))

        if mng.fitness.max() > max_fitness:
            max_fitness = mng.fitness.max()
            print('Best scored, gene written.')
            mng.alpha_list[mng.getParentsIndex()[0]].writeGene()

print('finish!')

#mng.makeAlphaByFile()
