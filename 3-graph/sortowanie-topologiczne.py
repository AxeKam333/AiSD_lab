

class Etykiety:
    def __init__(self, liczba_wierzcholkow):
        s = []
        f = []
        iterator = 0
        for i in range(liczba_wierzcholkow):
            s.append(0)
            f.append(0)


class Graf_MacierzSasiedztwa:

    def __init__(self):
        self.macierz = []

    def __init__(self, macierz):
        self.macierz = macierz


class Graf_ListaNastepnikow:

    def __init__(self):
        self.lista = []

    def generate(self, maciez_sasiedztwa):
        for wierzcholek_id in range(len(maciez_sasiedztwa)):
            self.lista.append([])
            for łuk_id in range(len(maciez_sasiedztwa[wierzcholek_id])):
                łuk = maciez_sasiedztwa[wierzcholek_id][łuk_id]
                if łuk != 0:
                    self.lista[wierzcholek_id].append(łuk_id)
                    

    def __str__(self) -> str:
        return str(self.lista)

if __name__=="__main__":
    g = Graf_ListaNastepnikow()
    m = Graf_MacierzSasiedztwa([[0, 1, 1, 0, 1, 1],[0, 0, 0, 1, 0, 1],[0, 0, 0, 1, 0, 0],[0, 0, 0, 0, 1, 1]])
    g.generate(m.macierz)
    print(g)