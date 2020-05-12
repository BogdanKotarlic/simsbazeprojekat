from PySide2 import QtCore, QtWidgets, QtGui
from app_view.structure_dock import StructureDock
from app_view.menu_bar import MenuBar
from app_view.workspace_widget import WorkspaceWidget
from app_view.tool_bar import ToolBar
from data_manipulation.serial_file_handler import SerialFileHandler
from data_manipulation.sequential_file_handler import SequentialFileHandler
import json

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.resize(640, 480)
        self.setWindowTitle("Rukovalac informacijama - InfHandler")
        self.setWindowIcon(QtGui.QIcon("icons/icons8-edit-file-64.png"))

        self.menu_bar = MenuBar(self)
        self.tool_bar = ToolBar(self)
        self.structure_dock = StructureDock("Structure dock", self)  
        self.central_widget = QtWidgets.QTabWidget(self)
        self.workspace_widget = WorkspaceWidget(self.central_widget)
        self.central_widget.addTab(self.workspace_widget, QtGui.QIcon("icons/icons8-edit-file-64.png"), "Prikaz tabele")
        self.central_widget.setTabsClosable(True)
        self.status_bar = QtWidgets.QStatusBar(self)
        self.status_bar.showMessage("Status bar!")
        
        self.setMenuBar(self.menu_bar)
        self.addToolBar(self.tool_bar)
        self.addDockWidget(QtCore.Qt.LeftDockWidgetArea, self.structure_dock)
        self.setCentralWidget(self.central_widget)
        self.setStatusBar(self.status_bar)
    
    def openFolderButton(self):
        path_to_folder = QtWidgets.QFileDialog.getExistingDirectory(self, self.tr("Open Folder"))
        print(path_to_folder)
        self.structure_dock.setRootPath(path_to_folder)

    def openNewFileButton(self):
        path_to_data_file, _ = QtWidgets.QFileDialog.getOpenFileName(self, self.tr("Open Data File"), self.tr("~/Desktop/"))
        print(path_to_data_file)
        self.openNewFile(path_to_data_file)

    def openNewFile(self, filepath):
        metadata_filepath = filepath.replace("_data", "_metadata.json")
        with open(metadata_filepath) as meta:
            metadata = json.load(meta)
        data_handler = self.getFileHandler(metadata, filepath, metadata_filepath)

        linked_files = metadata['linked_files']
        if len(linked_files) == 0:
            print("No linked files")
        else:
            linked_path = filepath[:filepath.rindex("/")]
            linked_data_filepath = linked_path + "/" + linked_files[0]
            linked_metadata_filepath = linked_data_filepath.replace("_data", "_metadata.json")
            with open(linked_metadata_filepath) as linked_meta:
                linked_meta = json.load(linked_meta)
            
            linked_filehandler = self.getFileHandler(linked_meta['type'], linked_data_filepath, linked_metadata_filepath)
            self.workspace_widget.refresh_subtable(linked_filehandler)

        self.workspace_widget.refresh_table(data_handler)

    def getFileHandler(self, fileType, data_filepath, metadata_filepath): 
        print(fileType)
        if fileType == "serijska":
            return SerialFileHandler(data_filepath, metadata_filepath)
        elif fileType == "sekvencijalna":
            return SequentialFileHandler(data_filepath, metadata_filepath)
        else: 
            return None

    def saveAction(self):
        self.workspace_widget.save()

    def insertAction(self):
        self.workspace_widget.insert()

    def deleteAction(self):
        self.workspace_widget.delete()
        