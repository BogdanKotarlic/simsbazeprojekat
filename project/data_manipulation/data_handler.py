from abc import ABC, abstractmethod

class DataHandler():
    def __init__(self):
        super().__init__()

    @abstractmethod
    def get_one(self, id):
        pass
    
    @abstractmethod
    def get_all(self):
        pass
    
    @abstractmethod
    def edit(self, obj):
        pass
    
    @abstractmethod
    def delete_one(self, id):
        pass

    @abstractmethod
    def insert(self, obj):
        pass