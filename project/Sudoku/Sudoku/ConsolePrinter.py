"""
This file is a part of practice project created by Kapil Sharma, while learning Python

ConsolePrinter class: Print sudoku grid on
"""

from . import Grid


class ConsolePrinter:

    def __init__(self, grid):
        if not isinstance(grid, Grid.Grid):
            raise Exception('Need instance of Grid')
        self.grid = grid

    def print(self):
        for row_no in range(9):
            if row_no % 3 == 0:
                self.__printHorizontalLine()
            row = self.grid.get_row(row_no + 1)
            for col_no in range(9):
                if col_no % 3 == 0:
                    print('|', end='')
                cell = row[col_no]
                if cell is None:
                    print('  ', end='')
                else:
                    print(row[col_no], end='')
            print('|')
        self.__printHorizontalLine()

    def __printHorizontalLine(self):
        for _ in range(22):
            print('-', end='')
        print()
