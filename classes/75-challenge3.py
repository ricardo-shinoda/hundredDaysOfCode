import random

stages = ['''
  +----+
  |    |
  0    |
/ | \  |
 / \   |
       |
===========''',
          '''
  +----+
  |    |
  0    |
/ | \  |
 /     |
       |
===========''',
          '''
  +----+
  |    |
  0    |
/ | \  |
       |
       |
===========''',
          '''
  +----+
  |    |
  0    |
/ |    |
       |
       |
===========''',
          '''
  +----+
  |    |
  0    |
  |    |
       |
       |
===========''',
          '''
  +----+
  |    |
  0    |
       |
       |
       |
===========''',
          '''
  +----+
  |    |
       |
       |
       |
       |
===========''']


word_list = ["banana", "clothes", "car"]
men = len(stages)
# Choose the word to be ckeched.
random_word = random.choice(word_list)

display = []
life = 6

# building the lentgh of the word to be discovered
for i in random_word:
    display.append('_')

# Look in every single letter from the chosen word and compare with the chosen letter
while '_' in display and life > 0:
    guess = input("Choose one letter: \n").lower()
    for i in range(len(random_word)):
        letter = random_word[i]
        if letter == guess:
            display[i] = guess
    if guess not in random_word:
        life = (life - 1)
        men -= 1
        print(stages[men - 1])
    print(display)


if '_' not in display:
    print('You win!')
    # print('this is men', men)
    print(f'You still have {life} life')
else:
    print('Game Over')

# print(men)
