def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


# Add these 4 functions into a dictionary as the values. Keys = "+", "-", "*", "/"

calc = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


# print(calc["*"](4, 8))

# program asks the user to type the first number
first_number = int(input("What is the first number?\n"))
operator = input("What is the mathematical operator?\n")
second_number = int(input("What is the second number?\n"))


result = print(calc[operator](first_number, second_number))

cont_previous = input(
    "Do you want to continue using the previous result?\n").lower()

if cont_previous == "yes":
    print(result)
    operator = input("What is the mathematical operator?\n")
    second_number = int(input("What is the second number?\n"))
    # print(calc[operator](result, second_number))
    print(calc[operator](first_number, second_number))
