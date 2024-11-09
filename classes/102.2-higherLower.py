from random import randint
import gameData


def gen_number():
    """Generate a random number"""
    random_number = randint(0, 49)
    return random_number


resul_gem = gen_number()
# print(resul_gem)


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
    result(resul_gem)


first_choice = generationg_new()
second_choice = generationg_new()


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
