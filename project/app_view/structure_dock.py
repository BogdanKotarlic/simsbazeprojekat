from PySide2 import QtWidgets, QtGui, QtCore

class StructureDock(QtWidgets.QDockWidget):
    def __init__(self, title, parent):
        super().__init__(title, parent)

        self.model = QtWidgets.QFileSystemModel()
        self.model.setRootPath(QtCore.QDir.currentPath())
        self.main_window = parent

        self.tree = QtWidgets.QTreeView()
        self.tree.setModel(self.model)
        self.tree.setRootIndex(self.model.index(QtCore.QDir.currentPath()))
        self.tree.clicked.connect(self.file_clicked)

        self.setWidget(self.tree)

    def file_clicked(self, index):
        print(self.model.filePath(index))
        filepath = self.model.filePath(index)
        self.main_window.openNewFile(filepath)
    
    def setRootPath(self, path):
        self.model.setRootPath(path)
        self.tree.setRootIndex(self.model.index(path))