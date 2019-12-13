from collections import OrderedDict


class IntCodeMachine:
    POSITION_MODE = '0'
    IMMEDIATE_MODE = '1'
    RELATIVE_MODE = '2'

    TILE_EMPTY = 0
    TILE_WALL = 1
    TILE_BLOCK = 2
    TILE_HORIZONTAL_PADDLE = 3
    TILE_BALL = 4

    STATE_X = 0
    STATE_Y = 1
    STATE_TILE = 2

    PADDLE_STAY = 0
    PADDLE_LEFT = -1
    PADDLE_RIGHT = 1

    def __init__(self, codes):
        self._codes = codes
        self._pointer = 0
        self._relative_base = 0
        self._result = 0
        self._halted = False

        self._map = {}
        self._command_state = 0
        self._current_x = 0
        self._current_y = 0

        self._ball_position = ()  # (x, y)
        self._paddle_position = 0  # only x

        self._score = 0

    @property
    def has_halted(self):
        return self._halted

    def _interpret_output(self):
        if self._command_state == 0:
            self._command_state += 1
            self._current_x = self._result
        elif self._command_state == 1:
            self._command_state += 1
            self._current_y = self._result
        else:
            if self._current_x == -1 and self._current_y == 0:
                self._score = self._result
            elif self._result == self.TILE_BALL:
                self._ball_position = self._current_x, self._current_y

            elif self._result == self.TILE_HORIZONTAL_PADDLE:
                self._paddle_position = self._current_x
            else:
                self._map[(self._current_x, self._current_y)] = self._result
            self._command_state = 0
            self._current_x = 0
            self._current_y = 0

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

    def _handle_input(self):
        if self._paddle_position > self._ball_position[0]:
            instruction = self.PADDLE_LEFT
        elif self._paddle_position < self._ball_position[0]:
            instruction = self.PADDLE_RIGHT
        else:
            instruction = self.PADDLE_STAY
        return instruction

    def run(self):
        while not self._halted:
            op_code = str(self._codes[self._pointer]).zfill(5)

            if op_code.endswith('99'):
                self._halted = True
                return self._map, self._score

            arg1_address, arg2_address, arg3_address = self._get_argument_addresses(op_code)

            if op_code.endswith('1'):
                self._codes[arg3_address] = self._codes[arg1_address] + self._codes[arg2_address]
                self._pointer += 4

            elif op_code.endswith('2'):
                self._codes[arg3_address] = self._codes[arg1_address] * self._codes[arg2_address]
                self._pointer += 4

            elif op_code.endswith('3'):
                self._codes[arg1_address] = self._handle_input()
                self._pointer += 2

            elif op_code.endswith('4'):
                self._result = self._codes[arg1_address]
                self._interpret_output()
                self._pointer += 2

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
