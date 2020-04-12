from PySide2 import QtWidgets, QtGui, QtCore
from data_models.generic_model import GenericModel
from data_models.model import *

class WorkspaceWidget(QtWidgets.QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.main_layout = QtWidgets.QVBoxLayout()
        self.tab_widget = None
        self.data_handler = None
        self.create_tab_widget()


        self.table = QtWidgets.QTableView(self.tab_widget)
        self.table.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.table.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.table.setModel(None)
        self.table.clicked.connect(self.element_selected)
        self.table.clicked.connect(self.show_tabs)

        self.subtable1 = QtWidgets.QTableView(self.tab_widget)
        self.subtable2 = QtWidgets.QTableView(self.tab_widget)

        self.main_layout.addWidget(self.table)
        self.main_layout.addWidget(self.tab_widget)
        self.setLayout(self.main_layout)

    def element_selected(self, index):
        model = self.table.model()
        element = model.get_element(index)

    def show_tabs(self):
        self.tab_widget.addTab(self.subtable1, QtGui.QIcon("icons8-edit-file-64.png"), "Polozeni predmeti")
        self.tab_widget.addTab(self.subtable2, QtGui.QIcon("icons8-edit-file-64.png"), "Nepolozeni predmeti")

    def create_tab_widget(self):
        self.tab_widget = QtWidgets.QTabWidget(self)
        self.tab_widget.setTabsClosable(True)
        self.tab_widget.tabCloseRequested.connect(self.delete_tab)

    def delete_tab(self, index):
        self.tab_widget.removeTab(index)
    
    def refresh_table(self, data_handler): 
        generic_model = GenericModel(self, data_handler.metadata)
        generic_model.elements = data_handler.get_all()
        self.data_handler = data_handler
        self.table.setModel(generic_model)

    def refresh_subtable(self, data_handler): 
        generic_model = GenericModel(self, data_handler.metadata)
        generic_model.elements = data_handler.get_all()
        self.subtable1.setModel(generic_model)

    def save(self):
        self.data_handler.save()

    def delete(self):
        indexes = self.table.selectedIndexes()
        if len(indexes) == 0:
            return False
        rowNum = indexes[0].row()
        element = self.table.model().elements[rowNum]
        self.data_handler.delete(getattr(element, self.data_handler.metadata['key']))
        self.refresh_table(self.data_handler)
        

    def insert(self):
        indexes = self.table.selectedIndexes()
        if len(indexes) == 0:   
            return False
        model = self.table.model()
        elem_type = type(model.elements[0]) 
        temp = elem_type()
        for column in self.data_handler.metadata['columns']:
            setattr(temp, column, "enter value")
        model.elements.append(temp)
        self.data_handler.save()
        self.table.setModel(model)
        self.refresh_table(self.data_handler)
