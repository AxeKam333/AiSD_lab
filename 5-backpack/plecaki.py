import random
import time
import copy

def czas_wykonania(funkcja, *args):
    start = time.time()
    wynik = funkcja(*args)
    time.sleep(0.2)
    end = time.time()
    return wynik, end - start - 0.2

def crafting(x, tablica):
    tablica = []
    suma = 0
    for i in range(x):
        tablica.append({'size':0, 'value':0, 'ratio':0, 'juz_uzyty':False, 'number':i})
        tablica[i]['size'] = random.randint(10,1000)
        tablica[i]['value'] = random.randint(100,10000)
        tablica[i]['ratio'] = tablica[i]['value']/tablica[i]['size']
        suma += tablica[i]['size']
        #print(f"suma: {suma}")
    return tablica, suma

def plecak_pojedyncze(pojemnosc, rzeczy):
    #print(pojemnosc, len(rzeczy))
    #print(rzeczy)
    #sys.exit(-1)
    rozwiazania = [[0] * (pojemnosc + 1) for i in range(len(rzeczy) + 1)]
    for nrPrzedmiot in range(len(rzeczy)):
        for rozmiar in range(pojemnosc + 1):
            if ((rozmiar >= rzeczy[nrPrzedmiot]['size'])
                and (rozwiazania[nrPrzedmiot][rozmiar - rzeczy[nrPrzedmiot]['size']] + rzeczy[nrPrzedmiot]['value'] > rozwiazania[nrPrzedmiot][rozmiar])):
                rozwiazania[nrPrzedmiot + 1][rozmiar] = rozwiazania[nrPrzedmiot][rozmiar - rzeczy[nrPrzedmiot]['size']] + rzeczy[nrPrzedmiot]['value']
            else:
                rozwiazania[nrPrzedmiot + 1][rozmiar] = rozwiazania[nrPrzedmiot][rozmiar]
        #print(rozwiazania)
    # kombinacja=0
    # rozmiar = pojemnoscPlecaka
    # nrPrzedmiot = len(rzeczy) - 1
    # while (nrPrzedmiot >= 0):
    #     if (rozwiazania[nrPrzedmiot + 1][rozmiar] != rozwiazania[nrPrzedmiot][rozmiar]):
    #         kombinacja+=2**nrPrzedmiot
    #         rozmiar -= przedmioty[nrPrzedmiot]['size']
    #     nrPrzedmiot -= 1
    # return rozwiazania[len(rzeczy)][pojemnoscPlecaka], kombinacja, len(rzeczy)*pojemnosc
    #print(len(rozwiazania))
    #print(len(rzeczy)+1)
    #print(len(rozwiazania[0]))
    #print(f"pojemnosc: {pojemnosc+1}")
    #print(rozwiazania[len(rzeczy)][pojemnosc])
    return rozwiazania[len(rzeczy)][pojemnosc], len(rzeczy)*pojemnosc

def podzial(dq, p, r, pivot, kryterium):
    dq[r],dq[pivot]=dq[pivot],dq[r]
    piwot = dq[r]
    #print(f"podzial po {piwot} ({dq})")
    i = p
    j = r
    while True:
        while ((dq[i][kryterium] <= piwot[kryterium]) and (i<j)):
            i += 1
        #print(f"dq[j-1] {dq[j-1]}")
        while((dq[j-1][kryterium] > piwot[kryterium]) and (j>i+1)):
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

def quick_skrajny(dq, p, r, kryterium):
    #print(f"skrajny {len(dq)}, {p}, {r}")
    if (p < r):
        q = podzial(dq, p, r, r, kryterium)
        #print(f"zwrocilo {q} na tablicy {dq}")
        quick_skrajny(dq, p, q-1, kryterium)
        quick_skrajny(dq, q+1, r, kryterium)
        #print(dq)
    return dq

