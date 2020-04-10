class Student():
    def __init__(self, indeks, ime, prezime, predmeti = []):
        super().__init__()
        self.indeks = indeks
        self.ime = ime
        self.prezime = prezime
        self.predmeti = predmeti