import sys
import os
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QWidget, QAction, QGridLayout, QTabWidget, QVBoxLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
from hodomon import hodomon

class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = "HodoMon"
        self.left = 0
        self.top = 0
        self.width = 800
        self.height = 200
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.layout = QVBoxLayout(self)

        self.tabs = QTabWidget()

        self.main_tab = QTabWidget()
        self.voltage_tab = voltage()
        self.main_tab.addTab(self.voltage_tab, "VOLTAGE")
        self.tabs.addTab(self.voltage_tab, " MAIN ")

        self.station1 = QTabWidget()
        # self.station1.layout = QVBoxLayout(self)
        self.H1XB = pmt23("H1XB")
        self.H1XT = pmt23("H1XT")
        self.H1YL = pmt20("H1YL")
        self.H1YR = pmt20("H1YR")
        self.station1.addTab(self.H1XB, "H1XB")
        self.station1.addTab(self.H1XT, "H1XT")
        self.station1.addTab(self.H1YL, "H1YL")
        self.station1.addTab(self.H1YR, "H1YR")
        self.tabs.addTab(self.station1, " H1 ")

        self.station2 = QTabWidget()
        # self.station1.layout = QVBoxLayout(self)
        self.H2XB = pmt16("H2XB")
        self.H2XT = pmt16("H2XT")
        self.H2YL = pmt19("H2YL")
        self.H2YR = pmt19("H2YR")
        self.station2.addTab(self.H2XB, "H2XB")
        self.station2.addTab(self.H2XT, "H2XT")
        self.station2.addTab(self.H2YL, "H2YL")
        self.station2.addTab(self.H2YR, "H2YR")
        self.tabs.addTab(self.station2, " H2 ")

        self.station3 = QTabWidget()
        # self.station1.layout = QVBoxLayout(self)
        self.H3XB = pmt16("H3XB")
        self.H3XT = pmt16("H3XT")
        self.station3.addTab(self.H3XB, "H3XB")
        self.station3.addTab(self.H3XT, "H3XT")
        self.tabs.addTab(self.station3, " H3 ")

        self.station4 = QTabWidget()
        # self.station1.layout = QVBoxLayout(self)
        self.H4XT_u = pmt16("H4XT-u")
        self.H4XT_d = pmt16("H4XT-d")
        self.H4XB_u = pmt16("H4XB-u")
        self.H4XB_d = pmt16("H4XB-d")
        self.station4.addTab(self.H4XT_u, "H4XT-u")
        self.station4.addTab(self.H4XT_d, "H4XT-d")
        self.station4.addTab(self.H4XB_u, "H4XB-u")
        self.station4.addTab(self.H4XB_d, "H4XB-d")

        self.H4Y1L_l = pmt16("H4Y1L-l")
        self.H4Y1L_r = pmt16("H4Y1L-r")
        self.H4Y1R_l = pmt16("H4Y1R-l")
        self.H4Y1R_r = pmt16("H4Y1R-r")
        self.station4.addTab(self.H4Y1L_l, "H4Y1L-l")
        self.station4.addTab(self.H4Y1L_r, "H4Y1L-r")
        self.station4.addTab(self.H4Y1R_l, "H4Y1R-l")
        self.station4.addTab(self.H4Y1R_r, "H4Y1R-r")

        self.H4Y2L_l = pmt16("H4Y2L-l")
        self.H4Y2L_r = pmt16("H4Y2L-r")
        self.H4Y2R_l = pmt16("H4Y2R-l")
        self.H4Y2R_r = pmt16("H4Y2R-r")
        self.station4.addTab(self.H4Y2L_l, "H4Y2L-l")
        self.station4.addTab(self.H4Y2L_r, "H4Y2L-r")
        self.station4.addTab(self.H4Y2R_l, "H4Y2R-l")
        self.station4.addTab(self.H4Y2R_r, "H4Y2R-r")

        self.tabs.addTab(self.station4, " H4 ")

        self.expert_tab = QTabWidget()
        self.expert_H1 = expert(" H1 ")
        self.expert_H2 = expert(" H2 ")
        self.expert_H3 = expert(" H3 ")
        self.expert_H4 = expert(" H4 ")
        self.expert_tab.addTab(self.expert_H1, " H1 ")
        self.expert_tab.addTab(self.expert_H2, " H2 ")
        self.expert_tab.addTab(self.expert_H3, " H3 ")
        self.expert_tab.addTab(self.expert_H4, " H4 ")
        self.tabs.addTab(self.expert_tab, "EXPERT")

        self.layout.addWidget(self.tabs)
        # self.setLayout(self.layout)

        self.setCentralWidget(self.tabs)
        self.show()