def heurystyka(rzeczy, pojemnosc, rodzaj):
    suma_pojemnosci = 0
    suma_wartosci = 0
    kombinacja = 0
    if(rodzaj != 'random'):
        quick_skrajny(rzeczy, 0, len(rzeczy)-1, rodzaj)
        #print(rodzaj, rzeczy)
    if(rodzaj == 'size'):
        i = 0
    else:
        i = len(rzeczy)-1
    while(suma_pojemnosci+rzeczy[i]['size'] < pojemnosc):
        kombinacja += 2**rzeczy[i]['number']
        suma_pojemnosci += rzeczy[i]['size']
        suma_wartosci += rzeczy[i]['value']
        if(rodzaj == 'size'):
            i += 1
        else:
            i -= 1
    return suma_wartosci,kombinacja

#tak zwana kombinacja to przechowywany int w postaci binarnej, który oznacza dla każdego przedmiotu przez 0, że nie został wzięty i przez 1, że został wzięty
def suma_kombinacji(kombinacja,rzeczy,pojemnosc):
    suma_pojemnosci = 0
    suma_wartosci = 0
    for j in range(len(rzeczy)):
        if ((kombinacja & 2 ** j) > 0):
            #print(f"  element {j}")
            suma_pojemnosci += rzeczy[j]['size']
            suma_wartosci += rzeczy[j]['value']
            if (suma_pojemnosci > pojemnosc):
                break
    return suma_pojemnosci, suma_wartosci

liczba = 0
najlepsze = 0
najlepsze_kombinacja = 0

def pelny_przeglad_noneliminacja(rzeczy, pojemnosc):
    global liczba
    global najlepsze
    global najlepsze_kombinacja
    liczba = 0
    najlepsze = 0
    najlepsze_kombinacja = 0
    for i in range(1,2**len(rzeczy)):
        #print(f"kombinacja {i}")
        suma_pojemnosci, suma_wartosci=suma_kombinacji(i,rzeczy,pojemnosc)
        #print(f"suma {suma_pojemnosci}")
        liczba += 1
        if(suma_pojemnosci <= pojemnosc):
            if(suma_wartosci > najlepsze):
                najlepsze = suma_wartosci
                najlepsze_kombinacja = i
    return najlepsze, najlepsze_kombinacja, liczba

def pelny_przeglad_eliminacja(rzeczy, poziom, kombinacja, pojemnosc, cut):
    global liczba
    global najlepsze
    global najlepsze_kombinacja
    if(poziom == 0):
        liczba = 0
        najlepsze = 0
        najlepsze_kombinacja = 0
    elif((kombinacja > 0) and ((cut) or (poziom == len(rzeczy)))):
        suma_pojemnosci, suma_wartosci = suma_kombinacji(kombinacja, rzeczy, pojemnosc)
        if(suma_pojemnosci <= pojemnosc):
            if(suma_wartosci > najlepsze):
                najlepsze = suma_wartosci
                najlepsze_kombinacja = kombinacja
        elif(cut):
            return
    if (poziom < len(rzeczy)):
        pelny_przeglad_eliminacja(rzeczy, poziom+1, kombinacja, pojemnosc, cut)
        pelny_przeglad_eliminacja(rzeczy, poziom+1, kombinacja+2**poziom, pojemnosc, cut)
    else:
        liczba += 1

w = open("wyniki.txt", "w")

