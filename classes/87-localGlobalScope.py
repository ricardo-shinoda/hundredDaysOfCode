# Glocal scope (not within another function)
enemies = 1

# local scope (within a function)


def increase_enemines():
    enemies = 2
    print(f"Enemies inside fucntion: {enemies}")


increase_enemines()
print(f"Enemies outside function: {enemies}")

# local scope


def drink_portion():
    potion_strenght = 2
