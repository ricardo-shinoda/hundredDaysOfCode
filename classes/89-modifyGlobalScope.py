# Glocal scope (not within another function)
enemies = 1


def increase_enemies():
    print(f"Enemies inside fucntion: {enemies}")
    return enemies + 1


enemies = increase_enemies()
print(f"Enemies outside function: {enemies}")
