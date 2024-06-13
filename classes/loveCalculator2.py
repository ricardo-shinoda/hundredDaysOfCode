name1 = input("What is your name?\n")
name2 = input("What is their name?\n")
names = name1.lower() + name2.lower()

t = names.count("t")
r = names.count("r")
u = names.count("u")
e = names.count("e")
l = names.count("l")
o = names.count("o")
v = names.count("v")
e = names.count("e")

first_digit = t + r + u + e
second_digit = l + o + v + e

print(str(first_digit) + str(second_digit))
