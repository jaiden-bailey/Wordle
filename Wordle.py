## Used for random word generation from text file.
import random
import sys

import nltk

#Used to create the yellow and green colors.
from termcolor import colored

nltk.download('words')
from nltk.corpus import words


def menu():
    print("Welcome to wordle!!")
    print("Type in a 5 letter word and then press enter. \n ")

def random_word():
    with open("wordle_words.txt", "r") as f:
        words = f.read().splitlines()
        return random.choice(words)

nltk.data.path.append('/work/words')
word_list = words.words()
words_five = [word for word in word_list if len(word) == 5]
print(len(words_five))

menu()

retry = " "
while retry != "quit":
# For loop that checks for the correct letter and position and colors them appropriately
    words = random_word()
    
    words = random.choice(words_five).lower()

    for attempt in range(1 ,7):
        guess = input().lower()
            
        sys.stdout.write('\x1b[1A')
        sys.stdout.write('\x1b[2K')

        
        for i in range( min(len(guess), 5) ):
            if guess[i] == words[i]:
                print(colored(guess[i], 'green'),end=" ")
            elif guess[i] in words:
                print(colored(guess[i], 'yellow'),end=" ")
            else:
                print(guess[i], end=" ")
                
        print()
        
        if guess == words:
            print(f" Congratulations!! You got the wordle in {attempt} tries!!")
            retry = input("Want to play again? Type quit to exit. Press enter to play: ")


            break
        elif attempt == 6:
            print(f"Sorry the wordle was.. {words}")

            retry = input("Want to play again? Type quit to exit. Press enter to play: ")

