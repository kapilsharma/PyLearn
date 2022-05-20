"""
This file is a part of practice project created by Kapil Sharma, while learning Python

Engine class: Define the Sudoku Engine
"""

from . import Grid
from . import ConsolePrinter


class Engine:

    def __init__(self):
        self.grid = Grid.Grid()
        self.printer = ConsolePrinter.ConsolePrinter(self.grid)