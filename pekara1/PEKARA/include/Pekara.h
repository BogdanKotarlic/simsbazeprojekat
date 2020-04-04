#ifndef PEKARA_H
#define PEKARA_H
#include <iostream>
#include <string>
#include <vector>
#include "Sirovina.h"

class Pekara
{
    public:
        Pekara(){};
        void dodajSirovinu(Sirovina *sirovina){
            sirovine.push_back(sirovina);
        };
        void prikaziSirovine(){
            for(Sirovina* i : sirovine){
                i->ispis();
            }
        };

    protected:
        vector<Sirovina*> sirovine;
};

#endif // PEKARA_H
