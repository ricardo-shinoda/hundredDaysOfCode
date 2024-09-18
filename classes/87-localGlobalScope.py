# Glocal scope (not within another function)
enemies = "Sheleton"

# local scope (within a function)
print(enemies)

# use global to modify a global scope, but not usefull


def increase_enemines():
    global enemies
    enemies = "Zombie"
    print(f"Enemies inside fucntion: {enemies}")


increase_enemines()
print(f"Enemies outside function: {enemies}")

# local scope


def drink_portion():
    potion_strenght = 2
