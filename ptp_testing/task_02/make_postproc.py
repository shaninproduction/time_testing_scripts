import os
import sys
from matplotlib import pyplot as plt

def get_size(filename : str):
    size = ""
    flag = False
    for i in filename:
        if i.isdigit():
            flag = True
            size += i
        else:
            if flag == True:
                return int(size)
    return int(size)

def get_name(name : str):
    cur_name = ""
    for i in range(len(name) - 2):
        if name[i + 2].isdigit():
            cur_name += name[i]
            return cur_name
        cur_name += name[i]

def get_name_with_O(name : str):
    if "O2" in name:
        return (get_name(name) + "_O2")
    return (get_name(name) + "_O0")

def second_graph():

    data = dict()

    dir = "./preproc/average/"

    files = os.listdir(dir)
    files.sort()

    for i in range(len(files)):
        for j in range(0, len(files) - i - 1):
            if(get_size(files[j]) > get_size(files[j + 1])):
                files[j], files[j + 1] = files[j + 1], files[j]

    for file in files:

        filename = os.fsdecode(file)        
        if filename.startswith("random"):
            with open(f"./preproc/average/{filename}", "r") as file:
                if get_name_with_O(filename) not in data:
                    data[get_name_with_O(filename)] = [[], []]

                data[get_name_with_O(filename)][0].append(get_size(filename))
                data[get_name_with_O(filename)][1].append(float(file.readline()[:-1]))

    for key in data:    
        plt.plot(data[key][0], data[key][1], label = key)

    plt.savefig("./graphs/second.svg")
    plt.legend()
    plt.xlabel("Размер массива")
    plt.ylabel("Время выполнения")
    plt.show()



def first_graph():
    data = dict()

    dir = "./preproc/average/"

    files = os.listdir(dir)
    files.sort()

    for i in range(len(files)):
        for j in range(0, len(files) - i - 1):
            if(get_size(files[j]) > get_size(files[j + 1])):
                files[j], files[j + 1] = files[j + 1], files[j]

    for file in files:

        filename = os.fsdecode(file)        
        if filename.startswith("sorted"):
            with open(f"./preproc/average/{filename}", "r") as file:
                if get_name_with_O(filename) not in data:
                    data[get_name_with_O(filename)] = [[], []]

                data[get_name_with_O(filename)][0].append(get_size(filename))
                data[get_name_with_O(filename)][1].append(float(file.readline()[:-1]))

    for key in data:    
        plt.plot(data[key][0], data[key][1], label = key)

    plt.savefig("./graphs/first.svg")
    plt.legend()
    plt.xlabel("Размер массива")
    plt.ylabel("Время выполнения")
    plt.show()


def third_graph():
    
    data = dict()

    dir = "./preproc/average/"

    files = os.listdir(dir)
    files.sort()

    for i in range(len(files)):
        for j in range(0, len(files) - i - 1):
            if(get_size(files[j]) > get_size(files[j + 1])):
                files[j], files[j + 1] = files[j + 1], files[j]

    for file in files:

        filename = os.fsdecode(file)        
        if filename.endswith("O2.txt"):
            with open(f"./preproc/average/{filename}", "r") as file, open(f"preproc/min/{filename}", "r") as file_min, \
                open(f"preproc/max/{filename}", "r") as file_max:
                if get_name_with_O(filename) not in data:
                    data[get_name_with_O(filename)] = [[], [], [[],[]]]

                avg = float(file.readline()[:-1])

                data[get_name_with_O(filename)][0].append(get_size(filename))
                data[get_name_with_O(filename)][1].append(avg)
                data[get_name_with_O(filename)][2][0].append(abs(avg - float(file_min.readline()[:-1])))
                data[get_name_with_O(filename)][2][1].append(float(file_max.readline()[:-1]) - avg)

    i = 1
    for key in data:
        plt.subplot(3, 2, i)
        plt.plot(data[key][0], data[key][1], label= key)
        plt.errorbar(data[key][0], data[key][1], yerr=data[key][2], fmt="o", ecolor="b", capsize=1)
        plt.legend()
        plt.xlabel("Размер массива")
        plt.ylabel("Время выполнения")
        i += 1

    plt.savefig("./graphs/third.svg", bbox_inches='tight')
    plt.show()

def fourth_graph():
     
    data = dict()

    dir = "./preproc/average/"

    files = os.listdir(dir)
    files.sort()

    for i in range(len(files)):
        for j in range(0, len(files) - i - 1):
            if(get_size(files[j]) > get_size(files[j + 1])):
                files[j], files[j + 1] = files[j + 1], files[j]

    for file in files:

        filename = os.fsdecode(file)        
        if filename.endswith("O2.txt") and "not_index" not in filename and "index" in filename:
            with open(f"./preproc/average/{filename}", "r") as file:
                if get_name_with_O(filename) not in data:
                    data[get_name_with_O(filename)] = [[], []]

                avg = float(file.readline()[:-1])

                data[get_name_with_O(filename)][0].append(get_size(filename))
                data[get_name_with_O(filename)][1].append(avg)
               
    mega_data = []
    keys = []
    for key in data:
        mega_data.append(data[key][1])
        keys.append(key)
    
    plt.boxplot(mega_data, labels=keys)
    plt.xlabel("Размер массива")
    plt.ylabel("Время выполнения")
    plt.legend()
    plt.savefig("./graphs/fourth.svg")
    plt.show()

if __name__ == "__main__":

    first_graph()
    second_graph()
    third_graph()
    fourth_graph()
    
