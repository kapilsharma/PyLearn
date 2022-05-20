"""
This file is a part of practice project created by Kapil Sharma, while learning Python

Grid class: Define the Sudoku grid
"""


class Grid:

    def __init__(self):
        self.grid = [
            # Row 1
            [None, None, None, None, None, None, None, None, None],
            # Row 2
            [None, None, None, None, None, None, None, None, None],
            # Row 3
            [None, None, None, None, None, None, None, None, None],
            # Row 4
            [None, None, None, None, None, None, None, None, None],
            # Row 5
            [None, None, None, None, None, None, None, None, None],
            # Row 6
            [None, None, None, None, None, None, None, None, None],
            # Row 7
            [None, None, None, None, None, None, None, None, None],
            # Row 8
            [None, None, None, None, None, None, None, None, None],
            # Row 9
            [None, None, None, None, None, None, None, None, None]
        ]

    def get_row(self, row_number):
        return self.grid[row_number - 1]

    def get_column(self, column_number):
        column = []
        for num in range(9):
            column.append(self.grid[num][column_number - 1])
        return column

    def get_box(self, box_no):
        pass

    def set_cell(self, row, column, value):
        if not (self.__validate(row) and self.__validate(column) and self.__validate(value)):
            return False

        self.grid[row - 1][column - 1] = value

        return True

    def __validate(self, num, min=1, max=9):
        if not (isinstance(num, int) and isinstance(min, int) and isinstance(max, int)):
            return False
        if num < min or num > max:
            return False
        return True
