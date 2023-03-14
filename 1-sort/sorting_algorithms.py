import heapq
import random
import time
import sys
sys.setrecursionlimit(6000)

# cale sterowanie odbywa sie za pomoca slownika 'wlaczniki' ponizej funkcji sortujacych

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


def merge(x):
    dq = x
    if len(dq) > 1:
        mid = len(dq) // 2
        left = dq[0:mid]
        right = dq[mid:len(dq)]
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
    output = [0]*(dlugosc+1)
    zliczone = [0]*(dlugosc+1)
    for i in range(dlugosc):
        zliczone[dq[i]] += 1
    for i in range(len(zliczone)):
        zliczone[i] += zliczone[i-1]
    i = dlugosc-1
    while(i>=0):

        # print(zliczone[dq[i]] -1)
        # 1000
        #
        # Traceback (most recent call last):
        # File "1-sort/sorting_algorithms.py", line 71, in count
        #     output[zliczone[dq[i]] -1] = dq[i]
        # IndexError: list assignment index out of range

        output[zliczone[dq[i]] -1] = dq[i]
        zliczone[dq[i]] -= 1
        i -= 1
    for i in range(dlugosc):
        dq[i] = output[i+1]
    return dq


def select(dq):
    dlugosc = len(dq)
    for i in range(dlugosc):
        najmniejszy = dq[i]
        indeks_min = i
        for j in range(i, dlugosc):
            if (dq[j] < najmniejszy):
                najmniejszy = dq[j]
                indeks_min = j
        dq[i], dq[indeks_min] = dq[indeks_min], dq[i]
    return dq


def insertion(dq):
    for i in range(1, len(dq)):
        klucz = dq[i]
        j = i-1
        while(j>=0 and klucz < dq[j]):
            dq[j+1] = dq[j]
            j -= 1
        dq[j+1] = klucz
    return dq

def podzial(dq, p, r, pivot):
    dq[r],dq[pivot]=dq[pivot],dq[r]
    piwot = dq[r]
    #print(f"podzial po {piwot} ({dq})")
    i = p
    j = r
    while True:
        while ((dq[i] <= piwot) and (i<j)):
            i += 1
        while((dq[j-1] > piwot) and (j>i+1)):
            dq[j]=dq[j-1]
            j -= 1
        if(i < j):
            dq[i], dq[j] = dq[j-1], dq[i]
            i += 1
            j -= 1
        else:
            #print(f"gdzie wstawic {dq} ({i} {j})")
            dq[j]=piwot
            return j

def quick_skrajny(dq, p, r):
    #print(f"skrajny {len(dq)}, {p}, {r}")
    if (p < r):
        q = podzial(dq, p, r, r)
        #print(f"zwrocilo {q} na tablicy {dq}")
        quick_skrajny(dq, p, q-1)
        quick_skrajny(dq, q+1, r)
        #print(dq)
    return dq

