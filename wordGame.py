import json, os, time
from random import choice, randrange
import msvcrt as m
from datetime import datetime
clear = lambda: os.system('cls')

class Word:
    ratings = {            
            "very easy": 
                {
                    "min": 4,
                    "max": 8
                },
            "easy": 
                {
                    "min": 8,
                    "max": 14
                },
            "medium": 
                {
                    "min": 14,
                    "max": 18
                },
            "hard": 
                {
                    "min": 18,
                    "max": 22
                },
            "very hard": 
                {
                    "min": 22,
                    "max": 26
                },
            "expert": 
                {
                    "min": 26,
                    "max": 30
                },
            "master": 
                {
                    "min": 30,
                    "max": 60
                }
        }
    def __init__(self, difficulty="very easy") -> None:        
        self.rating = difficulty
        self.value = ""
        self.score = 0
        self.getWord()
    
    def getWord(self):
        f = open('wordsByScore.txt')
        data = json.load(f)
        self.score = randrange(self.ratings[self.rating]["min"],self.ratings[self.rating]["max"])        
        self.value = choice(data[str(self.score)])
        print(f'Testing mode for dummies like me: {self.value}')
        time.sleep(2)

class Wordem:
    """
    Creates a self-running game object that returns a score. 
    Wordem Input: difficulty, which is passed to Word
    """
    def __init__(self, difficulty) -> None:
        self.start_time = datetime.now()
        self.guesses = []
        self.guessesLeft = 7     
        self.known_positions = set()
        
        self.word = Word(difficulty)
        self.display_word = self.displayWord()
        self.runGame()
        
    def runGame(self):
        while self.guessesLeft > 0 and len(self.known_positions) != len(self.word.value):
            clear()
            print(f'Your word has {len(self.word.value)} letters. You have {self.guessesLeft} guesses left. \nGood luck!\n')
            print(f"{self.display_word}\n")
            for guess in self.guesses:
                print(f"{' '.join(guess.split())}")
            self.guesses.append(input("Your guess: ")) 
            self.userGuess()
            
        game_time = datetime.now() - self.start_time
           
        total_guesses = 7 - self.guessesLeft
        game_score = (7-total_guesses) * self.word.score
        if  self.guesses[-1].lower() == self.word.value.lower():
            print(f"Congrats! You got it in {total_guesses}.")
        else:
            print(f"Bad luck.")
            print(f"The word was: {self.word.value}") 
            
        print(f"Your Score: {game_score}")
        print(f'Total time: {int(game_time.total_seconds()) // 60} minutes, {int(game_time.total_seconds()) % 60} seconds')
        print('Press any key to continue')
        self.wait()
        return game_score
          
    def wait(self):
        m.getch()
    
    def userGuess(self):
        for i in range(min(len(self.guesses[-1]),len(self.word.value))):
            if self.guesses[-1][i].lower() == self.word.value[i].lower():
                self.known_positions.add(i)
            self.display_word = self.displayWord()
        self.guessesLeft -= 1
        
    def displayWord(self):
        pos_list = list(self.known_positions)
        return " ".join([self.word.value[i] if i in pos_list else "_" for i in range(len(self.word.value))])
        
def main():
    clear()
    difficulties = [
    "very easy",
    "easy",
    "medium",
    "hard",
    "very hard",
    "expert",
    "master"]
    print(' Welcome to Wordem! '.center(40, "-"))
    print('')
    for i in range(len(difficulties)):
        print(f'[{i+1}]',f'{difficulties[i]}'.title(), end=" ")
    print('\n')
    try:
        difficulty = int(input('Choose Difficulty: '))-1
    except:
        print("That input wasn't recognized")
        time.sleep(2)
        
    game = Wordem(difficulties[difficulty])
    
main()