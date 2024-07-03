height = float(input("Please, what is your height?\n"))
bill = 0

if height > 120:
    age = int(input("What is your age?\n"))
    if age < 12:
        bill = 5
    elif age <= 18:
        bill = 7
    elif age >= 45 and age <= 55:
        bill = 0
    else:
        bill = 12
    wants_photo = input("Do you want photos? (Y/N)\n")
    if wants_photo == "Y":
        bill += 3

    print(f"Your final bill is: ${bill}")
else:
    print("You need to grow taller in order to ride the roller coaster")
