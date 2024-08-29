alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input(
    "Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def caesar(direction_imput, text_imput, shift_imput):
    encode_text = []
    if direction_imput == "decode":
        shift_imput *= -1
    for i in text_imput:
        position = alphabet.index(i) + shift_imput
        # return remainer so it counts only the last turn
        target = position % len(alphabet)
        value = alphabet[target]
        encode_text.append(value)
        text_output = ''.join(encode_text)

    print(f'This is the {direction_imput}d output: {text_output}')
    replay = input("Do you want to go again?\n").lower()

    if replay == 'yes':
        direction = input(
            "Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        caesar(direction_imput=direction,
               text_imput=text, shift_imput=shift)
    else:
        print("End of the game")


caesar(direction_imput=direction, text_imput=text, shift_imput=shift)
