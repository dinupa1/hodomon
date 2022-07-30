#!/usr/bin/python3

#
# GUI for hodoscope monitoring
#


import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QWidget
# from functools import partial
from hodomon import hodomon


class Window(QMainWindow):
  def __init__(self):
    super().__init__()
    
    self.window = QWidget()
    self.window.setWindowTitle('HodoMon')
    self.layout = QGridLayout()
    
#     self.hodo_names = ['H1YR', 'H1YL', 'H1XT', 'H1XB', 'H2XB', 'H2XT', 'H2YL', 'H2YR', 'H3XB', 'H3XT', 'H4Y1L-l', 'H4Y1L-r', 'H4Y1R-l', 'H4Y1R-r', 'H4Y2L-l', 'H4Y2L-r', 'H4Y2R-l', 'H4Y2R-r', 'H4XB-d', 'H4XB-u', 'H4XT-d', 'H4XT-u']
    
#     # PMT no.
#     self.pmt = []
#     self.hodo_button = []
    
    # hodoscope buttons
    self.hodo0 = QPushButton('H1YR')
    self.hodo0.clicked.connect(self.action0)
    self.layout.addWidget(self.hodo0, 0, 0)
    
    self.hodo1 = QPushButton('H1YL')
    self.hodo1.clicked.connect(self.action1)
    self.layout.addWidget(self.hodo1, 1, 0)
    
    self.hodo2 = QPushButton('H1XT')
    self.hodo2.clicked.connect(self.action2)
    self.layout.addWidget(self.hodo2, 2, 0)
    
    self.hodo3 = QPushButton('H1XB')
    self.hodo3.clicked.connect(self.action3)
    self.layout.addWidget(self.hodo3, 3, 0)
    
    self.hodo4 = QPushButton('H2XB')
    self.hodo4.clicked.connect(self.action4)
    self.layout.addWidget(self.hodo4, 4, 0)
    
    self.hodo5 = QPushButton('H2XT')
    self.hodo5.clicked.connect(self.action5)
    self.layout.addWidget(self.hodo5, 5, 0)
    
    self.hodo6 = QPushButton('H2YL')
    self.hodo6.clicked.connect(self.action6)
    self.layout.addWidget(self.hodo6, 6, 0)
    
    self.hodo7 = QPushButton('H2YR')
    self.hodo7.clicked.connect(self.action7)
    self.layout.addWidget(self.hodo7, 7, 0)
    
    self.hodo8 = QPushButton('H3XB')
    self.hodo8.clicked.connect(self.action8)
    self.layout.addWidget(self.hodo8, 8, 0)
    
    self.hodo9 = QPushButton('H3XT')
    self.hodo9.clicked.connect(self.action9)
    self.layout.addWidget(self.hodo9, 9, 0)
    
    self.hodo10 = QPushButton('H4Y1L-l')
    self.hodo10.clicked.connect(self.action10)
    self.layout.addWidget(self.hodo10, 10, 0)
    
    self.hodo11 = QPushButton('H4Y1L-r')
    self.hodo11.clicked.connect(self.action11)
    self.layout.addWidget(self.hodo11, 11, 0)
    
    self.hodo12 = QPushButton('H4Y1R-l')
    self.hodo12.clicked.connect(self.action12)
    self.layout.addWidget(self.hodo12, 12, 0)
    
    self.hodo13 = QPushButton('H4Y1R-r')
    self.hodo13.clicked.connect(self.action13)
    self.layout.addWidget(self.hodo13, 13, 0)
    
    self.hodo14 = QPushButton('H4Y2L-l')
    self.hodo14.clicked.connect(self.action14)
    self.layout.addWidget(self.hodo14, 14, 0)
    
    self.hodo15 = QPushButton('H4Y2L-r')
    self.hodo15.clicked.connect(self.action15)
    self.layout.addWidget(self.hodo15, 15, 0)
    
    self.hodo16 = QPushButton('H4Y2R-l')
    self.hodo16.clicked.connect(self.action16)
    self.layout.addWidget(self.hodo16, 16, 0)
    
    self.hodo17 = QPushButton('H4Y2R-r')
    self.hodo17.clicked.connect(self.action17)
    self.layout.addWidget(self.hodo17, 17, 0)
    
    self.hodo18 = QPushButton('H4XB-d')
    self.hodo18.clicked.connect(self.action18)
    self.layout.addWidget(self.hodo18, 18, 0)
    
    self.hodo19 = QPushButton('H4XB-u')
    self.hodo19.clicked.connect(self.action19)
    self.layout.addWidget(self.hodo19, 19, 0)
    
    self.hodo20 = QPushButton('H4XT-d')
    self.hodo20.clicked.connect(self.action20)
    self.layout.addWidget(self.hodo20, 20, 0)
    
    self.hodo21 = QPushButton('H4XT-u')
    self.hodo21.clicked.connect(self.action21)
    self.layout.addWidget(self.hodo21, 21, 0)
    
    # PMT buttons
    self.pmt1 = QPushButton('1')
    self.pmt1.clicked.connect(self.plot1)
    self.layout.addWidget(self.pmt1, 0, 1)
    
    self.pmt2 = QPushButton('2')
    self.pmt2.clicked.connect(self.plot2)
    self.layout.addWidget(self.pmt2, 1, 1)
    
    self.pmt3 = QPushButton('3')
    self.pmt3.clicked.connect(self.plot3)
    self.layout.addWidget(self.pmt3, 2, 1)
    
    self.pmt4 = QPushButton('4')
    self.pmt4.clicked.connect(self.plot4)
    self.layout.addWidget(self.pmt4, 3, 1)
    
    self.pmt5 = QPushButton('5')
    self.pmt5.clicked.connect(self.plot5)
    self.layout.addWidget(self.pmt5, 4, 1)
    
    self.pmt6 = QPushButton('6')
    self.pmt6.clicked.connect(self.plot6)
    self.layout.addWidget(self.pmt6, 5, 1)
    
    self.pmt7 = QPushButton('7')
    self.pmt7.clicked.connect(self.plot7)
    self.layout.addWidget(self.pmt7, 6, 1)
    
    self.pmt8 = QPushButton('8')
    self.pmt8.clicked.connect(self.plot8)
    self.layout.addWidget(self.pmt8, 7, 1)
    
    self.pmt9 = QPushButton('9')
    self.pmt9.clicked.connect(self.plot9)
    self.layout.addWidget(self.pmt9, 8, 1)
    
    self.pmt10 = QPushButton('10')
    self.pmt10.clicked.connect(self.plot10)
    self.layout.addWidget(self.pmt10, 9, 1)
    
    self.pmt11 = QPushButton('11')
    self.pmt11.clicked.connect(self.plot11)
    self.layout.addWidget(self.pmt11, 10, 1)
    
    self.pmt12 = QPushButton('12')
    self.pmt12.clicked.connect(self.plot12)
    self.layout.addWidget(self.pmt12, 11, 1)
    
    self.pmt13 = QPushButton('13')
    self.pmt13.clicked.connect(self.plot13)
    self.layout.addWidget(self.pmt13, 12, 1)
    
    self.pmt14 = QPushButton('14')
    self.pmt14.clicked.connect(self.plot14)
    self.layout.addWidget(self.pmt14, 13, 1)
    
    self.pmt15 = QPushButton('15')
    self.pmt15.clicked.connect(self.plot15)
    self.layout.addWidget(self.pmt15, 14, 1)
    
    self.pmt16 = QPushButton('16')
    self.pmt16.clicked.connect(self.plot16)
    self.layout.addWidget(self.pmt16, 15, 1)
    
    self.pmt17 = QPushButton('17')
    self.pmt17.clicked.connect(self.plot17)
    self.layout.addWidget(self.pmt17, 16, 1)
    
    self.pmt18 = QPushButton('18')
    self.pmt18.clicked.connect(self.plot18)
    self.layout.addWidget(self.pmt18, 17, 1)
    
    self.pmt19 = QPushButton('19')
    self.pmt19.clicked.connect(self.plot19)
    self.layout.addWidget(self.pmt19, 18, 1)
    
    self.pmt20 = QPushButton('20')
    self.pmt20.clicked.connect(self.plot20)
    self.layout.addWidget(self.pmt20, 19, 1)
    
    # for i in range(0, 20):
    #   self.pmt.append(str(i+1))
    
    # # hodoscope planes
    # for i in range(0, 22):
    #   self.hodo_button.append(QPushButton(self.hodo_names[i]))
    #   self.hodo_button[i].clicked.connect(self.show)
    #   self.layout.addWidget(self.hodo_button[i], i, 0)
    
    # for i in range(0, 20):
    #   pmt_button = QPushButton(self.pmt[i])
    #   self.layout.addWidget(pmt_button, i, 1)
    
    msg = QLabel('')
    self.layout.addWidget(msg)
    
    self.window.setLayout(self.layout)
    self.window.show()
  
  # hodo button actions
  def action0(self):
    self.hodo_name = self.hodo0.text() + "_"
    
  def action1(self):
    self.hodo_name = self.hodo1.text() + "_"
    
  def action2(self):
    self.hodo_name = self.hodo2.text() + "_"
    
  def action3(self):
    self.hodo_name = self.hodo3.text() + "_"
  
  def action4(self):
    self.hodo_name = self.hodo4.text() + "_"
  
  def action5(self):
    self.hodo_name = self.hodo5.text() + "_"
  
  def action6(self):
    self.hodo_name = self.hodo6.text() + "_"
  
  def action7(self):
    self.hodo_name = self.hodo7.text() + "_"
  
  def action8(self):
    self.hodo_name = self.hodo8.text() + "_"
  
  def action9(self):
    self.hodo_name = self.hodo9.text() + "_"
  
  def action10(self):
    self.hodo_name = self.hodo10.text() + "_"
  
  def action11(self):
    self.hodo_name = self.hodo11.text() + "_"
  
  def action12(self):
    self.hodo_name = self.hodo12.text() + "_"
  
  def action13(self):
    self.hodo_name = self.hodo13.text() + "_"
  
  def action14(self):
    self.hodo_name = self.hodo14.text() + "_"
  
  def action15(self):
    self.hodo_name = self.hodo15.text() + "_"
  
  def action16(self):
    self.hodo_name = self.hodo16.text() + "_"
  
  def action17(self):
    self.hodo_name = self.hodo17.text() + "_"
  
  def action18(self):
    self.hodo_name = self.hodo18.text() + "_"
  
  def action19(self):
    self.hodo_name = self.hodo19.text() + "_"
    
  def action20(self):
    self.hodo_name = self.hodo20.text() + "_"
  
  def action21(self):
    self.hodo_name = self.hodo21.text() + "_"
    
  
  # get plots
  def plot1(self):
    pmt_name = self.hodo_name + self.pmt1.text() + "_MV"
    # print(pmt_name)
    A = hodomon(pmt_name)
    A.display()
  
  def plot2(self):
    pmt_name = self.hodo_name + self.pmt2.text() + "_MV"
    # print(pmt_name)
    A = hodomon(pmt_name)
    A.display()
    
  def plot3(self):
    pmt_name = self.hodo_name + self.pmt3.text() + "_MV"
    # print(pmt_name)
    A = hodomon(pmt_name)
    A.display()
  
  def plot4(self):
    pmt_name = self.hodo_name + self.pmt4.text() + "_MV"
    # print(pmt_name)
    A = hodomon(pmt_name)
    A.display()
  
  def plot5(self):
    pmt_name = self.hodo_name + self.pmt5.text() + "_MV"
    # print(pmt_name)
    A = hodomon(pmt_name)
    A.display()
  
  def plot6(self):
    pmt_name = self.hodo_name + self.pmt6.text() + "_MV"
    # print(pmt_name)
    A = hodomon(pmt_name)
    A.display()
  
  def plot7(self):
    pmt_name = self.hodo_name + self.pmt7.text() + "_MV"
    # print(pmt_name)
    A = hodomon(pmt_name)
    A.display()
  
  def plot8(self):
    pmt_name = self.hodo_name + self.pmt8.text() + "_MV"
    # print(pmt_name)
    A = hodomon(pmt_name)
    A.display()
  
  def plot9(self):
    pmt_name = self.hodo_name + self.pmt9.text() + "_MV"
    # print(pmt_name)
    A = hodomon(pmt_name)
    A.display()
  
  def plot10(self):
    pmt_name = self.hodo_name + self.pmt10.text() + "_MV"
    # print(pmt_name)
    A = hodomon(pmt_name)
    A.display()
  
  def plot11(self):
    pmt_name = self.hodo_name + self.pmt11.text() + "_MV"
    # print(pmt_name)
    A = hodomon(pmt_name)
    A.display()
  
  def plot12(self):
    pmt_name = self.hodo_name + self.pmt12.text() + "_MV"
    # print(pmt_name)
    A = hodomon(pmt_name)
    A.display()
  
  def plot13(self):
    pmt_name = self.hodo_name + self.pmt13.text() + "_MV"
    # print(pmt_name)
    A = hodomon(pmt_name)
    A.display()
  
  def plot14(self):
    pmt_name = self.hodo_name + self.pmt14.text() + "_MV"
    # print(pmt_name)
    A = hodomon(pmt_name)
    A.display()
  
  def plot15(self):
    pmt_name = self.hodo_name + self.pmt15.text() + "_MV"
    # print(pmt_name)
    A = hodomon(pmt_name)
    A.display()
  
  def plot16(self):
    pmt_name = self.hodo_name + self.pmt16.text() + "_MV"
    # print(pmt_name)
    A = hodomon(pmt_name)
    A.display()
  
  def plot17(self):
    pmt_name = self.hodo_name + self.pmt17.text() + "_MV"
    # print(pmt_name)
    A = hodomon(pmt_name)
    A.display()
    
  def plot18(self):
    pmt_name = self.hodo_name + self.pmt18.text() + "_MV"
    # print(pmt_name)
    A = hodomon(pmt_name)
    A.display()
  
  def plot19(self):
    pmt_name = self.hodo_name + self.pmt19.text() + "_MV"
    # print(pmt_name)
    A = hodomon(pmt_name)
    A.display()
  
  def plot20(self):
    pmt_name = self.hodo_name + self.pmt20.text() + "_MV"
    # print(pmt_name)
    A = hodomon(pmt_name)
    A.display()
                   
app = QApplication(sys.argv)
window = Window()
sys.exit(app.exec())