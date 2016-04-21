#!/usr/bin/python
# _*_ coding:utf-8 _*_

import sys

from PyQt4.QtGui import *
from PyQt4.QtCore import *

class CalcUI(QMainWindow):

    DEBUG = False
    bufCal = ""
    bufNum = 0

    mX      = [40,   40, 90, 140,   40, 90, 140,   40, 90, 140, 190, 190, 190, 190, 240, 240, 240]
    mY      = [260,  200, 200, 200, 140, 140, 140, 80, 80, 80,  260, 200, 140, 80,  200, 140, 80] 
    sWidth  = [140,  40, 40, 40,    40, 40, 40,    40, 40, 40,  40, 40, 40, 40,     40, 40, 40]
    sHeight = [40,   40, 40, 40,    40, 40, 40,    40, 40, 40,  40, 40, 40, 40,     100, 40, 40]

    def btn_ClickedCal(self):

        btn = self.sender()
        text = self.textbox.text()
        text1 = self.label.text()
        btnText = btn.text()

        if self.DEBUG:
            print text + ":" + btnText + ":" + text1 + ":" + self.bufCal

        if btnText == "C":
            text = text[:-1]
            self.textbox.setText(text)
            return
        elif btnText == "AC":
            self.textbox.clear()
            self.label.setText("")
            return

        if btnText == "=":
            if self.DEBUG:
                print "1"
            btnText = self.bufCal
        else: 
            if self.DEBUG:
                print "2"
            tmp = self.bufCal
            self.bufCal = btnText
            btnText = tmp


        if self.label.text() == "":
            if self.DEBUG:
                print "3"
            self.label.setText(text)
            self.textbox.clear()
            return
        
        if text == "":
            if self.DEBUG:
                print "4"
            return

        if self.DEBUG:
            print "5"

        tmp1 = int(self.label.text())
        tmp2 = int(text)

        
        if self.DEBUG:
            print text + ":" + btnText + ":" + text1

        if btnText == "+":
            self.bufNum = tmp1 + tmp2
        elif btnText == "-":
            self.bufNum = tmp1 - tmp2
        elif btnText == "*":
            self.bufNum = tmp1 * tmp2
        elif btnText == "/":
            self.bufNum = tmp1 / tmp2
        else:
            pass

        if self.DEBUG:
            print "sum:" + str(self.bufNum)

        if btn.text() == "=":
            if self.DEBUG:
                print "6"
            self.textbox.setText(str(self.bufNum))
            self.label.setText("")
            self.bufCal = ""
        else:
            if self.DEBUG:
                print "7"
            self.textbox.clear()
            self.label.setText(str(self.bufNum))

        if self.DEBUG:
            print self.bufCal + ":" + btnText


    def btn_Clicked(self):

        btn = self.sender()
        text = self.textbox.text()

        self.textbox.setText(text + btn.text())
        
        if self.DEBUG:
            print self.bufCal


    def __init__(self):
        super(CalcUI, self).__init__()
        self.initUI()


    def createButton(self, btn, i):
        btn.move(self.mX[i], self.mY[i])
        btn.resize(self.sWidth[i], self.sHeight[i])
        if i < 10:
            btn.clicked.connect(self.btn_Clicked)
        else:
            btn.clicked.connect(self.btn_ClickedCal)


    def initUI(self):
        self.setGeometry(300, 300, 330, 350)
        self.setWindowTitle("Calculator")
        
        self.label = QLabel("", self)
        self.label.move(40, 5)
        self.label.resize(245, 20)
        self.textbox = QLineEdit(self)
        self.textbox.move(40, 35)
        self.textbox.resize(245, 40)

        self.btn0 = QPushButton("0", self)
        self.createButton(self.btn0 , 0)
        self.btn1 = QPushButton("1", self)
        self.createButton(self.btn1 , 1)
        self.btn2 = QPushButton("2", self)
        self.createButton(self.btn2 , 2)
        self.btn3 = QPushButton("3", self)
        self.createButton(self.btn3 , 3)
        self.btn4 = QPushButton("4", self)
        self.createButton(self.btn4 , 4)
        self.btn5 = QPushButton("5", self)
        self.createButton(self.btn5 , 5)
        self.btn6 = QPushButton("6", self)
        self.createButton(self.btn6 , 6)
        self.btn7 = QPushButton("7", self)
        self.createButton(self.btn7 , 7)
        self.btn8 = QPushButton("8", self)
        self.createButton(self.btn8 , 8)
        self.btn9 = QPushButton("9", self)
        self.createButton(self.btn9 , 9)


        self.btn10 = QPushButton("+", self)
        self.createButton(self.btn10 , 10)
        self.btn11 = QPushButton("-", self)
        self.createButton(self.btn11 , 11)
        self.btn12 = QPushButton("*", self)
        self.createButton(self.btn12 , 12)
        self.btn13 = QPushButton("/", self)

        self.createButton(self.btn13 , 13)
        self.btn14 = QPushButton("=", self)
        self.createButton(self.btn14 , 14)
        self.btn15 = QPushButton("C", self)
        self.createButton(self.btn15 , 15)
        self.btn16 = QPushButton("AC", self)
        self.createButton(self.btn16 , 16)

        self.show()

def main():

    app = QApplication(sys.argv)
    cl = CalcUI()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()


