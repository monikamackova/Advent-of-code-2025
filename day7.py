from time import time
from typing import Final, Any
import numpy as np
import collections

class BeamSplitter:
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def execute(self):
        data = self._load_txt_data()
        count = self._iterate_array_advanced2(data)
        return count

    def _load_txt_data(self):
        with open(self.filename, 'r') as file:
            content = file.read()
        data = content.split('\n')
        return data

    @staticmethod
    def _iterate_array(symbols):
        count = 0
        numbers_arr = np.zeros((len(symbols) - 1, len(list(symbols[0]))), dtype=str)
        for i in range(len(symbols)-1):
            symbol = symbols[i]
            numbers_arr[i, :] = list(symbol)

        start_index_y = np.where(numbers_arr=='S')[1]
        indexes_to_examine = set()
        indexes_to_examine.add(start_index_y[0])

        for i in range(1, len(symbols)-1):
            one_line = numbers_arr[i, :]
            change_index = False
            indexes_split = []
            for index in list(indexes_to_examine):
                if one_line[index] == "^":
                    count += 1
                    change_index = True
                    indexes_split.append(index)
                if one_line[index] == ".":
                    count += 0

            if change_index:
                for ind in indexes_split:
                    indexes_to_examine.remove(ind)
                    indexes_to_examine.add(ind + 1)
                    indexes_to_examine.add(ind - 1)
        print(count)
        return count

    @staticmethod
    def _iterate_array_advanced(symbols):
        count = 1
        numbers_arr = np.zeros((int((len(symbols)-1)/2), len(list(symbols[0]))), dtype=str)
        for i in range(0, len(symbols)-1, 2):
            symbol = symbols[i]
            numbers_arr[int(i/2), :] = list(symbol)

        start_index_y = np.where(numbers_arr == 'S')[1]
        indexes_to_examine = [start_index_y[0]]

        for i in range(1, (int((len(symbols)-1)/2))):
            one_line = numbers_arr[i, :]
            change_index = False
            indexes_split = []
            for index in indexes_to_examine:
                if one_line[index] == "^":
                    count += 1
                    change_index = True
                    indexes_split.append(index)

            if change_index:
                indexes_to_examine = np.array(indexes_to_examine, dtype=int)
                ind = np.array(indexes_split, dtype=int)
                indexes_to_examine = indexes_to_examine[~np.isin(indexes_to_examine, indexes_split)]
                array_to_add1 = ind + 1
                array_to_add2 = ind - 1
                indexes_to_examine = np.concatenate((indexes_to_examine, array_to_add1), axis=0)
                indexes_to_examine = np.concatenate((indexes_to_examine, array_to_add2), axis=0)


        print(count)
        return count

    @staticmethod
    def _iterate_array_advanced2(symbols):
        count = 1
        numbers_arr = np.zeros((int((len(symbols)-1)/2), len(list(symbols[0]))), dtype=str)
        for i in range(0, len(symbols)-1, 2):
            symbol = symbols[i]
            numbers_arr[int(i/2), :] = list(symbol)

        start_index_y = np.where(numbers_arr == 'S')[1]
        indexes_to_examine = {start_index_y[0]: 1}

        for i in range(1, int((len(symbols)-1)/2)):
            one_line = numbers_arr[i, :]
            indexes_to_check = list(indexes_to_examine.keys())
            for j in range(len(indexes_to_check)):
                index = indexes_to_check[j]
                if one_line[index] == "^":
                    add_val = indexes_to_examine[index]
                    count += add_val
                    del indexes_to_examine[index]
                    if index + 1 not in indexes_to_examine:
                        indexes_to_examine[index + 1] = 0
                    if index - 1 not in indexes_to_examine:
                        indexes_to_examine[index - 1] = 0
                    value = indexes_to_examine [index + 1]
                    indexes_to_examine[index + 1] = value + add_val
                    value2 = indexes_to_examine[index - 1]
                    indexes_to_examine[index - 1] = value2 + add_val

        print(count)
        return count



if __name__ == "__main__":
    start_time = time()
    BS = BeamSplitter("input7.txt")
    count = BS.execute()
    #print(count)
    end_time = time()
    print(f"Time taken: {end_time - start_time} seconds")