class pmt23(QWidget):
    def __init__(self, hodo_name):
        super(QWidget, self).__init__()
        self.hodo_name = hodo_name

        self.tab = QWidget()
        self.tab.layout = QGridLayout(self)

        # self.Hits = QPushButton(" Hits ")
        # self.Efficiency = QPushButton(" Efficiency ")

        self.pmt1 = QPushButton(" 1 ")
        self.pmt1.clicked.connect(lambda: self.action(self.hodo_name + "_1_MV"))
        self.pmt2 = QPushButton(" 2 ")
        self.pmt2.clicked.connect(lambda: self.action(self.hodo_name + "_2_MV"))
        self.pmt3 = QPushButton(" 3 ")
        self.pmt3.clicked.connect(lambda: self.action(self.hodo_name + "_3_MV"))
        self.pmt4 = QPushButton(" 4 ")
        self.pmt4.clicked.connect(lambda: self.action(self.hodo_name + "_4_MV"))
        self.pmt5 = QPushButton(" 5 ")
        self.pmt5.clicked.connect(lambda: self.action(self.hodo_name + "_5_MV"))
        self.pmt6 = QPushButton(" 6 ")
        self.pmt6.clicked.connect(lambda: self.action(self.hodo_name + "_6_MV"))
        self.pmt7 = QPushButton(" 7 ")
        self.pmt7.clicked.connect(lambda: self.action(self.hodo_name + "_7_MV"))
        self.pmt8 = QPushButton(" 8 ")
        self.pmt8.clicked.connect(lambda: self.action(self.hodo_name + "_8_MV"))
        self.pmt9 = QPushButton(" 9 ")
        self.pmt9.clicked.connect(lambda: self.action(self.hodo_name + "_9_MV"))
        self.pmt10 = QPushButton(" 10 ")
        self.pmt10.clicked.connect(lambda: self.action(self.hodo_name + "_10_MV"))
        self.pmt11 = QPushButton(" 11 ")
        self.pmt11.clicked.connect(lambda: self.action(self.hodo_name + "_11_MV"))
        self.pmt12 = QPushButton(" 12 ")
        self.pmt12.clicked.connect(lambda: self.action(self.hodo_name + "_12_MV"))
        self.pmt13 = QPushButton(" 13 ")
        self.pmt13.clicked.connect(lambda: self.action(self.hodo_name + "_13_MV"))
        self.pmt14 = QPushButton(" 14 ")
        self.pmt14.clicked.connect(lambda: self.action(self.hodo_name + "_14_MV"))
        self.pmt15 = QPushButton(" 15 ")
        self.pmt15.clicked.connect(lambda: self.action(self.hodo_name + "_15_MV"))
        self.pmt16 = QPushButton(" 16 ")
        self.pmt16.clicked.connect(lambda: self.action(self.hodo_name + "_16_MV"))
        self.pmt17 = QPushButton(" 17 ")
        self.pmt17.clicked.connect(lambda: self.action(self.hodo_name + "_17_MV"))
        self.pmt18 = QPushButton(" 18 ")
        self.pmt18.clicked.connect(lambda: self.action(self.hodo_name + "_18_MV"))
        self.pmt19 = QPushButton(" 19 ")
        self.pmt19.clicked.connect(lambda: self.action(self.hodo_name + "_19_MV"))
        self.pmt20 = QPushButton(" 20 ")
        self.pmt20.clicked.connect(lambda: self.action(self.hodo_name + "_20_MV"))
        self.pmt21 = QPushButton(" 21 ")
        self.pmt21.clicked.connect(lambda: self.action(self.hodo_name + "_21_MV"))
        self.pmt22 = QPushButton(" 22 ")
        self.pmt22.clicked.connect(lambda: self.action(self.hodo_name + "_22_MV"))
        self.pmt23 = QPushButton(" 23 ")
        self.pmt23.clicked.connect(lambda: self.action(self.hodo_name + "_23_MV"))

        # self.tab.layout.addWidget(self.Hits, 0, 0)
        # self.tab.layout.addWidget(self.Efficiency, 0, 1)
        self.tab.layout.addWidget(self.pmt1, 1, 0)
        self.tab.layout.addWidget(self.pmt2, 1, 1)
        self.tab.layout.addWidget(self.pmt3, 1, 2)
        self.tab.layout.addWidget(self.pmt4, 1, 3)
        self.tab.layout.addWidget(self.pmt5, 1, 4)
        self.tab.layout.addWidget(self.pmt6, 2, 0)
        self.tab.layout.addWidget(self.pmt7, 2, 1)
        self.tab.layout.addWidget(self.pmt8, 2, 2)
        self.tab.layout.addWidget(self.pmt9, 2, 3)
        self.tab.layout.addWidget(self.pmt10, 2, 4)
        self.tab.layout.addWidget(self.pmt11, 3, 0)
        self.tab.layout.addWidget(self.pmt12, 3, 1)
        self.tab.layout.addWidget(self.pmt13, 3, 2)
        self.tab.layout.addWidget(self.pmt14, 3, 3)
        self.tab.layout.addWidget(self.pmt15, 3, 4)
        self.tab.layout.addWidget(self.pmt16, 4, 0)
        self.tab.layout.addWidget(self.pmt17, 4, 1)
        self.tab.layout.addWidget(self.pmt18, 4, 2)
        self.tab.layout.addWidget(self.pmt19, 4, 3)
        self.tab.layout.addWidget(self.pmt20, 4, 4)
        self.tab.layout.addWidget(self.pmt21, 5, 0)
        self.tab.layout.addWidget(self.pmt22, 5, 1)
        self.tab.layout.addWidget(self.pmt23, 5, 2)

    @pyqtSlot()
    def action(self, name):
        # print(name)
        A = hodomon(name)
        A.display()


