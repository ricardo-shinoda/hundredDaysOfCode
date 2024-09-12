import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def black_jack():

    play_again = True
    start = input(
        "Do you want to play a game of Blackjack? Type 'y' or 'n':\n")

    if start == 'y':

        result1 = random.choice(cards)
        result2 = random.choice(cards)
        my_cards = [result1, result2]
        my_sum = sum(my_cards)
        computer_card = random.choice(cards)
        computer_card_list = [computer_card]

    print(f'Your cards: ', my_cards, 'current score is: ', my_sum)
    print(f"Computer's first card: ", computer_card)

    while play_again:

        result1 = random.choice(cards)
        result2 = random.choice(cards)
        computer_card = random.choice(cards)

        again = input('Type "y" to get another card, type "n" to pass:\n')

        if again == 'y':
            new_number = random.choice(cards)
            my_cards.append(new_number)
            print(f'Your cards: ', my_cards,
                  'current score is: ', sum(my_cards))
            computer_card_list.append(random.choice(cards))
            print(f"Computer's card is: ", computer_card_list,
                  "current score is: ", sum(computer_card_list))
            if sum(my_cards) >= 21 or sum(computer_card_list) >= 21:
                play_again = False
                print(f'This is my: ', sum(my_cards),
                      'This is computers: ', sum(computer_card_list))
        else:
            play_again = False

            while sum(computer_card_list) < 21:
                res = random.choice(cards)
                print(f'This is res: ', res)
                computer_card_list.append(res)

            print(f'This is the final computer score: ', sum(computer_card_list))


black_jack()
