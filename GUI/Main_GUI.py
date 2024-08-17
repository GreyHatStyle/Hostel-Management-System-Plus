from .home import *
import sys
from PyQt6.QtWidgets import QFileDialog,QProgressBar

from .icons_rc import *
from Custom_Widgets.Widgets import loadJsonStyle

from tkinter import messagebox
from subprocess import run
# https://khamisikibet.github.io/Docs-QT-PyQt-PySide-Custom-Widgets/docs/widgets/custom-slide-menu-widgets
# Linear
class GUI_Front:
    def __init__(self) -> None:
        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(MainWindow)
        MainWindow.setWindowTitle("Hostel Management System")
        MainWindow.setWindowOpacity(0.95)

        MainWindow.setWindowIcon(QtGui.QIcon("GUI\\feather-white\\globe.svg"))
        
        loadJsonStyle(self, self.ui, jsonFiles=["GUI\\style.json"])
        
        self.setter()
        MainWindow.show()
        app.exec()


    def setter(self):
        self.ui.pg1_btn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_1))
        self.ui.pg2_btn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_2))
        self.ui.pg3_btn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_3))
        self.ui.pg4_btn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_4))
        pass
        


if __name__ == '__main__':
    GUI_Front()
    