# list = [0, 3, 2, 34, 10, 9]
# new_list = []
# position = 0

# for i in list:
#     # print(i)
#     if i > list[position + 1]:
#         new_list.append(list[position])
#         print(new_list)
#     else:
#         new_list.append(i)

# print(new_list)


numbers = [1, 9, 3, 40, 5]
new_list = []
position = 0

for i in numbers:
    for j in numbers:
        if i > j:
            print(i)
        else:
            print(j)
