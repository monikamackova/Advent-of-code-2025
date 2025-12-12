from time import time
from typing import Final, Any
import numpy as np

class CheckIDs:
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def execute(self):
        data = self._load_txt_data()
        count = self._iterate_array_advanced(data)
        return count

    def _load_txt_data(self):
        with open(self.filename, 'r') as file:
            content = file.read()
        data = content.split(',')
        data = np.array(data)
        return data

    def _iterate_array(self, array):
        count = 0
        for string in array:
            split_range = string.split('-')
            start_num = int(split_range[0])
            end_num = int(split_range[1])
            for id in range(start_num, end_num+1):
                digit_list = [int(digit) for digit in str(id)]
                number_of_digits = len(digit_list)
                if number_of_digits % 2 == 0:
                    index = int(number_of_digits/2)
                    if digit_list[0:index] == digit_list[index:number_of_digits]:
                        count += id
        return count

    def _iterate_array_advanced(self, array):
        count = 0
        for string in array:
            split_range = string.split('-')
            start_num = int(split_range[0])
            end_num = int(split_range[1])
            lens = []
            for id in range(start_num, end_num+1):
                digit_list = [int(digit) for digit in str(id)]
                number_of_digits = len(digit_list)

                if number_of_digits == 2:
                    if digit_list[0] == digit_list[1]:
                        count += id

                if number_of_digits == 3:
                    if digit_list[0] == digit_list[1] == digit_list[2]:
                        count += id

                if number_of_digits == 4:
                    if digit_list[0] == digit_list[1] == digit_list[2] == digit_list[3]:
                        count += id
                    elif digit_list[0:2] == digit_list[2:4]:
                        count += id

                if number_of_digits == 5:
                    if digit_list[0] == digit_list[1] == digit_list[2] == digit_list[3] == digit_list[4]:
                        count += id

                if number_of_digits == 6:
                    if digit_list[0] == digit_list[1] == digit_list[2] == digit_list[3] == digit_list[4] == digit_list[5]:
                        count += id
                    elif digit_list[0:2] == digit_list[2:4] == digit_list[4:6]:
                        count += id
                    elif digit_list[0:3] == digit_list[3:6]:
                        count += id

                if number_of_digits == 7:
                    if digit_list[0] == digit_list[1] == digit_list[2] == digit_list[3] == digit_list[4] == digit_list[5] == digit_list[6]:
                        count += id

                if number_of_digits == 8:
                    if digit_list[0] == digit_list[1] == digit_list[2] == digit_list[3] == digit_list[4] == digit_list[5] == digit_list[6] == digit_list[7]:
                        count += id
                    elif digit_list[0:2] == digit_list[2:4] == digit_list[4:6] == digit_list[6:8]:
                        count += id
                    elif digit_list[0:4] == digit_list[4:8]:
                        count += id

                if number_of_digits == 9:
                    if digit_list[0] == digit_list[1] == digit_list[2] == digit_list[3] == digit_list[4] == digit_list[5] == digit_list[6] == digit_list[7] == digit_list[8]:
                        count += id
                    elif digit_list[0:3] == digit_list[3:6] == digit_list[6:9]:
                        count += id

                if number_of_digits == 10:
                    if digit_list[0] == digit_list[1] == digit_list[2] == digit_list[3] == digit_list[4] == digit_list[5] == digit_list[6] == digit_list[7] == digit_list[8] == digit_list[9]:
                        count += id
                    elif digit_list[0:2] == digit_list[2:4] == digit_list[4:6] == digit_list[6:8] == digit_list[8:10]:
                        count += id
                    elif digit_list[0:5] == digit_list[5:10]:
                        count += id

        return count


if __name__ == "__main__":
    start_time = time()
    FNC = CheckIDs("input2.txt")
    count = FNC.execute()
    print(count)
    end_time = time()
    print(f"Time taken: {end_time - start_time} seconds")