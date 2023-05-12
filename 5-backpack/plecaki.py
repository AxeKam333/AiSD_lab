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
    return tablica, suma

def heurystyki(rzeczy, pojemnosc)

liczba_przedmiotow = 5
przedmioty = []
pojemnoscPlecaka = None
najlepsze_rozwiazanie = 0
kryteria=[
    {'nazwa':'random','aktywne':True},
    {'nazwa':'size','aktywne':True},
    {'nazwa':'value','aktywne':True},
    {'nazwa':'ratio','aktywne':True}]
pojemnosci=[
    {'wartosc':0.25,'aktywne':True},
    {'wartosc':0.5,'aktywne':True},
    {'wartosc':0,75,'aktywne':True}
]

for i in range(10):
    liczba_przedmiotow += i
    przedmioty, pojemnoscPlecaka = crafting(liczba_przedmiotow, przedmioty)
    for pojemnosc in pojemnosci:
        if(pojemnosc['aktywne']):
            pojemnosc_robocza = pojemnoscPlecaka*pojemnosc['wartosc']
