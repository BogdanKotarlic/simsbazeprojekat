#ifndef BRASNO_H
#define BRASNO_H
#include "Sirovina.h"
#include <string>
using namespace std;

class Brasno : public Sirovina
{
    public:
        Brasno(string, int, int, string);
        void setTip(string){};
        string getTip(){return tip;}
        void ispis();

    protected:
        string tip;
};

#endif // BRASNO_H
