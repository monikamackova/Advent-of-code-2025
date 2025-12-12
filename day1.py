from time import time
from typing import Final, Any
import numpy as np


class FindNumberCombination:
    _INITIAL_NUMBER: Final = 50

    def __init__(self, filename: str) -> None:
        self.filename = filename

    def execute(self):
        combinations = self._load_txt_data()
        arrays = self._split(combinations)
        count_zeros = self._iterate_arrays(arrays)
        return count_zeros

    def _load_txt_data(self):
        with open(self.filename, 'r') as file:
            content = file.read()
        return list(content)

    def _split(self, combinations: list):
        array = np.array(combinations)
        indexes = np.where(array == '\n')[0]
        array_list = np.split(array, indexes)
        array_list.pop(-1)
        return array_list

    def _iterate_arrays(self, array_list):
        final_number = self._INITIAL_NUMBER
        count_zeros = 0
        array_list[0]=np.insert(array_list[0], 0, 0)
        for array in array_list:
            orientation = array[1]
            digits = np.delete(array,[0,1])
            number = int("".join(digits))
            if orientation == "R":
                final_number += number
            if orientation == "L":
                final_number += -number
            print(final_number)
            final_number = final_number % 100
            if final_number == 0:
                count_zeros += 1
        return count_zeros

    def _iterate_arrays_advanced(self, array_list):
        final_number = self._INITIAL_NUMBER
        count_zeros = 0
        array_list[0]=np.insert(array_list[0], 0, 0)
        for array in array_list:
            orientation = array[1]
            digits = np.delete(array,[0,1])
            number = int("".join(digits))
            initial_number = final_number
            if orientation == "R":
                final_number += number
            if orientation == "L":
                final_number += -number
            if final_number == 0:
                count_zeros += 1
                print(1)
            if final_number < 0 and initial_number==0:
                turns = int(-final_number // 100)
                print(turns)
                count_zeros += turns
            if final_number < 0 and initial_number!=0:
                turns = int(-final_number // 100)+1
                print(turns)
                count_zeros += turns

            if final_number > 99:
                turns = int(final_number // 100)
                count_zeros += turns
                print(turns)
            if final_number > 0 and final_number < 99:
                print(0)

            final_number = final_number % 100
        return count_zeros












if __name__ == "__main__":
    start_time = time()
    FNC = FindNumberCombination("input1.txt")
    count = FNC.execute()
    print(count)
    end_time = time()
    print(f"Time taken: {end_time - start_time} seconds")

