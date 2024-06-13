name1 = input("What is your name?\n")
name2 = input("What is their name?\n")
names = name1.lower() + name2.lower()

# print(len(name1))
count1 = 0
count2 = 0
# print(names)


for i in names:
    if i == "t" or i == "r" or i == "u" or i == "e":
        count1 += 1
for i in names:
    if i == "l" or i == "o" or i == "v" or i == "e":
        count2 += 1

score = int(str(count1) + str(count2))


if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif score >= 40 and score <= 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")
