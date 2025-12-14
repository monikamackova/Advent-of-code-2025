from time import time
import matplotlib.pyplot as plt
import numpy as np


class Tiles:
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def execute(self):
        data = self._load_txt_data()
        final_number = self._find_biggest_rectangle_inside_boders(data)
        return final_number

    def _load_txt_data(self):
        with open(self.filename, 'r') as file:
            content = file.read()
        data = content.splitlines()
        numbers_arr = np.zeros((len(data) - 1, 2), dtype=int)
        for i in range(len(data) - 1):
            dat = data[i].split(sep=",")
            numbers_arr[i, :] = dat
        return numbers_arr

    @staticmethod
    def _find_area(data):
        lengh = len(data[:, 0])
        area_array = np.zeros((lengh, lengh), dtype=int)
        for i in range(lengh):
            one_point = data[i,:]
            for j in range(i, lengh):
                if i != j:
                    other_point = data[j, :]
                    area_array[i, j] = (np.abs(one_point[0]-other_point[0])+1)*(np.abs(one_point[1]-other_point[1])+1)
        return area_array


    @staticmethod
    def _find_border_points(data):
        border_points: set[tuple[int, int]] = set()
        lengh = len(data[:, 0])
        for i in range(lengh):
            one_point = data[i, :]
            if i == lengh-1:
                next_point = data[-1, :]
            else:
                next_point = data[i+1, :]
            if one_point[0] == next_point[0]:
                sorted_points = np.sort([one_point[1], next_point[1]])
                y_points = np.arange(sorted_points[0], sorted_points[1]+1)
                for y in y_points:
                    border_points.add(tuple([int(one_point[0]),int(y)]))
            if one_point[1] == next_point[1]:
                sorted_points = np.sort([one_point[0], next_point[0]])
                x_points = np.arange(sorted_points[0], sorted_points[1]+1)
                for x in x_points:
                    border_points.add(tuple([int(x), int(one_point[1])]))
        """
        border_points_display =np.array(list(border_points))
        plt.scatter(border_points_display[:, 0], border_points_display[:, 1], s=0.5, color="blue")
        plt.scatter(data[:, 0], data[:, 1], s=0.5, color="red")
        plt.title("2D Scatter Plot")
        plt.xlabel("X-Axis")
        plt.ylabel("Y-Axis")
        plt.legend()
        plt.show()
        """
        return border_points

    def _find_biggest_rectangle_inside_boders(self, data):
        area_array = self._find_area(data)
        border_points = np.array(list(self._find_border_points(data)))
        border_points_x = border_points[:, 0]
        border_points_y = border_points[:, 1]
        lengh = len(data[:, 0])
        points = int(lengh * lengh / 2 - lengh / 2)
        max_area = 0
        for i in range(points):
            print(i)
            indexes_max_1 = int(np.where(area_array == np.max(area_array))[0][0])
            indexes_max_2 = int(np.where(area_array == np.max(area_array))[1][0])
            max_area = area_array[indexes_max_1, indexes_max_2]
            area_array[indexes_max_1, indexes_max_2] = 0
            point1 = data[indexes_max_1, :]
            point2 = data[indexes_max_2, :]
            x_range = np.sort([point1[0], point2[0]])
            y_range = np.sort([point1[1], point2[1]])

            inside_points_x_h = set(np.where(x_range[0] < border_points_x)[0])
            inside_points_x_l = set(np.where(border_points_x < x_range[1])[0])
            set_x = inside_points_x_h & inside_points_x_l

            inside_points_y_h = set(np.where(y_range[0] < border_points_y)[0])
            inside_points_y_l = set(np.where(border_points_y < y_range[1])[0])
            set_y = inside_points_y_h & inside_points_y_l
            intersection = set_x & set_y
            if len(list(intersection)) == 0:
                break
        return max_area



if __name__ == "__main__":
    start_time = time()
    T = Tiles("input9.txt")
    result = T.execute()
    print(result)
    end_time = time()
    print(f"Time taken: {end_time - start_time} seconds")
