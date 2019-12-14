from alpha_hang import *
from word import *

word = Word('words.txt')
secret_word = word.randFromDB()

cur_word = ''.join(['_' for x in range(len(secret_word))])
fail_alphabets = []

alphahang = AlphaHang()
alphahang.perceive(cur_word, fail_alphabets)