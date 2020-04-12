from PySide2 import QtWidgets, QtCore

class PolozeniPredmetModel(QtCore.QAbstractTableModel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.polozeni_predmeti = []

    def get_element(self, index):
        return self.polozeni_predmeti[index.row()]

    def row_count(self, index):
        return len(self.polozeni_predmeti)

    def column_count(self, index):
        return 3 

    def data(self, index, role=QtCore.Qt.DisplayRole):
        self.polozeni_predmet = self.get_element(index)
        if index.column() == 0 and role == QtCore.Qt.DisplayRole:
            return self.polozeni_predmet.naziv
        elif index.column() == 1 and role == QtCore.Qt.DisplayRole:
            return self.polozeni_predmet.silabus
        elif index.column() == 2 and role == QtCore.Qt.DisplayRole:
            return self.polozeni_predmet.ocena

    def header_data(self, section, orientation, role=QtCore.Qt.DisplayRole):
        if section == 0 and orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
            return "Naziv"
        elif section == 1 and orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
            return "Silabus"
        elif section == 2 and orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
            return "Ocena"

    def set_data(self, index, value, role=QtCore.Qt.EditRole):
        polozeni_predmet = self.get_element(index)
        if value == "":
            return False
        if index.column() == 0 and role == QtCore.Qt.EditRole:
            polozeni_predmet.naziv = value
            return True
        elif index.column() == 1 and role == QtCore.Qt.EditRole:
            polozeni_predmet.silabus = value
            return True
        elif index.column() == 2 and role == QtCore.Qt.EditRole:
            polozeni_predmet.ocena = value
            return True
        return False 


    def flags(self, index):
        return super().flags(index) | QtCore.Qt.ItemIsEditable 