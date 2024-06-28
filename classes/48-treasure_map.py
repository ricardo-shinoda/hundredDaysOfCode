line1 = ["⬜️", "️⬜️", "️⬜️"]
line2 = ["⬜️", "⬜️", "️⬜️"]
line3 = ["⬜️️", "⬜️️", "⬜️️"]

print("Hiding your treasure X marks the spot.")
location = input("Where do you want to put the treasure?\n")
l1 = location[0].lower()
l2 = location[1]

if l1 == 'a':
    if l2 == '1':
        line1[0] = "X"
    elif l2 == '2':
        line2[0] = "X"
    else:
        line3[0] = "X"
elif l1 == 'b':
    if l2 == '1':
        line1[1] = "X"
    elif l2 == '2':
        line2[1] = "X"
    else:
        line3[1] = "X"
elif l1 == 'c':
    if l2 == '1':
        line1[2] = "X"
    elif l2 == '2':
        line2[2] = "X"
    else:
        line3[2] = "X"


print(f"{line1}\n{line2}\n{line3}")
