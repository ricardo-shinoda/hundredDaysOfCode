from art import text2art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

initial_text = text2art('Caesar Cypher', font='standard')
print(initial_text)


def caesar(direction_imput, text_imput, shift_imput):
    encode_text = []
    for i in text_imput:
        if i not in alphabet:
            encode_text.append(i)
            text_output = ''.join(encode_text)
        else:
            if direction_imput == "decode":
                shift_imput *= -1

            position = alphabet.index(i) + shift_imput
            # return remainer so it counts only the last turn
            target = position % len(alphabet)
            value = alphabet[target]
            encode_text.append(value)
            text_output = ''.join(encode_text)

    print(f'This is the {direction_imput}d output: {text_output}')


should_continue = True

while should_continue:
    direction = input(
        "Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(direction_imput=direction,
           text_imput=text, shift_imput=shift)

    replay = input("Do you want to go again?\n").lower()
    if replay == "no":
        should_continue = False
        print("End of the game")
