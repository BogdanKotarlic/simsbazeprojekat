from data_models.nastavnik import Nastavnik
from data_models.student import Student
from data_models.predmet import Predmet
from data_manipulation.serial_file_handler import SerialFileHandler
import pickle

studenti = []
studenti.append(Student("2018/270150", "Srdjan", "Horvat", ["2"]))
studenti.append(Student("2017/270075", "Bogdan", "Kotarlic", ["2"]))

predmeti = []
predmeti.append(Predmet("111", "Baze podataka", "SII", ["2"]))
predmeti.append(Predmet("222", "SIMS", "SII", ["2"]))
predmeti.append(Predmet("333", "Programiranje 2", "SII", ["2"]))

nastavnici = []
nastavnici.append(Nastavnik("101", "Pera", "Peric", "Profesor"))
nastavnici.append(Nastavnik("201", "Jovan", "Jovanovic", "Asistent"))

with open("student_data", 'wb') as d:
    pickle.dump(studenti, d)
with open("predmet_data", 'wb') as d:
    pickle.dump(predmeti, d)
with open("nastavnik_data", 'wb') as d:
    pickle.dump(nastavnici, d)

student_file_handler = SerialFileHandler("student_data", "student_metadata.json")
predmet_file_handler = SerialFileHandler("predmet_data", "predmet_metadata.json")
nastavnik_file_handler = SerialFileHandler("nastavnik_data", "nastavnik_metadata.json")

studenti = student_file_handler.get_all()
predmeti = predmet_file_handler.get_all()
nastavnici = nastavnik_file_handler.get_all()