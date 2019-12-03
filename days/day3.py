import sys


class Day3:

    def __init__(self):
        self._wire_one = []
        self._wire_two = []
        self._current_wire = None
        self._new_zero = (0, 0)
        self._wires = None
        with open('inputs/03-input.txt') as data:
            self._wires = data.readlines()

    @staticmethod
    def _shortest_manhattan_distance(array_of_coordinates):
        local_minimum = sys.maxsize
        for idx, val in enumerate(array_of_coordinates):
            new_minimum = abs(val[0]) + abs(val[1])
            if local_minimum > new_minimum:
                local_minimum = new_minimum
        return local_minimum

    def _append_coordinates_to_wire(self, wire, direction, distance):
        if direction is 'R':
            for idx in range(0, int(distance)):
                self._new_zero = self._new_zero[0] + 1, self._new_zero[1]
                wire.append(self._new_zero)
        if direction is 'L':
            for idx in range(0, int(distance)):
                self._new_zero = self._new_zero[0] - 1, self._new_zero[1]
                wire.append(self._new_zero)
        if direction is 'U':
            for idx in range(0, int(distance)):
                self._new_zero = self._new_zero[0], self._new_zero[1] + 1
                wire.append(self._new_zero)
        if direction is 'D':
            for idx in range(0, int(distance)):
                self._new_zero = self._new_zero[0], self._new_zero[1] - 1
                wire.append(self._new_zero)

    def solve(self, full_quiz=True):
        for idx, wire in enumerate(self._wires):
            self._new_zero = (0, 0)
            input_instructions = wire.split(',')

            self._current_wire = self._wire_one if idx == 0 else self._wire_two

            for element in input_instructions:
                direction = element[:1]
                distance = element[1:]
                self._append_coordinates_to_wire(self._current_wire, direction, distance)

        intersections = list(set(self._wire_one) & set(self._wire_two))

        if not full_quiz:
            return self._shortest_manhattan_distance(intersections)

        indices_wire_one = [self._wire_one.index(x) + 1 for x in intersections]
        indices_wire_two = [self._wire_two.index(x) + 1 for x in intersections]

        local_minimum = sys.maxsize
        for idx, val in enumerate(indices_wire_one):
            new_minimum = indices_wire_one[idx] + indices_wire_two[idx]
            if local_minimum > new_minimum:
                local_minimum = new_minimum
        return local_minimum
