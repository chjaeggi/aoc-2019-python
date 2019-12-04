import time

from days.day1 import Day1
from days.day2 import Day2
from days.day3 import Day3
from days.day4 import Day4


class Advent:

    def __init__(self):
        self._day1 = Day1().solve(full_quiz=True)
        self._day2 = Day2().solve(full_quiz=True)
        self._day3 = Day3().solve(full_quiz=True)
        self._day4 = Day4().solve(full_quiz=True)

        print(self._day1)
        print(self._day2)
        print(self._day3)
        print(self._day4)


if __name__ == '__main__':
    start = time.time()
    advent = Advent()
    end = time.time()
    print("Computation time: {}".format(end - start))
