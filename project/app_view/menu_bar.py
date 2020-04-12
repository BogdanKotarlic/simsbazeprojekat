from PySide2 import QtWidgets, QtGui
from app_view.structure_dock import StructureDock

class MenuBar(QtWidgets.QMenuBar):
    def __init__(self, parent):
        super().__init__(parent)
        self.main_window = parent

        file_menu = QtWidgets.QMenu("File", self)
        edit_menu = QtWidgets.QMenu("Edit", self)
        view_menu = QtWidgets.QMenu("View", self)
        help_menu = QtWidgets.QMenu("Help", self)

        openFileAction = QtWidgets.QAction("&Open File", self,
                shortcut=QtGui.QKeySequence.Open,
                statusTip="Open", triggered=self.main_window.openNewFileButton)

        openFolderAction = QtWidgets.QAction("&Open Folder", self,
                shortcut=None,
                statusTip="Open", triggered=self.main_window.openFolderButton)

        saveAction = QtWidgets.QAction("&Save", self,
                shortcut=QtGui.QKeySequence.Save,
                statusTip="Open", triggered=self.main_window.saveAction)

        file_menu.addAction(openFileAction)
        file_menu.addAction(openFolderAction)
        file_menu.addAction(saveAction)
        
        toggle_structure_dock_action = self.main_window.structure_dock.toggleViewAction()
        view_menu.addAction(toggle_structure_dock_action)

        self.addMenu(file_menu)
        self.addMenu(edit_menu)
        self.addMenu(view_menu)
        self.addMenu(help_menu)