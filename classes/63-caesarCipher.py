from art import text2art
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

header = text2art("Caesar Cypher", font="standard")
print(header)

direction = input(
    "Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def caesar(direction_imput, text_imput, shift_imput):
    encode_text = []
    decode_text = []
    if direction_imput == "encode":
        def encrypt():
            for i in text_imput:
                if i in alphabet:
                    position = alphabet.index(i) + shift_imput
                    # return remainer so it counts only the last turn
                    target = position % len(alphabet)
                    value = alphabet[target]
                    encode_text.append(value)
                else:
                    encode_text.append(i)

            text_output = ''.join(encode_text)
            print(f'This is the decode output: {text_output}')

        encrypt()

    elif direction_imput == "decode":
        def decrypt():
            for i in text_imput:
                if i in alphabet:
                    position = alphabet.index(i) - shift_imput
                    target = position % len(alphabet)
                    value = alphabet[target]
                    decode_text.append(value)
                    text_output = ''.join(decode_text)
                else:
                    decode_text.append(i)

            print(f'This is the decode output: {text_output}')
        decrypt()

    continue_encoding = input(
        "Type 'Yes' if you want to continue encoding/decoding words, otherwise type 'No'\n").lower()

    if continue_encoding == 'yes':
        direction = input(
            "Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        caesar(direction_imput=direction, text_imput=text, shift_imput=shift)
    else:
        print("This is the end of the encoding/decoding\n")


caesar(direction_imput=direction, text_imput=text, shift_imput=shift)