class pmt20(QWidget):
    def __init__(self, hodo_name):
        super(QWidget, self).__init__()
        self.hodo_name = hodo_name

        self.tab = QWidget()
        self.tab.layout = QGridLayout(self)

        # self.Hits = QPushButton(" Hits ")
        # self.Efficiency = QPushButton(" Efficiency ")

        self.pmt1 = QPushButton(" 1 ")
        self.pmt1.clicked.connect(lambda: self.action(self.hodo_name + "_1_MV"))
        self.pmt2 = QPushButton(" 2 ")
        self.pmt2.clicked.connect(lambda: self.action(self.hodo_name + "_2_MV"))
        self.pmt3 = QPushButton(" 3 ")
        self.pmt3.clicked.connect(lambda: self.action(self.hodo_name + "_3_MV"))
        self.pmt4 = QPushButton(" 4 ")
        self.pmt4.clicked.connect(lambda: self.action(self.hodo_name + "_4_MV"))
        self.pmt5 = QPushButton(" 5 ")
        self.pmt5.clicked.connect(lambda: self.action(self.hodo_name + "_5_MV"))
        self.pmt6 = QPushButton(" 6 ")
        self.pmt6.clicked.connect(lambda: self.action(self.hodo_name + "_6_MV"))
        self.pmt7 = QPushButton(" 7 ")
        self.pmt7.clicked.connect(lambda: self.action(self.hodo_name + "_7_MV"))
        self.pmt8 = QPushButton(" 8 ")
        self.pmt8.clicked.connect(lambda: self.action(self.hodo_name + "_8_MV"))
        self.pmt9 = QPushButton(" 9 ")
        self.pmt9.clicked.connect(lambda: self.action(self.hodo_name + "_9_MV"))
        self.pmt10 = QPushButton(" 10 ")
        self.pmt10.clicked.connect(lambda: self.action(self.hodo_name + "_10_MV"))
        self.pmt11 = QPushButton(" 11 ")
        self.pmt11.clicked.connect(lambda: self.action(self.hodo_name + "_11_MV"))
        self.pmt12 = QPushButton(" 12 ")
        self.pmt12.clicked.connect(lambda: self.action(self.hodo_name + "_12_MV"))
        self.pmt13 = QPushButton(" 13 ")
        self.pmt13.clicked.connect(lambda: self.action(self.hodo_name + "_13_MV"))
        self.pmt14 = QPushButton(" 14 ")
        self.pmt14.clicked.connect(lambda: self.action(self.hodo_name + "_14_MV"))
        self.pmt15 = QPushButton(" 15 ")
        self.pmt15.clicked.connect(lambda: self.action(self.hodo_name + "_15_MV"))
        self.pmt16 = QPushButton(" 16 ")
        self.pmt16.clicked.connect(lambda: self.action(self.hodo_name + "_16_MV"))
        self.pmt17 = QPushButton(" 17 ")
        self.pmt17.clicked.connect(lambda: self.action(self.hodo_name + "_17_MV"))
        self.pmt18 = QPushButton(" 18 ")
        self.pmt18.clicked.connect(lambda: self.action(self.hodo_name + "_18_MV"))
        self.pmt19 = QPushButton(" 19 ")
        self.pmt19.clicked.connect(lambda: self.action(self.hodo_name + "_19_MV"))
        self.pmt20 = QPushButton(" 20 ")
        self.pmt20.clicked.connect(lambda: self.action(self.hodo_name + "_20_MV"))

        # self.tab.layout.addWidget(self.Hits, 0, 0)
        # self.tab.layout.addWidget(self.Efficiency, 0, 1)
        self.tab.layout.addWidget(self.pmt1, 1, 0)
        self.tab.layout.addWidget(self.pmt2, 1, 1)
        self.tab.layout.addWidget(self.pmt3, 1, 2)
        self.tab.layout.addWidget(self.pmt4, 1, 3)
        self.tab.layout.addWidget(self.pmt5, 1, 4)
        self.tab.layout.addWidget(self.pmt6, 2, 0)
        self.tab.layout.addWidget(self.pmt7, 2, 1)
        self.tab.layout.addWidget(self.pmt8, 2, 2)
        self.tab.layout.addWidget(self.pmt9, 2, 3)
        self.tab.layout.addWidget(self.pmt10, 2, 4)
        self.tab.layout.addWidget(self.pmt11, 3, 0)
        self.tab.layout.addWidget(self.pmt12, 3, 1)
        self.tab.layout.addWidget(self.pmt13, 3, 2)
        self.tab.layout.addWidget(self.pmt14, 3, 3)
        self.tab.layout.addWidget(self.pmt15, 3, 4)
        self.tab.layout.addWidget(self.pmt16, 4, 0)
        self.tab.layout.addWidget(self.pmt17, 4, 1)
        self.tab.layout.addWidget(self.pmt18, 4, 2)
        self.tab.layout.addWidget(self.pmt19, 4, 3)
        self.tab.layout.addWidget(self.pmt20, 4, 4)

    @pyqtSlot()
    def action(self, name):
        # print(name)
        A = hodomon(name)
        A.display()


