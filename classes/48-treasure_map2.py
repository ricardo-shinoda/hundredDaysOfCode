line1 = ["⬜️", "️⬜️", "️⬜️"]
line2 = ["⬜️", "⬜️", "️⬜️"]
line3 = ["⬜️️", "⬜️️", "⬜️️"]

map = [line1, line2, line3]

location = input("Where do you want to put the treasure?\n")
l1 = location[0].lower()
l2 = location[1]
abc = ['a', 'b', 'c']
letter_index = abc.index(l1)
number_index = int(l2) - 1
map[number_index][letter_index] = 'X'

print("Hiding your treasure X marks the spot.")
print(f"{line1}\n{line2}\n{line3}")
