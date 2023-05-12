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
        tablica.append({'size':0, 'value':0, 'criteria':0, 'juz_uzyty':False})
        tablica[i]['size'] = random.randint(10,1000)
        tablica[i]['value'] = random.randint(100,10000)
        suma += tablica[i]['size']
    return tablica

liczba_przedmiotow = 5
przedmioty = []
pojemnoscPlecaka = None

for i in range(10):
    liczba_przedmiotow += i
    przedmioty = crafting(liczba_przedmiotow, przedmioty)
