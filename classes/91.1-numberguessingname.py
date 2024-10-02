from random import randint

# Choosing a random number between 1 and 100

choosen = randint(1, 100)
EASY = 10
HARD = 5
rounds = ''

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
print(choosen)

# Function to set difficulty


def level_game():
    level = input("Choose a difficulty. Type 'easy' or 'hard': \n")
    if level == 'easy':
        rounds = EASY
    elif level == 'hard':
        rounds = HARD


level_game()


# Let the user guess a number

tentative = int(input('Make a guess: '))

# Fuction to ckeck users guess against actual  answers


def check_guess(user_try, computer_try):
    global rounds
    if user_try == computer_try:
        print("You got it right!")
    elif user_try > computer_try:
        print("Too high.")
        rounds -= 1
        print(rounds)
    elif user_try < computer_try:
        print('Too low.')
        rounds -= 1
        print(rounds)


check_guess(user_try=tentative, computer_try=choosen)


# track the number of turns and reduce by 1 if they get it wrong


# Repeat the guessing functionality if they get it wrong
