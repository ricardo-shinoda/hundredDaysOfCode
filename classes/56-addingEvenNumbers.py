# number = 0
# target = int(input('type a number\n'))

# for i in range(0, target + 1):
#     if i % 2 == 0:
#         number += i

# print(number)

# Another solution

number = 0
target = int(input('type a number\n'))

for i in range(2, target + 1, 2):
    number += i

print(number)
