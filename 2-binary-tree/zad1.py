from array import array
import time
import random

def quicksort(arr, start=0, end=None):
    if end is None:
        end = len(arr) - 1

    if start < end:
        pivot_index = partition(arr, start, end)
        quicksort(arr, start, pivot_index - 1)
        quicksort(arr, pivot_index + 1, end)

def partition(arr, start, end):
    pivot_value = arr[end]
    i = start - 1

    for j in range(start, end):
        if arr[j] <= pivot_value:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[end] = arr[end], arr[i + 1]
    return i + 1

def linear_search(arr, value):
    for i in range(len(arr)):
        if arr[i] == value:
            return i


def binary_search(arr, value):
    left = 0
    right = len(arr) - 1

    while left <= right:
        middle = (left + right) // 2
        if arr[middle] == value:
            return middle
        elif arr[middle] < value:
            left = middle + 1
        else:
            right = middle - 1

    return -1

def time_of_search(arr, tab, search_function):
    start = time.time()
    for value in tab:
        search_function(arr, value)
    time.sleep(0.2)
    return time.time() - start - 0.2

n=0
for i in range(10):
    tab = array('i')
    n+=50
    for j in range(n):
        #elements cannot repeat
        while True:
            x = random.randint(0, 1000)
            if x not in tab:
                tab.append(x)
                break

    #kolejne wartości tablicy tab mają być znajdowane w jej posortowanych kopiach 

    # CB
    start = time.time()
    tab_copy = array('i', tab)
    quicksort(tab_copy)
    time.sleep(0.2)
    CB = time.time() - start - 0.2

    #SA
    SA = time_of_search(tab_copy, tab, linear_search)

    #SB
    SB = time_of_search(tab_copy, tab, binary_search)