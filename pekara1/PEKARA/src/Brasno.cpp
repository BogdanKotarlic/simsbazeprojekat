#include "Brasno.h"

Brasno::Brasno(string naziv, int kolicina, int cena, string tip) : Sirovina(naziv, kolicina, cena), tip(tip){};

void Brasno::ispis(){
    Sirovina::ispis();
    cout << " , tip: " << tip << endl;
}
