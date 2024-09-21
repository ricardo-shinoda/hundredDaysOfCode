
import random

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
level = input("Choose a difficulty. Type 'easy' or 'hard':\n")

easy = 10
hard = 5
rounds = ""

choosen = int(random.choice(range(1, 100)))

if level == 'hard':
    rounds = 5
    # print(f"You have {rounds} atempts remaining to guess the number")
elif level == 'easy':
    rounds = 10
    # print(f"You have {rounds} atempts remaining to guess the number")


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
