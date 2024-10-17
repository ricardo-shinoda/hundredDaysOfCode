from random import randint
import gameData
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
    
        path_b = gameData.data[second_choice]
        # path_b = second_pick
        print(f"Compare B: {path_b['name']}, a {path_b['description']}, from {path_b['country']}")
        followers_b = path_b['follower_count']
        # print(followers_b)
        print(followers_b)

        guess = input("Who has more followers? Type 'A' or 'B': ").upper()

        return guess

    user_guess = keep_playing(first_choice=first_pick, second_choice=second_pick)
    print(f'THIS IS USER_GURSS: {user_guess}')

    if user_guess == 'A' and result_one > result_two:
        print('You are winning! result 1 bigger then result two')
        first_pick = first_one
    elif user_guess == 'B' and result_two > result_one:
        print('You are winning! result 2 bigger then result 1')
        first_pick = second_pick
        second_pick = int(randint(0, 49))
    else:
        print('You loose...')
        winning = False
    
