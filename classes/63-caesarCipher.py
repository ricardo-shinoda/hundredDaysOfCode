alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input(
    "Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
if text in alphabet:
    shift = int(input("Type the shift number:\n"))

    def caesar(direction_imput, text_imput, shift_imput):
        encode_text = []
        decode_text = []
        if direction_imput == "encode":
            def encrypt():
                for i in text_imput:
                    position = alphabet.index(i) + shift_imput
                    # return remainer so it counts only the last turn
                    target = position % len(alphabet)
                    value = alphabet[target]
                    encode_text.append(value)
                    text_output = ''.join(encode_text)

                print(f'This is the encode output: {text_output}')
            encrypt()

        elif direction_imput == "decode":
            def decrypt():
                for i in text_imput:
                    position = alphabet.index(i) - shift_imput
                    target = position % len(alphabet)
                    value = alphabet[target]
                    decode_text.append(value)
                    text_output = ''.join(decode_text)

                print(f'This is the decode output: {text_output}')
            decrypt()

    caesar(direction_imput=direction, text_imput=text, shift_imput=shift)

else:
    print('Try again with right characters')
