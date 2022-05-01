from nltk.corpus import words
from random import choice
import json
from collections import OrderedDict


word_list = words.words()

letter_difficulty = {
    'a': 1,
    'b': 3,
    'c': 3,
    'd': 2,
    'e': 1,
    'f': 4,
    'g': 2,
    'h': 4,
    'i': 1,
    'j': 8,
    'k': 5,
    'l': 1,
    'o': 1,
    'p': 3,
    'q': 10,
    'r': 1,
    's': 1,
    't': 1,
    'u': 1,
    'v': 4,
    'w': 4,
    'x': 8,
    'y': 4,
    'z': 10,
}

byWordScore = {}
words_by_difficulty = {}
for word in word_list:
    if len(word) > 3:
        word_sum = 0
        for i in range(len(word)): # word[i] = letter
            word_sum += int(letter_difficulty.get(word[i]) or 0)
            if i > 5:
                word_sum += 1
        if not byWordScore.get(word_sum):
            byWordScore[word_sum] = [word]
        else:             
            byWordScore[word_sum].append(word)
            
            
        # words_by_difficulty[word] = { "score": word_sum, "rating": 0}

# scores = {}
# w = words_by_difficulty
# for word in w: 
#     if w[word]['score'] < 7: 
#         w[word]['rating'] = 'very easy'
#     elif  w[word]['score'] < 10:
#         w[word]['rating'] = 'easy'
#     elif w[word]['score'] < 14:
#         w[word]['rating'] = 'medium'
#     elif w[word]['score'] < 18:
#         w[word]['rating'] = 'hard'
#     elif w[word]['score'] < 22:
#         w[word]['rating'] = 'very hard'
#     elif w[word]['score'] < 26:
#         w[word]['rating'] = 'expert'
#     elif w[word]['score']:
#         w[word]['rating'] = 'master'
        
# ratings = {}
# for word in w:
#     ratings[w[word]['rating']] = int(ratings.get(w[word]['rating']) or 0) + 1
# print(byWordScore)
with open('./wordsByScore.txt', 'w') as convert_file:
    convert_file.write(json.dumps(dict(byWordScore)))