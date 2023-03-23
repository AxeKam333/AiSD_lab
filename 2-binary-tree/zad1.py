from array import array
import time
import random

def quicksort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = array('i')
    right = array('i')

    for item in arr:
        if item <= pivot:
            left.append(item)
        else:
            right.append(item)

    return quicksort(left) + pivot + quicksort(right)

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
    print(tab)

    # CB
    start = time.time()

    # create copy of array tab
    tab_copy = array('i', tab)

