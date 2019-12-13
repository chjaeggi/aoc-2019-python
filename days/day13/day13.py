from PIL import Image

from days.day13.int_code_machine import IntCodeMachine


class Day13:

    def __init__(self):
        self._input = None
        self._result = None
        with open('inputs/13-input.txt') as data:
            self._original_numbers = list(map(int, data.read().split(',')))

    def solve(self, full_quiz=True):
        self._original_numbers.extend([0] * len(self._original_numbers))
        if full_quiz:
            self._original_numbers[0] = 2
            _, self._result = IntCodeMachine(self._original_numbers).run()
        else:
            self._result, _ = IntCodeMachine(self._original_numbers).run()
            self._result = sum(value == 2 for value in self._result.values())

        return self._result
