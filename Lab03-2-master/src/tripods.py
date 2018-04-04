"""
CSapx Lab 3: tripods.py

A program that reads a tripod puzzle grid from a file, then solves that puzzle

$ python3 tripods.py filename

The side length and levels are gotten from standard input.

author: Dean Trivisani
"""
import sys
import fileinput
import collections
import rit_sort

Tripod = collections.namedtuple('Tripod', ['sum', 'orientation', 'location'])

def save_puzzle():
    """
    Takes the puzzle taken from the given text file and saves it to a list
    :return: a list containing the values of the puzzle grid
    """
    grid = []
    for line in fileinput.input():
        split_line = line.split()
        grid.append(split_line)
    return grid

def display_puzzle(grid):
    """
    Prints the puzzle grid to standard output
    :param grid: the list containing the puzzle grid
    :return:
    """
    i = 0
    while i < len(grid):
        j = 0
        while j < len(grid[i]):
            print(grid[i][j] + " ", end="")
            j += 1
        print('')
        i += 1

def puzzle_length(grid):
    """
    Finds the total number of values in the puzzle grid
    :param grid: The list containing the puzzle grid
    :return: the number of values in the puzzle grid
    """
    length = 0
    i = 0
    while i < len(grid):
        j = 0
        while j < len(grid[i]):
            length += 1
            j += 1
        i += 1
    return length

def tripod_list(grid):
    """
    Creates a list of all of the tripods possible in the provided grid
    :param grid: the list containing the puzzle grid
    :return: the sorted list of all possible tripods
    """
    lst=[]
    for y in range(1, len(grid)):
        for x in range(1, len(grid[y])-1):
            tripod = Tripod((int(grid[y][x - 1]) + (int(grid[y][x + 1])) + (int(grid[y - 1][x]))), 'N', [y, x])
            lst.append(tripod)
    for y in range(1, len(grid)-1):
        for x in range(0, len(grid[y])-1):
            tripod = Tripod((int(grid[y + 1][x]) + (int(grid[y][x + 1])) + (int(grid[y - 1][x]))), 'E', [y, x])
            lst.append(tripod)
    for y in range(0, len(grid)-1):
        for x in range(1, len(grid[y])-1):
            tripod = Tripod((int(grid[y][x - 1]) + (int(grid[y][x + 1])) + (int(grid[y + 1][x]))), 'S', [y, x])
            lst.append(tripod)
    for y in range(1, len(grid)-1):
        for x in range(1, len(grid[y])):
            tripod = Tripod((int(grid[y + 1][x]) + (int(grid[y][x - 1])) + (int(grid[y - 1][x]))), 'W', [y, x])
            lst.append(tripod)
    sorted_lst = rit_sort.merge_sort(lst)
    return sorted_lst

def tripod_total(tripods):
    """
    Gives the total sum of all of the tripod sums combined
    :param tripods: the list of all of the tripods requested by the user
    :return: the sum of all of the tripod sums combined
    """
    total = 0
    for i in range (0, len(tripods)-1):
        total += int(tripods[i][0])
    return total

def display_num_tripods(num, tripods):
    """
    Displays the tripods requested by the user in a readable format
    :param num: the number of tripods requested by the user
    :param tripods: the list of all the tripods possible on the grid
    :return: all of the tripods requested by the user from highest to lowest in a friendly format
    """
    sum = 0
    for i in range (0, num):
        sum += int(tripods[i][0])
        print('loc: (' + str(tripods[i][2][0]) + ',' + str(tripods[i][2][1]) + '), facing: ' + str(tripods[i][1]) + ', sum: ' + str(tripods[i][0]))
    return sum

def main():
    """
    The main function. Checks if input is valid, and asks for the number of tripods the user would like displayed
    :return: None
    """
    if len(sys.argv) != 2:
        print('python3 tripods.py filename')
        quit()
    puzzle = save_puzzle()
    display_puzzle(puzzle)
    tripod_num = int(input("Enter number of tripods: "))
    if tripod_num > puzzle_length(puzzle) - 4:
        print('Too many tripods to place!')
        quit()
    all = tripod_list(puzzle)
    if tripod_num > 0:
        print('Optimal Placement:')
    sum = display_num_tripods(tripod_num, all)
    print('Total: ' + str(sum))

# only run this program if it is not being imported by another main module
if __name__ == '__main__':
    main()