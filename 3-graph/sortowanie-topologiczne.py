import random
import time

class Etykiety:
    def __init__(self, liczba_wierzcholkow):
        self.s = []
        self.f = []
        self.iterator = 1
        for i in range(liczba_wierzcholkow):
            self.s.append(False)
            self.f.append(False)

    def __str__(self):
        return "s: " + str(self.s) + " \nf: " + str(self.f)

    def czy_odwiedzony(self, v):
        return self.s[v]
    
    def odwiedz(self, v):
        self.s[v] = self.iterator
        self.iterator += 1

    def opusc(self, v):
        self.f[v] = self.iterator
        self.iterator += 1
    
    def podstaw_pod_wzor(self, u, v):
        s = self.s
        f = self.f
        return s[v] < s[u] and s[u] < f[u] and f[u] < f[v]

class Graf_MacierzSasiedztwa:
    def __init__(self, macierz=[]):
        self.macierz = macierz

    def generuj_losowo(self, liczba_wierzcholkow, gestosc):
        for i in range(liczba_wierzcholkow):
            self.macierz.append([])
            for j in range(liczba_wierzcholkow):
                los = random.randint(0, 100)/100
                if los <= gestosc:
                    self.macierz[i].append(1)
                else:
                    self.macierz[i].append(0)
            self.macierz[i][i] = 0

    def bez_lukow_wchodzacych(self):
        a = len(self.macierz)
        dq = []
        for idx_sasiada in range(a):
            jest_pusty = True
            for idx_wierzcholka in range(a):
                if self.macierz[idx_wierzcholka][idx_sasiada] == 1:
                    jest_pusty = False
                    break
            if jest_pusty:
                dq.append(idx_sasiada)
        return dq
    
    def liczba_lukow_pow(self, etykiety: Etykiety):
        a = len(self.macierz)
        licz = 0
        print(self.macierz)
        for wierzcholek_idx in range(a):
            for sasiad_idx in range(a):
                if self.macierz[wierzcholek_idx][sasiad_idx] == 1 \
                and etykiety.podstaw_pod_wzor(wierzcholek_idx, sasiad_idx):
                    licz += 1
        return licz


class Graf_ListaNastepnikow:

    def __init__(self, lista = []):
        self.lista = lista

    def __str__(self):
        return str(self.lista)
    
    def from_macierzsasiedztwa(self, maciez_sasiedztwa):
        for wierzcholek_id in range(len(maciez_sasiedztwa)):
            self.lista.append([])
            for luk_id in range(len(maciez_sasiedztwa[wierzcholek_id])):
                luk = maciez_sasiedztwa[wierzcholek_id][luk_id]
                if luk != 0:
                    self.lista[wierzcholek_id].append(luk_id)

    # def generate(self, maciez_sasiedztwa):
    #     for wierzcholek_id in range(len(maciez_sasiedztwa)):
    #         self.lista[wierzcholek_id] = (set())
    #         for luk_id in range(len(maciez_sasiedztwa[wierzcholek_id])):
    #             luk = maciez_sasiedztwa[wierzcholek_id][luk_id]
    #             if luk != 0:
    #                 self.lista[wierzcholek_id].add(luk_id)

        return 

    def sasiedzi(self, v):
        return self.lista[v]

    def topological_sort_util(self, v, stos: list):
        e = self.ety
        stos_pomocniczy = [(v, self.sasiedzi(v))]
        e.odwiedz(v)
        while len(stos_pomocniczy) > 0:
            wierzcholek, sasiedzi = stos_pomocniczy[-1]
            ma_nieodwiedzonych_sasiadow = False

            for nastepny_sasiad in sasiedzi:
                if not(e.czy_odwiedzony(nastepny_sasiad)):
                    e.odwiedz(nastepny_sasiad)
                    stos_pomocniczy.append((nastepny_sasiad, self.sasiedzi(nastepny_sasiad)))
                    ma_nieodwiedzonych_sasiadow = True
                    break
            
            if not ma_nieodwiedzonych_sasiadow:
                e.opusc(wierzcholek)
                stos.append(wierzcholek)
                stos_pomocniczy.pop()

    def topological_sort(self,bez_lukow_wchodzacych) -> Etykiety:
        self.ety = Etykiety(len(self.lista))
        stos = []
        for i in bez_lukow_wchodzacych:
            if not(self.ety.czy_odwiedzony(i)):
                self.topological_sort_util(i, stos)

        for i in range(len(self.lista)): #na wypadek cyklu
            if not(self.ety.czy_odwiedzony(i)):
                self.topological_sort_util(i, stos)
        stos.reverse()
        # print("kolejność topologiczna: ", stos)
        return self.ety

    def liczba_lukow_pow(self, etykiety: Etykiety):
        licz = 0
        for wierzcholek_idx in range(len(self.lista)):
            for sasiad in self.lista[wierzcholek_idx]:
                if etykiety.podstaw_pod_wzor(wierzcholek_idx, sasiad):
                    licz += 1
        return licz
            

