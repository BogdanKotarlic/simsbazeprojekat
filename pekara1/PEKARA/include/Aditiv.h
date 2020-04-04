#ifndef ADITIV_H
#define ADITIV_H
#include "Sirovina.h"

class Aditiv : public Sirovina
{
    public:
        Aditiv(string, int, int, int);
        void setSifra(int){};
        int getSifra(){return sifra;}
        void ispis();

    protected:
        int sifra;
};

#endif // ADITIV_H
