class Day5:

    def __init__(self):
        self._original_numbers = None
        with open('inputs/05-input.txt') as data:
            self._original_numbers = list(map(int, data.read().split(',')))

    @staticmethod
    def _int_code_machine(starting_value, codes):
        pointer = 0

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
                codes[codes[pointer + 1]] = starting_value
                pointer += 2

            elif op_code.endswith('4'):
                result = codes[codes[pointer + 1]]
                if codes[pointer + 2] == 99:
                    return result
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

            else:
                print("Error, breaking now")
                break

    def solve(self, full_quiz=True):
        starting_input = 5 if full_quiz else 1
        return self._int_code_machine(starting_input, self._original_numbers)
