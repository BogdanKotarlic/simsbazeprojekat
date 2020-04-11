from data_manipulation.data_handler import DataHandler
import pickle
import json

class SequentialFileHandler(DataHandler):
    def __init__(self, filepath, meta_filepath):
        super().__init__()
        self.filepath = filepath
        self.meta_filepath = meta_filepath
        self.data = []
        self.metadata = []
        self.load_data()

    def load_data(self):
        #metoda za ucitavanje podataka
        with open((self.filepath), 'rb') as dfile:
            self.data = pickle.load(dfile)

        with open(self.meta_filepath) as meta_file:
            self.metadata = json.load(meta_file)

    def binary_search(self, id, start, end):
        while start <= end:
            mid = start + (end - start)//2

            if getattr(self.data[mid], (self.metadata["key"])) == id:
                return mid

            elif getattr(self.data[mid], (self.metadata["key"])) < id:
                start = mid + 1
            
            else:
                end = mid - 1

        return None #nije nista pronadjeno

    def get_one(self, id):
        #treba jos razmotriti sta ako vrati None
        return self.data[self.binary_search(id, 0, (len(self.data)))]

    def find_location_for_insert(self, obj):
        for i in range(len(self.data)):
            if getattr(self.data[i], (self.metadata["key"])) > getattr(obj, (self.metadata["key"])):
                return i
        return None

    def insert(self, obj):
        location = self.find_location_for_insert(obj)
        if(location == None):
            self.data.append(obj)
        else:
            self.data.insert(location-1, obj)

    #treba dodati preostale metode
        
        