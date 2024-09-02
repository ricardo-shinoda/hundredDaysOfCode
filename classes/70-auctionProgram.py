

bid_users = {

}


def auction():
    replay = True

    while replay == True:
        name = input('What is your name?:\n')
        ammount = input("what is your bid:\n")
        bid_users[name] = ammount
        quest = input('Do you want to add another use?\n')

        if quest == 'no':
            replay = False

    for i in bid_users:
        highest_bid = 0
        print(bid_users[0][0])

    # print(highest_bid)


auction()
# print(bid_users)
