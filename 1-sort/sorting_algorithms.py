import heapq


def bubble(dq):
    sortd = False
    while True:
        cont = False
        for i in range(len(dq) - 1):
            if dq[i] > dq[i + 1]:
                cont = True
                sv = dq[i]
                dq[i] = dq[i + 1]
                dq[i + 1] = sv
        if not cont:
            return dq


def heap(dq):  # uzywa wbudowanej biblioteki do stworzenia stogu w czasie rzeczywistym
    heapq.heapify(dq)
    res = []
    while len(dq):
        res.append(heapq.heappop(dq))
    return res


def merge(dq):
    if len(dq) > 1:

        mid = len(dq) // 2
        left = dq[:mid]
        right = dq[mid:]
        merge(left)
        merge(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                dq[k] = left[i]
                i += 1
            else:
                dq[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            dq[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            dq[k] = right[j]
            j += 1
            k += 1
        return dq

def count(dq):
    dlugosc = len(dq)
    zliczone = [0]*dlugosc
    output = [None]*dlugosc
    for i in range(dlugosc):
        zliczone[dq[i]] += 1
    for i in range(dlugosc-1, -1, -1):
        output[zliczone[dq[i]] - 1] = dq[i]
        zliczone[dq[i]] -= 1
    dq = output
    return dq

def select(dq):
    dlugosc = len(dq)
    for i in range(dlugosc):
        najmniejszy = dq[i]
        indeks_min = i
        for j in range(i, dlugosc):
            if(dq[j] < najmniejszy):
                najmniejszy = dq[j]
                indeks_min = j
        dq[i], dq[indeks_min] = dq[indeks_min], dq[i]
    return dq

def insertion(dq):
    dlugosc = len(dq)
    for i in range(dlugosc):
        j = i
        while(j > 0 and dq[j-1] > dq[j])
            dq[j-1], dq[j] = dq[j], dq[j-1]
    return dq
    

lista = [9, 8, 7, 6, 5, 4, 3, 2, 1]
bubble(lista)
heap(lista)
merge(lista)
count(lista)
select(lista)
insertion(lista)
