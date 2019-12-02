import time


class Advent:

    def __init__(self, number_of_challenge):

        self._function_map = {1: self._challenge_1,
                              2: self._challenge_2}

        self._solution = self._function_map[number_of_challenge]()

        print("Solution = {}".format(self._solution))

    def _challenge_1(self):

        def _calc_fuel_for_mass(mass):
            return int(int(int(mass) / 3) - 2)

        with open('01-input.txt') as data:
            numbers = data.read().split()
            fuel = 0

            for number in numbers:
                fuel_add = _calc_fuel_for_mass(number)
                fuel += fuel_add
                while _calc_fuel_for_mass(fuel_add) > 0:
                    fuel_add = _calc_fuel_for_mass(fuel_add)
                    fuel += fuel_add

            return fuel

    def _challenge_2(self):
        with open('02-input.txt') as data:
            self._original_numbers = list(map(int, data.read().split(',')))

        self._final_noun = 0
        self._final_verb = 0

        def try_new_combination(op_code_array, noun_to_test, verb_to_test):
            op_code_array[1] = noun_to_test
            op_code_array[2] = verb_to_test

            for idx, val in enumerate(op_code_array):
                if idx % 4 == 0:
                    if val == 1:
                        op_code_array[op_code_array[idx + 3]] = op_code_array[op_code_array[idx + 1]] + op_code_array[
                            op_code_array[idx + 2]]
                    elif val == 2:
                        op_code_array[op_code_array[idx + 3]] = op_code_array[op_code_array[idx + 1]] * op_code_array[
                            op_code_array[idx + 2]]
                    else:
                        break
                else:
                    continue
            return op_code_array[0]

        for new_noun in range(0, 99):
            for new_verb in range(0, 99):
                numbers = list(self._original_numbers)
                if try_new_combination(numbers, new_noun, new_verb) == 19690720:
                    self._final_noun = new_noun
                    self._final_verb = new_verb
                    return 100 * self._final_noun + self._final_verb


if __name__ == '__main__':
    start = time.time()
    Advent(2)
    end = time.time()

    print("Computation time: {}".format(end - start))
