#include <iostream>

using namespace std;

int blank() {
    clock_t start = clock();

    clock_t end = clock();
    double elapsed = double(end - start)/CLOCKS_PER_SEC;
    return elapsed;
}

int* losowa(int size){  //dodac losowanie liczb
    int* dq = new int[size];
    return dq;
}

int main() {
    double T[10][7]; //T[numer próby][metoda sortowania]
    for(int i=0;i<10;i++) {
        int* dq = losowa(100*(i+1));
        // T[i][1] = 0;
    }
}

// SS (przez proste wybieranie), 
//     IS (przez proste wstawianie), 
//     BS (bąbelkowe), 
    
//     HS (stogowe/kopcowe), 
//     MS (przez scalanie), 
//     QS (szybkie z podziałem:
//         QS1 wg skrajnego 
//         QS2 i środkowego elementu tablicy),
//     CS (przez zliczanie)