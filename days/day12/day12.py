import itertools

import numpy as np

from days.day12.planet import Planet


class Day12:

    def __init__(self):
        self._input = None
        self._result = 0
        self._planets = []
        self._iterations_per_axis = [0] * 3

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

    def solve(self, full_quiz=True):
        self._planets = [Planet(14, 15, -2), Planet(17, -3, 4), Planet(6, 12, -13), Planet(-2, 10, -8)]
        combinations = list(itertools.combinations(range(len(self._planets)), 2))

        if full_quiz:
            planet_px_hashes = {}
            planet_py_hashes = {}
            planet_pz_hashes = {}
            x_repeated = False
            y_repeated = False
            z_repeated = False
            counter = 0
            while not (x_repeated and y_repeated and z_repeated):

                px_hash = hash((self._planets[0].x, self._planets[1].x,
                                self._planets[2].x, self._planets[3].x,
                                self._planets[0].v_x, self._planets[1].v_x,
                                self._planets[2].v_x, self._planets[3].v_x))

                py_hash = hash((self._planets[0].y, self._planets[1].y,
                                self._planets[2].y, self._planets[3].y,
                                self._planets[0].v_y, self._planets[1].v_y,
                                self._planets[2].v_y, self._planets[3].v_y))

                pz_hash = hash((self._planets[0].z, self._planets[1].z,
                                self._planets[2].z, self._planets[3].z,
                                self._planets[0].v_z, self._planets[1].v_z,
                                self._planets[2].v_z, self._planets[3].v_z))

                if not x_repeated:
                    if px_hash in planet_px_hashes:
                        x_repeated = True
                        self._iterations_per_axis[0] = counter
                    else:
                        planet_px_hashes[px_hash] = counter

                if not y_repeated:
                    if py_hash in planet_py_hashes:
                        y_repeated = True
                        self._iterations_per_axis[1] = counter
                    else:
                        planet_py_hashes[py_hash] = counter

                if not z_repeated:
                    if pz_hash in planet_pz_hashes:
                        z_repeated = True
                        self._iterations_per_axis[2] = counter
                    else:
                        planet_pz_hashes[pz_hash] = counter

                for combination in combinations:
                    self._update_gravity(self._planets[combination[0]], self._planets[combination[1]])
                self._apply_gravity()
                counter += 1

            return np.lcm.reduce(
                [self._iterations_per_axis[0], self._iterations_per_axis[1], self._iterations_per_axis[2]])

        for i in range(1000):
            for combination in combinations:
                self._update_gravity(self._planets[combination[0]], self._planets[combination[1]])
            self._apply_gravity()

        for planet in self._planets:
            self._result += planet.total_energy

        return self._result
