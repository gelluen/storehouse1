import sys
from PyQt5 import QtWidgets
from untitled import Ui_MainWindow
import tkinter.messagebox
a=''


class mywindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def btn1(self):
        sender = self.sender()
        self.getButtonExp(sender.objectName())

    def getButtonExp(self, string: str):
        global a
        tempindex = string.index('_')
        tempText = string[tempindex + 1:]
        if tempText != 'AC' and tempText != 'del':
            self.lcdNumber.display(tempText)
        else:
            return
        if tempText == '=':
            try:
                self.lcdNumber.display(eval(a))
            except ZeroDivisionError and SyntaxError:
                self.lcdNumber.display('Error')

            a = ''
            self.repaint()
            return
        if tempText == 'AC':
            self.lcdNumber.display('0')
            self.repaint()
            return
        a += tempText

        self.lcdNumber.repaint()
 

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = mywindow()
    window.show()
    sys.exit(app.exec_())
