from random import choice, randint
import pygame

def GenerateSudoku() -> list:
    Sudoku = []
    for x in range(0, 9):
        tempx = []
        for y in range(0, 9):
            number = choice(list(range(0, 10)))
            while True:
                if number != 0:
                    if number in tempx:
                        number = choice(list(range(0, 10)))
                    notvalid = False
                    for x in Sudoku:
                        if x[y] == number:
                            notvalid = True
                    if notvalid:
                        number = choice(list(range(0, 10)))
                    else:
                        break
                else:
                    break
            tempx.append(number)
        Sudoku.append(tempx)
    for i in range(0, randint(0, 25)):
        Sudoku[randint(0, 8)][randint(0, 8)] = 0

    return Sudoku