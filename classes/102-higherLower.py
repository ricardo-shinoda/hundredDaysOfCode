from random import randint
import gameData

# from art import *

# logo1 = text2art("Higher or Lower")
# print(logo1)

# logo2 = text2art("VS")
# print(logo2)

# create an random number search
first_pick = randint(0, 49)
print(first_pick)

second_pick = randint(0, 49)
print(second_pick)

# create a compare A
path = gameData.data[first_pick]
print(f"Compare A: {path['name']}, a {path['description']}, from {path['country']}")
# print(path['name'])

# create a compare b
path = gameData.data[second_pick]
print(f"Compare B: {path['name']}, a {path['description']}, from {path['country']}")

#! To do list
# make a list of dice emojis
# compare dice value against previous value
# What should be printed:
# make the logo1
# make the logo 2

#! Layout 1 round
# logo1
# compare a:
# VS logo
# agains b:
# who has more followers? Tpe a or b:

#! layout 2 round
# logo 1
# result (right/wrong) - current score ( += 1)
# -- if is wrong:
# ---- Logo 1
# ---- "Sorry, that's wrong. Final score: xx"
# Compare A = previous compare B
# Vs logo
# Against B:
# Who has more followers?
