from time import time
from typing import Final, Any
import numpy as np

class FlipSwitch:
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def execute(self):
        data = self._load_txt_data()
        count = self._iterate_array_advanced(data)
        return count

    def _load_txt_data(self):
        with open(self.filename, 'r') as file:
            content = file.read()
        data= content.split('\n')
        data = np.array(data)
        return data

    def _iterate_array(self, array):
        count = 0
        for string in array:
            digit_list = [int(digit) for digit in string]
            digit_array = np.array(digit_list, dtype=int)
            max_digit = np.max(digit_array)
            index_max = np.where(digit_array == max_digit)[0]
            if len(index_max) > 1:
                number_str = str(max_digit) + str(max_digit)
                number = int(number_str)
                count += number
            elif index_max == [len(digit_array)-1]:
                digit_array_deleted = np.delete(digit_array, index_max)
                next_max = np.max(digit_array_deleted)
                number_str = str(next_max) + str(max_digit)
                number = int(number_str)
                count += number
            else:
                digit_array_deleted = np.delete(digit_array, np.arange(index_max+1))
                next_max = np.max(digit_array_deleted)
                number_str = str(max_digit)+str(next_max)
                number = int(number_str)
                count += number

        return count

    def _iterate_array_advanced(self, array):
        count = 0
        for string in array:
            resulting_digits = []
            digit_list = [int(digit) for digit in string]
            digit_array = np.array(digit_list, dtype=int)

            for i in range(0, 12):
                digit_array_it = digit_array
                digit_array_cropped = np.delete(digit_array, np.arange(len(digit_array) - np.abs(i-11), len(digit_array)))
                max_digit = np.max(digit_array_cropped)
                resulting_digits.append(str(max_digit))
                index_max = np.where(digit_array == max_digit)[0][0]
                digit_array = np.delete(digit_array, np.arange(index_max+1))

            number = int("".join(resulting_digits))
            count += number

        return count


if __name__ == "__main__":
    start_time = time()
    FNC = FlipSwitch("input3.txt")
    count = FNC.execute()
    print(count)
    end_time = time()
    print(f"Time taken: {end_time - start_time} seconds")

