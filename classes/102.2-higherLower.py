import random
from gameData import data
from os import system


# Formata DATA into desired readable format
def format_data(pick):
    """Take the account data into printable format."""
    name = pick['name']
    desc = pick['description']
    country = pick['country']
    followers = pick['follower_count']
    return f'{name}, a {desc} from {country}, with {followers} followers.'


def check_answer(user_choice, follower_a, follower_b):
    """Take teh users guess, compare if they got it right"""
    if follower_a > follower_b:
        return user_choice == "a"
    else:
        return user_choice == "b"


score = 0
game_should_continue = True
account_b = random.choice(data)

while game_should_continue:

    # found the random account information
    account_a = account_b
    account_b = random.choice(data)

    if account_a == account_a:
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}")
    print("*** VS ***")
    print(f"Against B {format_data(account_b)}")

    # get user choice
    user_choice = input("What is your pick: A or B: ? ").lower()
    print(user_choice)

    follower_account_a = account_a["follower_count"]
    follower_account_b = account_b["follower_count"]
    is_correct = check_answer(
        user_choice, follower_account_a, follower_account_b)

    system("clear")

    if is_correct:
        score += 1
        print(f"You've got it right! Current score: {score}")
        # system("clear")
    else:
        print(f"Sorry, you've got it wrong. Final Score: {score}")
        game_should_continue = False
