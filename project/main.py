import sys
from PySide2 import QtWidgets, QtGui, QtCore
from app_view.workspace_widget import WorkspaceWidget
from polozeni_predmet_model import PolozeniPredmetModel
from app_view.main_window import MainWindow

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv) 
    main_window = MainWindow()

    main_window.show()
    sys.exit(app.exec_())