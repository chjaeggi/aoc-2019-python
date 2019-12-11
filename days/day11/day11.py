import sys
from collections import OrderedDict

from PIL import Image

from days.day11.int_code_machine import IntCodeMachine


class Day11:

    def __init__(self):
        self._input = None
        self._result = None
        with open('inputs/11-input.txt') as data:
            self._original_numbers = list(map(int, data.read().split(',')))

    def solve(self, full_quiz=True):
        self._original_numbers.extend([0] * len(self._original_numbers))
        if full_quiz:
            result = IntCodeMachine(self._original_numbers).run(1)
            max_x = 0
            max_y = 0

            for key, value in result.items():
                if key[0] > max_x:
                    max_x = key[0]

                if key[1] > max_y:
                    max_y = key[1]

            for row in range(max_y+1):
                line = list('')
                for col in range(max_x+1):
                    try:
                        res = result[(col, row)]
                        if res == 1:
                            line.append("#")
                        else:
                            line.append(".")
                    except KeyError:
                        result[(col, row)] = 0
                        line.append(".")
                print(line)

        else:
            result = len(IntCodeMachine(self._original_numbers).run(0))

        return result
