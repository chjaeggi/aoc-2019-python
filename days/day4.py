class Day4:

    def __init__(self):
        self._full_quiz = None
        self._numbers = None
        self._number_of_solutions = 0
        with open('inputs/04-input.txt') as data:
            self._numbers = list(map(int, data.read().split('-')))

    @staticmethod
    def _is_decreasing(number):
        number_as_array = list(str(number))
        for idx, val in enumerate(number_as_array):
            if idx == 0:
                continue
            else:
                if val < number_as_array[idx - 1]:
                    return True
        return False

    def _has_double_digit(self, number):
        number_as_array = list(str(number))
        number_dict = {'0': 0, '1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0, }

        if self._full_quiz:
            for element in number_as_array:
                number_dict[element] += 1
            if 2 in number_dict.values():
                return True
            return False
        else:
            for idx, val in enumerate(number_as_array):
                if idx == 0:
                    continue
                else:
                    if val == number_as_array[idx - 1]:
                        return True
            return False

    def solve(self, full_quiz=True):
        self._full_quiz = full_quiz
        for element in range(self._numbers[0], self._numbers[1]):
            if self._has_double_digit(element) and not self._is_decreasing(element):
                self._number_of_solutions += 1
        return self._number_of_solutions
