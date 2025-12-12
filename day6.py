from time import time
from typing import Final, Any
import numpy as np

class MathProblem:
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def execute(self):
        symbols, numbers = self._load_txt_data()
        count = self._iterate_array_advanced(symbols, numbers)
        return count

    def _load_txt_data(self):
        with open(self.filename, 'r') as file:
            content = file.read()
        data = content.split('\n')
        symbols = data[-2]
        numbers = data[:len(data)-2]
        return symbols, numbers

    def _iterate_array(self, symbols, numbers):
        count = 0
        list_symbols = []
        for symbol in symbols:
            if symbol != " ":
                list_symbols.append(symbol)

        numbers_arr = np.zeros((4, 1000), dtype=int)
        for i in range(len(numbers)):
            split_range = numbers[i].split(' ')
            array = np.array(split_range)
            indexes = np.where(array == '')[0]
            array = np.delete(array, indexes)
            array = np.array(array, dtype=int)
            numbers_arr[i, :] = array

        for i in range(1000):
            result = self._perform_operation(list_symbols[i], numbers_arr[0, i], numbers_arr[1, i], numbers_arr[2, i], numbers_arr[3, i])
            count += result
        return count


    def _iterate_array_advanced(self, symbols, numbers):
        count = 0
        list_symbols = []
        for symbol in symbols:
            if symbol != " ":
                list_symbols.append(symbol)

        numbers_arr = np.zeros((4, 3762), dtype=str)
        for i in range(len(numbers)):
            split_range = list(numbers[i])
            numbers_arr[i, :] = split_range

        list_nums = []
        for i in range(3761, -1, -1):
            str1 = numbers_arr[0, i]
            str2 = numbers_arr[1, i]
            str3 = numbers_arr[2, i]
            str4 = numbers_arr[3, i]

            number = str1+str2+str3+str4
            chars = np.array(list(number))
            indexes = np.where(chars == " ")[0]
            if len(indexes) == 4:
                number = 0
            else:
                chars = np.delete(chars, indexes)
                number = "".join(list(chars))
                number = int(number)

            list_nums.append(number)

        list_nums = np.array(list_nums[::-1])
        list_symbols = list_symbols
        indexes = np.where(list_nums==0)[0]

        list_nums = np.split(list_nums, indexes+1)


        for i in range(0, 1000):
            sym = list_symbols[i]
            if sym =='+':
                number = np.sum(list_nums[i])
                count+=number
            if sym =='*':
                multi = 1
                for j in range(len(list_nums[i])):
                    if list_nums[i][j] != 0:
                        multi = multi * list_nums[i][j]
                number = multi
                count+=number

        print(count)
        return count

    def _perform_operation(self, sym, num1, num2, num3, num4):
        if sym =='*':
            return num1 * num2 * num3 * num4
        if sym =='+':
            return num1 + num2 + num3 + num4


if __name__ == "__main__":
    start_time = time()
    MP = MathProblem("input6.txt")
    count = MP.execute()
    #print(count)
    end_time = time()
    print(f"Time taken: {end_time - start_time} seconds")