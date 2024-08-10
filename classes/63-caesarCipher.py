alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input(
    "Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()

encode_text = []
# TODO-2  create a function called encrypt() that takes original_text and shift_amount as 2 inputs

if direction == "encode":
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    def encrypt(original_text, shift_amount):
        for i in original_text:
            position = alphabet.index(i) + shift_amount
            # return remainer so i counst only the last turn
            target = position % len(alphabet)
            value = alphabet[target]
            encode_text.append(value)
            text_output = ''.join(encode_text)

        print(f'This is the encode output: {text_output}')

    encrypt(original_text=text, shift_amount=shift)
else:
    print("Need to finish this code")
