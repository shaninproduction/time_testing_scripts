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

def get_median(filename : str):
    data = []
    with open(filename, "r") as file:
        for num in file:
            data.append(int(num))
        data.sort()
        mid = len(data) // 2
        res = (data[mid] + data[~mid]) / 2
    return res
        
def get_min(filename : str):
    min = float("inf")
    with open(filename, "r") as file:
        for num in file:
            if int(num) < min:
                min = int(num)
    return min

def get_max(filename : str):
    max = float("-inf")
    with open(filename, "r") as file:
        for num in file:
            if int(num) > max:
                max = int(num)
    return max

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


if __name__ == "__main__":
    dir = os.fsencode("./data")

    for file in os.listdir(dir):
        filename = os.fsdecode(file)
        
        average = get_average(f"./data/{filename}")
        with open(f"./preproc/average/{filename}", "w") as file:
            print(f"{float(average):.3f}", file=file)

        median = get_median(f"./data/{filename}")
        with open(f"./preproc/median/{filename}", "w") as file:
            print(median, file=file)
        
        min = get_min(f"./data/{filename}")
        with open(f"./preproc/min/{filename}", "w") as file:
            print(min, file=file)

        max = get_max(f"./data/{filename}")
        with open(f"./preproc/max/{filename}", "w") as file:
            print(max, file=file)

        stderr = get_stderr(f"./data/{filename}")
        with open(f"./preproc/stderr/{filename}", "w") as file:
            print(stderr, file=file)

        stderr_avg = get_stderr_avg(f"./data/{filename}")
        with open(f"./preproc/stderr_avg/{filename}", "w") as file:
            print(stderr_avg, file=file)

        