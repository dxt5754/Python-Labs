"""
CSapx Lab 1: tinyturtle

A program that draws a square of a given side length.  If the program is run
as:

$ python3 square.py

The side length is gotten from standard input.

author: Dean Trivisani
"""

import turtle



def main() -> None:
    """
    The main function.
    :return: None
    """
    turt_cmd = input("Please enter a string containing only basic and enhanced TinyTurtle commands: ")
    evaluate(turt_cmd)
    turtle.mainloop()


def evaluate(cmds) -> None:
    """
    Evaluates basic TT commands and prints the corresponding turtle command
    :param cmds: string of basic TT commands
    :return: None
    """
    split_list = cmds.split()
    for command in split_list:
        if command[0] == 'F':
            turtle.forward(int(command[1:]))
            print("forward(" + str(int(command[1:])) + ")")
        elif command[0] == 'L':
            turtle.left(int(command[1:]))
            print("left(" + str(int(command[1:])) + ")")
        elif command[0] == 'R':
            turtle.right(int(command[1:]))
            print("right(" + str(int(command[1:])) + ")")
        elif command[0] == 'B':
            turtle.backward(int(command[1:]))
            print("backward(" + str(int(command[1:])) + ")")
        elif command[0] == 'U':
            turtle.up()
            print("up()")
        elif command[0] == 'D':
            turtle.down()
            print("down()")
        elif command[0] == 'C':
            turtle.circle(int(command[1:]))
            print("circle(" + str(int(command[1:])) + ")")
        elif command[0] == 'I':
            evaluate(iterate(cmds, command[1:]))
        elif command[0] == 'P':
            side_length_evaluate = cmds[cmds.find(command[0:])+3:cmds.find(command[:2])+6]
            evaluate(polygon(command[1:], side_length_evaluate))


def iterate(input, iterate_num):
    """
    Translates the Enhanced TT command Iterate (which iterates contained commands) into basic TT commands
    :param input: the list of input basic TT commands
    :param iterate_num: number of times the contained commands iterate
    :return: string of basic commands that iterate the contained commands
    """
    repeat = input[input.find("I")+1:input.find("@")]
    toggle = int(iterate_num)
    new_string = ""
    while toggle != 1:
        new_string += " " + repeat
        toggle -= 1
    return new_string


def polygon(inputsides, inputlength):
    """
    Translates the Enhanced TT command Polygon (which creates a polygon of given side number and length) into basic TT
    commands
    :param inputsides: The number of sides the polygon will have
    :param inputlength: The lengths that the sides of the polygon will be
    :return: string of basic commands that create a polygon with the given parameters
    """
    side_nums = int(inputsides)
    side_length = inputlength
    new_string = ""
    if side_nums != 0:
        angle_btwn_sides = str(int(360/side_nums))
    while side_nums !=0:
        new_string += "F" + side_length + " L" + angle_btwn_sides + " "
        side_nums -=1
    return new_string

# only run this program if it is not being imported by another main module
if __name__ == '__main__':
    main()