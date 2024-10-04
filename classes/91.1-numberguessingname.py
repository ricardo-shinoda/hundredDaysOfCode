from random import randint

# Choosing a random number between 1 and 100

EASY = 10
HARD = 5
rounds = 0


def check_answer(user_try, computer_try, rounds):
    if user_try > computer_try:
        print("Too high.")
        return rounds - 1
    elif user_try < computer_try:
        print('Too low.')
        return rounds - 1
    else:
        print(f"You got it right! {user_try}")


# Repeat the guessing functionality if they get it wrong


def set_dificulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': \n")
    if level == 'easy':
        return EASY
    elif level == 'hard':
        return HARD


# Let the user guess a number


def game():

    # Function to set difficulty
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    choosen = randint(1, 100)
    print(choosen)

    rounds = set_dificulty()
    guess = 0
    while guess != choosen:
        print(f"You have {rounds} attempts remaining to guess the number.")
        guess = int(input('Make a guess: '))
        rounds = check_answer(guess, choosen, rounds)
        # add an if with the turn
        if rounds == 0:
            print("You've ran out of guesses, you lose.")
            return
        elif guess != choosen:
            print("Guess again.")


game()git s


# Fuction to ckeck users guess against actual  answers


# track the number of turns and reduce by 1 if they get it wrong
