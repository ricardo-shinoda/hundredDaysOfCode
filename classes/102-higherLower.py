from random import randint
import gameData


def gen_one():
    primeiro = randint(0, 49)
    return primeiro


generating = gen_one()
print(f'this is generating: {generating}')


def followers_first_pick(x):
    first_one_generating = gameData.data[x]
    resulting_gen = first_one_generating['follower_count']
    return resulting_gen


first_followers = followers_first_pick(generating)
print(f'this is firsto followers: {first_followers}')


def gen_two():
    second = randint(0, 49)
    return second


generating_second = gen_two()
print(f'This is generating two: {generating_second}')


def followers_second_pick(x):
    second_one_generating = gameData.data[x]
    result = second_one_generating['follower_count']
    return result


second_followers = followers_second_pick(generating_second)
print(f'This is second followers: {second_followers}')


winning = True
# create a compare A
while winning:
    def keep_playing(first_choice, second_choice):
        path_a = gameData.data[first_choice]
        # path_a = first_pick
        print(
            f"Compare A: {path_a['name']}, a {path_a['description']}, from {path_a['country']}")
        followers_a = path_a['follower_count']
        print(followers_a)

        path_b = gameData.data[second_choice]
        # path_b = second_pick
        print(
            f"Compare B: {path_b['name']}, a {path_b['description']}, from {path_b['country']}")
        followers_b = path_b['follower_count']
        # print(followers_b)
        print(followers_b)

        guess = input("Who has more followers? Type 'A' or 'B': ").upper()

        return guess

    user_guess = keep_playing(first_choice=generating,
                              second_choice=generating_second)
    print(f'THIS IS USER_GUESS: {user_guess}')

    if user_guess == 'A':
        if first_followers > second_followers:
            print(
                f'You are winning! result 1 is:{first_followers}, result 2 {second_followers}')
            generating = generating
            generating_second = gen_two()
            first_followers = followers_first_pick(generating)
    if user_guess == 'B':
        if second_followers > first_followers:
            print(
                f'You are winning! result 2 is: {second_followers}, result one {first_followers}')
            generating = generating_second
            generating_second = gen_two()
            second_followers = followers_first_pick(generating_second)
    else:
        print('You loose...')
        print(f'This followers from 1: {first_followers}')
        print(f'This is followers from 2: {second_followers}')
        winning = False
