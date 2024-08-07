import math


def prime_checker(number):
    prime = 0
    root = int(math.sqrt(number))
    if number < 1:
        print(f"Number is not a prime number")
    elif number == 2:
        print("It's is prime number")
    for i in range(2, root + 1):
        if number % i == 0:
            prime += 1
    if prime >= 1:
        print("It's not a prime number")
    else:
        print("It's prime number")


prime_checker(87)
