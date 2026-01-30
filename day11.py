from time import time
import matplotlib.pyplot as plt
import numpy as np


class Reactor:
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def execute(self) -> tuple[int, int]:
        data = self._load_txt_data()
        input_list, output_list = self._extract_data(data)
        part1_result = self._part1(input_list, output_list)
        #part2_result = self._part2(input_list, output_list)
        return part1_result

    def _load_txt_data(self) -> list[str]:
        with open(self.filename, 'r') as file:
            content = file.read()
        return content.splitlines()

    @staticmethod
    def _extract_data(data: list[str]) -> tuple[list[str], list[set[str]]]:
        input_list: list[str] = []
        output_list: list[set[str]] = []

        for line in data:
            input_list.append(line.split(' ')[0][0:-1])
            output_list.append(set(line.split(' ')[1:]))
        return input_list, output_list

    @staticmethod
    def _iterate_tree(
            input_list: list[str],
            output_list: list[set[str]],
            start_str: str,
            wanted_str: str,
    ) -> int:
        count = 0
        index_start = [input_list.index(start_str)]

        while True:
            index_next: list[int] = []
            for index in index_start:
                for out in output_list[index]:
                    if out in input_list:
                        index_next.append(input_list.index(out))
                    if out == wanted_str:
                        count += 1
            index_start = index_next
            if len(index_next) == 0:
                return count

    def _part1(self, input_list: list[str], output_list: list[set[str]]) -> int:
        return self._iterate_tree(input_list, output_list, 'you', 'out')

    def _part2(self, input_list: list[str], output_list: list[set[str]]) -> int:
        count_svr_fft = self._iterate_tree(input_list, output_list, 'svr', 'fft')
        count_fft_dac = self._iterate_tree(input_list, output_list, 'fft', 'dac')
        return count_svr_fft * count_fft_dac


if __name__ == "__main__":
    start_time = time()
    R = Reactor("input11.txt")
    #part1, part2 = R.execute()
    part1 = R.execute()
    print(f"Result part 1: {part1}")
    #print(f"Result part 2: {part2}")
    end_time = time()
    print(f"Time taken: {end_time - start_time} seconds")
        