wynik_ilosc = 'ilosc:\t'
wynik_czas_pelny_noneliminacja_05 = 'czas_BF1:\t'
wynik_czas_pelny_noneliminacja_025 = 'czas_BF1:\t'
wynik_czas_pelny_noneliminacja_075 = 'czas_BF1:\t'
wynik_czas_pelny_eliminacja_05 = 'czas_BF2:\t'
wynik_czas_pelny_eliminacja_025 = 'czas_BF2:\t'
wynik_czas_pelny_eliminacja_075 = 'czas_BF2:\t'
wynik_czas_heurystyka_ratio_05 = 'czas_GH4:\t'
wynik_czas_heurystyka_ratio_025 = 'czas_GH4:\t'
wynik_czas_heurystyka_ratio_075 = 'czas_GH4:\t'
wynik_czas_dynamiczne_05 = 'czas_PD:\t'
wynik_czas_dynamiczne_025 = 'czas_PD:\t'
wynik_czas_dynamiczne_075 = 'czas_PD:\t'
rozwiazanie_PD_05 = 'rozwiazanie_PD:\t'
rozwiazanie_PD_025 = 'rozwiazanie_PD:\t'
rozwiazanie_PD_075 = 'rozwiazanie_PD:\t'
rozwiazanie_GH1_05 = 'rozwiazanie_GH1:\t'
rozwiazanie_GH1_025 = 'rozwiazanie_GH1:\t'
rozwiazanie_GH1_075 = 'rozwiazanie_GH1:\t'
rozwiazanie_GH2_05 = 'rozwiazanie_GH2:\t'
rozwiazanie_GH2_025 = 'rozwiazanie_GH2:\t'
rozwiazanie_GH2_075 = 'rozwiazanie_GH2:\t'
rozwiazanie_GH3_05 = 'rozwiazanie_GH3:\t'
rozwiazanie_GH3_025 = 'rozwiazanie_GH3:\t'
rozwiazanie_GH3_075 = 'rozwiazanie_GH3:\t'
rozwiazanie_GH4_05 = 'rozwiazanie_GH4:\t'
rozwiazanie_GH4_025 = 'rozwiazanie_GH4:\t'
rozwiazanie_GH4_075 = 'rozwiazanie_GH4:\t'
blad_GH1_05 = 'blad_GH1:\t'
blad_GH1_025 = 'blad_GH1:\t'
blad_GH1_075 = 'blad_GH1:\t'
blad_GH2_05 = 'blad_GH2:\t'
blad_GH2_025 = 'blad_GH2:\t'
blad_GH2_075 = 'blad_GH2:\t'
blad_GH3_05 = 'blad_GH3:\t'
blad_GH3_025 = 'blad_GH3:\t'
blad_GH3_075 = 'blad_GH3:\t'
blad_GH4_05 = 'blad_GH4:\t'
blad_GH4_025 = 'blad_GH4:\t'
blad_GH4_075 = 'blad_GH4:\t'

liczba_przedmiotow = 15
przedmioty = []
pojemnoscPlecaka = 0
najlepsze_rozwiazanie = 0

