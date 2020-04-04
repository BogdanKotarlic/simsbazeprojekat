from abc import ABCMeta, abstractmethod

class FileHandler(metaclass = ABCMeta):
    def __init__(self):
        super().__init__()
        podaci = []

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
    def update(self, obj):
        pass