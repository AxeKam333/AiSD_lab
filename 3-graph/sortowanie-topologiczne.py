

class Graf_ListaNastepnikow:

    def __init__(self):
        self.lista = []

    def generate(self):
        self.lista = [[1],[2],[0],[0]]

    def __str__(self) -> str:
        return str(self.lista)

if __name__=="__main__":
    g = Graf_ListaNastepnikow()
    g.generate()
    print(g)