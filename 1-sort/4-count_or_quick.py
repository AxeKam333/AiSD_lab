import random
import time
import sys
sys.setrecursionlimit(6000)

# cale sterowanie odbywa sie za pomoca slownika 'wlaczniki' ponizej funkcji sortujacych

def count(dq,a,b):
    dlugosc = len(dq)
    output = [0]*(dlugosc+2)
    zliczone = [0]*(dlugosc+2)
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

def quick_srodkowy(dq, p, r):
    #print(f"srodkowy {len(dq)}, {p}, {r}")
    if (p < r):
        q = podzial(dq, p, r, (p + r) // 2)
        #print(f"po podziale {dq} na {q}")
        quick_srodkowy(dq, p, q-1)
        quick_srodkowy(dq, q+1, r)
    return dq


# nazwa pliku wynikowego moze byc dowolna, ale musi zostac zmieniona rowniez w ostatniej petli
wynikowy = open("wyniki.txt", "w")
wielkosc = 500

# tablica wlaczniki sluzy do sterowania tym, ktore algorytmy sortowania zostana wykonane razem z pomiarem czasu, a ktore wcale
wlaczniki = {'count': True, 'quick_srodkowy': True}
wyniki = {'wielkosci': []}

for element in wlaczniki:
    if (wlaczniki[element]):
        wyniki[element] = []


def licz_czas(lista,fun_sortuj):
    start_time = time.time()
    lista = fun_sortuj(lista, 0, len(lista)-1)
    time.sleep(0.5)
    return lista,time.time() - start_time - 0.5


for i in range(2):
    wielkosc += 500
    lista_original = [None]*wielkosc
    wyniki['wielkosci'].append(len(lista_original))
    for j in range(len(lista_original)):
        lista_original[j] = random.randint(1, wielkosc)
    #lista_original=[4,4,3,1,2]
    #print(lista_original)
    if (wlaczniki['count']):
        sortd,czas=licz_czas(lista_original,count)
        print("QSŚ",sortd)
        wyniki['quick_srodkowy'].append(czas)
    if (wlaczniki['quick_srodkowy']):
        sortd,czas=licz_czas(lista_original,quick_srodkowy)
        print("QSŚ",sortd)
        wyniki['quick_srodkowy'].append(czas)
for element in wyniki:
    wypis = element
    for i in range(len(wyniki[element])):
        wypis += '\t' + str(wyniki[element][i])
    wypis += '\n'
    wynikowy.write(wypis)
