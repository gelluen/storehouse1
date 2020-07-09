import random
import sys
from tkinter import messagebox, Tk
from PyQt5 import QtWidgets
from UI import Ui_MainWindow

root = Tk()
root.withdraw()
ts = messagebox.showwarning('警告', '如果出现卡顿，那是电脑在计算，不满意可强制退出')
if not ts:
    exit(0)


class window(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.checkBox_2.setChecked(True)

    def ct(self):
        global srk1, srk2
        self.textBrowser.clear()
        self.textBrowser.append('**********出题中**********')
        try:
            srk1 = int(self.lineEdit_3.text())
            srk2 = int(self.lineEdit_4.text())
        except ValueError:
            messagebox.showwarning('警告', '不可以输入字符')
        xz1 = self.checkBox.isChecked()
        if xz1:
            ysf = ['+', '-', '*', '/', '^', '√']
        else:
            ysf = ['+', '-', '*', '/']
        for i in range(1, srk1 + 1):
            ysfh = str(random.choice(ysf))
            sz2 = random.randint(1, srk2)
            if ysfh == '/':
                sz1 = random.randint(sz2 + 1, srk2 + 2)
            else:
                sz1 = random.randint(1, srk2)

            ss = str(sz1) + str(ysfh) + str(sz2)

            if xz1:
                if ysfh == '^':
                    if self.checkBox_2.isChecked():
                        self.textBrowser.append(str(ss + '=' + str(sz1 ** sz2)))
                        continue
                    else:
                        self.textBrowser.append(str(ss))
                        continue
                if ysfh == '√':
                    if self.checkBox_2.isChecked():
                        self.textBrowser.append(str(ss + '=' + str(sz1 ** (1 / sz2))))
                        continue
                    else:
                        self.textBrowser.append(str(ss))
                        continue

            if self.checkBox_2.isChecked():
                self.textBrowser.append(ss + '=' + str(eval(ss)))
            else:
                self.textBrowser.append(ss)
            self.repaint()
        self.textBrowser.append('**********已完成**********')
        self.repaint()


app = QtWidgets.QApplication(sys.argv)
window = window()
window.show()
sys.exit(app.exec_())
' ོོུུ࿆ྂ'