from PySide2 import QtWidgets, QtGui, QtCore
from student import Student
from student_model import StudentModel
from predmet import Predmet
from polozeni_predmet import PolozeniPredmet
from polozeni_predmet_model import PolozeniPredmetModel
from nepolozeni_predmet_model import NepolozeniPredmetModel
from nepolozeni_predmet import NepolozeniPredmet

class WorkspaceWidget(QtWidgets.QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.main_layout = QtWidgets.QVBoxLayout()
        self.tab_widget = None
        self.create_tab_widget()


        self.table1 = QtWidgets.QTableView(self.tab_widget)
        self.table1.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.table1.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.student_model = self.create_dummy_model()
        self.table1.setModel(self.student_model)

        self.table1.clicked.connect(self.student_selected)
        self.table1.clicked.connect(self.show_tabs)

        self.subtable1 = QtWidgets.QTableView(self.tab_widget)
        self.subtable2 = QtWidgets.QTableView(self.tab_widget)

        self.main_layout.addWidget(self.table1)
        self.main_layout.addWidget(self.tab_widget)
        self.setLayout(self.main_layout)

    def student_selected(self, index):
        model = self.table1.model() #?
        selected_student = model.get_element(index)

        polozeni_predmeti_model = PolozeniPredmetModel()
        polozeni_predmeti_model.polozeni_predmeti = selected_student.polozeni_predmeti

        nepolozeni_predmeti_model = NepolozeniPredmetModel()
        nepolozeni_predmeti_model.nepolozeni_predmeti = selected_student.nepolozeni_predmeti

        self.subtable1.setModel(polozeni_predmeti_model)
        self.subtable2.setModel(nepolozeni_predmeti_model)


    def show_tabs(self):
        self.tab_widget.addTab(self.subtable1, QtGui.QIcon("icons8-edit-file-64.png"), "Polozeni predmeti")
        self.tab_widget.addTab(self.subtable2, QtGui.QIcon("icons8-edit-file-64.png"), "Nepolozeni predmeti")


    def create_table(self, rows, columns):
        table_widget = QtWidgets.QTableWidget(rows, columns, self)

        for i in range(rows):
            for j in range(columns):
                table_widget.setItem(i, j, QtWidgets.QTableWidgetItem("Celija " + str(i) + str(j)))
        labels = []
        for i in range(columns):
            labels.append("Kolona" + str(i))
        table_widget.setHorizontalHeaderLabels(labels)
        return table_widget

    def create_tab_widget(self):
        self.tab_widget = QtWidgets.QTabWidget(self)
        self.tab_widget.setTabsClosable(True)
        self.tab_widget.tabCloseRequested.connect(self.delete_tab)

    def delete_tab(self, index):
        self.tab_widget.removeTab(index)

    def create_dummy_model(self):
        student_model = StudentModel()
        student_model.students = [
            Student("2018270150", "Srdjan Horvat", [
                PolozeniPredmet("SIMS", "", 10),
                PolozeniPredmet("BP", "", 8),
            ],
            [
                NepolozeniPredmet("AR", "", 2),
                NepolozeniPredmet("Web", "", 1)
            ]),
            Student("2018270150", "Nenad Horvat", [
                PolozeniPredmet("OP", "", 10),
                PolozeniPredmet("OOP1", "", 8),
                PolozeniPredmet("OOP2", "", 9),
            ],
            [
                NepolozeniPredmet("AR", "", 3),
                NepolozeniPredmet("Web", "", 2)
            ]),
            Student("2018270150", "Aleksandra Horvat", [
                PolozeniPredmet("AR", "", 7),
                PolozeniPredmet("OOP1", "", 8),
                PolozeniPredmet("Web", "", 9),
            ],
            [
                NepolozeniPredmet("Strukture", "", 1),
                NepolozeniPredmet("Eng", "", 1)
            ]),
            Student("2018270150", "Josip Horvat", [
                PolozeniPredmet("Strukture", "", 10),
                PolozeniPredmet("Web", "", 8),
                PolozeniPredmet("AR", "", 9),
            ],
            [
                NepolozeniPredmet("OP", "", 2),
                NepolozeniPredmet("OOP", "", 3)
            ]),
            Student("2018270150", "Neda Horvat")
        ]
        return student_model 