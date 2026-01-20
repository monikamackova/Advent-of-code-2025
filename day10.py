from time import time
import matplotlib.pyplot as plt
import numpy as np
import inspect
from scipy.optimize import linprog

class Machines:
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def execute(self) -> int:
        data = self._load_txt_data()
        return self._iterate_lines(data)

    def _load_txt_data(self) -> list[str]:
        with open(self.filename, 'r') as file:
            content = file.read()
        return content.splitlines()

    def _iterate_lines(self, data: list[str]) -> int:
        count = 0
        for line in data:
            split_line = line.split(' ')

            buttons_arr: list[set[np.int64]] = []
            for button in np.array(split_line[1:-1]):
                button = button[1:-1]
                button_add = set(np.array(button.split(sep=","), dtype=int))
                buttons_arr.append(button_add)

            indexes_on = [set(np.where(np.array(list(split_line[0][1:-1])) == '#')[0])]

            result = self._part1_ajbnsajkns(buttons_arr, indexes_on, 0)
            #joltage = np.array(split_line[-1][1:-1].split(sep=","), dtype=int)
            #buttons_j = self._buttons_to_joltage(buttons_arr, joltage)
            #result = self._part2(buttons_j, joltage, 0)
            count += result
        return count

    def _part1(self, buttons_arr: list[set[np.ndarray]], indexes_to_flip: list[set[np.ndarray]], count: int) -> int:
        count += 1
        indexes_to_flip_next = set()
        for index_to_flip in indexes_to_flip:
            common = []
            for i in range(len(buttons_arr)):
                common_i = index_to_flip & buttons_arr[i]
                common.append(len(common_i))
                if index_to_flip == buttons_arr[i]:
                    return count

            indexes_max = [i for i, val in enumerate(common) if val >= 1]
            for index in indexes_max:
                index_to_flip_now = buttons_arr[index] ^ index_to_flip
                index_to_flip_now = frozenset(index_to_flip_now)
                indexes_to_flip_next.add(index_to_flip_now)
        return self._part1(buttons_arr, indexes_to_flip_next, count)

    def _part1_ajbnsajkns(self, buttons_arr: list[set[np.int64]], indexes_to_flip: list[set[np.ndarray]], count: int) -> int:
        while True:
            count += 1
            indexes_to_flip_next: set[frozenset[np.int64]] = set()
            for index_to_flip in indexes_to_flip:
                common = []
                for button in buttons_arr:
                    common.append(len(index_to_flip & button))
                    if index_to_flip == button:
                        return count

                indexes_max = [i for i, val in enumerate(common) if val >= 1]
                for index in indexes_max:
                    index_to_flip_now = buttons_arr[index] ^ index_to_flip
                    index_to_flip_now = frozenset(index_to_flip_now)
                    indexes_to_flip_next.add(index_to_flip_now)

            indexes_to_flip = indexes_to_flip_next

    def _buttons_to_joltage(self, buttons_arr: list[set[np.ndarray]], joltage: np.ndarray) -> list:
        buttons = []
        for button in buttons_arr:
            buttons_joltage = np.zeros(len(joltage), dtype=int)
            indexes = list(button)
            buttons_joltage[indexes] = 1
            buttons.append(buttons_joltage)
        return buttons

    def _part2(self, buttons_j, joltage, count):
        button_matrix = np.vstack(buttons_j)
        """

        presses = joltage @ np.linalg.pinv(button_matrix)
        presses_int = np.round(presses)
        check_val = np.sum(np.abs(presses) - np.abs(presses_int))
        indexes_to_check = np.where(presses_int < -0.5)[0]
        if np.abs(check_val) < 10e-9 and len(indexes_to_check) == 0:
            resulting_presses = presses_int

        else:
            resulting_presses = self._part2_optimization(button_matrix, joltage)
        """
        resulting_presses = self._part2_optimization(button_matrix, joltage)
        count += np.sum(resulting_presses)
        return count

    def _part2_optimization(self, button_matrix, joltage):
        presses = np.zeros(len(button_matrix[:, 0]), dtype=int)+1
        result = linprog(presses, A_eq=button_matrix.T, b_eq=joltage, bounds=(0, np.max(joltage)), integrality= 1)
        return result.x



if __name__ == "__main__":
    start_time = time()
    M = Machines("input10.txt")
    result = M.execute()
    print(result)
    end_time = time()
    print(f"Time taken: {end_time - start_time} seconds")