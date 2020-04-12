from data_manipulation.data_handler import DataHandler
import json
import pickle

class SequentialFileHandler():
    def __init__(self, filepath, meta_filepath):
        super().__init__()
        self.filepath = filepath
        self.meta_filepath = meta_filepath
        self.data = []
        self.metadata = {}
        self.load_data()

    def load_data(self):
        with open((self.filepath), 'rb') as dfile:
            self.data = pickle.load(dfile)

        with open(self.meta_filepath) as meta:
            self.metadata = json.load(meta)

    def binary_search(self, id):
        bot = 0
        top = len(self.data)-1
        while bot <= top:
            mid = (top+bot)//2
            if getattr(self.data[mid], (self.metadata["key"])) == id:
                return mid
            elif getattr(self.data[mid], (self.metadata["key"])) < id:
                bot = mid+1
            else:
                top = mid - 1
        return None

    def get_one(self,id):
        index = self.binary_search(id)
        return self.data[index]
            
            
    def get_all(self):
        return self.data

    def insert(self, id, obj):
        bot = 0
        top = len(self.data)-1
        biggest = True
        found = False
        while bot <= top:
            mid = (top+bot)//2
            
            if getattr(self.data[mid], (self.metadata["key"])) == id:
                print("Vec postoji element sa unesenim kljucem!")
                found = True
                break
            elif getattr(self.data[mid], (self.metadata["key"])) > id:
                self.data.insert(mid, obj)
                biggest = False
                break
            else:
                bot = mid + 1
                
        if biggest == True and found == False:
            self.data.insert(mid+1, obj)
        
        if found == False:
            with open(self.filepath, 'wb') as f:
                pickle.dump(self.data, f)

    def edit(self, id, value):
        index = self.binary_search(id)
        self.data[index] = value

        with open(self.filepath, 'wb') as f:
            pickle.dump(self.data, f)

    def delete(self, id):
        index = self.binary_search(id)
        if index is not None:
            self.data.remove(self.data[index])
            with open(self.filepath, 'wb') as data:
                pickle.dump(self.data, data)
        else:
            print("Ne postoji element sa unesenim ID-em!")

    def save(self):
        with open(self.filepath, 'wb') as data:
                pickle.dump(self.data, data)
