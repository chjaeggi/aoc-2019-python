from collections import Counter, OrderedDict


class Day6:

    def __init__(self):
        self._planets_input = None
        self._planets_dict = OrderedDict()
        self._sum = 0
        with open('inputs/06-input.txt') as data:
            self._planets_input = data.read().replace('\n', ')').split(')')

    def _evaluate_ascendants(self, key, resulting_list=None):
        if key != '':
            self._sum += 1
            if resulting_list is not None:
                resulting_list.append(key)
            new_parent = self._planets_dict[key]
            self._evaluate_ascendants(new_parent, resulting_list)

    @staticmethod
    def _get_first_common_element(first_list, second_list):
        for element in first_list:
            if element in second_list:
                return element
        return None

    @staticmethod
    def _get_number_of_items_until_element(list_to_check, element):
        result = 0
        for value in list_to_check:
            if value != element:
                result += 1
            else:
                break
        return result

    def solve(self, full_quiz=True):
        for planet in self._planets_input:
            self._planets_dict[planet] = ''

        for index, _ in enumerate(self._planets_input):
            if index % 2 == 1:
                child = self._planets_input[index]
                parent = self._planets_input[index - 1]
                self._planets_dict[child] = parent

        for child, parent in self._planets_dict.items():
            if parent != '':
                self._evaluate_ascendants(parent)

        result = self._sum

        if full_quiz:
            santa_tree = []
            you_tree = []

            for child, parent in self._planets_dict.items():
                if child == 'SAN':
                    self._evaluate_ascendants(parent, resulting_list=santa_tree)
                if child == 'YOU':
                    self._evaluate_ascendants(parent, resulting_list=you_tree)

            common_element = self._get_first_common_element(santa_tree, you_tree)
            santa = self._get_number_of_items_until_element(santa_tree, common_element)
            you = self._get_number_of_items_until_element(you_tree, common_element)
            result = santa + you

        return result
