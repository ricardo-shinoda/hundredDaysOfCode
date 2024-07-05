list = [1, 3, 0, 2, 5, 120]
new_list = []
ind = 1

for i in list:
    for j in list:
        if ind < len(list) and i > list[ind]:
            new_list.append(i)
            ind = + 1
        else:
            new_list.append(j)
            ind += 1

print(new_list)
