from time import time
from typing import Final, Any
import numpy as np

class PaperRolls:
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def execute(self):
        data = self._load_txt_data()
        matrix = self._create_matrix(data)
        count = self._count_rolls(matrix)
        return matrix

    def _load_txt_data(self):
        with open(self.filename, 'r') as file:
            content = file.read()
        data = content.split('\n')
        data = np.array(data)
        return data

    def _create_matrix(self, array):
        matrix = np.zeros((len(array), 139), dtype=str)
        for i in range(0, len(array)):
            symbol_list = [str(symbol) for symbol in array[i]]
            symbol_array = np.array(symbol_list)
            matrix[i, :] = symbol_array
        return matrix

    def _count_rolls(self, matrix):
        count = 0
        count_new = -1
        shape = np.shape(matrix)
        while count_new < count:
            count_new = count
            for y in range(0, shape[0]):
                for x in range(0, shape[1]):
                    roll_count = 0
                    if matrix[y, x] == '@':
                        if y - 1 >= 0:
                            if matrix[y - 1, x] == '@':
                                roll_count += 1

                        if y + 1 <= 138:
                            if matrix[y + 1, x] == '@':
                                roll_count += 1

                        if x + 1 <= 138:
                            if matrix[y, x + 1] == '@':
                                roll_count += 1

                        if x - 1 >= 0:
                            if matrix[y, x - 1] == '@':
                                roll_count += 1

                        if x - 1 >= 0 and y - 1 >= 0:
                            if matrix[y - 1, x - 1] == '@':
                                roll_count += 1

                        if x + 1 <= 138 and y + 1 <= 138:
                            if matrix[y + 1, x + 1] == '@':
                                roll_count += 1

                        if x + 1 <= 138 and y - 1 >= 0:
                            if matrix[y - 1, x + 1] == '@':
                                roll_count += 1

                        if x - 1 >= 0 and y + 1 <= 138:
                            if matrix[y + 1, x - 1] == '@':
                                roll_count += 1
                        print(roll_count)
                        if roll_count < 4:
                            matrix[y, x] = 'x'
                            count += 1

        print(count)

        return count



if __name__ == "__main__":
    start_time = time()
    PR = PaperRolls("input4.txt")
    count = PR.execute()
    end_time = time()
    print(f"Time taken: {end_time - start_time} seconds")