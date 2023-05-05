#whyyyyyy m c a

import random
import time
import copy

def generator_macierzy(liczba, gestosc):
    generowana = [[0]*liczba for x in range(liczba)]
    y = gestosc
    krawedzi = ((liczba*(liczba-1))*gestosc)//2
    for i in range(liczba):
        for j in range(liczba):
            if(i == j):
                continue
            losowo = random.randint(0,100)/100
            if(losowo < gestosc and generowana[i][j] == 0):
                generowana[i][j] = 1
                generowana[j][i] = 1
    # for i in range(liczba):
    #     print(generowana[i])
    #print(generowana)
    nieparzyste = []
    for i in range(liczba):
        licznik = 0
        for j in range(liczba):
            licznik += generowana[i][j]
        if((licznik%2) != 0):
            nieparzyste.append(i)
    #print(f"nieparzyste: {nieparzyste}")
    for i in range(0,len(nieparzyste),2):
        if(generowana[nieparzyste[i]][nieparzyste[i+1]] == 1):
            generowana[nieparzyste[i]][nieparzyste[i+1]] = 0
            generowana[nieparzyste[i+1]][nieparzyste[i]] = 0
        elif(generowana[nieparzyste[i]][nieparzyste[i+1]] == 0):
            generowana[nieparzyste[i]][nieparzyste[i+1]] = 1
            generowana[nieparzyste[i+1]][nieparzyste[i]] = 1
    return generowana

