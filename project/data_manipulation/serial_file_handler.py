from data_manipulation.data_handler import DataHandler
import json
import pickle

class SerialFileHandler():
    def __init__(self, filepath, meta_filepath):
        super().__init__()
        self.filepath = filepath
        self.meta_filepath = meta_filepath
        self.data = []
        self.metadata = []
        self.load_data()

    def load_data(self):
        with open((self.filepath), 'rb') as dfile:
            self.data = pickle.load(dfile)
        with open(self.meta_filepath) as m:
            self.metadata = json.load(m)

    def get_one(self, id):
        for i in self.data: 
            if getattr(i, (self.metadata["key"])) == id: 
                return i
        return None

    def get_all(self):
        return self.data()

    def insert(self, obj):
        self.data.append(obj)
        with open(self.filepath, 'wb') as f:
            pickle.dump(self.data, f)

    def delete(self, id):
        for i in self.data:
            if getattr(i, (self.metadata["key"]) == id):
                self.data.remove(i)
        with open((self.filepath), 'wb') as data:
            pickle.dump(self.data, data)

    def edit(self, id, value):
        x = False
        index = 0
        for i in self.data:
            if getattr(i, (self.metadata["key"])) == id:
                self.data[index] = value
                x = True
            else:
                index += 1
        if x == False:
            print("Ne postoji element sa ovim ID.")
        else:
            with open(self.filepath, 'wb') as dfile:
                pickle.dump(self.data, dfile)

    def save(self):
        with open(self.filepath, 'wb') as data:
            pickle.dump(self.data, data)