#ifndef SIROVINA_H
#define SIROVINA_H
#include <iostream>
#include <string>

using namespace std;

class Sirovina
{
    public:
        Sirovina(string, int, int);
        virtual void setKolicina(int){};
        virtual int getKolicina(){return kolicina;};
        virtual void setNaziv(string){};
        virtual string getNaziv(){return naziv;};
        virtual void setCena(int){};
        virtual int getCena(){return cena;};

        virtual void ispis()=0;

    protected:
        string naziv;
        int kolicina;
        int cena;
};

#endif // SIROVINA_H
