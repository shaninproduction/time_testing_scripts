import os
import math as m

def get_average(filename : str):
    average = 0
    counter = 1
    with open(filename, "r") as file:
        for num in file:
            average += int(num)
            counter += 1
    
    return average / counter

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
    if "O0" in name:
        return (get_name(name) + "_O0")
    elif "O3" in name:
            return (get_name(name) + "_O3")
    return (get_name(name) + "_Os")


def get_dispersion(filename :str):
    count = 0
    tavg = get_average(filename)
    summa = 0
    with open(filename, "r") as file:
        for time_i in file:
            summa += (int(time_i) - tavg)**2
            count += 1

    if count == 1:
        return 0
    
    dispersion = 1/(count - 1) * summa

    return dispersion


def get_stddev(filename : str):
    return m.sqrt(get_dispersion(filename))

def get_stderr(filename):
    count = 0

    with open(filename, "r") as file:
        for i in file:
            count += 1

    return get_stddev(filename) / count 


def get_stderr_avg(filename : str):
    tn = get_average(filename)
    
    if tn != 0:
        return get_stderr(filename) / tn * 100
    
    return get_stderr(filename) * 100

def sort(filename : str):
    with open(filename, 'r') as f:
        new_list = []
        for line in f.readlines():
            new_list.append(line.split(' '))
        new_list.sort(key=lambda x: int(x[0]))
    with open(filename, 'w') as f:
        for line in new_list:
            f.write(' '.join(line))

def get_ln(filename : str):

    with open(filename, "r") as file:
        values = file.readlines()

        for i in range(len(values) - 1):
            cur = values[i].split()
            next = values[i + 1].split()
            
            ln = ((m.log(float(next[1])) - m.log(float(cur[1]))) / (m.log(int(next[0])) - m.log(int(cur[0]))))
            cur.append(f"{ln:.3f}")

            values[i] = " ".join(cur)


    with open(filename, "w") as file:
        for value in values:
            if value[-1:] == "\n":
                print(value[:-2], file=file)
            else:
                print(value, file=file)

if __name__ == "__main__":

    os.system("./clean_preproc.sh")
    dir = os.fsencode("./data")

    for file in os.listdir(dir):
        filename = os.fsdecode(file)
        
        average = get_average(f"./data/{filename}")
        stderr = get_stderr(f"./data/{filename}")
        with open(f"./preproc/{get_name_with_O(filename)}.txt", "a+") as file:
            print(f"{get_size(filename)} {average:.3f} {stderr:.3f}", file=file)
    
    dir = os.fsencode("./preproc")

    for file in os.listdir(dir):
        filename = os.fsdecode(file)
        sort(f"./preproc/{filename}")


    dir = os.fsencode("./preproc")

    for file in os.listdir(dir):
        filename = os.fsdecode(file)
        get_ln(f"./preproc/{filename}")
    