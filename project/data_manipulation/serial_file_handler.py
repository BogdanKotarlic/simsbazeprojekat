from data_manipulation.data_handler import DataHandler
import json
import pickle #koristimo pickle za serijalizaciju i deserijalizaciju objekata

class SerialFileHandler(DataHandler):
    def __init__(self, filepath, meta_filepath):
        super().__init__()
        self.filepath = filepath
        self.meta_filepath = meta_filepath
        self.data = []
        self.metadata = []
        self.load_data()

    def load_data(self):
        #ucitavanje Podataka
        with open((self.filepath), 'rb') as dfile:
            self.data = pickle.load(dfile) #koristimo pickle za deserijalizaciju podataka

        #ucitavanje Meta Podataka
        with open(self.meta_filepath) as meta_file:
            self.metadata = json.load(meta_file)

    def get_one(self, id):
        for d in self.data: #za serijsku datoteku moramo proci linearno kroz sve slogove kada trazimo
            if getattr(d, (self.metadata["key"])) == id: #ako se poklopi kljucna kolona, koju dobavlja
                return d
        return None

    def get_all(self):
        return self.data()

    def insert(self, obj):
        self.data.append(obj)
        with open(self.filepath, 'wb') as f:
            pickle.dump(self.data, f)

    def delete(self, id):
        for d in self.data:
            if getattr(d, (self.metadata["key"]) == id):
                self.data.remove(d)
        with open((self.filepath), 'wb') as new_data:
            self.data = pickle.dump(self.data, new_data)

    def edit(self, id, value):
        pronadjen = False
        index = 0
        for i in self.data:
            if getattr(i, (self.metadata["key"])) == id:
                self.data[index] = value
                pronadjen = True
            else:
                index += 1
        if pronadjen == False:
            print("Ne postoji objekat u listi sa unetim id-em!")

    #def print_all(self):
    #    all_data = self.get_all()
    #    for i in all_data:
     #       print(i.ime)