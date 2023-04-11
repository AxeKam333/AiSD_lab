

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
    
    def czy_cykliczny(self, etykiety: Etykiety):
        a = len(self.macierz)
        for wierzcholek_idx in range(a):
            for sasiad_idx in range(a):
                if self.macierz[wierzcholek_idx][sasiad_idx] == 1 \
                and etykiety.podstaw_pod_wzor(wierzcholek_idx, sasiad_idx):
                    return True
        return False


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
        print("kolejność topologiczna: ", stos)
        return self.ety

    def czy_cykliczny(self, etykiety: Etykiety):
        for wierzcholek_idx in range(len(self.lista)):
            for sasiad in self.lista[wierzcholek_idx]:
                if etykiety.podstaw_pod_wzor(wierzcholek_idx, sasiad):
                    return True
        return False
            

class Graf_ListaLukow:
    
    def __init__(self,lista = []):
        self.lista = lista
        
    def from_listanastepnikow(self, listanastepnikow): 
        self.lista = []    
        for wierzcholek_idx in range(len(listanastepnikow)):
            for luk in listanastepnikow[wierzcholek_idx]:
                self.lista.append((wierzcholek_idx, luk))
        print(self.lista)

    def czy_cykliczny(self, etykiety: Etykiety, lista = []):
        if lista != []:
            self.__init__(lista)

        for i in self.lista:
            if etykiety.podstaw_pod_wzor(i[0],i[1]):
                return True
        return False



if __name__=="__main__":
    
    m = Graf_MacierzSasiedztwa([
    [0, 1, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ])
    n = Graf_ListaNastepnikow()
    n.from_macierzsasiedztwa(m.macierz)
    print(n)
    etykiety = n.topological_sort(m.bez_lukow_wchodzacych())
    print(etykiety)
    l = Graf_ListaLukow(n.lista)
    l.from_listanastepnikow(n.lista)
    print(m.czy_cykliczny(etykiety))
    print(n.czy_cykliczny(etykiety))
    print(l.czy_cykliczny(etykiety))
