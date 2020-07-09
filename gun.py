import sys
import sqlite3
import pygame
from PyQt5 import QtWidgets
from gunfinder import Ui_MainWindow
from tkinter import messagebox, Tk

conn = sqlite3.connect('guninfo20.db')
cursor = conn.cursor()
root = Tk()
root.withdraw()
SCREEN_WIDTH = 480
SCREEN_HEIGHT = 400
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('枪械查询器')
background = pygame.image.load('guns.png')
screen.fill(0)
screen.blit(background, (0, 0))
pygame.display.update()
pygame.quit()
pygame.time.delay(3000)


class mywindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(self.width(), self.height())
        aaa = messagebox.askokcancel('重要提示/版权声明,Important notes/copyright notice', '''点击'cancel'退出
        Click "Cancel" to exit
        1、(重要)删除按钮测试中，如果不写枪械名按删除按钮会导致所有枪械数据丢失
        2、请勿添加一些世界上没有的枪械或其他物品
        3、禁止添加脏话或违法话语，一旦发现就会被处罚
        4、枪械信息内容请勿照搬置其他地方发布''')

        if not aaa:
            exit(0)
        self.checkBox.setChecked(True)

    def chaxunbtn(self):
        self.textBrowser.clear()
        if not self.checkBox.isChecked():
            messagebox.showinfo('提示', '请勾选"已读重要提示"')
            return
        a = str(self.lineEdit_2.text())
        a = a.strip()
        if a == '':
            aa = '不可以不输入'
            self.textBrowser.append(aa)
            self.lineEdit_2.clear()
            self.repaint()
            return
        if a == 'EG':
            a = ''
        cursor.execute(
            'select gunname,types,infor from gun where gunname like "%' + a + '%"or nickname like "%' + a + '%"or types like "%' + a + '%"COLLATE NOCASE')
        aa = cursor.fetchall()
        if aa == []:
            aa = '未查询到相关枪械'

        aa = str(aa)
        aa = aa.strip()
        aa = aa.strip('[')
        aa = aa.strip(']')

        self.textBrowser.append(aa)
        self.lineEdit_2.clear()
        self.repaint()

    def baocunbtn(self):
        self.textBrowser.clear()
        if str(self.lineEdit_2.text()) == '':
            self.textBrowser.append('枪械名不能为空')
            self.lineEdit_2.clear()
            self.lineEdit_3.clear()
            self.lineEdit_4.clear()
            self.lineEdit_9.clear()
            self.repaint()
            return
        cursor.execute('insert into gun (gunname,types,infor,nickname) VALUES(?,?,?,?)',
                       (self.lineEdit_2.text(), self.lineEdit_3.text(), self.lineEdit_4.text(), self.lineEdit_9.text()))
        conn.commit()
        self.textBrowser.append('添加枪械信息成功')
        self.lineEdit_2.clear()
        self.lineEdit_3.clear()
        self.lineEdit_4.clear()
        self.lineEdit_9.clear()
        self.repaint()

    def xiugaibtn(self):
        self.textBrowser.clear()
        if str(self.lineEdit_2.text()) == '':
            self.textBrowser.append('枪械名不能为空')
            self.lineEdit_2.clear()
            self.lineEdit_3.clear()
            self.lineEdit_4.clear()
            self.lineEdit_9.clear()
            self.repaint()
            return

        cursor.execute('UPDATE gun SET types=?,infor=?,nickname=? where gunname=? COLLATE NOCASE',
                       (self.lineEdit_3.text(), self.lineEdit_4.text(), self.lineEdit_9.text(), self.lineEdit_2.text()))
        conn.commit()
        self.textBrowser.append('修改枪械信息成功')
        self.lineEdit_2.clear()
        self.lineEdit_3.clear()
        self.lineEdit_4.clear()
        self.lineEdit_9.clear()
        self.repaint()

    def shanchubtn(self):
        self.textBrowser.clear()
        if str(self.lineEdit_2.text()) == '':
            self.textBrowser.append('枪械名不能为空')
            self.lineEdit_2.clear()
            self.lineEdit_3.clear()
            self.lineEdit_4.clear()
            self.lineEdit_9.clear()
            self.repaint()
            return
        cursor.execute('DELETE FROM gun WHERE gunname=? COLLATE NOCASE', (self.lineEdit_2.text(),))
        conn.commit()
        self.lineEdit_2.clear()
        self.textBrowser.append('删除信息成功')
        self.repaint()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = mywindow()
    window.show()
    sys.exit(app.exec_())
