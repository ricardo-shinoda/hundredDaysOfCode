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
        else:
            play_again = False


black_jack()
