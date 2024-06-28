print("Thank you for choosing Python Pizza Deliveries!")
bill = 0

size = input("What size pizza do you want? S, M or L?\n")

if size == "S":
    bill = 15
    add_pepperoni = input("Do you want pepperoni? Y/N\n")
    if add_pepperoni == "Y":
        bill += 2
elif size == "M":
    bill = 20
    add_pepperoni = input("Do you want pepperoni? Y/N\n")
    if add_pepperoni == "Y":
        bill += 3
elif size == "L":
    bill = 25
    add_pepperoni = input("Do you want pepperoni? Y/N\n")
    if add_pepperoni == "Y":
        bill += 3

    extra_cheese = input("Do you want extra cheese? Y/N\n")
    print("Thank you for choosing Python Pizza Deliveries!")
    if extra_cheese == "Y":
        bill += 1
        print(f"Your final bill is ${bill}")
    else:
        print(f"Your final bill is $ {bill}")
