"""
This file is a part of practice project created by Kapil Sharma, while learning Python

Game class: Define the Game logic
"""

from . import Engine
from . import util


class Game:

    def __init__(self):
        self.engine = Engine.Engine()

        util.welcome()

