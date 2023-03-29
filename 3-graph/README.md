cechy grafu:
- liczba wierzchołków
- liczba łuków
    graf pusty nie ma połączeń

ścieżka, droga, cykl, 

reprezentacja maszynowa grafu - implementacja abstrakcji.
- macież sąsiedztwa 
O(n^2)
1
    binarny zapis czy istnieją łuki między wierzchołkami

    wierzchołki: 1,2,3

            1   2   3
        1   0   1   1
        2   0   0   0
        3   1   1   1

    oznacza 2>1,3>1,1>3,2>3,3>3 lub na odwrót w zależności od interpretacji

- lista łuków

    - tablica par (lista łuków) 
    pamiec O(m) *
    wyszukiwanie O(m)

        początek    1   1   3   
        koniec      2   3   3
    
    
    - lista następników O(n+m)
    pamiec O(n+m)
    wyszukiwanie O(m)
        1 >2 >3
        2
        3 > 3
        4
    
    - lista poprzedników O(n+m)

        1 <2
        2 <1 <3
        3 <3
        4

- lista krawędzi: analogicznie, ale 

    macież może być trójkątna
    nie ma rozróżnienia nast/poprz
    pamietać o usuwaniu w dwie srony w tablicy sąsiedztwa

- macież incydencji O(n*m)

    ma tyle kolumn co łuków
    cała kolumna opisuje jeden łuk
    tam gdzie sie zaczyna ma -1, tam gdzie się kończy 1
    nie nadaje się do klasycznych grafów, jedynie do hipergrafów

złożoność w kategoriach:

    pamięciowa
    test łuków (czy jest czy nie ma)
    zbiór następników
    zbiór poprzedników
    zbiór łuku (wypisz wszystkie)

- macież sąsiedztwa 

        n^2
        1
        n
        n
        n^2
- tablica par (lista łuków) 

        m
        m
        m
        m
        n *
- lista następników O(n+m)

        n+m
        n
        n (liczba następników)
        n+m
        n+m
- lista poprzedników O(n+m)

        n+m
        n
        n+m
        n *
        n+m
- macież incydencji

        n*m
        n
        n*m
        n*m
        n*m

metody

przegolądanie grafu:
- wgłąb(DFS, depth first search)
    
    być może zacząć od najmniejszego wartością wierzchołku

    idz do pierwszego nieodwiedzonego sąsiada, jego numer połuż na stosie
    
    najlepiej wybrać 