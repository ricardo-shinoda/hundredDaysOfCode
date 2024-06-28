year = int(input("Type a year: \n"))
four = year % 4
hundred = year % 100
quatr = year % 400

if year % 4 == 0 and year % 100 != 0:
    print(f"This is a leap year(4): {four}")
    if year % 100 == 0:
        print(f"This is a no leap year(100): {hundred}")
        if year % 400 == 0:
            print(f"This is a leap year(400): {quatr}")
else:
    print("This is not a leap year")