class Graf_ListaLukow:
    
    def __init__(self,lista = []):
        self.lista = lista
        
    def from_listanastepnikow(self, listanastepnikow): 
        self.lista = []    
        for wierzcholek_idx in range(len(listanastepnikow)):
            for luk in listanastepnikow[wierzcholek_idx]:
                self.lista.append((wierzcholek_idx, luk))

    def liczba_lukow_pow(self, etykiety: Etykiety, lista = []):
        licz = 0

        for i in self.lista:
            if etykiety.podstaw_pod_wzor(i[0],i[1]):
                licz += 1
        return licz

def czas_wykonania(funkcja, *args):
    start = time.time()
    wynik = funkcja(*args)
    time.sleep(0.2)
    end = time.time()
    return wynik, end - start - 0.2

if __name__=="__main__":
    # m = Graf_MacierzSasiedztwa([
    # ])
    # n = Graf_ListaNastepnikow()
    # n.from_macierzsasiedztwa(m.macierz)
    # print(n)
    # etykiety = n.topological_sort(m.bez_lukow_wchodzacych())
    # print(etykiety)
    # l = Graf_ListaLukow(n.lista)
    # l.from_listanastepnikow(n.lista)
    # print(m.liczba_lukow_pow(etykiety))
    # print(n.liczba_lukow_pow(etykiety))
    # print(l.liczba_lukow_pow(etykiety))
    d = [0.2, 0.4]

    for gestosc in d:
        n = 0
        print("Gestosc: " + str(gestosc))
        for i in range(10):
            n+=200
            print("Dla n = " + str(n))

            graf_macierz = Graf_MacierzSasiedztwa()

            czas_gen = czas_wykonania(graf_macierz.generuj_losowo, n, gestosc)[1]
            print("Czas generowania grafu (s): " + str(czas_gen))

            graf_nast = Graf_ListaNastepnikow()
            graf_nast.from_macierzsasiedztwa(graf_macierz.macierz)

            graf_luk = Graf_ListaLukow()
            graf_luk.from_listanastepnikow(graf_nast.lista)

            # czy tutaj też liczyć czas generowania punktów startowych?
            punkty_startowe = graf_macierz.bez_lukow_wchodzacych()
            etykiety, czas_ety = czas_wykonania(graf_nast.topological_sort, punkty_startowe)
            print("Czas zliczania etykiet (s): " + str(czas_ety))

            powroty, czas_pow_nast = czas_wykonania(graf_nast.liczba_lukow_pow, etykiety)
            print("Liczba lukow powrotnych: " + str(powroty))
            print("Czas zliczania lukow powrotnych (lista_nastepnikow): " + str(czas_pow_nast))

            powroty, czas_pow_luk = czas_wykonania(graf_luk.liczba_lukow_pow, etykiety)
            print("Czas zliczania lukow powrotnych (lista_lukow): " + str(czas_pow_luk))

            powroty, czas_pow_mac = czas_wykonania(graf_macierz.liczba_lukow_pow, etykiety)
            print("Czas zliczania lukow powrotnych (macierz sasiedztwa)): " + str(czas_pow_mac))
