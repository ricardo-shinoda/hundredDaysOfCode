alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# direction = input(
#     "Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
# text = input("Type your message:\n").lower()
# shift = int(input("Type the shift number:\n"))

new_alphabet = []
# TODO-2  create a function called encrypt() that takes original_text and shift_amount as 2 inputs


def encrypt(original_text, shift_amount):
    for i in original_text:
        position = alphabet.index(i)
        target = position + (shift_amount % len(alphabet))
        result = alphabet[target]
        new_alphabet.append(result)
        text_output = ''.join(new_alphabet)

    print(text_output)


encrypt('hello', 1)