def zrob_wyspy(graf):
    n = len(graf)
    for i in range(n//2):
        for j in range(n//2, n):
            graf[i][j] = 0
            graf[j][i] = 0
    graf[0][n-1] = 1
    graf[n-1][0] = 1
    graf[n//2-1][n//2] = 1
    graf[n//2][n//2-1] = 1

def czas_wykonania(funkcja, *args):
    start = time.time()
    wynik = funkcja(*args)
    time.sleep(0.2)
    end = time.time()
    return wynik, end - start - 0.2

def bound(graf, cykl):
    #print(f"BOUND {graf},\n {cykl}")
    zredukowany_graf = copy.deepcopy(graf)
    n = len(graf)
    for w in cykl:
        for i in range(n):
            zredukowany_graf[w][i] = 0
            zredukowany_graf[i][w] = 0
    for i in range(n):
        licznik = 0
        for j in range(n):
            if(zredukowany_graf[i][j] > 0):
                licznik += 1
        if((licznik < 2) and (not i in cykl)
                and ((licznik != 1) or ((graf[cykl[-1]][i] == 0) and (graf[i][cykl[0]]==0)))
                and ((len(cykl) < n-1) or (licznik != 0) or (graf[cykl[-1]][i]==0) or (graf[i][cykl[0]] == 0))):
            #print(f"Oh no 1 {i}, {licznik}")
            # print(f"""({licznik} < 2) and (not {i} in {cykl})
            #     and (({licznik} != 1) or (({graf[cykl[-1]][i]} == 0) and ({graf[i][cykl[0]]}==0)))
            #     and (({len(cykl)} < {n}-1) or ({licznik} != 0) or ({graf[cykl[-1]][i]}==0) or ({graf[i][cykl[0]]} == 0))):""")
            return False
    odleglosci = [-1]*n
    zoptymalizowane = [False]*n
    for w in cykl:
        odleglosci[w] = -2
    pierwszy_lepszy = -1
    for i in range(n):
        if(odleglosci[i] == -1):
            pierwszy_lepszy = i
            odleglosci[i] = 0
            break
    for i in range(n):
        najmniejszy = -1
        for j in range(n):
            if((odleglosci[j] >= 0) and (zoptymalizowane[j] == False)):
                if((najmniejszy == -1) or (odleglosci[najmniejszy] > odleglosci[j])):
                    najmniejszy = j
        if(najmniejszy < 0):
            break
        zoptymalizowane[najmniejszy] = True
        for j in range(n):
            if(zredukowany_graf[najmniejszy][j] == 0):
                continue
            if((odleglosci[j] < 0) or (odleglosci[najmniejszy]+1 < odleglosci[j])):
                odleglosci[j] = odleglosci[najmniejszy]+1
    for i in range(n):
        if(odleglosci[i] == -1):
            #print(f"Oh no 2 {odleglosci[i]}, {i}")
            return False
    #print("RETURNUJE TRUE AAAAAA")
    return True

cykle = []

def czy_hamilton(graf, cykl, one_enough):
    print(f"hamilton {one_enough}")
    global cykle
    if(len(cykl) == 1):
        cykle = []
    if(len(cykl) == len(graf)):
        if(graf[cykl[0]][cykl[-1]] > 0):
            cykle.append(cykl.copy())
    else:
        if(bound(graf, cykl)):
        #if(True):
            #print(f"graf: {graf}")
            #print(f"cykl: {cykl}")
            #print(f"one_enough: {one_enough}")
            biezacy = cykl[-1]
            for i in range(len(graf)):
                if(graf[biezacy][i] == 0):
                    continue
                if(not i in cykl):
                    cykl.append(i)
                    czy_hamilton(graf, cykl, one_enough)
                    if(one_enough and len(cykle) > 0):
                        return
                    cykl.pop(-1)

def DFSEuler(graf, v, wynik):
    for u in range(len(graf[v])):
        if graf[v][u] == 1:
            print(f"rozpatruje krawedz {v} {u}")
            graf[v][u] = 0
            graf[u][v] = 0
            graf, wynik = DFSEuler(graf, u, wynik)
            wynik.append(u)
    return graf, wynik


def czy_euler(graf):
    n = len(graf)
    for i in range(n):
        suma_krawędzi_wychodzących = 0
        for j in range(n):
            if graf[i][j] == 1:
                suma_krawędzi_wychodzących += 1
        if suma_krawędzi_wychodzących % 2 != 0:
            return None
    graf, wynik = DFSEuler(graf, 0, [])
    wynik.append(0)
    return graf, wynik

gestosci = [0.2,0.6]

#macierz = [[0, 1, 0, 0, 1],[1, 0, 1, 1, 1],[0, 1, 0, 0, 1,],[0, 1, 0, 0, 1],[1, 1, 1, 1, 0]]

# macierz = generator_macierzy(ilosc, 0.6)
# zrob_wyspy(macierz)
# print("\n".join([str(x) for x in macierz]))
# czas=czas_wykonania(czy_hamilton, macierz, [0], True)
# print(f"alamakota {len(cykle)} {cykle}")
# print(czas)
# print("\n".join([str(x) for x in macierz]))

w = open("wyniki.txt", "w")

ilosc = 7

wynik_ilosc = 'liczba_elementow\t'
wynik_h1 = 'hamilton_1\t'
wynik_ha = 'hamilton_all\t'
wynik_eu = 'euler\t'
wynik_liczba = 'liczba\t'
for gestosc in gestosci:
    #for i in range(10):
    #ilosc += i
    wynik_ilosc += str(ilosc)+'\t'
    macierz = generator_macierzy(ilosc, gestosc)
    # while(czy_euler(macierz) == False):
    #     macierz = generator_macierzy(ilosc,gestosc)
    pusta,czas = czas_wykonania(czy_hamilton,macierz,[0],True)
    wynik_h1 += str(czas)+'\t'
    pusta,czas = czas_wykonania(czy_hamilton,macierz,[0],False)
    wynik_ha += str(czas)+'\t'
    wynik_liczba += str(len(cykle))+'\t'
    pusta,czas = czas_wykonania(czy_euler,macierz)
    wynik_eu += str(czas)+'\t'
w.write(wynik_ilosc+'\n')
w.write(wynik_h1+'\n')
w.write(wynik_ha+'\n')
w.write(wynik_liczba+'\n')
w.write(wynik_eu)
