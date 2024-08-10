alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# direction = input(
#     "Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
# text = input("Type your message:\n").lower()
# shift = int(input("Type the shift number:\n"))

new_alphabet = []
# TODO-1  create a function called encrypt() that takes original_text and shift_amount as 2 inputs


def encrypt(original_text, shift_amount):
    # text = input(f'This is original_text {original_text}')
    # amount = input(f'This is shift_amount {shift_amount}')
    # print(text)
    # print(amount)
    for i in original_text:
        # print(i)
        # position = (i).index()
        position = alphabet.index(i)
        target = position + shift_amount
        # print(position)
        # print(target)
        test = alphabet[target]
        new_alphabet.append(test)
        # print(test)

    print(new_alphabet)


encrypt('hello', 1)
