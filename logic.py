import random


def new_game(n):
    # matrix = [[5, 2, 7, 3], [9, 1, 15, 4], [10, 6, 8, 12], [13, 11, 14, 0]]
    matrix = []

    numbers = [x for x in range(n*n)]
    random.shuffle(numbers)

    for i in range(n):
        row = []
        for j in range(n):
            row.append(numbers.pop())
        matrix.append(row)
    return matrix


# Check whether the correct order of numbers has been reached
def game_state(mat, n):

    solution = []

    for i in range(n):
        row = []
        for j in range(n):
            row.append(i*n+j+1)
        solution.append(row)
    solution[n-1][n-1] = 0

    if mat == solution:
        return 'win'
    return 'not over'


# Define a function which finds the location of 0 in a 4x4 array and returns it as a tuple (x,y) where the top
# left corner is (0,0).


def find_zero(array):
    location = (0, 0)
    y = 0
    for row in array:
        if row.count(0) == 1:
            location = (row.index(0), y)
        else:
            y += 1
    return location


# Now define the functions which allow the 0 tile, representing the blank tile from the puzzle,
# to move up, down, left and right.
def up(array):
    # If the 0 is not in the top row swap the 0 with the number above it.
    x, y = find_zero(array)
    if y != 0:
        # Find the number to swap with
        number_to_swap = array[y-1][x]
        # Set the 0 to the new number
        array[y][x] = number_to_swap
        # Set the number to swap with to 0.
        array[y-1][x] = 0

    return array


def down(array):
    # If the 0 is in the bottom row return an error code
    x, y = find_zero(array)
    if y != len(array) - 1:
        # Find the number to swap with
        number_to_swap = array[y+1][x]
        # Set the 0 to the new number
        array[y][x] = number_to_swap
        # Set the number to swap with to 0.
        array[y+1][x] = 0

    return array


def left(array):
    # If the 0 is in the left column return an error code
    x, y = find_zero(array)
    if x != 0:
        # Find the number to swap with
        number_to_swap = array[y][x-1]
        # Set the 0 to the new number
        array[y][x] = number_to_swap
        # Set the number to swap with to 0.
        array[y][x-1] = 0

    return array


def right(array):
    # If the 0 is in the right column return an error code
    x, y = find_zero(array)
    if x != len(array) - 1:
        # Find the number to swap with
        number_to_swap = array[y][x+1]
        # Set the 0 to the new number
        array[y][x] = number_to_swap
        # Set the number to swap with to 0.
        array[y][x+1] = 0

    return array
