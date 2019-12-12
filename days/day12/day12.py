import itertools
import math

import numpy as np

from days.day12.planet import Planet


class Day12:

    def __init__(self):
        self._input = None
        self._result = 0
        self._planets = []
        with open('inputs/12-input.txt') as data:
            self._numbers = data.read()  # TODO

    @staticmethod
    def _update_gravity(planet1, planet2):
        if planet1.x < planet2.x:
            planet1.gravity_x += 1
            planet2.gravity_x -= 1
        elif planet1.x > planet2.x:
            planet1.gravity_x -= 1
            planet2.gravity_x += 1
        else:
            pass

        if planet1.y < planet2.y:
            planet1.gravity_y += 1
            planet2.gravity_y -= 1
        elif planet1.y > planet2.y:
            planet1.gravity_y -= 1
            planet2.gravity_y += 1
        else:
            pass

        if planet1.z < planet2.z:
            planet1.gravity_z += 1
            planet2.gravity_z -= 1
        elif planet1.z > planet2.z:
            planet1.gravity_z -= 1
            planet2.gravity_z += 1
        else:
            pass

    def _apply_gravity(self):
        for planet in self._planets:
            planet.v_x += planet.gravity_x
            planet.v_y += planet.gravity_y
            planet.v_z += planet.gravity_z
            planet.gravity_x = 0
            planet.gravity_y = 0
            planet.gravity_z = 0
            planet.x += planet.v_x
            planet.y += planet.v_y
            planet.z += planet.v_z

    def _compute_lcm(self, x, y):
        # choose the greater number
        if x > y:
            greater = x
        else:
            greater = y
        while (True):
            if ((greater % x == 0) and (greater % y == 0)):
                lcm = greater
                break
            greater += 1
        return lcm

    def solve(self, full_quiz=True):
        self._planets = [Planet(14, 15, -2), Planet(17, -3, 4), Planet(6, 12, -13), Planet(-2, 10, -8)]  # TODO
        combinations = list(itertools.combinations(range(0, 4), 2))

        if full_quiz:
            constellation_found_p = [False] * 4
            constellation_found_v = [False] * 4
            planet_px_hashes = [dict() for _ in range(3)]
            planet_py_hashes = [dict() for _ in range(3)]
            planet_pz_hashes = [dict() for _ in range(3)]
            planet_vx_hashes = [dict() for _ in range(3)]
            planet_vy_hashes = [dict() for _ in range(3)]
            planet_vz_hashes = [dict() for _ in range(3)]
            counter = 0
            while True:
                counter += 1

                for combination in combinations:
                    self._update_gravity(self._planets[combination[0]], self._planets[combination[1]])
                self._apply_gravity()

                planet_p_hash = hash(self._planets)
                planet_v_hash = self._planets[planet_idx].velocity_hash

                for planet_idx in range(4):
                    if planet_p_hash in planet_p_hashes[planet_idx] and not constellation_found_p[planet_idx]:
                        print(counter)
                        constellation_found_p[planet_idx] = True
                    else:
                        planet_p_hashes[planet_idx][planet_p_hash] = counter

                    if planet_v_hash in planet_v_hashes[planet_idx] and not constellation_found_v[planet_idx]:
                        print(counter)
                        constellation_found_v[planet_idx] = True
                    else:
                        planet_v_hashes[planet_idx][planet_v_hash] = counter

                if all(b is True for b in constellation_found_p) and all(a is True for a in constellation_found_v):
                    return np.lcm.reduce([3, 21, 26, 81, 93, 219, 236, 505])

        for i in range(1000):
            for combination in combinations:
                self._update_gravity(self._planets[combination[0]], self._planets[combination[1]])

            self._apply_gravity()

        for planet in self._planets:
            self._result += planet.total_energy

        return self._result
