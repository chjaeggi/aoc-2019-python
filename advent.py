import time

from days.day1 import Day1
from days.day2 import Day2
from days.day3 import Day3
from days.day4 import Day4
from days.day5 import Day5
from days.day6 import Day6
from days.day7.day7_1 import Day7_1
from days.day7.day7_2 import Day7_2
from days.day8 import Day8


class Advent:

    def __init__(self):
        self._day1 = Day1().solve(full_quiz=True)
        self._day2 = Day2().solve(full_quiz=True)
        self._day3 = Day3().solve(full_quiz=True)
        self._day4 = Day4().solve(full_quiz=True)
        self._day5 = Day5().solve(full_quiz=True)
        self._day6 = Day6().solve(full_quiz=True)
        self._day7_1 = Day7_1().solve()
        self._day7_2 = Day7_2().solve()
        self._day8 = Day8().solve(full_quiz=True)

        print("Day1:     {}".format(self._day1))
        print("Day2:     {}".format(self._day2))
        print("Day3:     {}".format(self._day3))
        print("Day4:     {}".format(self._day4))
        print("Day5:     {}".format(self._day5))
        print("Day6:     {}".format(self._day6))
        print("Day7-1:   {}".format(self._day7_1))
        print("Day7-2:   {}".format(self._day7_2))
        print("Day8:     {}".format(self._day8))


if __name__ == '__main__':
    start = time.time()
    advent = Advent()
    end = time.time()
    print("------ Computation time: {} ------".format(end - start))
