number = 0
target = int(input('type a number\n'))

for i in range(0, target + 1):
    if i % 2 == 0:
        number += i

print(number)
