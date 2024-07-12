import random

word_list = ["banana", "clothes", "car"]

# Choose the word to be ckeched.
random_word = random.choice(word_list)

display = []

for i in random_word:
    display.append('_')

# Ask the user which letter to check on word.


# Look in every single letter from the chosen word and compare with the chosen letter


while '_' in display:
    guess = input("Choose one letter: \n").lower()
    for i in range(len(random_word)):
        letter = random_word[i]
        if letter == guess:
            display[i] = guess

    print(display)

if '_' not in display:
    print('You win!')


# print(random_word)
# print(display)
