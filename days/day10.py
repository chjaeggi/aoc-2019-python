import math
from math import sqrt

import numpy as np


class Day10:

    def __init__(self):
        self._input = None
        self._result = None
        self._asteroids = []
        self._number_of_asteroids = 0
        self._can_see = {}
        self._can_shoot = []
        self._max = 0
        self._max_coords = ()

        with open('inputs/10-input.txt') as data:
            self._input = data.read().split()
            for line in self._input:
                self._asteroids.append(list(line))
                self._number_of_asteroids += line.count('#')

    @staticmethod
    def angle_between(p1, p2):
        ang1 = np.arctan2(*p1)
        ang2 = np.arctan2(*p2)
        return np.rad2deg((ang1 - ang2) % (2 * np.pi))

    def solve(self, full_quiz=True):

        for y, line in enumerate(self._asteroids):
            for x, asteroid in enumerate(line):
                if asteroid == '#':
                    self._can_see[(x, y)] = []

        for coords in self._can_see.keys():
            for second_coords in self._can_see.keys():
                if second_coords == coords:
                    continue
                resulting_vector = (second_coords[0] - coords[0], second_coords[1] - coords[1])
                length = sqrt(resulting_vector[0] ** 2 + resulting_vector[1] ** 2)
                gcd = math.gcd(resulting_vector[0], resulting_vector[1])
                norm_vector = (resulting_vector[0] / gcd, resulting_vector[1] / gcd)

                if coords == (17, 23):
                    theta = self.angle_between((0, -1), (resulting_vector[0], resulting_vector[1]))
                    self._can_shoot.append((theta, length, second_coords))

                if norm_vector not in self._can_see[coords]:
                    self._can_see[coords].append(norm_vector)

            if self._max < len(self._can_see[coords]):
                self._max = len(self._can_see[coords])
                self._max_coords = coords

        can_shoot_sorted = sorted(self._can_shoot, key=lambda element: (element[0], element[1]))

        current_angle = -1.0
        counter = 0
        shoot_counter = 0

        while True:
            if current_angle < can_shoot_sorted[counter][0]:
                current_angle = can_shoot_sorted[counter][0]
                shoot_counter += 1
                if shoot_counter == 200:
                    print(can_shoot_sorted[counter][2])
                    break
                current_angle %= 360
                can_shoot_sorted.pop(counter)
                counter -= 1
            counter += 1
            if counter >= len(can_shoot_sorted):
                counter = 0
                current_angle = -1.0

        print("{} at {}".format(self._max, self._max_coords))
        return self._max
