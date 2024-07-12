def turn_right():
    turn_left()
    turn_left()
    turn_left()


def move_over():
    turn_right()
    move()
    turn_right()
    move()


while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif not right_is_clear() and front_is_clear():
        move()
    elif not right_is_clear() and not front_is_clear():
        turn_left()
    else:
        move()