for i in range(10):
    print(i)
    liczba_przedmiotow += 1
    wynik_ilosc += str(liczba_przedmiotow)+'\t'
    przedmioty, pojemnoscPlecaka = crafting(liczba_przedmiotow, przedmioty)
    #zadanie 2
    uzytkowa = int(pojemnoscPlecaka/2)
    pusta, czas = czas_wykonania(plecak_pojedyncze,uzytkowa, przedmioty)
    wynik_czas_dynamiczne_05 += str(czas)+'\t'
    pusta, czas = czas_wykonania(pelny_przeglad_eliminacja,przedmioty, 0, 0, uzytkowa, False)
    wynik_czas_pelny_noneliminacja_05 += str(czas)+'\t'
    pusta, czas = czas_wykonania(pelny_przeglad_eliminacja,przedmioty, 0, 0, uzytkowa, True)
    wynik_czas_pelny_eliminacja_05 += str(czas)+'\t'
    pusta, czas = czas_wykonania(heurystyka,przedmioty, uzytkowa, 'ratio')
    wynik_czas_heurystyka_ratio_05 += str(czas)+'\t'
    #zadanie 3
    #b=0.25
    uzytkowa = int(pojemnoscPlecaka *0.25)
    pusta, czas = czas_wykonania(plecak_pojedyncze,uzytkowa, przedmioty)
    wynik_czas_dynamiczne_025 += str(czas) + '\t'
    pusta, czas = czas_wykonania(pelny_przeglad_eliminacja,przedmioty, 0, 0, uzytkowa, False)
    wynik_czas_pelny_noneliminacja_025 += str(czas) + '\t'
    pusta, czas = czas_wykonania(pelny_przeglad_eliminacja,przedmioty, 0, 0, uzytkowa, True)
    wynik_czas_pelny_eliminacja_025 += str(czas) + '\t'
    pusta, czas = czas_wykonania(heurystyka,przedmioty, uzytkowa, 'ratio')
    wynik_czas_heurystyka_ratio_025 += str(czas) + '\t'
    #b=0.75
    uzytkowa = int(pojemnoscPlecaka * 0.75)
    pusta, czas = czas_wykonania(plecak_pojedyncze,uzytkowa, przedmioty)
    wynik_czas_dynamiczne_075 += str(czas) + '\t'
    pusta, czas = czas_wykonania(pelny_przeglad_eliminacja,przedmioty, 0, 0, uzytkowa, False)
    wynik_czas_pelny_noneliminacja_075 += str(czas) + '\t'
    pusta, czas = czas_wykonania(pelny_przeglad_eliminacja,przedmioty, 0, 0, uzytkowa, True)
    wynik_czas_pelny_eliminacja_075 += str(czas) + '\t'
    pusta, czas = czas_wykonania(heurystyka,przedmioty, uzytkowa, 'ratio')
    wynik_czas_heurystyka_ratio_075 += str(czas) + '\t'
    #zadanie 4
    #b=0.25
    uzytkowa = int(pojemnoscPlecaka*0.25)
    wynik_dokladny, liczba = plecak_pojedyncze(uzytkowa, przedmioty)
    rozwiazanie_PD_025 += str(wynik_dokladny)+'\t'
    wynik, kombinacja = heurystyka(przedmioty, uzytkowa, 'random')
    rozwiazanie_GH1_025 += str(wynik)+'\t'
    blad_GH1_025 += str(((wynik_dokladny-wynik)/wynik_dokladny)*100)+'\t'
    wynik, kombinacja = heurystyka(przedmioty, uzytkowa, 'size')
    rozwiazanie_GH2_025 += str(wynik) + '\t'
    blad_GH2_025 += str(((wynik_dokladny - wynik) / wynik_dokladny) * 100)+'\t'
    wynik, kombinacja = heurystyka(przedmioty, uzytkowa, 'value')
    rozwiazanie_GH3_025 += str(wynik) + '\t'
    blad_GH3_025 += str(((wynik_dokladny - wynik) / wynik_dokladny) * 100) + '\t'
    wynik, kombinacja = heurystyka(przedmioty, uzytkowa, 'ratio')
    rozwiazanie_GH4_025 += str(wynik) + '\t'
    blad_GH4_025 += str(((wynik_dokladny - wynik) / wynik_dokladny) * 100) + '\t'
    # b=0.5
    uzytkowa = int(pojemnoscPlecaka * 0.5)
    wynik_dokladny, liczba = plecak_pojedyncze(uzytkowa, przedmioty)
    rozwiazanie_PD_05 += str(wynik_dokladny) + '\t'
    wynik, kombinacja = heurystyka(przedmioty, uzytkowa, 'random')
    rozwiazanie_GH1_05 += str(wynik) + '\t'
    blad_GH1_05 += str(((wynik_dokladny - wynik) / wynik_dokladny) * 100) + '\t'
    wynik, kombinacja = heurystyka(przedmioty, uzytkowa, 'size')
    rozwiazanie_GH2_05 += str(wynik) + '\t'
    blad_GH2_05 += str(((wynik_dokladny - wynik) / wynik_dokladny) * 100) + '\t'
    wynik, kombinacja = heurystyka(przedmioty, uzytkowa, 'value')
    rozwiazanie_GH3_05 += str(wynik) + '\t'
    blad_GH3_05 += str(((wynik_dokladny - wynik) / wynik_dokladny) * 100) + '\t'
    wynik, kombinacja = heurystyka(przedmioty, uzytkowa, 'ratio')
    rozwiazanie_GH4_05 += str(wynik) + '\t'
    blad_GH4_05 += str(((wynik_dokladny - wynik) / wynik_dokladny) * 100) + '\t'
    # b=0.75
    uzytkowa = int(pojemnoscPlecaka * 0.75)
    wynik_dokladny, liczba = plecak_pojedyncze(uzytkowa, przedmioty)
    rozwiazanie_PD_075 += str(wynik_dokladny) + '\t'
    wynik, kombinacja = heurystyka(przedmioty, uzytkowa, 'random')
    rozwiazanie_GH1_075 += str(wynik) + '\t'
    blad_GH1_075 += str(((wynik_dokladny - wynik) / wynik_dokladny) * 100) + '\t'
    wynik, kombinacja = heurystyka(przedmioty, uzytkowa, 'size')
    rozwiazanie_GH2_075 += str(wynik) + '\t'
    blad_GH2_075 += str(((wynik_dokladny - wynik) / wynik_dokladny) * 100) + '\t'
    wynik, kombinacja = heurystyka(przedmioty, uzytkowa, 'value')
    rozwiazanie_GH3_075 += str(wynik) + '\t'
    blad_GH3_075 += str(((wynik_dokladny - wynik) / wynik_dokladny) * 100) + '\t'
    wynik, kombinacja = heurystyka(przedmioty, uzytkowa, 'ratio')
    rozwiazanie_GH4_075 += str(wynik) + '\t'
    blad_GH4_075 += str(((wynik_dokladny - wynik) / wynik_dokladny) * 100) + '\t'
