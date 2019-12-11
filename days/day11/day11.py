from PIL import Image

from days.day11.int_code_machine import IntCodeMachine


class Day11:

    def __init__(self):
        self._input = None
        self._result = None
        with open('inputs/11-input.txt') as data:
            self._original_numbers = list(map(int, data.read().split(',')))

    @staticmethod
    def _get_offsets(img_map):
        max_x = 0
        max_y = 0
        for key, value in img_map.items():
            if key[0] > max_x:
                max_x = key[0]

            if key[1] > max_y:
                max_y = key[1]
        return max_x, max_y

    @staticmethod
    def _create_image_vector(image_map, max_x, max_y):
        pic = []
        for row in range(max_y + 1):
            for col in range(max_x + 1):
                try:
                    res = image_map[(col, row)]
                    pic.append(res)
                except KeyError:
                    pic.append(0)
        return pic

    def solve(self, full_quiz=True):
        self._original_numbers.extend([0] * len(self._original_numbers))
        if full_quiz:
            img_map = IntCodeMachine(self._original_numbers).run(1)
            x_max, y_max = self._get_offsets(img_map)

            image_out = Image.new('1', (x_max + 1, y_max + 1))
            image_out.putdata(self._create_image_vector(img_map, x_max, y_max))
            image_out.save('days/day11/answer.png')
            image_out.show()

        else:
            self._result = len(IntCodeMachine(self._original_numbers).run(0))
            return self._result
