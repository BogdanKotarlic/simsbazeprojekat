#include "Aditiv.h"

Aditiv::Aditiv(string naziv, int kolicina, int cena, int sifra) : Sirovina(naziv, kolicina, cena), sifra(sifra) {};

void Aditiv::ispis(){
    Sirovina::ispis();
    cout << " ,sifra: " << sifra << endl;
}

