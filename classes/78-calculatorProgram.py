from os import system
from art import *


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


def calculator():
    label = text2art("Calculator")
    print(label)

    should_accumulate = True
    first_number = float(input("What is the first number?\n"))

    while should_accumulate:
        for i in calc:
            print(i)

        operator = input("What is the mathematical operator?\n")
        second_number = float(input("What is the second number?\n"))
        answer = calc[operator](first_number, second_number)
        print(f"{first_number} {operator} {second_number} = {answer}")

        choice = input(
            f"Type: 'yes' to continue calculating with {answer}, or 'not'to start all over again\n")

        if choice == "yes":
            first_number = answer
        else:
            should_accumulate = False
            system("clear")
            calculator()


calculator()
