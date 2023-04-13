from array import array
import binary_search_tree as BST
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

def search_time(searched, values, search_function):
    start = time.time()
    for value in values:
        search_function(searched, value)
    time.sleep(0.2)
    return time.time() - start - 0.2

def search_in_tree_time(tree, values):
    start = time.time()
    for value in values:
        tree.find(value)
    time.sleep(0.2)
    return time.time() - start - 0.2

n=500
for i in range(10):
    A = array('i')
    n+=500
    for j in range(n):
        while True:
            x = random.randint(0, 1000)
            if x not in A:
                A.append(x)
                break

    #kolejne wartości tablicy tab mają być znajdowane w jej posortowanych kopiach 

    # CB
    start = time.time()

    B = array('i', A)
    quicksort(B)
    time.sleep(0.2)
    CB = time.time() - start - 0.2

    #SA

    SA = search_time(A, B, linear_search)

    #SB
    SB = search_time(B, A, binary_search)

    #CTA
    start = time.time()
    TA = BST.Node(A[0])
    for i in A:
        TA.insert(i)

    time.sleep(0.2)
    CTA = time.time() - start - 0.2

    #hTA
    hTA = TA.height()

    #STA
    STA = search_in_tree_time(TA, A)
    
    #tablica pomocnicza
    help = array('i')
