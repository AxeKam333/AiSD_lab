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

    # CB
    start = time.time()
    tab_copy = array('i', tab)
    quicksort(tab_copy)
    time.sleep(0.2)
    CB = time.time() - start - 0.2