
from os import system
bid_users = {

}


def auction():
    replay = True

    while replay == True:
        name = input('What is your name?:\n')
        ammount = input("what is your bid:\n")
        bid_users[name] = ammount
        quest = input('Do you want to add another use?\n')
        #! to clear  terminal
        system("clear")

        if quest == 'no':
            replay = False

    for i in bid_users:
        highest_bid = 0
        base = {}
        if int(bid_users[i]) > highest_bid:
            base[i] = bid_users[i]

    print(f'The winner is:', i, 'with a bid of:', base[i])


auction()
