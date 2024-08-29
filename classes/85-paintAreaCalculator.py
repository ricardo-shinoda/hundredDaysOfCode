import math


def paint_calc(height, width, cover):
    result = math.ceil(height * width / cover)
    print(f"You'll need {result} cans of paint.")


paint_calc(3, 9, 5)
