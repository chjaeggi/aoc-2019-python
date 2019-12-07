from itertools import permutations

from days.day7.int_code_machine import IntCodeMachine


class Day7_2:

    def __init__(self):
        self._original_numbers = None
        self._highest_output = 0
        self._global_input = 0
        with open('inputs/07-input.txt') as data:
            self._original_numbers = list(map(int, data.read().split(',')))

    def solve(self):
        possible_sequences = list(permutations([5, 6, 7, 8, 9]))
        for possible_sequence in possible_sequences:
            int_code_machines = []
            for index, element in enumerate(possible_sequence):
                int_code_machines.append(IntCodeMachine(self._original_numbers, element))

            current_index = 0
            while not int_code_machines[4].has_halted:
                self._global_input = int_code_machines[current_index].run(self._global_input)
                if current_index < 4:
                    current_index += 1
                else:
                    current_index = 0

            if self._highest_output < self._global_input:
                self._highest_output = self._global_input
            self._global_input = 0

        return self._highest_output
