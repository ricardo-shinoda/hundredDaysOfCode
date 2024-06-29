import random

letters = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']


print('Welcome to the PyPassword Generator!')
number_letters = int(
    input('How many number of letters in your password (52 max)?\n'))
number_symbols = int(input('How many symbols would you like (9 max)?\n'))
number_numbers = int(input('How many numbers would you like (10 max)?\n'))


let_sample = random.sample(letters, number_letters)
sym_sample = random.sample(symbols, number_symbols)
num_sample = random.sample(numbers, number_numbers)

result = []
result.append(let_sample)
result.append(sym_sample)
result.append(num_sample)

result2 = []

for i in result:
    result2 += i

final = ''.join(result2)
print(final)
