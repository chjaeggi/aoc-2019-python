import math
from math import sqrt

import numpy as np


class Day13:

    def __init__(self):
        self._input = None
        self._result = None
        with open('inputs/13-input.txt') as data:
            self._input = data.read()

    def solve(self, full_quiz=True):
        return self._result
