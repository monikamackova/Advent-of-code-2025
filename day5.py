from time import time
from typing import Final, Any
import numpy as np

class CheckIDs:
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def execute(self):
        ranges, ids = self._load_txt_data()
        count = self._iterate_array(ranges, ids)
        fresh = self._fresh_list(ranges)
        return fresh

    def _load_txt_data(self):
        with open(self.filename, 'r') as file:
            content = file.read()
        data = content.split('\n')
        data_arr = np.array(data)
        split_index = np.where(data_arr == "")[0][0]
        ranges = data[:split_index]
        ids = data[split_index+1:]
        return ranges, ids

    def _iterate_array(self, ranges, ids):
        count = 0
        for id in ids:
            id = int(id)
            for r in ranges:
                split_range = r.split('-')
                start_num = int(split_range[0])
                end_num = int(split_range[1])
                if end_num >= id >= start_num:
                    count += 1
                    break

    def _fresh_list(self, ranges):
        count = 0
        # Create starts and ends arrays
        starts = np.zeros(len(ranges), dtype=int)
        ends = np.zeros(len(ranges), dtype=int)
        for i in range(0, len(ranges)):
            split_range = ranges[i].split('-')
            start_num = int(split_range[0])
            end_num = int(split_range[1])
            starts[i] = start_num
            ends[i] = end_num

        # Find indexes of nested and duplicated ranges
        indexes_to_delete = set()
        indexes_duplicated = []
        for i in range(0, len(ranges)):
            checked_interval_start = starts[i]
            checked_interval_end = ends[i]
            for j in range(0, len(ranges)):
                if j != i:
                    start = starts[j]
                    end = ends[j]
                    if start <= checked_interval_start and end > checked_interval_end:
                        indexes_to_delete.add(i)
                    elif start < checked_interval_start and end >= checked_interval_end:
                        indexes_to_delete.add(i)
                    elif start == checked_interval_start and end == checked_interval_end:
                        indexes_duplicated.append([i,j])

        # Get only one of the duplicated indexes
        indexes_to_delete_from_dup = set()
        index1 = np.zeros(len(indexes_duplicated), dtype=int)
        index2 = np.zeros(len(indexes_duplicated), dtype=int)
        for i in range(0, len(indexes_duplicated)):
            index1[i] = indexes_duplicated[i][0]
            index2[i] = indexes_duplicated[i][1]
            for j in range(i+1, len(indexes_duplicated)):
                if indexes_duplicated[i][0] == indexes_duplicated[j][1] and indexes_duplicated[i][1] == indexes_duplicated[j][0]:
                    indexes_to_delete_from_dup.add(j)

        # Delete indexes of nested and duplicated ranges
        index1 = np.delete(index1, list(indexes_to_delete_from_dup))
        for ind in index1: indexes_to_delete.add(ind)
        starts = np.delete(starts, list(indexes_to_delete))
        ends = np.delete(ends, list(indexes_to_delete))

        # Iterate intervals, leave only the part that is not cut-off by following intervals
        for i in range(0, len(starts)-1):
            checked_interval_start = starts[i]
            checked_interval_end = ends[i]
            for j in range(i+1, len(starts)):
                start = starts[j]
                end = ends[j]
                if start <= checked_interval_start and end >= checked_interval_end:
                    checked_interval_end = - 1
                    checked_interval_start = 0
                    break
                if checked_interval_end >= start > checked_interval_start:
                    checked_interval_end = start - 1
                elif checked_interval_end > end >= checked_interval_start:
                    checked_interval_start = end + 1
            number = checked_interval_end - checked_interval_start + 1
            count += number

        # Add last interval
        additinal_number = ends[-1] - starts[-1] + 1
        count += additinal_number

        return count


if __name__ == "__main__":
    start_time = time()
    CHI = CheckIDs("input5.txt")
    count = CHI.execute()
    print(count)
    end_time = time()
    print(f"Time taken: {end_time - start_time} seconds")