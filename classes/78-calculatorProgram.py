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

# program asks the user to type the first number


def first_count():
    first_number = int(input("What is the first number?\n"))
    operator = input(
        "Chose one mathematical operator?\n+\n-\n*\n/\n")
    second_number = int(input("What is the second number?\n"))
    return calc[operator](first_number, second_number)


result = first_count()
print(result)

cont_previous = input(
    "Do you want to continue using the previous result?\n").lower()

while cont_previous == "yes":
    operator = input("Chose one mathematical operator?\n+\n-\n*\n/\n")
    second_number = int(input("What is the second number?\n"))
    print(calc[operator](result, second_number))
    cont_previous = input(
        "Do you want to continue using the previous result?\n").lower()
result = first_count()
print(result)
