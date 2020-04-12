from PySide2 import QtWidgets, QtGui
from app_view.structure_dock import StructureDock

class ToolBar(QtWidgets.QToolBar):
    def __init__(self, parent):
        super().__init__(parent)
        self.main_window = parent

        #save action
        saveAction = QtWidgets.QAction(QtGui.QIcon("icons/icons8-save-32.png"), "Save", self)
        saveAction.setStatusTip("Save updated file")
        saveAction.triggered = self.main_window.saveAction

        #delete action
        deleteAction = QtWidgets.QAction(QtGui.QIcon("icons/icons8-delete-file-32.png"), "Delete", self)
        deleteAction.setStatusTip("Delete file")
        deleteAction.triggered = self.main_window.deleteAction

        self.addAction(saveAction)
        self.addAction(deleteAction)