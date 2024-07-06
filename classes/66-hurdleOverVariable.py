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
    if wall_in_front() and not right_is_clear():
        turn_left()
    elif front_is_clear() and not wall_on_right():
        move_over()
    elif right_is_clear():
        move_over()
    else:
        move()
