import random

states_of_america = ["New York", "Chicago", "Delaware"]
states_of_america[0] = "Nevada"

states_of_america.append("Los Angeles")

# print(states_of_america)


names = ["Angela", "Ben", "Jenny", "Michael", "Chloe"]
lenght = len(names)
index = lenght - 1

zero = 0
final = int(index)

result = random.randint(zero, final)

print(f'{names[result]} is going to buy the meal today!')


# Lists inside a list

fruits = ["banana", "mango", "orange", "lemon"]
vegetables = ["letuce", "potatoe", "onion"]

dirty_dozen = [fruits, vegetables]
print(dirty_dozen[1][2])
