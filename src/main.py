from alpha_hang import *
from word import *


class Manager(object):
    def __init__(self):
        self.generation = -1
        self.alpha_list = []
        self.goal = 10000
        self.check = 100

        self.word = Word('words.txt')
        self.secret_word = ''

        self.cur_word = ''
        self.fail_alphabets = []

        self.fitness = np.zeros(10, dtype=int)
        self.mutant_rate = 0.5

    def makeGeneration(self):
        self.generation += 1

        self.secret_word = self.word.randFromDB([8, 9, 10, 11, 12])

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

        for i in range(10):
            if self.generation == self.goal:
                print('Gene ' + str(i))
            self.cur_word = ''.join(['_' for x in range(len(self.secret_word))])
            self.fail_alphabets = []

            for cnt in range(len(self.secret_word)):
                self.alpha_list[i].perceive(self.cur_word, self.fail_alphabets)
                self.alpha_list[i].evaluate()
                guessed = self.alpha_list[i].guess(self.generation == self.goal)

                if guessed in self.fail_alphabets or guessed in self.cur_word:
                    self.fitness[i] -= 10000 * (self.fail_alphabets.count(guessed) + 1)
                    self.fail_alphabets.append(guessed)
                elif guessed in self.secret_word:
                    for j in range(len(self.secret_word)):
                        if self.secret_word[j] == guessed:
                            self.cur_word = self.cur_word[:j] + guessed + self.cur_word[j + 1:]
                            self.fitness[i] += 100
                else:
                    self.fitness[i] -= 50
                    self.fail_alphabets.append(guessed)

    def getParentsIndex(self):
        rank = self.fitness.argsort()[::-1]

        return rank[0], rank[1]

    def crossover(self, _parents, _word_len):
        alpha_ret = AlphaHang(_word_len)

        for i in range(len(alpha_ret.layers)):
            if np.random.rand() < 0.5:
                # cross row
                row_point = np.random.randint(0, alpha_ret.layers[i].w.shape[0])
                rand = np.random.randint(0, 2)

                alpha_ret.layers[i].w = np.concatenate((_parents[rand].layers[i].w[:row_point, :],
                                                       _parents[abs(rand - 1)].layers[i].w[row_point:, :]), axis=0)
                alpha_ret.layers[i].w += np.random.rand() * self.mutant_rate * np.random.randn()

                rand = np.random.randint(0, 2)
                alpha_ret.layers[i].b = np.concatenate((_parents[rand].layers[i].b[:row_point, :],
                                                        _parents[abs(rand - 1)].layers[i].b[row_point:, :]),
                                                       axis=0)
                alpha_ret.layers[i].b += np.random.rand() * self.mutant_rate * np.random.randn()
            else:
                # cross col
                col_point = np.random.randint(0, alpha_ret.layers[i].w.shape[1])
                rand = np.random.randint(0, 2)

                alpha_ret.layers[i].w = np.concatenate((_parents[rand].layers[i].w[:, :col_point],
                                                        _parents[abs(rand - 1)].layers[i].w[:, col_point:]),
                                                       axis=1)
                alpha_ret.layers[i].w += np.random.rand() * self.mutant_rate * np.random.randn()

                rand = np.random.randint(0, 2)
                alpha_ret.layers[i].b = np.concatenate((_parents[rand].layers[i].b[:, :col_point],
                                                        _parents[abs(rand - 1)].layers[i].b[:, col_point:]),
                                                       axis=1)
                alpha_ret.layers[i].b += np.random.rand() * self.mutant_rate * np.random.randn()

        return alpha_ret


mng = Manager()

max_fitness = -9999999
for i in range(mng.goal + 1):
    mng.makeGeneration()
    mng.runGeneration()
    if mng.generation % mng.check == 0:
        print('Best: ' + str(mng.fitness.max()))

        if mng.fitness.max() > max_fitness:
            max_fitness = mng.fitness.max()
            print('Best scored, gene written.')
            mng.alpha_list[mng.getParentsIndex()[0]].writeGene()

print('finish!')
