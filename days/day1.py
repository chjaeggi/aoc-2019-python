class Day1:

    def __init__(self):
        self._numbers = None
        self._fuel = 0
        with open('inputs/01-input.txt') as data:
            self._numbers = data.read().split()
            self._fuel = 0

    @staticmethod
    def _calc_fuel_for_mass(mass):
        return int(int(int(mass) / 3) - 2)

    def solve(self, full_quiz=True):
        for number in self._numbers:
            fuel_add = self._calc_fuel_for_mass(number)
            self._fuel += fuel_add

            if not full_quiz:
                return self._fuel

            while self._calc_fuel_for_mass(fuel_add) > 0:
                fuel_add = self._calc_fuel_for_mass(fuel_add)
                self._fuel += fuel_add

        return self._fuel
