import threading
threading.stack_size(33554432)
from matplotlib import pyplot as plt
import json
import timeit
import sys
sys.setrecursionlimit(20000)

def func1(arr, low, high):
    if low < high:
        pi = func2(arr, low, high)
        func1(arr, low, pi-1)
        func1(arr, pi + 1, high)

def func2(array, start, end):
    p = array[start]
    low = start + 1
    high = end
    while True:
        while low <= high and array[high] >= p:
            high = high - 1
        while low <= high and array[low] <= p:
            low = low + 1
        if low <= high:
            array[low], array[high] = array[high], array[low]
        else:
            break
    array[start], array[high] = array[high], array[start]
    return high

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
    plt.title("Timing Results for func1 (2.2)")
    plt.xlabel("Length of Array")
    plt.ylabel("Time taken for Array to be Sorted (sec)")
    plt.show()



