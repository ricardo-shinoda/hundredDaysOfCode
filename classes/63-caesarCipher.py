alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input(
    "Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


# TODO-1  create a function called encrypt() that takes original_text and shift_amount as 2 inputs

def encrypt(original_text, shift_amount):
    print(f'This is original_text {original_text}')
    print(f'This is shift_amount {shift_amount}')


encrypt('hello', 1)
