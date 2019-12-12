import time

from days.day12.day12 import Day12


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
        # self._day10 = Day10().solve(full_quiz=True)
        # self._day11 = Day11().solve(full_quiz=True)
        self._day12 = Day12().solve(full_quiz=True)

        # print("Day1:     {}".format(self._day1))
        # print("Day2:     {}".format(self._day2))
        # print("Day3:     {}".format(self._day3))
        # print("Day4:     {}".format(self._day4))
        # print("Day5:     {}".format(self._day5))
        # print("Day6:     {}".format(self._day6))
        # print("Day7:     {}".format(self._day7))
        # print("Day8:     {}".format(self._day8))
        # print("Day9:     {}".format(self._day9))
        # print("Day10:    {}".format(self._day10))
        # print("Day11:    {}".format(self._day11))
        print("Day12:    {}".format(self._day12))


if __name__ == '__main__':
    start = time.time()
    advent = Advent()
    end = time.time()
    print("------ Computation time: {} ------".format(end - start))
