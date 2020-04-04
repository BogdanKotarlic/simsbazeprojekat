#include "Sirovina.h"
#include <iostream>
#include <string>

using namespace std;

Sirovina::Sirovina(string naziv, int kolicina, int cena) {
    this->naziv = naziv;
    this->kolicina = kolicina;
    this->cena = cena;
}

void Sirovina::ispis(){
    cout << "Naziv: " << naziv << " ,kolicina: " << kolicina << " ,cena: " << cena;
}
