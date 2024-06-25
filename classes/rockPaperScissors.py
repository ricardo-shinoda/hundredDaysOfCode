import random

scissors = '''
    __________
---'    ______)_____
            ________)
        ______________)
        (_____)
---,_____(___)
'''

rock = '''
    __________
---'    ______)
        (______)
        (______)
        (_____)
---,_____(___)
'''

paper = '''
    ___________
---'     ______)____
            ________)
        _____________)
        (___________)
---,_____(_________)
'''

user = int(input('Please type 0 for Rock, 1 for Paper and 2 for Scissors\n'))

if user >= 3 or user < 0:
    print("Invalid Input")
else:
    if user == 0:
        print(rock)
    elif user == 1:
        print(paper)
    else:
        print(scissors)

    pc = random.randint(0, 2)

    if pc == 0:
        print('Computer chose: ', rock)
    elif pc == 1:
        print('Computer chose: ', paper)
    else:
        print('Computer chose: ', scissors)

    if user == 0:  # Rock
        if pc == 0:
            print('Tie game')
        elif pc == 1:
            print('You lose')
        elif pc == 2:
            print('You win')

    elif user == 1:  # Paper
        if pc == 0:
            print('You win')
        elif pc == 1:
            print('Tie game')
        elif pc == 2:
            print('You lose')

    elif user == 2:  # Scissors
        if pc == 0:
            print('You lose')
        elif pc == 1:
            print('You win')
        elif pc == 2:
            print('Tie game')
