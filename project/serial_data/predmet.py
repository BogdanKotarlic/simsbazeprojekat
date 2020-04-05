class Predmet():
    def __init__(self, sifra_predmeta, naziv, smer, nastavnici=[]):
        super().__init__()
        self.sifra_predmeta = sifra_predmeta
        self.naziv = naziv
        self.smer = smer
        self.nastavnici = nastavnici