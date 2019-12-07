from itertools import permutations


class Day7:

    def __init__(self):
        self._original_numbers = None
        self._highest_output = 0
        with open('inputs/07-input.txt') as data:
            self._original_numbers = list(map(int, data.read().split(',')))

    @staticmethod
    def _int_code_machine(input_instruction, phase_setting, codes):
        pointer = 0
        phase_setting_done = False
        result = 0
        while True:
            op_code = str(codes[pointer]).zfill(5)

            if not (op_code.endswith('3') or op_code.endswith('4')):
                param1_poistion_mode = list(op_code)[2] == '0'
                param2_poistion_mode = list(op_code)[1] == '0'
                if param1_poistion_mode:
                    value1 = codes[codes[pointer + 1]]
                else:
                    value1 = codes[pointer + 1]
                if param2_poistion_mode:
                    value2 = codes[codes[pointer + 2]]
                else:
                    value2 = codes[pointer + 2]

            if op_code.endswith('1'):
                codes[codes[pointer + 3]] = value1 + value2
                pointer += 4

            elif op_code.endswith('2'):
                codes[codes[pointer + 3]] = value1 * value2
                pointer += 4

            elif op_code.endswith('3'):
                if not phase_setting_done:
                    phase_setting_done = True
                    codes[codes[pointer + 1]] = phase_setting
                else:
                    codes[codes[pointer + 1]] = input_instruction
                pointer += 2

            elif op_code.endswith('4'):
                result = codes[codes[pointer + 1]]
                pointer += 2

            elif op_code.endswith('5'):
                if value1 != 0:
                    pointer = value2
                else:
                    pointer += 3

            elif op_code.endswith('6'):
                if value1 == 0:
                    pointer = value2
                else:
                    pointer += 3

            elif op_code.endswith('7'):
                if value1 < value2:
                    codes[codes[pointer + 3]] = 1
                else:
                    codes[codes[pointer + 3]] = 0
                pointer += 4

            elif op_code.endswith('8'):
                if value1 == value2:
                    codes[codes[pointer + 3]] = 1
                else:
                    codes[codes[pointer + 3]] = 0
                pointer += 4

            elif op_code.endswith('99'):
                return result

            else:
                print("Error, breaking now")
                break

    def solve(self, full_quiz=True):
        input_instruction = 0
        possible_sequences = list(permutations([0, 1, 2, 3, 4]))
        for possible_sequence in possible_sequences:
            for element in possible_sequence:
                input_instruction = self._int_code_machine(input_instruction, element, self._original_numbers)

            if self._highest_output < input_instruction:
                self._highest_output = input_instruction
            input_instruction = 0

        return self._highest_output
