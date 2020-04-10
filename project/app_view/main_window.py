from PySide2 import QtCore, QtWidgets, QtGui
from app_view.structure_dock import StructureDock
from app_view.menu_bar import MenuBar
from app_view.tool_bar import ToolBar
from app_view.workspace_widget import WorkspaceWidget

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.resize(640, 480)
        self.setWindowTitle("Rukovalac informacijama - InfHandler")
        self.setWindowIcon(QtGui.QIcon("icons/icons8-edit-file-64.png"))

        self.structure_dock = StructureDock("Structure dock", self)
        self.menu_bar = MenuBar(self)
        self.tool_bar = ToolBar(self)
        self.central_widget = QtWidgets.QTabWidget(self)
        self.workspace_widget = WorkspaceWidget(self.central_widget)
        self.status_bar = QtWidgets.QStatusBar(self)
        self.status_bar.showMessage("Status bar je prikazan!")
        self.central_widget.addTab(self.workspace_widget, QtGui.QIcon("icons/icons8-edit-file-64.png"), "Prikaz tabele")
        self.central_widget.setTabsClosable(True)

        self.setMenuBar(self.menu_bar)
        self.setStatusBar(self.status_bar)
        self.addToolBar(self.tool_bar)
        self.setCentralWidget(self.central_widget)
        self.addDockWidget(QtCore.Qt.LeftDockWidgetArea, self.structure_dock)
        
        