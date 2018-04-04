"""Dean Trivisani"""


import turtle
import sys

def main():
    turt_cmd = input("Please enter a string containing only basic TinyTurtle commands: ")
    evaluate(turt_cmd)
    turtle.mainloop()


def evaluate(cmds):
    split_list = cmds.split()
    for command in split_list:
        if command[0] == 'F':
            turtle.forward(int(command[1:]))
        elif command[0] == 'L':
            turtle.left(int(command[1:]))
        elif command[0] == 'R':
            turtle.right(int(command[1:]))
        elif command[0] == 'B':
            turtle.backward(int(command[1:]))
        elif command[0] == 'U':
            turtle.up()
        elif command[0] == 'D':
            turtle.down()
        elif command[0] == 'C':
            turtle.circle(int(command[1:]))

if __name__ == '__main__':
    main()