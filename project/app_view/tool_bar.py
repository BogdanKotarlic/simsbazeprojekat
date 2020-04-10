from PySide2 import QtWidgets, QtGui
from app_view.structure_dock import StructureDock

class ToolBar(QtWidgets.QToolBar):
    def __init__(self, parent):
        super().__init__(parent)
        self.main_window = parent

        saveAction = QtWidgets.QAction(QtGui.QIcon("icons/icons8-save-32.png"), "Save", self)
        saveAction.setStatusTip("Save program")

        leftAction = QtWidgets.QAction("Left", self)
        leftAction.setIcon(QtGui.QIcon("icons/icons8-arrow-left-32.png"))

        rightAction = QtWidgets.QAction("Right", self)
        rightAction.setIcon(QtGui.QIcon('icons/icons8-arrow-right-32.png'))

        self.addAction(saveAction)
        self.addAction(leftAction)
        self.addAction(rightAction)