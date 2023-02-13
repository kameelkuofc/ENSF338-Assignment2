import threading
threading.stack_size(33554432)
from matplotlib import pyplot as plt
import json
import timeit
import sys
sys.setrecursionlimit(20000)
import random

def func1(arr, low, high):
    if low < high:
        pi = func2(arr, low, high)
        func1(arr, low, pi)
        func1(arr, pi + 1, high)

def func2(array, start, end):
    pivot = random.randint(start, end)
    array[pivot], array[end] = array[end], array[pivot]
    pivot = array[end]
    i = start - 1
    for j in range(start, end):
        if array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]
    array[i + 1], array[end] = array[end], array[i + 1]
    return i


if __name__ == '__main__':

    with open("quickSort_q2.json", "r") as arrays:
        arr = json.load(arrays)
    timeArray = []
    lengthArray = []
    i = 0
    while(i < len(arr)):
        end = len(arr[i]) - 1
        elapsed = timeit.timeit(lambda : func1((arr[i]), 0, end), number=1)
        timeArray.append(elapsed)
        lengthArray.append(len(arr[i]))
        i += 1


    print(timeArray)
    plt.plot(lengthArray, timeArray)
    plt.title("Timing Results for func1 (2.4)")
    plt.xlabel("Length of Array")
    plt.ylabel("Time taken for Array to be Sorted (sec)")
    plt.show()



