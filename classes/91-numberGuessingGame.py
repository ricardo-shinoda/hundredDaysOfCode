
from random import randint
from art import *

label = text2art("Guessing Number Game")
print(label)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
level = input("Choose a difficulty. Type 'easy' or 'hard':\n")

easy = 10
hard = 5
rounds = ""

choosen = randint(1, 100)


if level == 'hard':
    rounds = 5
elif level == 'easy':
    rounds = 10

while rounds == 5 or rounds == 10:
    while rounds > 0:
        print(f"You have {rounds} attempts remaining to guess the number.")
        tentative = int(input("Make a guess: "))
        print(choosen)
        if tentative > choosen:
            print("Too high.")
            rounds -= 1
        elif tentative < choosen:
            print('Too low.')
            rounds -= 1
        elif tentative == choosen:
            print(f'You got it! The answer was {tentative}')
            rounds = 0
    print("End of the game")
