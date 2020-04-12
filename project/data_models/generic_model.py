from PySide2 import QtCore

class GenericModel(QtCore.QAbstractTableModel):
    def __init__(self, parent = None, metadata = []):
        super().__init__(parent)
        self.elements = []
        self.metadata = metadata
    

    def get_element(self, index):
        return self.elements[index.row()]

    def row_count(self, index):
        return len(self.elements)
        
    def column_count(self, index):
        return len(self.metadata['columns'])

    def data(self, index, role = QtCore.Qt.DisplayRole):
        element = self.get_element(index)
        if role == QtCore.Qt.DisplayRole:
            return getattr(element, self.metadata['columns'][index.column()])

        return None

    def header_data(self, section, orientation, role = QtCore.Qt.DisplayRole):
        if orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
            return self.metadata['columns'][section]

        return None

    def set_data(self, index, value, role = QtCore.Qt.EditRole):
        element = self.get_element(index)
        if value == " ":
            return False

        if role == QtCore.Qt.EditRole:
            setattr(element, self.metadata['columns'][index.column()], value)
            return True

        return False

    def flags(self, index):
        return super().flags(index) | QtCore.Qt.ItemIsEditable