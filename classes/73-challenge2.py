import random

word_list = ["banana", "clothes", "car"]

# Choose the word to be ckeched.
random_word = random.choice(word_list)
lenght = len(random_word)

display = []
ind = 0

for i in random_word:
    display.append('_')

# Ask the user which letter to check on word.
guess = input("Choose one letter: \n").lower()

# Look in every single letter from the chosen word and compare with the chosen letter
for i in range(len(random_word)):
    letter = random_word[i]
    if letter == guess:
        display[i] = letter

print(random_word)
print(display)
