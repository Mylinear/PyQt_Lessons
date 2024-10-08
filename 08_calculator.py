# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calculator.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

g_value = 0 # when we push the sign button it assigns the value to g_value
e_value = 0 # when we push the equal button it assigns the value to e_value
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(361, 608)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label1 = QtWidgets.QLabel(self.centralwidget)
        self.label1.setGeometry(QtCore.QRect(10, 10, 341, 91))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.label1.setFont(font)
        self.label1.setFrameShape(QtWidgets.QFrame.Box)
        self.label1.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label1.setLineWidth(3)
        self.label1.setTextFormat(QtCore.Qt.MarkdownText)
        self.label1.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label1.setObjectName("label1")
        self.button_percent = QtWidgets.QPushButton(self.centralwidget,clicked = lambda : self.press('%'))
        self.button_percent.setGeometry(QtCore.QRect(13, 110, 80, 80))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.button_percent.setFont(font)
        self.button_percent.setObjectName("button_percent")
        self.button_c = QtWidgets.QPushButton(self.centralwidget,clicked = lambda : self.press('C'))
        self.button_c.setGeometry(QtCore.QRect(98, 110, 80, 80))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.button_c.setFont(font)
        self.button_c.setObjectName("button_c")
        self.arrow_button = QtWidgets.QPushButton(self.centralwidget,clicked = lambda : self.farrow())
        self.arrow_button.setGeometry(QtCore.QRect(183, 110, 80, 80))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.arrow_button.setFont(font)
        self.arrow_button.setObjectName("arrow_button")
        self.divide_button = QtWidgets.QPushButton(self.centralwidget,clicked = lambda : self.fsign('/'))
        self.divide_button.setGeometry(QtCore.QRect(268, 110, 80, 80))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.divide_button.setFont(font)
        self.divide_button.setObjectName("divide_button")
        self.button_9 = QtWidgets.QPushButton(self.centralwidget,clicked = lambda : self.fnumbers('9'))
        self.button_9.setGeometry(QtCore.QRect(180, 200, 80, 80))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.button_9.setFont(font)
        self.button_9.setObjectName("button_9")
        self.button_x = QtWidgets.QPushButton(self.centralwidget,clicked = lambda : self.fsign('X'))
        self.button_x.setGeometry(QtCore.QRect(265, 200, 80, 80))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.button_x.setFont(font)
        self.button_x.setObjectName("button_x")
        self.button_8 = QtWidgets.QPushButton(self.centralwidget,clicked = lambda : self.fnumbers('8'))
        self.button_8.setGeometry(QtCore.QRect(95, 200, 80, 80))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.button_8.setFont(font)
        self.button_8.setObjectName("button_8")
        self.button_7 = QtWidgets.QPushButton(self.centralwidget,clicked = lambda : self.fnumbers('7'))
        self.button_7.setGeometry(QtCore.QRect(10, 200, 80, 80))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.button_7.setFont(font)
        self.button_7.setObjectName("button_7")
        self.button_6 = QtWidgets.QPushButton(self.centralwidget,clicked = lambda : self.fnumbers('6'))
        self.button_6.setGeometry(QtCore.QRect(180, 290, 80, 80))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.button_6.setFont(font)
        self.button_6.setObjectName("button_6")
        self.button_minus = QtWidgets.QPushButton(self.centralwidget,clicked = lambda : self.fsign('-'))
        self.button_minus.setGeometry(QtCore.QRect(265, 290, 80, 80))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.button_minus.setFont(font)
        self.button_minus.setObjectName("button_minus")
        self.button_5 = QtWidgets.QPushButton(self.centralwidget,clicked = lambda : self.fnumbers('5'))
        self.button_5.setGeometry(QtCore.QRect(95, 290, 80, 80))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.button_5.setFont(font)
        self.button_5.setObjectName("button_5")
        self.button_4 = QtWidgets.QPushButton(self.centralwidget,clicked = lambda : self.fnumbers('4'))
        self.button_4.setGeometry(QtCore.QRect(10, 290, 80, 80))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.button_4.setFont(font)
        self.button_4.setObjectName("button_4")
        self.button_3 = QtWidgets.QPushButton(self.centralwidget,clicked = lambda : self.fnumbers('3'))
        self.button_3.setGeometry(QtCore.QRect(180, 380, 80, 80))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.button_3.setFont(font)
        self.button_3.setObjectName("button_3")
        self.button_plus = QtWidgets.QPushButton(self.centralwidget,clicked = lambda : self.fsign('+'))
        self.button_plus.setGeometry(QtCore.QRect(265, 380, 80, 80))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.button_plus.setFont(font)
        self.button_plus.setObjectName("button_plus")
        self.button_2 = QtWidgets.QPushButton(self.centralwidget,clicked = lambda : self.fnumbers('2'))
        self.button_2.setGeometry(QtCore.QRect(95, 380, 80, 80))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.button_2.setFont(font)
        self.button_2.setObjectName("button_2")
        self.button_1 = QtWidgets.QPushButton(self.centralwidget,clicked = lambda : self.fnumbers('1'))
        self.button_1.setGeometry(QtCore.QRect(10, 380, 80, 80))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.button_1.setFont(font)
        self.button_1.setObjectName("button_1")
        self.button_dot = QtWidgets.QPushButton(self.centralwidget,clicked = lambda : self.fdot())
        self.button_dot.setGeometry(QtCore.QRect(180, 470, 80, 80))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.button_dot.setFont(font)
        self.button_dot.setObjectName("button_dot")
        self.button_equal = QtWidgets.QPushButton(self.centralwidget,clicked = lambda : self.fequal())
        self.button_equal.setGeometry(QtCore.QRect(265, 470, 80, 80))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.button_equal.setFont(font)
        self.button_equal.setObjectName("button_equal")
        self.button_0 = QtWidgets.QPushButton(self.centralwidget,clicked = lambda : self.fnumbers('0'))
        self.button_0.setGeometry(QtCore.QRect(95, 470, 80, 80))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.button_0.setFont(font)
        self.button_0.setObjectName("button_0")
        self.button_plus_minus = QtWidgets.QPushButton(self.centralwidget,clicked = lambda : self.fplus_minus())
        self.button_plus_minus.setGeometry(QtCore.QRect(10, 470, 80, 80))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.button_plus_minus.setFont(font)
        self.button_plus_minus.setObjectName("button_plus_minus")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 361, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Calculator"))
        self.label1.setText(_translate("MainWindow", "0"))
        self.button_percent.setText(_translate("MainWindow", "%"))
        self.button_c.setText(_translate("MainWindow", "C"))
        self.arrow_button.setText(_translate("MainWindow", "<<"))
        self.divide_button.setText(_translate("MainWindow", "/"))
        self.button_9.setText(_translate("MainWindow", "9"))
        self.button_x.setText(_translate("MainWindow", "x"))
        self.button_8.setText(_translate("MainWindow", "8"))
        self.button_7.setText(_translate("MainWindow", "7"))
        self.button_6.setText(_translate("MainWindow", "6"))
        self.button_minus.setText(_translate("MainWindow", "-"))
        self.button_5.setText(_translate("MainWindow", "5"))
        self.button_4.setText(_translate("MainWindow", "4"))
        self.button_3.setText(_translate("MainWindow", "3"))
        self.button_plus.setText(_translate("MainWindow", "+"))
        self.button_2.setText(_translate("MainWindow", "2"))
        self.button_1.setText(_translate("MainWindow", "1"))
        self.button_dot.setText(_translate("MainWindow", "."))
        self.button_equal.setText(_translate("MainWindow", "="))
        self.button_0.setText(_translate("MainWindow", "0"))
        self.button_plus_minus.setText(_translate("MainWindow", "+/-"))
   
    def fnumbers(self,pressed):
        global e_value
        
        screen = self.label1.text()
        if screen == '0' or e_value != 0:
            self.label1.setText(pressed)
            e_value = 0
        else:
            self.label1.setText(self.label1.text() + pressed)
    
    def fdot(self):
        if '.' not in self.label1.text():
            self.label1.setText(self.label1.text() + '.')
        else:
            pass
    
    def farrow(self):
        screen = self.label1.text()
        self.label1.setText(screen[:-1])
        
    def fplus_minus(self):
        screen = self.label1.text()
        if screen[0] =='-':
            self.label1.setText(screen[1:])
        else:
            self.label1.setText('-' + screen)
    def fsign(self,sign):
        global g_value ,  g_sign
        g_sign = sign
        g_value = self.label1.text()
        self.label1.setText('')
    
    def fequal(self):
        global g_value ,  g_sign, e_value
        screen = self.label1.text()
        result = eval(g_value + g_sign + screen)
        self.label1.setText(str(result))
        e_value = result
        
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
