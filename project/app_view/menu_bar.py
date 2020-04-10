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

        newFileAction = QtWidgets.QAction("New File", self)
        newFileAction.setShortcut("CTRL+N")
        newFileAction.setStatusTip("Create a New File")
        editFileAction = QtWidgets.QAction("Edit", self)
        editFileAction.setShortcut("CTRL+E")
        editFileAction.setStatusTip("Edit File")
        saveFileAction = QtWidgets.QAction("Save", self)
        saveFileAction.setShortcut("CTRL+S")
        saveFileAction.setStatusTip("Save File")
        deleteFileAction = QtWidgets.QAction("Delete", self)
        deleteFileAction.setShortcut("CTRL+D")
        deleteFileAction.setStatusTip("Delete File")
        quitAction = QtWidgets.QAction("Quit", self)
        quitAction.setShortcut("CTRL+Q")
        quitAction.setStatusTip("Quit Application")
        
        file_menu.addAction(newFileAction)
        file_menu.addAction(saveFileAction)
        file_menu.addAction(editFileAction)
        file_menu.addAction(deleteFileAction)
        file_menu.addAction(quitAction)
        
        toggle_structure_dock_action = self.main_window.structure_dock.toggleViewAction()
        view_menu.addAction(toggle_structure_dock_action)

        self.addMenu(file_menu)
        self.addMenu(edit_menu)
        self.addMenu(view_menu)
        self.addMenu(help_menu)