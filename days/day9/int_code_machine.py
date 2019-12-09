class IntCodeMachine:
    POSITION_MODE = '0'
    IMMEDIATE_MODE = '1'
    RELATIVE_MODE = '2'

    def __init__(self, codes):
        self._codes = codes
        self._pointer = 0
        self._relative_base = 0
        self._result = 0
        self._halted = False

    @property
    def has_halted(self):
        return self._halted

    def _get_argument_addresses(self, op_code):

        param_modes = [list(op_code)[2], list(op_code)[1], list(op_code)[0]]
        addresses = [''] * 3

        for idx in range(len(param_modes)):
            if param_modes[idx] == self.POSITION_MODE:
                addresses[idx] = self._codes[self._pointer + 1 + idx]
            elif param_modes[idx] == self.IMMEDIATE_MODE:
                addresses[idx] = self._pointer + 1 + idx
            else:
                addresses[idx] = self._relative_base + self._codes[self._pointer + 1 + idx]
        return addresses[0], addresses[1], addresses[2]

    def run(self, instruction_input):
        while not self._halted:
            op_code = str(self._codes[self._pointer]).zfill(5)

            if op_code.endswith('99'):
                self._halted = True
                return self._result

            arg1_address, arg2_address, arg3_address = self._get_argument_addresses(op_code)

            if op_code.endswith('1'):
                self._codes[arg3_address] = self._codes[arg1_address] + self._codes[arg2_address]
                self._pointer += 4

            elif op_code.endswith('2'):
                self._codes[arg3_address] = self._codes[arg1_address] * self._codes[arg2_address]
                self._pointer += 4

            elif op_code.endswith('3'):
                self._codes[arg1_address] = instruction_input
                self._pointer += 2

            elif op_code.endswith('4'):
                self._result = self._codes[arg1_address]
                self._pointer += 2
                print(self._result)

            elif op_code.endswith('5'):
                if self._codes[arg1_address] != 0:
                    self._pointer = self._codes[arg2_address]
                else:
                    self._pointer += 3

            elif op_code.endswith('6'):
                if self._codes[arg1_address] == 0:
                    self._pointer = self._codes[arg2_address]
                else:
                    self._pointer += 3

            elif op_code.endswith('7'):
                if self._codes[arg1_address] < self._codes[arg2_address]:
                    self._codes[arg3_address] = 1
                else:
                    self._codes[arg3_address] = 0
                self._pointer += 4

            elif op_code.endswith('8'):
                if self._codes[arg1_address] == self._codes[arg2_address]:
                    self._codes[arg3_address] = 1
                else:
                    self._codes[arg3_address] = 0
                self._pointer += 4

            elif op_code.endswith('9'):
                self._relative_base += self._codes[arg1_address]
                self._pointer += 2

            else:
                print("Error, breaking now")
                break
