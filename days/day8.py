class Day8:

    def __init__(self):
        self._input = None
        with open('inputs/08-input.txt') as data:
            self._input = data.read().split()

    def solve(self, full_quiz=True):
        return self._input
