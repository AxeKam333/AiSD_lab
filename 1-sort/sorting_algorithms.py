import heapq
import random
import time
sys.setrecursionlimit(6000)

#cale sterowanie odbywa sie za pomoca slownika 'wlaczniki' ponizej funkcji sortujacych

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
    output = [0]*(dlugosc)
    zliczone = [0]*(dlugosc+1)
    for i in range(dlugosc):
        zliczone[dq[i]] += 1
    for i in range(dlugosc):
        zliczone[i] += zliczone[i-1]
    i = dlugosc-1
    while(i >= 0):
        output[zliczone[dq[i]]] = dq[i]
        zliczone[dq[i]] -= 1
        i -= 1
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
        while(j > 0 and dq[j-1] > dq[j]):
            dq[j-1], dq[j] = dq[j], dq[j-1]
    return dq

def podzial(dq, p, r, pivot):
    dq[r],dq[pivot]=dq[pivot],dq[r]
    piwot = dq[r]
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
            dq[j]=piwot
            return j

def quick_skrajny(dq, p, r):
    if(p < r):
        q = podzial(dq, p, r, r)
        quick_skrajny(dq, p, q-1)
        quick_skrajny(dq, q+1, r)
    return dq

def quick_srodkowy(dq, p, r):
    if(p < r):
        q = podzial(dq, p, r, (p+r)//2)
        quick_srodkowy(dq, p, q-1)
        quick_srodkowy(dq, q+1, r)
    return dq

#nazwa pliku wynikowego moze byc dowolna, ale musi zostac zmieniona rowniez w ostatniej petli
wynikowy = open("wyniki.txt", "w")
wielkosc = 500

#tablica wlaczniki sluzy do sterowania tym, ktore algorytmy sortowania zostana wykonane razem z pomiarem czasu, a ktore wcale
wlaczniki = {'bubble':True, 'heap':True, 'merge':True, 'count':True, 'count':True, 'select':True, 'insertion':True, 'quick_skrajny':True, 'quick_srodkowy':True}
wyniki = {'wielkosci':[]}

for element in wlaczniki:
	if(wlaczniki[element]):
		wyniki[element] = []

for i in range(10):
	wielkosc += 500
	lista_original = [None]*wielkosc
	wyniki['wielkosci'].append(len(lista_original))
	for j in range(len(lista_original))::
		lista_original[j] = random.randint(0, len(lista_original))
	#lista = [9, 8, 7, 6, 5, 4, 3, 2, 1]
	if(wlaczniki['bubble']):
        lista = lista_original.copy()
		start_time = time.time()
		bubble(lista)
		time.sleep(0.5)
		czas = time.time() - start_time - 0.5
		wyniki['bubble'].append(czas)
	if(wlaczniki['heap']):
        lista = lista_original.copy()
		start_time = time.time()
		heap(lista)
		time.sleep(0.5)
		czas = time.time() - start_time - 0.5
		wyniki['heap'].append(czas)
	if(wlaczniki['merge']):
        lista = lista_original.copy()
		start_time = time.time()
		merge(lista)
		time.sleep(0.5)
		czas = time.time() - start_time - 0.5
		wyniki['merge'].append(czas)
	if(wlaczniki['count']):
        lista = lista_original.copy()
		start_time = time.time()
		count(lista)
		time.sleep(0.5)
		czas = time.time() - start_time - 0.5
		wyniki['count'].append(czas)
	if(wlaczniki['select']):
        lista = lista_original.copy()
		start_time = time.time()
		select(lista)
		czas = time.time() - start_time - 0.5
		wyniki['select'].append(czas)
	if(wlaczniki['insertion']):
        lista = lista_original.copy()
		start_time = time.time()
		insertion(lista)
		time.sleep(0.5)
		czas = time.time() - start_time - 0.5
		wyniki['insertion'].append(czas)
	if(wlaczniki['quick_skrajny']):
        lista = lista_original.copy()
		start_time = time.time()
		quick_skrajny(lista)
		time.sleep(0.5)
		czas = time.time() - start_time - 0.5
		wyniki['quick_skrajny'].append(czas)
	if(wlaczniki['quick_srodkowy']):
        lista = lista_original.copy()
		start_time = time.time()
		quick_srodkowy(lista)
		time.sleep(0.5)
		czas = time.time() - start_time - 0.5
		wyniki['quick_srodkowy'].append(czas)
		
for element in wyniki:
	wypis = element
	for i in range(len(wyniki[element])):
		wypis += '\t'+str(wyniki[element][i])
	wypis += '\n'
	wynikowy.write(wypis)