w.write(wynik_ilosc+'\n')
w.write("b = 0,5"+'\n')
w.write(wynik_czas_dynamiczne_05+'\n')
w.write(wynik_czas_pelny_noneliminacja_05+'\n')
w.write(wynik_czas_pelny_eliminacja_05+'\n')
w.write(wynik_czas_heurystyka_ratio_05+'\n')
w.write("b = 0,25"+'\n')
w.write(wynik_czas_dynamiczne_025+'\n')
w.write(wynik_czas_pelny_noneliminacja_025+'\n')
w.write(wynik_czas_pelny_eliminacja_025+'\n')
w.write(wynik_czas_heurystyka_ratio_025+'\n')
w.write("b = 0,75"+'\n')
w.write(wynik_czas_dynamiczne_075+'\n')
w.write(wynik_czas_pelny_noneliminacja_075+'\n')
w.write(wynik_czas_pelny_eliminacja_075+'\n')
w.write(wynik_czas_heurystyka_ratio_075+'\n')
w.write("b = 0,25"+'\n')
w.write(rozwiazanie_PD_025+'\n')
w.write(rozwiazanie_GH1_025+'\n')
w.write(rozwiazanie_GH2_025+'\n')
w.write(rozwiazanie_GH3_025+'\n')
w.write(rozwiazanie_GH4_025+'\n')
w.write("b = 0,5"+'\n')
w.write(rozwiazanie_PD_05+'\n')
w.write(rozwiazanie_GH1_05+'\n')
w.write(rozwiazanie_GH2_05+'\n')
w.write(rozwiazanie_GH3_05+'\n')
w.write(rozwiazanie_GH4_05+'\n')
w.write("b = 0,75"+'\n')
w.write(rozwiazanie_PD_075+'\n')
w.write(rozwiazanie_GH1_075+'\n')
w.write(rozwiazanie_GH2_075+'\n')
w.write(rozwiazanie_GH3_075+'\n')
w.write(rozwiazanie_GH4_075+'\n')
w.write("b = 0,25"+'\n')
w.write(blad_GH1_025+'\n')
w.write(blad_GH2_025+'\n')
w.write(blad_GH3_025+'\n')
w.write(blad_GH4_025+'\n')
w.write("b = 0,5"+'\n')
w.write(blad_GH1_05+'\n')
w.write(blad_GH2_05+'\n')
w.write(blad_GH3_05+'\n')
w.write(blad_GH4_05+'\n')
w.write("b = 0,75"+'\n')
w.write(blad_GH1_075+'\n')
w.write(blad_GH2_075+'\n')
w.write(blad_GH3_075+'\n')
w.write(blad_GH4_075+'\n')

