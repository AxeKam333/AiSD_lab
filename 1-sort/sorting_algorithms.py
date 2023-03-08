// SS (przez proste wybieranie), 
//     IS (przez proste wstawianie), 
//     BS (bąbelkowe), 
    
//     HS (stogowe/kopcowe), 
//     MS (przez scalanie), 
//     QS (szybkie z podziałem:
//         QS1 wg skrajnego 
//         QS2 i środkowego elementu tablicy),
//     CS (przez zliczanie)

import random
import time

tablica = [None]*500
dlugosc = 500

for i in range(10):
    tablica += [None]*500
    dlugosc += 500
    for j in range(len(tablica)):
        tablica[j] = random.randint(0,dlugosc)
    
    
    
