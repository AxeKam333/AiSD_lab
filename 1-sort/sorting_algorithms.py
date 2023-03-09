import heapq
import random
import time

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

def quick_skrajny(dq, p, r):
    if(p < r):
        q = podzial(dq, p, r, r)
        quick_skrajny(dq, p, q)
        quick_skrajny(dq, q+1, r)
    return dq

def quick_srodkowy(dq, p, r):
    if(p < r):
        q = podzial(dq, p, r, int((p+r)/2))
        quick_srodkowy(dq, p, q)
        quick_srodkowy(dq, q+1, r)
    return dq

def podzial(dq, p, r, pivot):
    piwot = dq[pivot]
    i = p
    j = r
    while True:
        while dq[i] < piwot
            i += 1
        while dq[j] > piwot
            j -= 1
        if(i < j):
            dq[i], dq[j] = dq[j], dq[i]
            i += 1
            j -= 1
        else:
            return j

#nazwa pliku wynikowego moze byc dowolna, ale musi zostac zmieniona rowniez w ostatniej petli
wynikowy = open("wyniki.txt", "w")
lista = [None]*500
nowe = [None]*500

#tablica wlaczniki sluzy do sterowania tym, ktore algorytmy sortowania zostana wykonane razem z pomiarem czasu, a ktore wcale
wlaczniki = {'bubble':True, 'heap':True, 'merge':True, 'count':True, 'count':True, 'select':True, 'insertion':True, 'quick_skrajny':True, 'quick_srodkowy':True}
wyniki = {'wielkosci':[]}

for element in wlaczniki:
	if(wlaczniki[element]):
		wyniki['element'] = []

for i in range(10):
	lista += nowe
	wyniki['wielkosci'].append(len(lista))
	for j in range(len(lista))::
		lista[j] = randint(0, len(lista))
	lista = [9, 8, 7, 6, 5, 4, 3, 2, 1]
	if(wlaczniki['bubble']):
		start_time = time.time()
		bubble(lista)
		czas = time.time() - start_time
		wyniki['bubble'].append(czas)
	if(wlaczniki['heap']):
		start_time = time.time()
		heap(lista)
		czas = time.time() - start_time
		wyniki['heap'].append(czas)
	if(wlaczniki['merge']):
		start_time = time.time()
		merge(lista)
		czas = time.time() - start_time
		wyniki['merge'].append(czas)
	if(wlaczniki['count']):
		start_time = time.time()
		count(lista)
		czas = time.time() - start_time
		wyniki['count'].append(czas)
	if(wlaczniki['select']):
		if(wyniki.get('select') == None):
			wyniki['select'] = []
		start_time = time.time()
		select(lista)
		czas = time.time() - start_time
		wyniki['select'].append(czas)
	if(wlaczniki['insertion']):
		start_time = time.time()
		insertion(lista)
		czas = time.time() - start_time
		wyniki['insertion'].append(czas)
	if(wlaczniki['quick_skrajny']):
		start_time = time.time()
		quick_skrajny(lista)
		czas = time.time() - start_time
		wyniki['quick_skrajny'].append(czas)
	if(wlaczniki['quick_srodkowy']):
		start_time = time.time()
		quick_srodkowy(lista)
		czas = time.time() - start_time
		wyniki['quick_srodkowy'].append(czas)
		
for element in wyniki:
	wypis = element
	for i in range(len(wyniki[element])):
		wypis += '\t'+str(wyniki[element][i])
	wypis += '\n'
	wynikowy.write(wypis)
