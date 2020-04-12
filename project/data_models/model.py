from PySide2 import QtCore
class Model(QtCore.QAbstractTableModel):
    def __init__(self, parent = None, kolone = []):
        super().__init__(parent)
        self.kolone = kolone
        self.model = self.__dict__
        for key in kolone:
            self.model.key = None

          
    def __getitem__(self, key):
        return self.model[key]

    def __setitem__(self, key, value):
        self.model[key] = value

    def __len__(self):
        return len(self.model)

    def get_element(self, index):
        return self.model[index.row()]

    def row_count(self, index):
        return len(self.model)

    def column_count(self, index):
        return len(self.kolone)

    def data(self, index, role = QtCore.Qt.DisplayRole):
        element = self.get_element(index)
        counter = 0
        for i in self.model:
            for j in element.__dict__.items():
                if index.column() == counter and role == QtCore.Qt.DisplayRole:
                    return j[1]
                else:
                    counter+=1
        return None

    def header_data(self, section, orientation, role = QtCore.Qt.DisplayRole):
        for i in range(len(self.kolone)):
            if section == i and orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
                return self.kolone[i]

        return None

    def set_data(self, index, value, role = QtCore.Qt.EditRole):
        element = self.get_element(index)
        if value == " ":
            return False

        for i in range(len(self.model)):
            if index.column() == i and role == QtCore.Qt.EditRole:
                kolona = self.model[i]
                element.kolona = value
                return True

        return False

    def flags(self, index):
        return super().flags(index) | QtCore.Qt.ItemIsEditable


    