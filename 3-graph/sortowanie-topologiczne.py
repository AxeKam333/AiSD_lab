

class Etykiety:
    def __init__(self, liczba_wierzcholkow):
        self.s = []
        self.f = []
        self.iterator = 0
        for i in range(liczba_wierzcholkow):
            self.s.append(0)
            self.f.append(0)


class Graf_MacierzSasiedztwa:

    def __init__(self):
        self.macierz = []

    def __init__(self, macierz):
        self.macierz = macierz

    def bez_łuków_wchodzacych(self):
        a = len(self.macierz)
        lista = []
        for idx_sasiada in range(a):
            jest_pusty = True
            for idx_wierzchołka in range(a):
                if self.macierz[idx_wierzchołka][idx_sasiada] == 1:
                    jest_pusty = False
                    break
            if jest_pusty:
                lista.append(idx_sasiada)
        print(lista)


class Graf_ListaNastepnikow:

    def __init__(self):
        self.lista = []

    def __str__(self):
        return str(self.lista)
    
    def generate(self, maciez_sasiedztwa):
        for wierzcholek_id in range(len(maciez_sasiedztwa)):
            self.lista.append([])
            for łuk_id in range(len(maciez_sasiedztwa[wierzcholek_id])):
                łuk = maciez_sasiedztwa[wierzcholek_id][łuk_id]
                if łuk != 0:
                    self.lista[wierzcholek_id].append(łuk_id)

    def topological_sort(self):
        etykiety = Etykiety(len(self.lista))

        return etykiety



if __name__=="__main__":
    g = Graf_ListaNastepnikow()
    m = Graf_MacierzSasiedztwa([[0, 1, 1, 0, 1, 1],[0, 0, 0, 1, 0, 1],[0, 0, 0, 1, 0, 0],[0, 0, 0, 0, 1, 1],[0,0,0,0,0,0],[0,0,0,0,1,0]])
    g.generate(m.macierz)
    m.bez_łuków_wchodzacych()
    print(g)