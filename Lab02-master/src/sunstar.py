"""
CSapx Lab 2: sunstar.py

A program that draws a pattern in the turtle window using recursive techniques

$ python3 sunstar.py

The side length and levels are gotten from standard input.

author: Dean Trivisani
"""

import turtle
import math

def draw_side(length, level, angle):
    """
    Draws a side of a sunstar with given parameters
    :param length: Length, in pixels, of the side to be drawn
    :param level: Number of times the function is to recurse
    :param angle: Angle to to turn left after having drawn one side
    :return: the total length of all of the sides that have been drawn
    """
    total_length = 0
    if level == 1:
        turtle.forward(length)
        total_length += length
    else:
        turtle.forward(length / 4)
        total_length += (length / 4)
        turtle.left(angle)
        total_length += draw_side(length / (4 * math.cos(angle * math.pi / 180)), level - 1, angle)
        turtle.right(2 * angle)
        total_length += draw_side(length / (4 * math.cos(angle * math.pi / 180)), level - 1, angle)
        turtle.left(angle)
        turtle.forward(length / 4)
        total_length += (length / 4)
    return total_length

def draw_sun_star(sides, length, level, angle):
    """
    Draws a sunstar  with the specified properties
    :param sides: Number of sides the sunstar will have
    :param length: Length, in pixels, of each side
    :param level: Number of times the function is to recurse
    :param angle: Angle to to turn left after having drawn one side
    :return: total perimeter of the sunstar
    """

    total_length = 0
    angle_btwn_sides = int(360 / sides)
    while sides > 0:
        total_length += draw_side(length, level, angle)
        turtle.right(angle_btwn_sides)
        sides -=1
    return(total_length)

def main() -> None:
    """
    The main function. Takes inputs to draw a sunstar, re-prompts user if input is not an integer
    :return: None
    """

    while True:
        try:
            input_sides = int(input("Enter Sides: "))
        except ValueError:
            print("Invalid input. Please try again.")
            continue
        else:
            break
    while True:
        try:
            input_length = int(input("Enter Side Length: "))
        except ValueError:
            print("Invalid input. Please try again.")
            continue
        else:
            break
    while True:
        try:
            input_levels = int(input("Enter Levels: "))
        except ValueError:
            print("Invalid input. Please try again.")
            continue
        else:
            break
    while True:
        try:
            input_angle = int(input("Enter Angle: "))
        except ValueError:
            print("Invalid input. Please try again.")
            continue
        else:
            break

    turtle.speed(0)
    print(draw_sun_star(input_sides, input_length, input_levels, input_angle))
    turtle.mainloop()


# only run this program if it is not being imported by another main module
if __name__ == '__main__':
    main()