class pmt19(QWidget):
    def __init__(self, hodo_name):
        super(QWidget, self).__init__()
        self.hodo_name = hodo_name

        self.tab = QWidget()
        self.tab.layout = QGridLayout(self)

        # self.Hits = QPushButton(" Hits ")
        # self.Efficiency = QPushButton(" Efficiency ")

        self.pmt1 = QPushButton(" 1 ")
        self.pmt1.clicked.connect(lambda: self.action(self.hodo_name + "_1_MV"))
        self.pmt2 = QPushButton(" 2 ")
        self.pmt2.clicked.connect(lambda: self.action(self.hodo_name + "_2_MV"))
        self.pmt3 = QPushButton(" 3 ")
        self.pmt3.clicked.connect(lambda: self.action(self.hodo_name + "_3_MV"))
        self.pmt4 = QPushButton(" 4 ")
        self.pmt4.clicked.connect(lambda: self.action(self.hodo_name + "_4_MV"))
        self.pmt5 = QPushButton(" 5 ")
        self.pmt5.clicked.connect(lambda: self.action(self.hodo_name + "_5_MV"))
        self.pmt6 = QPushButton(" 6 ")
        self.pmt6.clicked.connect(lambda: self.action(self.hodo_name + "_6_MV"))
        self.pmt7 = QPushButton(" 7 ")
        self.pmt7.clicked.connect(lambda: self.action(self.hodo_name + "_7_MV"))
        self.pmt8 = QPushButton(" 8 ")
        self.pmt8.clicked.connect(lambda: self.action(self.hodo_name + "_8_MV"))
        self.pmt9 = QPushButton(" 9 ")
        self.pmt9.clicked.connect(lambda: self.action(self.hodo_name + "_9_MV"))
        self.pmt10 = QPushButton(" 10 ")
        self.pmt10.clicked.connect(lambda: self.action(self.hodo_name + "_10_MV"))
        self.pmt11 = QPushButton(" 11 ")
        self.pmt11.clicked.connect(lambda: self.action(self.hodo_name + "_11_MV"))
        self.pmt12 = QPushButton(" 12 ")
        self.pmt12.clicked.connect(lambda: self.action(self.hodo_name + "_12_MV"))
        self.pmt13 = QPushButton(" 13 ")
        self.pmt13.clicked.connect(lambda: self.action(self.hodo_name + "_13_MV"))
        self.pmt14 = QPushButton(" 14 ")
        self.pmt14.clicked.connect(lambda: self.action(self.hodo_name + "_14_MV"))
        self.pmt15 = QPushButton(" 15 ")
        self.pmt15.clicked.connect(lambda: self.action(self.hodo_name + "_15_MV"))
        self.pmt16 = QPushButton(" 16 ")
        self.pmt16.clicked.connect(lambda: self.action(self.hodo_name + "_16_MV"))
        self.pmt17 = QPushButton(" 17 ")
        self.pmt17.clicked.connect(lambda: self.action(self.hodo_name + "_17_MV"))
        self.pmt18 = QPushButton(" 18 ")
        self.pmt18.clicked.connect(lambda: self.action(self.hodo_name + "_18_MV"))
        self.pmt19 = QPushButton(" 19 ")
        self.pmt19.clicked.connect(lambda: self.action(self.hodo_name + "_19_MV"))

        # self.tab.layout.addWidget(self.Hits, 0, 0)
        # self.tab.layout.addWidget(self.Efficiency, 0, 1)
        self.tab.layout.addWidget(self.pmt1, 1, 0)
        self.tab.layout.addWidget(self.pmt2, 1, 1)
        self.tab.layout.addWidget(self.pmt3, 1, 2)
        self.tab.layout.addWidget(self.pmt4, 1, 3)
        self.tab.layout.addWidget(self.pmt5, 1, 4)
        self.tab.layout.addWidget(self.pmt6, 2, 0)
        self.tab.layout.addWidget(self.pmt7, 2, 1)
        self.tab.layout.addWidget(self.pmt8, 2, 2)
        self.tab.layout.addWidget(self.pmt9, 2, 3)
        self.tab.layout.addWidget(self.pmt10, 2, 4)
        self.tab.layout.addWidget(self.pmt11, 3, 0)
        self.tab.layout.addWidget(self.pmt12, 3, 1)
        self.tab.layout.addWidget(self.pmt13, 3, 2)
        self.tab.layout.addWidget(self.pmt14, 3, 3)
        self.tab.layout.addWidget(self.pmt15, 3, 4)
        self.tab.layout.addWidget(self.pmt16, 4, 0)
        self.tab.layout.addWidget(self.pmt17, 4, 1)
        self.tab.layout.addWidget(self.pmt18, 4, 2)
        self.tab.layout.addWidget(self.pmt19, 4, 3)


    @pyqtSlot()
    def action(self, name):
        # print(name)
        A = hodomon(name)
        A.display()

