# This program will add the tip and divide the bill by the number of people

print("Welcome to the tip calculator!")
bill = input("What was the total bill? $")
tip = input("How much woudl you like to give? 10, 12, or 15?\n")
people = input("How many people to split the bill?\n")

tip_ammount = int(tip) / 100 + 1
total_bill = float(bill) * float(tip_ammount)
each = float(total_bill) / float(people)

print("Each person will pay: $", float(each))
