#include <iostream>
#include <vector>
#include "Sirovina.h"
#include "Pekara.h"
#include "Brasno.h"
#include "Aditiv.h"
using namespace std;
using namespace std;

int main()
{
    Sirovina *prva = new Brasno("Brasno1", 10, 100, "Tip500");
    Sirovina *druga = new Brasno("Brasno2", 20, 150, "Tip400");
    Sirovina *treca = new Aditiv("Aditiv1", 30, 200, 12345);

    Pekara pekara;
    pekara.dodajSirovinu(prva);
    pekara.dodajSirovinu(druga);
    pekara.dodajSirovinu(treca);
    pekara.prikaziSirovine();
}
