import time

from days.day1 import Day1
from days.day10 import Day10
from days.day2 import Day2
from days.day3 import Day3
from days.day4 import Day4
from days.day5 import Day5
from days.day6 import Day6
from days.day7.day7 import Day7
from days.day8.day8 import Day8
from days.day9.day9 import Day9


class Advent:

    def __init__(self):
        # self._day1 = Day1().solve(full_quiz=True)
        # self._day2 = Day2().solve(full_quiz=True)
        # self._day3 = Day3().solve(full_quiz=True)
        # self._day4 = Day4().solve(full_quiz=True)
        # self._day5 = Day5().solve(full_quiz=True)
        # self._day6 = Day6().solve(full_quiz=True)
        # self._day7 = Day7().solve(full_quiz=True)
        # self._day8 = Day8().solve(full_quiz=False)
        # self._day9 = Day9().solve(full_quiz=True)
        self._day10 = Day10().solve(full_quiz=True)

        # print("Day1:     {}".format(self._day1))
        # print("Day2:     {}".format(self._day2))
        # print("Day3:     {}".format(self._day3))
        # print("Day4:     {}".format(self._day4))
        # print("Day5:     {}".format(self._day5))
        # print("Day6:     {}".format(self._day6))
        # print("Day7:     {}".format(self._day7))
        # print("Day8:     {}".format(self._day8))
        # print("Day9:     {}".format(self._day9))
        print("Day10:    {}".format(self._day10))


if __name__ == '__main__':
    start = time.time()
    advent = Advent()
    end = time.time()
    print("------ Computation time: {} ------".format(end - start))