def quick_srodkowy(dq, p, r):
    #print(f"srodkowy {len(dq)}, {p}, {r}")
    if (p < r):
        q = podzial(dq, p, r, (p + r) // 2)
        #print(f"po podziale {dq} na {q}")
        quick_srodkowy(dq, p, q-1)
        quick_srodkowy(dq, q+1, r)
    return dq

def quick_losowy(dq, p, r):
    #print(f"losowy {len(dq)}, {p}, {r}")
    if (p < r):
        q = podzial(dq, p, r, random.randint(p,r))
        #print(f"po podziale {dq} na {q}")
        quick_srodkowy(dq, p, q-1)
        quick_srodkowy(dq, q+1, r)
    return dq

#t=[5,4,2,1,0]
#t=[5,4,2,1,6]
#t=[5,4,2,1,3]
# print(podzial(t,0,len(t)-1,len(t)-1))
#t=[5,4,6,1,2]
#t=[5,4,0,1,2]
#t=[5,4,3,1,2]
# print(podzial(t,0,len(t)-1,2))

# print(quick_srodkowy(t,0,len(t)-1))
# print(t)
# sys.exit(-1)


# nazwa pliku wynikowego moze byc dowolna, ale musi zostac zmieniona rowniez w ostatniej petli
wynikowy = open("wyniki.txt", "w")
wielkosc = 500

# tablica wlaczniki sluzy do sterowania tym, ktore algorytmy sortowania zostana wykonane razem z pomiarem czasu, a ktore wcale
wlaczniki = {'bubble': True, 'heap': True, 'merge': True, 'count': True, 'select': True,
             'insertion': True, 'quick_skrajny': True, 'quick_srodkowy': True, 'quick_losowy': True}
wyniki = {'wielkosci': []}

for element in wlaczniki:
    if (wlaczniki[element]):
        wyniki[element] = []




#for i in range(10):
for i in range(1):
    wielkosc += 500
    lista_original = [None]*wielkosc
    wyniki['wielkosci'].append(len(lista_original))
    for j in range(len(lista_original)):
        lista_original[j] = random.randint(1, wielkosc)
    #lista_original=[4,4,3,1,2]
    #print(lista_original)
    if (wlaczniki['bubble']):
        lista=lista_original.copy()
        start_time = time.time()
        print("BS",bubble(lista))
        time.sleep(0.5)
        czas = time.time() - start_time - 0.5
        wyniki['bubble'].append(czas)
    if (wlaczniki['heap']):
        lista=lista_original.copy()
        start_time = time.time()
        print("HS",heap(lista))
        time.sleep(0.5)
        czas = time.time() - start_time - 0.5
        wyniki['heap'].append(czas)
    #print(lista)
    if (wlaczniki['merge']):
        lista = lista_original.copy()
        start_time = time.time()
        print("MS",merge(lista))
        time.sleep(0.5)
        czas = time.time() - start_time - 0.5
        wyniki['merge'].append(czas)
    if (wlaczniki['count']):
        lista = lista_original.copy()
        start_time = time.time()
        print("CS",count(lista))
        time.sleep(0.5)
        czas = time.time() - start_time - 0.5
        wyniki['count'].append(czas)
    if (wlaczniki['select']):
        lista = lista_original.copy()
        start_time = time.time()
        print("SS",select(lista))
        time.sleep(0.5)
        czas = time.time() - start_time - 0.5
        wyniki['select'].append(czas)
    if (wlaczniki['insertion']):
        lista = lista_original.copy()
        start_time = time.time()
        print("IS",insertion(lista))
        time.sleep(0.5)
        czas = time.time() - start_time - 0.5
        wyniki['insertion'].append(czas)
    if (wlaczniki['quick_skrajny']):
        lista = lista_original.copy()
        start_time = time.time()
        print("QSS",quick_skrajny(lista, 0, len(lista)-1))
        time.sleep(0.5)
        czas = time.time() - start_time - 0.5
        wyniki['quick_skrajny'].append(czas)
    if (wlaczniki['quick_srodkowy']):
        lista = lista_original.copy()
        start_time = time.time()
        print("QSŚ",quick_srodkowy(lista, 0, len(lista)-1))
        time.sleep(0.5)
        czas = time.time() - start_time - 0.5
        wyniki['quick_srodkowy'].append(czas)
    if (wlaczniki['quick_losowy']):
        lista = lista_original.copy()
        start_time = time.time()
        print("QSL",quick_losowy(lista, 0, len(lista)-1))
        time.sleep(0.5)
        czas = time.time() - start_time - 0.5
        wyniki['quick_losowy'].append(czas)
        # da sie to zrobic jedna procedura ktora jako argument przyjmuje funkcje sortujace 
for element in wyniki:
    wypis = element
    for i in range(len(wyniki[element])):
        wypis += '\t' + str(wyniki[element][i])
    wypis += '\n'
    wynikowy.write(wypis)
