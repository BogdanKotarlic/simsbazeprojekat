import sys
from PySide2 import QtWidgets, QtGui, QtCore
from workspace_widget import WorkspaceWidget
from polozeni_predmet_model import PolozeniPredmetModel
from structure_dock import StructureDock

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv) 

    main_window = QtWidgets.QMainWindow()
    main_window.resize(640, 480)
    main_window.setWindowTitle("Rukovalac informacijama - InfHandler")
    main_window.setWindowIcon(QtGui.QIcon("icons8-edit-file-64.png"))

    menu_bar = QtWidgets.QMenuBar(main_window)
    file_menu = QtWidgets.QMenu("File", menu_bar)
    edit_menu = QtWidgets.QMenu("Edit", menu_bar)
    view_menu = QtWidgets.QMenu("View", menu_bar)
    help_menu = QtWidgets.QMenu("Help", menu_bar)

    menu_bar.addMenu(file_menu)
    menu_bar.addMenu(edit_menu)
    menu_bar.addMenu(view_menu)
    menu_bar.addMenu(help_menu)

    newFileAction = QtWidgets.QAction("New File", main_window)
    newFileAction.setShortcut("CTRL+N")
    newFileAction.setStatusTip("Create a New File")
    editFileAction = QtWidgets.QAction("Edit", main_window)
    editFileAction.setShortcut("CTRL+E")
    editFileAction.setStatusTip("Edit File")
    saveFileAction = QtWidgets.QAction("Save", main_window)
    saveFileAction.setShortcut("CTRL+S")
    saveFileAction.setStatusTip("Save File")
    deleteFileAction = QtWidgets.QAction("Delete", main_window)
    deleteFileAction.setShortcut("CTRL+D")
    deleteFileAction.setStatusTip("Delete File")
    quitAction = QtWidgets.QAction("Quit", main_window)
    quitAction.setShortcut("CTRL+Q")
    quitAction.setStatusTip("Quit Application")

    #copyAction = QtWidgets.QAction("Copy", main_window)
    #copyAction.setShortcut("CTRL+C")
    #copyAction.setStatusTip("Copy Item")

    #cutAction = QtWidgets.QAction("Cut", main_window)
    #cutAction.setShortcut("CTRL+X")
    #cutAction.setStatusTip("Cut Item")

    #pasteAction = QtWidgets.QAction("Paste", main_window)
    #pasteAction.setShortcut("CTRL+V")
    #pasteAction.setStatusTip("Paste Item")

    #findAc = QtWidgets.QAction("Find...", main_window)
    #findAc.setStatusTip("Find...")
    #replace = QtWidgets.QAction("Replace", main_window)
    #replace.setStatusTip("Replace")
    
    file_menu.addAction(newFileAction)
    file_menu.addAction(saveFileAction)
    file_menu.addAction(editFileAction)
    file_menu.addAction(deleteFileAction)
    file_menu.addAction(quitAction)

    #edit_menu.addAction(copyAction)
    #edit_menu.addAction(cutAction)
    #edit_menu.addAction(pasteAction)
    #edit_menu.addSeparator()

    #findAction = edit_menu.addMenu("Find")
    #findAction.addAction(findAc)
    #findAction.addAction(replace)

    tool_bar = QtWidgets.QToolBar("Toolbar", main_window)
    toggle_toolbar_widget_action = tool_bar.toggleViewAction()
    view_menu.addAction(toggle_toolbar_widget_action)

    saveAction = QtWidgets.QAction(QtGui.QIcon("icons8-save-32.png"), "Save", tool_bar)
    saveAction.setStatusTip("Save program")

    leftAction = QtWidgets.QAction("Left", tool_bar)
    leftAction.setIcon(QtGui.QIcon("icons8-arrow-left-32.png"))

    rightAction = QtWidgets.QAction("Right", tool_bar)
    rightAction.setIcon(QtGui.QIcon('icons8-arrow-right-32.png'))

    tool_bar.addAction(saveAction)
    tool_bar.addAction(leftAction)
    tool_bar.addAction(rightAction)

    central_widget = QtWidgets.QTabWidget(main_window)
    workspace = WorkspaceWidget(central_widget)
    central_widget.addTab(workspace, QtGui.QIcon("icons8-edit-file-64.png"), "Prikaz podataka")

    structure_dock = StructureDock("Struktura informacionog resursa", main_window)
    toggle_structure_widget_action = structure_dock.toggleViewAction()
    view_menu.addAction(toggle_structure_widget_action)

    status_bar = QtWidgets.QStatusBar(main_window)

    main_window.setMenuBar(menu_bar)
    main_window.setStatusBar(status_bar)
    main_window.addToolBar(tool_bar)
    main_window.setCentralWidget(central_widget)
    main_window.addDockWidget(QtCore.Qt.LeftDockWidgetArea, structure_dock)

    main_window.show()
    sys.exit(app.exec_())