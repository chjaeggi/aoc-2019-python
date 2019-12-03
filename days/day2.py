class Day2:

    def __init__(self):
        self._final_noun = 0
        self._final_verb = 0
        self._original_numbers = None
        with open('inputs/02-input.txt') as data:
            self._original_numbers = list(map(int, data.read().split(',')))

    @staticmethod
    def _try_new_combination(codes, noun_to_test, verb_to_test):
        codes[1] = noun_to_test
        codes[2] = verb_to_test

        for idx, val in enumerate(codes):
            if idx % 4 == 0:
                if val == 1:
                    codes[codes[idx + 3]] = codes[codes[idx + 1]] + codes[codes[idx + 2]]
                elif val == 2:
                    codes[codes[idx + 3]] = codes[codes[idx + 1]] * codes[codes[idx + 2]]
                else:
                    break
            else:
                continue
        return codes[0]

    def solve(self, full_quiz=True):

        if not full_quiz:
            return self._try_new_combination(self._original_numbers, 12, 2)

        for new_noun in range(0, 100):
            for new_verb in range(0, 100):
                numbers = list(self._original_numbers)
                if self._try_new_combination(numbers, new_noun, new_verb) == 19690720:
                    self._final_noun = new_noun
                    self._final_verb = new_verb
                    return 100 * self._final_noun + self._final_verb


