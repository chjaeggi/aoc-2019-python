import sys

from PIL import Image


class Day8:

    def __init__(self):
        self._input = None
        self._layers = []
        self._height = 6
        self._width = 25
        self._number_of_layers = 0
        self._number_of_0 = []
        self._number_of_1 = []
        self._number_of_2 = []
        with open('inputs/08-input.txt') as data:
            self._input = list(data.read())

    def solve(self, full_quiz=True):
        layer_number = 0

        self._number_of_layers = int(len(self._input) / (self._height * self._width))
        for _ in range(self._number_of_layers):
            self._layers.append([])
            for line in range(self._height):
                for pixel in range(self._width):
                    self._layers[layer_number].append(self._input.pop(0))
            self._number_of_0.append(len([i for i, v in enumerate(self._layers[layer_number]) if v == '0']))
            self._number_of_1.append(len([i for i, v in enumerate(self._layers[layer_number]) if v == '1']))
            self._number_of_2.append(len([i for i, v in enumerate(self._layers[layer_number]) if v == '2']))
            layer_number += 1

        min_0 = sys.maxsize
        result = 0
        for index, element in enumerate(self._number_of_0):
            if min_0 > element:
                result = self._number_of_1[index] * self._number_of_2[index]
                min_0 = element

        if full_quiz:
            pixels = [2] * self._height * self._width
            for index in range(len(pixels)):
                for layer in self._layers:
                    if int(layer[index]) != 2 and pixels[index] == 2:
                        pixels[index] = int(layer[index])

            image_out = Image.new('1', (self._width, self._height))
            image_out.putdata(pixels)
            image_out.save('days/day8/answer.png')
            image_out.show()
            return "See solution open image viewer"

        return result
