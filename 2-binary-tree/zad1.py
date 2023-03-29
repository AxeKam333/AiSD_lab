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

def wypelnienie_polowkowe(Z, help, p, r):
    if (p>r):
        return
    elif (p==r):
        #print(f"Wstawiam element {p} o wartosci {Z[p]}")
        help.append(Z[p])
    else:
        s=(p+r)//2
        help.append(Z[s])
        wypelnienie_polowkowe(Z, help, p, s-1)
        wypelnienie_polowkowe(Z, help, s+1, r)

w = open("wyniki.txt", 'w')
wynik_wielkosci = ''
wynik_CB = ''
wynik_SA = ''
wynik_SB = ''
wynik_CTA = ''
wynik_hTA = ''
wynik_STA = ''
wynik_CTB = ''
wynik_STB = ''
wynik_hTB = ''
n=500
for i in range(10):
    A = array('i')
    n+=500
    print(n)
    wynik_wielkosci += str(n) + '\t'
    for j in range(n):
        while True:
            x = random.randint(1, n)
            if x not in A:
                A.append(x)
                break
    CB = 0
    SA = 0
    SB = 0
    CTA = 0
    hTA = 0
    STA = 0
    CTB = 0
    STB = 0
    hTB = 0
    #kolejne wartości tablicy tab mają być znajdowane w jej posortowanych kopiach 
    for j in range(10):
        #CB
        start = time.time()
        B = array('i', A)
        quicksort(B)
        time.sleep(0.2)
        CB += (time.time() - start - 0.2)

        #SA
        SA += search_time(A, B, linear_search)

        #SB
        SB += search_time(B, A, binary_search)

        #CTA
        start = time.time()
        TA = BST.Node(A[0])
        for i in A:
            TA.insert(i)

        time.sleep(0.2)
        CTA += (time.time() - start - 0.2)

        #hTA
        hTA += TA.height()

        #STA
        STA += search_in_tree_time(TA, A)

        #tablica pomocnicza
        help = array('i')
        #Z = B.copy()
        wypelnienie_polowkowe(B, help, 0, len(B)-1)
        start = time.time()
        TB = BST.Node(help[0])
        for i in range(1,len(help)):
            TB.insert(help[i])
        time.sleep(0.2)
        CTB += time.time() - start - 0.2
        hTB += TB.height()

        STB += search_in_tree_time(TB, A)
    CB /= 10
    wynik_CB += str(CB) + '\t'
    SA /= 10
    wynik_SA += str(SA) + '\t'
    SB /= 10
    wynik_SB += str(SB) + '\t'
    CTA /= 10
    wynik_CTA += str(CTA) + '\t'
    hTA //= 10
    wynik_hTA += str(hTA) + '\t'
    STA /= 10
    wynik_STA += str(STA) + '\t'
    CTB /= 10
    wynik_CTB += str(CTB) + '\t'
    hTB //= 10
    wynik_hTB += str(hTB) + '\t'
    STB /= 10
    wynik_STB += str(STB) + '\t'

w.write(wynik_wielkosci + '\n')
w.write(wynik_CB + '\n')
w.write(wynik_CTA + '\n')
w.write(wynik_CTB + '\n')
w.write(wynik_SA + '\n')
w.write(wynik_SB + '\n')
w.write(wynik_STA + '\n')
w.write(wynik_STB + '\n')
w.write(wynik_hTA + '\n')
w.write(wynik_hTB)
