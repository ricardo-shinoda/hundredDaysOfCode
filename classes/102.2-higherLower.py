from random import randint
import gameData


def gen_number():
    random_number = randint(0, 49)
    return random_number

resul_gem = gen_number()
print(resul_gem)
