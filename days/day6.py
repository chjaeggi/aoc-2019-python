class Day6:

    def __init__(self):
        self._original_numbers = None
        with open('inputs/06-input.txt') as data:
            self._original_numbers = list(map(int, data.read().split(',')))

    def solve(self, full_quiz=True):
        pass