class pmt16(QWidget):
    def __init__(self, hodo_name):
        super(QWidget, self).__init__()
        self.hodo_name = hodo_name

        self.tab = QWidget()
        self.tab.layout = QGridLayout(self)

        # self.Hits = QPushButton(" Hits ")
        # self.Efficiency = QPushButton(" Efficiency ")

        self.pmt1 = QPushButton(" 1 ")
        self.pmt1.clicked.connect(lambda: self.action(self.hodo_name + "_1_MV"))
        self.pmt2 = QPushButton(" 2 ")
        self.pmt2.clicked.connect(lambda: self.action(self.hodo_name + "_2_MV"))
        self.pmt3 = QPushButton(" 3 ")
        self.pmt3.clicked.connect(lambda: self.action(self.hodo_name + "_3_MV"))
        self.pmt4 = QPushButton(" 4 ")
        self.pmt4.clicked.connect(lambda: self.action(self.hodo_name + "_4_MV"))
        self.pmt5 = QPushButton(" 5 ")
        self.pmt5.clicked.connect(lambda: self.action(self.hodo_name + "_5_MV"))
        self.pmt6 = QPushButton(" 6 ")
        self.pmt6.clicked.connect(lambda: self.action(self.hodo_name + "_6_MV"))
        self.pmt7 = QPushButton(" 7 ")
        self.pmt7.clicked.connect(lambda: self.action(self.hodo_name + "_7_MV"))
        self.pmt8 = QPushButton(" 8 ")
        self.pmt8.clicked.connect(lambda: self.action(self.hodo_name + "_8_MV"))
        self.pmt9 = QPushButton(" 9 ")
        self.pmt9.clicked.connect(lambda: self.action(self.hodo_name + "_9_MV"))
        self.pmt10 = QPushButton(" 10 ")
        self.pmt10.clicked.connect(lambda: self.action(self.hodo_name + "_10_MV"))
        self.pmt11 = QPushButton(" 11 ")
        self.pmt11.clicked.connect(lambda: self.action(self.hodo_name + "_11_MV"))
        self.pmt12 = QPushButton(" 12 ")
        self.pmt12.clicked.connect(lambda: self.action(self.hodo_name + "_12_MV"))
        self.pmt13 = QPushButton(" 13 ")
        self.pmt13.clicked.connect(lambda: self.action(self.hodo_name + "_13_MV"))
        self.pmt14 = QPushButton(" 14 ")
        self.pmt14.clicked.connect(lambda: self.action(self.hodo_name + "_14_MV"))
        self.pmt15 = QPushButton(" 15 ")
        self.pmt15.clicked.connect(lambda: self.action(self.hodo_name + "_15_MV"))
        self.pmt16 = QPushButton(" 16 ")
        self.pmt16.clicked.connect(lambda: self.action(self.hodo_name + "_16_MV"))

        # self.tab.layout.addWidget(self.Hits, 0, 0)
        # self.tab.layout.addWidget(self.Efficiency, 0, 1)
        self.tab.layout.addWidget(self.pmt1, 1, 0)
        self.tab.layout.addWidget(self.pmt2, 1, 1)
        self.tab.layout.addWidget(self.pmt3, 1, 2)
        self.tab.layout.addWidget(self.pmt4, 1, 3)
        self.tab.layout.addWidget(self.pmt5, 1, 4)
        self.tab.layout.addWidget(self.pmt6, 2, 0)
        self.tab.layout.addWidget(self.pmt7, 2, 1)
        self.tab.layout.addWidget(self.pmt8, 2, 2)
        self.tab.layout.addWidget(self.pmt9, 2, 3)
        self.tab.layout.addWidget(self.pmt10, 2, 4)
        self.tab.layout.addWidget(self.pmt11, 3, 0)
        self.tab.layout.addWidget(self.pmt12, 3, 1)
        self.tab.layout.addWidget(self.pmt13, 3, 2)
        self.tab.layout.addWidget(self.pmt14, 3, 3)
        self.tab.layout.addWidget(self.pmt15, 3, 4)
        self.tab.layout.addWidget(self.pmt16, 4, 0)

    @pyqtSlot()
    def action(self, name):
        # print(name)
        A = hodomon(name)
        A.display()


