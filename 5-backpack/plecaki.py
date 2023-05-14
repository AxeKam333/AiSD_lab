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
        tablica.append({'size':0, 'value':0, 'criteria':0, 'ratio':0, 'juz_uzyty':False})
        tablica[i]['size'] = random.randint(10,1000)
        tablica[i]['value'] = random.randint(100,10000)
        suma += tablica[i]['size']
    return tablica, suma

def plecak_pojedyncze(x, rzeczy):
    liczbaPrzedmiotow = len(rzeczy)
    rozwiazania = [[0] * (liczbaPrzedmiotow + 1) for i in range(x + 1)]
    for nrPrzedmiot in range(x):
        for rozmiar in range(x + 1):
            if (rzeczy[nrPrzedmiot]['size'] <= x):
                if (rozwiazania[nrPrzedmiot][x - rzeczy[nrPrzedmiot]['size']] +
                        rzeczy[nrPrzedmiot]['value'] > rozwiazania[nrPrzedmiot][x]):
                    rozwiazania[nrPrzedmiot + 1][x] = rozwiazania[nrPrzedmiot][
                                                                x - rzeczy[nrPrzedmiot]['value']] + \
                                                            rzeczy[nrPrzedmiot]['value']
                else:
                    rozwiazania[nrPrzedmiot + 1][x] = rozwiazania[nrPrzedmiot][x]
            else:
                rozwiazania[nrPrzedmiot + 1][x] = rozwiazania[nrPrzedmiot][x]
        print(rozwiazania)
    print(rozwiazania[liczbaPrzedmiotow][pojemnoscPlecaka])

def heurystyka(rzeczy, pojemnosc, rodzaj):
    wynik = 0
    if(rodzaj == 'size'):
        print('size')
    elif(rodzaj == 'value'):
        print('value')
    elif(rodzaj == 'ratio'):
        print('ratio')
        for i in range(len(rzeczy)):
            rzeczy[i]['ratio'] = rzeczy[i]['value']/rzeczy[i]['size']
    elif(rodzaj=='random'):
        print('random')

liczba_przedmiotow = 5
przedmioty = []
pojemnoscPlecaka = None
najlepsze_rozwiazanie = 0

for i in range(10):
    liczba_przedmiotow += i
    przedmioty, pojemnoscPlecaka = crafting(liczba_przedmiotow, przedmioty)

