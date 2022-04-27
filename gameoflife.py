import numpy as np
import os
import time
import random

HEIGHT = 20
WIDTH = 20


DEAD = 0
ALIVE = 1


board = np.zeros([HEIGHT,WIDTH])
image = np.zeros([HEIGHT,WIDTH])

# INITIAL CONDITIONS.


def square(row, col):
    board[row, col] = ALIVE
    board[row + 1, col] = ALIVE
    board[row + 1, col+ 1] = ALIVE
    board[row, col + 1] = ALIVE


def boat(row, col):
    board[row, col] = ALIVE
    board[row + 1, col] = ALIVE
    board[row, col + 1] = ALIVE
    board[row + 2, col + 1] = ALIVE
    board[row + 1, col + 2] = ALIVE


def loaf(row,col):
    board[row, col] = ALIVE
    board[row, col + 1] = ALIVE
    board[row + 1, col - 1] = ALIVE
    board[row + 2, col - 1] = ALIVE
    board[row + 3, col] = ALIVE
    board[row + 2, col + 1] = ALIVE
    board[row + 1, col + 2] = ALIVE


def ship(row,col):
    board[row, col] = ALIVE
    board[row, col + 1] = ALIVE
    board[row + 1, col] = ALIVE
    board[row + 2, col + 1] = ALIVE
    board[row + 2, col + 2] = ALIVE
    board[row + 2, col + 1] = ALIVE


def is_alive(row, col):
    if board[row][col] == 0:
        return False
    else:
        return True


def check_box(row,col):
    values = []
    for i in range(row-1, row+2):
        for j in range(col-1, col + 2):
            if i == row and j == col:
                continue
            values.append(board[i%HEIGHT,j%WIDTH])

    return sum(values)


def main():
    for i in range(HEIGHT):
        for j in range(WIDTH):
            if is_alive(i, j):
                if check_box(i, j) <= 1:     # SOLITUDE.
                    board[i, j] = DEAD

                if check_box(i, j) >= 4:     # OVERPOPULATION.
                    board[i, j] = DEAD

                if check_box(i,j) == 2 or check_box(i, j) == 3:      # SURVIVE.
                    board[i, j] = ALIVE

            else:

                if check_box(i, j) == 3:
                    board[i, j] = ALIVE



def random_gen(rangeof):
    a = random.randint(0,rangeof)
    b = random.randint(0,rangeof)
    return a,b

square(random.randint(0,WIDTH-5),random.randint(0,WIDTH-5))
boat(random.randint(0,WIDTH-5),random.randint(0,WIDTH-5))
loaf(random.randint(0,WIDTH-5),random.randint(0,WIDTH-5))
ship(random.randint(0,WIDTH-5),random.randint(0,WIDTH-5))



iteration = 0
while iteration < 50:
    print(board, end="\r")
    main()
    time.sleep(1)
    os.system("clear")
    iteration += 1









