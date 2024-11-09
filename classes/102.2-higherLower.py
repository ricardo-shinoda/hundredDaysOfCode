import random
from gameData import data

account_a = random.choice(data)
account_b = random.choice(data)

if account_a == account_a:
    account_b = random.choice(data)


def description(chosen):
    data = gameData.data[chosen]
    compare_name = data['name']
    compare_descrip = data['description']
    compare_contry = data['country']
    compar_foll = data['follower_count']
    return f"{compare_name}, a {compare_descrip}, from {compare_contry} with {compar_foll} followers"


result = description(resul_gem)
# print(gameData.data[0])
print(result)


def generationg_new():
    response = result(resul_gem)
    return response


generator = generationg_new()


first_choice = generator
second_choice = generator


def question(a, b):
    print("Who would you pick?")
    # first = a
    print(f"Would you pick a: {a}")
    print("VS")
    # second = input(b)
    print(f"Would you pick : {b}")
    return


questioning = question(a=first_choice, b=second_choice)
print(questioning)
