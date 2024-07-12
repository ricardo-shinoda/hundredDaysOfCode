height = float(input("Please, type your height\n"))
age = int(input("Also, type your your age\n"))

if height >= 120:
    print("You can go to this playground")
    if age < 12:
        print("You are going to pay 5 dollars")
    elif age < 18:
        print("You are going to pay 7 dollars")
    else:
        print("You are going to pay 12 dollars")
else:
    print("YOu cannot go to this playground")


minha_lista = [2, 3, 4]
minha_lista.insert(0, 1)
print(minha_lista)  # Saída: [1, 2, 3, 4]
