from collections import Counter, OrderedDict


class Day6:

    def __init__(self):
        self._planets_input = None
        self._planets_dict = OrderedDict()
        self._sum = 0
        self._santa_tree = []
        self._you_tree = []
        with open('inputs/06-input.txt') as data:
            self._planets_input = data.read().replace('\n', ')').split(')')

    def _evaluate_ascendants(self, key, resulting_list=None):
        if key != '':
            self._sum += 1
            if resulting_list is not None:
                resulting_list.append(key)
            try:
                new_parent = self._planets_dict[key]
                self._evaluate_ascendants(new_parent, resulting_list)
            except KeyError:
                pass

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

    def _calculate_sum(self):
        self._sum = 0
        for child, parent in self._planets_dict.items():
            if parent != '':
                self._evaluate_ascendants(parent)
        return self._sum

    def _create_planet_relations(self):
        for index, _ in enumerate(self._planets_input):
            if index % 2 == 1:
                child = self._planets_input[index]
                parent = self._planets_input[index - 1]
                self._planets_dict[child] = parent

    def solve(self, full_quiz=True):
        self._create_planet_relations()
        result = self._calculate_sum()

        if full_quiz:
            self._evaluate_ascendants(self._planets_dict['SAN'], resulting_list=self._santa_tree)
            self._evaluate_ascendants(self._planets_dict['YOU'], resulting_list=self._you_tree)
            common_element = self._get_first_common_element(self._santa_tree, self._you_tree)
            santa = self._get_number_of_items_until_element(self._santa_tree, common_element)
            you = self._get_number_of_items_until_element(self._you_tree, common_element)
            result = santa + you

        return result
