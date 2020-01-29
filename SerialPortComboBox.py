from PyQt5.QtWidgets import QComboBox
from PyQt5.QtSerialPort import QSerialPortInfo
from PyQt5.QtCore import pyqtSignal


class SerialPortComboBox(QComboBox):
    popupAboutToBeShown = pyqtSignal

    def __init__(self, parent=None):
        super(SerialPortComboBox, self).__init__(parent)

    def showPopup(self):
        self.clear()
        self._enumSerialPort()
        QComboBox.showPopup()

    def _enumSerialPort(self):
        port_list = QSerialPortInfo.availablePorts()
        for port in port_list:
            self.addItem(port.portName())
