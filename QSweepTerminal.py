# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QSweepTerminal'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!
import sys
import mainwindow
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QIcon, QPixmap


def readQSS(file):
    with open(file, 'r') as f:
        return f.read()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    qss_file = "F:/QSweepTerminal/qss/Obit.qss"
    qss = readQSS(qss_file)
    app.setStyleSheet(qss)

    MainWindow = mainwindow.MainWindow()

    icon = QIcon()
    icon.addPixmap(QPixmap("logo.ico"), QIcon.Normal, QIcon.Off)
    MainWindow.setWindowIcon(icon)

    MainWindow.showMaximized()
    sys.exit(app.exec_())
