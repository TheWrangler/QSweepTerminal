from PyQt5.QtSerialPort import QSerialPort
from PyQt5.QtCore import QIODevice


class SerialRtx(object):
    def __init__(self, parent=None):
        self._bOpened = False
        self._serialPort = QSerialPort()
        self._reseStatics()

    def openPort(self, port, baud):
        self._serialPort.setPortName(port)
        self._bOpened = self._serialPort.open(QIODevice.ReadWrite)
        if self._bOpened:
            self._serialPort.setBaudRate(baud)
            self._serialPort.setDataBits(QSerialPort.Data8)
            self._serialPort.setParity(QSerialPort.NoParity)
            self._serialPort.setStopBits(QSerialPort.OneStop)
            self._serialPort.setReadBufferSize(4096)
            return True
        else:
            return False

    def closePort(self):
        self._serialPort.close()
        self._bOpened = False
        self._reseStatics()

    def send(self, data, len):
        self._serialPort.writeData(data)
        self._sendBytesNum += len

    def bindRecvSignal(self, recvProcess):
        self._serialPort.readyRead.connect(recvProcess)

    def recv(self):
        # len = self._serialPort.bytesAvailable()
        data = self._serialPort.readAll()
        data = bytes(data)
        self._recvBytesNum += len(data)
        return data

    def isOpened(self):
        return self._bOpened

    def _reseStatics(self):
        self._recvBytesNum = 0
        self._sendBytesNum = 0

    def recvBytesNum(self):
        return self._recvBytesNum

    def sendBytesNum(self):
        return self._sendBytesNum