class expert(QWidget):
    def __init__(self, hodo_name):
        super(QWidget, self).__init__()
        self.hodo_name = hodo_name

        self.tab = QWidget()
        self.tab.layout = QGridLayout(self)

        self.on_button = QPushButton(" ON ")
        self.on_button.clicked.connect(lambda: self.on_key(self.hodo_name))

        self.off_button = QPushButton(" OFF ")
        self.off_button.clicked.connect(lambda: self.off_key(self.hodo_name))

        self.set_nominal_button = QPushButton(" SET-NOMINAL ")
        self.set_nominal_button.clicked.connect(lambda: self.set_nominal_key(self.hodo_name))

        self.status_button = QPushButton(" STATUS ")
        self.status_button.clicked.connect(lambda: self.status_key(self.hodo_name))

        self.monitor_button = QPushButton(" MONITOR ")
        self.monitor_button.clicked.connect(lambda: self.monitor_key(self.hodo_name))

        self.tab.layout.addWidget(self.on_button, 0, 0)
        self.tab.layout.addWidget(self.off_button, 0, 1)
        self.tab.layout.addWidget(self.set_nominal_button, 0, 2)
        self.tab.layout.addWidget(self.status_button, 1, 0)
        self.tab.layout.addWidget(self.monitor_button, 1, 1)

    @pyqtSlot()
    def on_key(self, name):
        os.system("cd /data2/e1039/daq/slowcontrols/lecroy/hv/ && ./on " + name)
        # os.system("./on " + name)
        # os.system("cd -")

    @pyqtSlot()
    def off_key(self, name):
        os.system("cd /data2/e1039/daq/slowcontrols/lecroy/hv/ && ./off " + name)
        # os.system("./off " + name)
        # os.system("cd -")

    @pyqtSlot()
    def set_nominal_key(self, name):
        os.system("cd /data2/e1039/daq/slowcontrols/lecroy/hv/ && ./set-nominal " + name)
        # os.system("./set-nominal " + name)
        # os.system("cd -")

    @pyqtSlot()
    def status_key(self, name):
        os.system("cd /data2/e1039/daq/slowcontrols/lecroy/hv/ && ./status " + name)
        # os.system("./satus " + name)
        # os.system("cd -")

    @pyqtSlot()
    def monitor_key(self, name):
        os.system("cd /data2/e1039/daq/slowcontrols/lecroy/hv/ && ./monitor " + name)
        # os.system("./monitor " + name)
        # os.system("cd -")


class voltage(QWidget):
    def __init__(self):
        super(QWidget, self).__init__()
        self.tab = QWidget()
        self.tab.layout = QGridLayout(self)

        self.voltage_button = QPushButton(" VOLTAGE ")
        self.voltage_button.clicked.connect(lambda: self.voltage_key())
        self.tab.layout.addWidget(self.voltage_button, 0, 0)

    @pyqtSlot()
    def voltage_key(self):
        os.system("cd /data2/e1039/daq/slowcontrols/lecroy/hv/ && wish hodomon.tcl &")
        # os.system("wish hodomon.tcl & ")
        # os.system("cd -")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())