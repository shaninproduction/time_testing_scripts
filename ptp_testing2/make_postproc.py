import os
import sys
from matplotlib import pyplot as plt


def graph():
    data = dict()

    dir = "./preproc/"

    files = os.listdir(dir)
    files.sort()

    for file in files:

        filename = os.fsdecode(file)        
        with open(f"./preproc/{filename}", "r") as file:
            if filename not in data:
                data[filename] = [[], []]

            values = file.readlines()
            for i in range(len(values)):
                values[i] = values[i].split()

            for value in values:
                data[filename][0].append(int(value[0]))
                data[filename][1].append(float(value[1]))

    for key in data:    
        plt.plot(data[key][0], data[key][1], label = key)

    plt.savefig("./graphs/graph.svg")
    plt.legend()
    plt.title("Линейно-кусочный график")
    plt.xlabel("Размер матрицы")
    plt.ylabel("Время выполнения, мс")
    plt.show()


if __name__ == "__main__":
    graph()
