from words import list_words
from stages import stage_list
# from replit import clear
import random

# word_list = ["banana", "clothes", "car"]
men = len(stage_list)
# Choose the word to be ckeched.
random_word = random.choice(list_words)

display = []
life = 6

# building the lentgh of the word to be discovered
for i in random_word:
    display.append('_')

list_guessed = []
# Look in every single letter from the chosen word and compare with the chosen letter
while '_' in display and life > 0:
    guess = input("Choose one letter: \n").lower()
    print(f'the word is {random_word}')
    # clear()
    for i in range(len(random_word)):
        letter = random_word[i]
        if letter == guess:
            display[i] = guess
        if letter in list_guessed:
            print(f'The letter: {letter} has already been chosen')
        # break
    if guess not in random_word:
        life = (life - 1)
        men -= 1
        print(
            f'You choose a letter: "{guess}" that is not in a guessed word, you will loose a life')
        print(stage_list[men - 1])
    list_guessed.append(guess)
    print(display)

if '_' not in display:
    print('You win!')
    # print('this is men', men)
    print(f'You still have {life} life')
else:
    print('Game Over')

print(f'The word was: {random_word} ')

# fixed the repeated guessed word, need to work on repeated wrong word and avoid using lives on the same word.
