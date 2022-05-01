import json

f = open('wordsAndDifficulty.txt')

data = json.load(f)


wordsByRating = {
    "very easy": [],
    "easy": [],
    "medium": [],
    "hard": [],
    "very hard": [],
    "expert": [],
    "master": [],
               }
for word in data:
    wordsByRating[data[word]["rating"]].append(word)

with open('./wordsByRating.txt', 'w') as convert_file:
    convert_file.write(json.dumps(wordsByRating))