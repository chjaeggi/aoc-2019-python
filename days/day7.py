from itertools import permutations


class IntCodeMachine:

    def __init__(self, codes, phase):
        self._codes = codes
        self._phase_setting = phase
        self._phase_setting_done = False
        self._pointer = 0
        self._result = 0
        self._halted = False

    @property
    def has_halted(self):
        return self._halted

    def run(self, instruction_input):
        while not self._halted:
            op_code = str(self._codes[self._pointer]).zfill(5)

            if op_code.endswith('99'):
                self._halted = True
                return self._result

            if not (op_code.endswith('3') or op_code.endswith('4')):
                param1_poistion_mode = list(op_code)[2] == '0'
                param2_poistion_mode = list(op_code)[1] == '0'
                if param1_poistion_mode:
                    value1 = self._codes[self._codes[self._pointer + 1]]
                else:
                    value1 = self._codes[self._pointer + 1]
                if param2_poistion_mode:
                    value2 = self._codes[self._codes[self._pointer + 2]]
                else:
                    value2 = self._codes[self._pointer + 2]

            if op_code.endswith('1'):
                self._codes[self._codes[self._pointer + 3]] = value1 + value2
                self._pointer += 4

            elif op_code.endswith('2'):
                self._codes[self._codes[self._pointer + 3]] = value1 * value2
                self._pointer += 4

            elif op_code.endswith('3'):
                if not self._phase_setting_done:
                    self._phase_setting_done = True
                    self._codes[self._codes[self._pointer + 1]] = self._phase_setting
                else:
                    self._codes[self._codes[self._pointer + 1]] = instruction_input
                self._pointer += 2

            elif op_code.endswith('4'):
                self._result = self._codes[self._codes[self._pointer + 1]]
                self._pointer += 2
                return self._result

            elif op_code.endswith('5'):
                if value1 != 0:
                    self._pointer = value2
                else:
                    self._pointer += 3

            elif op_code.endswith('6'):
                if value1 == 0:
                    self._pointer = value2
                else:
                    self._pointer += 3

            elif op_code.endswith('7'):
                if value1 < value2:
                    self._codes[self._codes[self._pointer + 3]] = 1
                else:
                    self._codes[self._codes[self._pointer + 3]] = 0
                self._pointer += 4

            elif op_code.endswith('8'):
                if value1 == value2:
                    self._codes[self._codes[self._pointer + 3]] = 1
                else:
                    self._codes[self._codes[self._pointer + 3]] = 0
                self._pointer += 4

            else:
                print("Error, breaking now")
                break


class Day7:

    def __init__(self):
        self._original_numbers = None
        self._highest_output = 0
        self._global_input = 0
        with open('inputs/07-input.txt') as data:
            self._original_numbers = list(map(int, data.read().split(',')))

    def solve(self, full_quiz=True):
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
