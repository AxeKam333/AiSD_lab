#whyyyyyy m c a

import random
import time
import copy

def generator_macierzy(liczba, gestosc):
    generowana = [[0]*liczba for x in range(liczba)]
    y = gestosc
    licznik = 0
    for i in range(liczba):
        #generowana[i] = [0]*liczba
        for j in range(liczba):
            if(i!=j and generowana[i][j] == 0):
                losowo = random.randint(0, 100)/100
                if(losowo <= y):
                    generowana[i][j] = int(1.0)
                    generowana[j][i] = 1
                    licznik += 1
    # for i in range(liczba):
    #     for j in range(liczba):
    #         if(generowana[i][j] == 1):
    #             generowana[j][i] = 1
    print(licznik)
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
    global cykle
    if(len(cykl) == 1):
        cykle = []
    if(len(cykl) == len(graf)):
        if(graf[cykl[0]][cykl[-1]] > 0):
            cykle.append(cykl.copy())
    else:
        if(bound(graf, cykl)):
        #if(True):
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

ilosc = 14
gestosci = [0.2,0.6]

#macierz = [[0, 1, 0, 1, 0],[1, 0, 1, 1, 1],[0, 1, 0, 0, 1,],[1, 1, 0, 0, 1],[0, 1, 1, 1, 0]]

macierz = generator_macierzy(ilosc, 1)
zrob_wyspy(macierz)
print("\n".join([str(x) for x in macierz]))
czas=czas_wykonania(czy_hamilton, macierz, [0], False)
print(f"alamakota {len(cykle)} {cykle}")
print(czas)

for gestosc in gestosci:
    macierz = generator_macierzy(ilosc, gestosc)
    # for i in range(ilosc):
    #     print(macierz[i])
    uzytkowa = macierz.copy()
