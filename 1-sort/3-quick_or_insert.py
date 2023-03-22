import random
import time
import sys
sys.setrecursionlimit(6000)

# cale sterowanie odbywa sie za pomoca slownika 'wlaczniki' ponizej funkcji sortujacych

def insertion(dq,a,b):
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

# nazwa pliku wynikowego moze byc dowolna, ale musi zostac zmieniona rowniez w ostatniej petli
file_name="zad3.txt"
wynikowy = open(file_name, "w")
wielkosc = 500

# tablica wlaczniki sluzy do sterowania tym, ktore algorytmy sortowania zostana wykonane razem z pomiarem czasu, a ktore wcale
wlaczniki = {'insertion': True, 'quick_skrajny': True, 'quick_srodkowy': True}
wyniki = {'wielkosci': []}

for element in wlaczniki:
    if (wlaczniki[element]):
        wyniki[str(element)+'notsorted'] = []
        wyniki[str(element)+'presorted'] = []


def licz_czas(lista,fun_sortuj):
    start_time = time.time()
    lista = fun_sortuj(lista, 0, len(lista)-1)
    time.sleep(0.5)
    return lista,time.time() - start_time - 0.5

presorted = 'notsorted'
for j in range(2):
    wielkosc=500
    for i in range(10):
    # for i in range(1):
        wielkosc += 500
        lista_ = [None]*wielkosc
        wyniki['wielkosci'].append(len(lista_))
        for j in range(len(lista_)):
            lista_[j] = random.randint(1, wielkosc)
            
        if presorted=='presorted':
            lista_=quick_srodkowy(lista_,0,len(lista_)-1)

        if (wlaczniki['insertion']):
            sortd,czas=licz_czas(lista_,insertion)
            print("IS",sortd)
            wyniki['insertion'+presorted].append(czas)
        if (wlaczniki['quick_skrajny']):
            sortd,czas=licz_czas(lista_,quick_skrajny)
            print("QSS",sortd)
            wyniki['quick_skrajny'+presorted].append(czas)
        if (wlaczniki['quick_srodkowy']):
            sortd,czas=licz_czas(lista_,quick_srodkowy)
            print("QSŚ",sortd)
            wyniki['quick_srodkowy'+presorted].append(czas)
    for element in wyniki:
        wypis = element
        for i in range(len(wyniki[element])):
            wypis += '\t' + str(wyniki[element][i])
        wypis += '\n'
        wynikowy.write(wypis)
    presorted = 'presorted'
