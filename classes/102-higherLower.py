from random import randint
import gameData

# from art import *

# logo1 = text2art("Higher or Lower")
# print(logo1)

# logo2 = text2art("VS")
# print(logo2)

# create an random number search
first_pick = randint(0, 49)
# print(first_pick)
first_one = gameData.data[first_pick]
result_one = first_one['follower_count']

second_pick = randint(0, 49)
second_one = gameData.data[second_pick]
result_two = second_one['follower_count']
# print(second_pick)

winning = True
# create a compare A
while winning:
    def keep_playing(first_choice, second_choice):
        path_a = gameData.data[first_choice]
        # path_a = first_pick
        print(f"Compare A: {path_a['name']}, a {path_a['description']}, from {path_a['country']}")
        followers_a = path_a['follower_count']
        print(followers_a)
        # print(followers_a)
        # print(path['name'])

        # create a compare b
        path_b = gameData.data[second_choice]
        # path_b = second_pick
        print(f"Compare B: {path_b['name']}, a {path_b['description']}, from {path_b['country']}")
        followers_b = path_b['follower_count']
        # print(followers_b)
        print(followers_b)

        guess = input("Who has more followers? Type 'A' or 'B': ")

        return guess

    user_guess = keep_playing(first_choice=first_pick, second_choice=second_pick)
    print(f'THIS IS USER_GURSS: {user_guess}')

    if user_guess == 'A' and result_one > result_two:
        print('You are winning!')
        # first_choice = second_pick
    elif user_guess == 'B' and result_two > result_one:
        print('You are winning!')
        # first_choice = second
    else:
        print('You loose...')
        winning = False
    
# return guess
    

# winning = True

# while winning:
#         keep_playing(first_choice=first_pick, second_choice=second_pick)
# winning = False



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
