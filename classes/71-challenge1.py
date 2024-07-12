import random

word_list = ["banana", "clothes", "car"]

# Choose the word to be ckeched.
random_word = random.choice(word_list)

# Ask the user which letter to check on word.
guess = input("Choose one letter: \n").lower()

# Look in every single letter from the chosen word and compare with the chosen letter
for i in random_word:
    if i == guess:
        print('Right')
    else:
        print("wrong")

print(random_word)
