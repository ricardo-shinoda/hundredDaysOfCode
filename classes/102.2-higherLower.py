import random
from gameData import data


# found the random account information
account_a = random.choice(data)
account_b = random.choice(data)

if account_a == account_a:
    account_b = random.choice(data)

# Formata DATA into desired readable format


def create_sentence(pick):
    name = pick['name']
    desc = pick['description']
    country = pick['country']
    followers = pick['follower_count']
    return f'Compare a: {name}, from {country}, with {followers} followers.'


description1 = create_sentence(account_a)
description2 = create_sentence(account_b)
print(description1)
print(description2)

# def question(a, b):
#     print("Who would you pick?")
#     # first = a
#     print(f"Would you pick a: {a}")
#     print("VS")
#     # second = input(b)
#     print(f"Would you pick : {b}")
#     return


# questioning = question(a=first_choice, b=second_choice)
# print(questioning)
