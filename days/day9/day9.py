import sys

from days.day9.int_code_machine import IntCodeMachine


class Day9:

    def __init__(self):
        self._input = None
        self._result = None
        with open('inputs/09-input.txt') as data:
            self._original_numbers = list(map(int, data.read().split(',')))

    def solve(self, full_quiz=True):
        arr = [0] * len(self._original_numbers)
        self._original_numbers.extend(arr)
        if full_quiz:
            result = IntCodeMachine(self._original_numbers).run(2)
        else:
            result = IntCodeMachine(self._original_numbers).run(1)
        return result

