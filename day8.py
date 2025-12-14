from time import time
import numpy as np


class Circuits:
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def execute(self):
        data = self._load_txt_data()
        final_number = self._iterate_array_advanced(data)
        return final_number

    def _load_txt_data(self):
        with open(self.filename, 'r') as file:
            content = file.read()
        data = content.split('\n')
        return data

    @staticmethod
    def _iterate_array(data):
        numbers_arr = np.zeros((len(data) - 1, 3), dtype=int)
        for i in range(len(data) - 1):
            dat = data[i].split(sep=",")
            numbers_arr[i, :] = dat

        lengh = len(numbers_arr[:, 0])
        # Matice rozdílů
        diff_array = np.zeros((lengh, lengh), dtype=int)+np.inf # Ano ten np.inf jsem tam dala dneska
        for i in range(lengh):
            one_point = numbers_arr[i, :] #Díky tomu, že to jde od i bude vyplněná jenom horní část matice nad diagonálou
            for j in range(i, lengh):
                if i != j:
                    other_point = numbers_arr[j, :]
                    diff_array[i, j] = np.linalg.norm(one_point - other_point)

        list_of_sets = []
        points = int(lengh*lengh/2 - lengh/2)
        count = 0 # count počtu připojení
        fin_x = 0
        fin_y = 0
        for i in range(1000):
            # Toto je jeden bod z matice ale v podstatě indexy dvou bodů, které spojuju
            indexes_min_x = int(np.where(diff_array == np.min(diff_array))[0][0])
            indexes_min_y = int(np.where(diff_array == np.min(diff_array))[1][0])
            fin_x = indexes_min_x
            fin_y = indexes_min_y

            # Teď ten rozdíl zvětším, aby další iterace vzala jiné minimum
            diff_array[indexes_min_x, indexes_min_y] = np.inf

            count_not_in_set = 0
            indexes_of_set = []

            # Tady pro všechny sety v list_of_sets zkontroluju jak do nich spadají kontrolované body
            for j in range(len(list_of_sets)):
                set_points = list_of_sets[j]

                # Pokud jsou v nějakém setu oba body tak se pokračuje k další iteraci
                if indexes_min_x in set_points and indexes_min_y in set_points:
                    break

                # Pokud je v jednom setu tak se uloží index toho setu
                elif (indexes_min_x in set_points and indexes_min_y not in set_points) or (indexes_min_y in set_points and indexes_min_x not in set_points):
                    indexes_of_set.append(j)

                # Není v setu tak se to připočítá sem
                else:
                    count_not_in_set += 1

            # Když nebyly v žádném setu, tak se přidají a připočítá se count počtu připojení
            if count_not_in_set == len(list_of_sets):
                list_of_sets.append({indexes_min_x, indexes_min_y})

            # Jenom jeden z nich byl v setu, tak se přidají oba, takže se přidá ten co tam nebyl protože je to set :D
            if len(indexes_of_set) == 1:
                i = indexes_of_set[0]
                list_of_sets[i].add(indexes_min_x)
                list_of_sets[i].add(indexes_min_y)

            # Jeden byl v jednom setu a druhý v druhém, tak se to sloučí do setu s nižším indexem a smaže se ten s vyšším
            if len(indexes_of_set) == 2:
                k = indexes_of_set[0]
                m = indexes_of_set[1]
                if m > k:
                    list_of_sets[k] = list_of_sets[k].union(list_of_sets[m])
                    list_of_sets.pop(m)
                    list_of_sets[k].add(indexes_min_x)
                    list_of_sets[k].add(indexes_min_y)

                if m < k:
                    list_of_sets[m] = list_of_sets[m].union(list_of_sets[k])
                    list_of_sets.pop(k)
                    list_of_sets[m].add(indexes_min_x)
                    list_of_sets[m].add(indexes_min_y)

        # Velikosti setů a sortování
        sizes = []
        for set_points in list_of_sets:
            sizes.append(len(list(set_points)))
        sorted_sizes = np.array(sizes)
        sorted_sizes = np.sort(sorted_sizes)
        print(sorted_sizes)
        result = sorted_sizes[-1]*sorted_sizes[-2]*sorted_sizes[-3]

        return result

    @staticmethod
    def _iterate_array_advanced(data):
        numbers_arr = np.zeros((len(data) - 1, 3), dtype=int)
        for i in range(len(data) - 1):
            dat = data[i].split(sep=",")
            numbers_arr[i, :] = dat

        lengh = len(numbers_arr[:, 0])
        # Matice rozdílů
        diff_array = np.zeros((lengh, lengh),
                              dtype=int) + np.inf  # Ano ten np.inf jsem tam dala dneska
        for i in range(lengh):
            one_point = numbers_arr[i,
                        :]  # Díky tomu, že to jde od i bude vyplněná jenom horní část matice nad diagonálou
            for j in range(i, lengh):
                if i != j:
                    other_point = numbers_arr[j, :]
                    diff_array[i, j] = np.linalg.norm(one_point - other_point)

        list_of_sets = []
        points = int(lengh * lengh / 2 - lengh / 2)
        print(points)
        count = 0  # count počtu připojení
        fin_x = 0
        fin_y = 0
        for i in range(points):
            print(i)
            print(len(list_of_sets))
            # Toto je jeden bod z matice ale v podstatě indexy dvou bodů, které spojuju
            indexes_min_x = int(np.where(diff_array == np.min(diff_array))[0][0])
            indexes_min_y = int(np.where(diff_array == np.min(diff_array))[1][0])

            # Teď ten rozdíl zvětším, aby další iterace vzala jiné minimum
            diff_array[indexes_min_x, indexes_min_y] = np.inf

            count_not_in_set = 0
            indexes_of_set = []

            # Tady pro všechny sety v list_of_sets zkontroluju jak do nich spadají kontrolované body
            for i in range(len(list_of_sets)):
                set_points = list_of_sets[i]

                # Pokud jsou v nějakém setu oba body tak se pokračuje k další iteraci
                if indexes_min_x in set_points and indexes_min_y in set_points:
                    break

                # Pokud je v jednom setu tak se uloží index toho setu
                elif (indexes_min_x in set_points and indexes_min_y not in set_points) or (
                        indexes_min_y in set_points and indexes_min_x not in set_points):
                    indexes_of_set.append(i)

                # Není v setu tak se to připočítá sem
                else:
                    count_not_in_set += 1

            # Když nebyly v žádném setu, tak se přidají a připočítá se count počtu připojení
            if count_not_in_set == len(list_of_sets):
                # count += 1
                list_of_sets.append({indexes_min_x, indexes_min_y})

            # Jenom jeden z nich byl v setu, tak se přidají oba, takže se přidá ten co tam nebyl protože je to set :D
            if len(indexes_of_set) == 1:
                # count += 1
                i = indexes_of_set[0]
                list_of_sets[i].add(indexes_min_x)
                list_of_sets[i].add(indexes_min_y)
                fin_x = indexes_min_x
                fin_y = indexes_min_y

            # Jeden byl v jednom setu a druhý v druhém, tak se to sloučí do setu s nižším indexem a smaže se ten s vyšším
            if len(indexes_of_set) == 2:
                # count += 1
                k = indexes_of_set[0]
                m = indexes_of_set[1]
                fin_x = indexes_min_x
                fin_y = indexes_min_y
                if m > k:
                    list_of_sets[k] = list_of_sets[k].union(list_of_sets[m])
                    list_of_sets.pop(m)
                    list_of_sets[k].add(indexes_min_x)
                    list_of_sets[k].add(indexes_min_y)

                if m < k:
                    list_of_sets[m] = list_of_sets[m].union(list_of_sets[k])
                    list_of_sets.pop(k)
                    list_of_sets[m].add(indexes_min_x)
                    list_of_sets[m].add(indexes_min_y)
            if len(list(list_of_sets[0]))==lengh:
                break


        print(len(list(list_of_sets[0])))
        print(lengh)
        result = numbers_arr[fin_x, 0] * numbers_arr[fin_y, 0]
        return result

if __name__ == "__main__":
    start_time = time()
    C = Circuits("input8.txt")
    result = C.execute()
    print(result)
    end_time = time()
    print(f"Time taken: {end_time - start_time} seconds")