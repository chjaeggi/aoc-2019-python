import math
from math import sqrt

import numpy as np


class Day10:

    def __init__(self):
        self._input = None
        self._result = None
        self._asteroids = []
        self._can_see = {}
        self._can_shoot = {}
        self._max = 0
        self._max_coords = ()

        with open('inputs/10-input.txt') as data:
            self._input = data.read().split()
            for line in self._input:
                self._asteroids.append(list(line))

    def _get_coords_for_shot_number(self, can_shoot_sorted, number):
        current_angle = -1.0
        counter = 0
        shoot_counter = 0
        while shoot_counter < 200:
            if current_angle < can_shoot_sorted[counter][0]:
                current_angle = can_shoot_sorted[counter][0]
                shoot_counter += 1
                if shoot_counter == number:
                    return can_shoot_sorted[counter][2]
                current_angle %= 360
                can_shoot_sorted.pop(counter)
                counter -= 1  # the popped one
            counter += 1
            if counter >= len(can_shoot_sorted):  # ring-buffer back to beginning
                counter = 0
                current_angle = -1.0

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
                gcd = math.gcd(resulting_vector[0], resulting_vector[1])
                norm_vector = (resulting_vector[0] / gcd, resulting_vector[1] / gcd)

                if full_quiz:
                    length = sqrt(resulting_vector[0] ** 2 + resulting_vector[1] ** 2)
                    theta = self.angle_between((0, -1), (resulting_vector[0], resulting_vector[1]))
                    try:
                        self._can_shoot[coords].append((theta, length, second_coords))
                    except KeyError:
                        self._can_shoot[coords] = [(theta, length, second_coords)]

                if norm_vector not in self._can_see[coords]:
                    self._can_see[coords].append(norm_vector)

            if self._max < len(self._can_see[coords]):
                self._max = len(self._can_see[coords])
                self._max_coords = coords

        self._result = "{} at {}".format(self._max, self._max_coords)

        if full_quiz:
            can_shoot_sorted = sorted(self._can_shoot[self._max_coords], key=lambda element: (element[0], element[1]))
            self._result = self._get_coords_for_shot_number(can_shoot_sorted, 200)

        return self._result
