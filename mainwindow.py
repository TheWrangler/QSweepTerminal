from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QMessageBox
from PyQt5.QtCore import QTimer, Qt, QEvent
from PyQt5.QtSerialPort import QSerialPortInfo
import pyqtgraph
import numpy

from ui.mainwindow import Ui_MainWindow
from serialrtx import SerialRtx


class MainWindow(QWidget):
    _PHASE_SCALE = 5.625
    _serial_process_buf = bytearray()
    temp = 0.0
    bite = 0.0
    recvFrameNum = 0
    sendFrameNum = 0

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.verticalLayout = QVBoxLayout()
        self.ui.horizontalLayout.addLayout(self.verticalLayout)

        self._initPlot()
        self._initUI()
        self._updateFrame()

        self._serialRtx = SerialRtx()
        self._serialRtx.bindRecvSignal(self._serialRecvHandle)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self._timerHandle)
        self.timer.start(200)

    def _initUI(self):
        self._enumSerialPort()
        self.ui.m_BaudEdit.setText('9600')
        self.ui.m_SerialPortCtrlBtn.clicked.connect(self._serialPortCtrl)

        self.ui.m_ModulateFreqEdit.setText("20")
        self.ui.m_CenterFreqEdit.setText("17500")
        self.ui.m_PulseWidthEdit.setText("50")
        self.ui.m_PulseReplyPeriodEdit.setText("100000")
        self.ui.m_AttEdit.setText("10")
        self.ui.m_GNEdit.setText("30")
        self.ui.m_RadioSwitchCheckBox.setChecked(True)
        self.ui.m_RadioSwitchCheckBox.setText('开')
        self.ui.m_SysModeCombox.setCurrentIndex(0)
        self.ui.m_CaliPeriodEdit.setText("5")
        self.ui.m_ChAAmpEdit.setText("5")
        self.ui.m_ChAPhaseEdit.setText("28.125")
        self.ui.m_ChBAmpEdit.setText("5")
        self.ui.m_ChBPhaseEdit.setText("28.125")
        self.ui.m_ChCAmpEdit.setText("5")
        self.ui.m_ChCPhaseEdit.setText("28.125")

        self.ui.m_CenterFreqEdit.editingFinished.connect(self._updateFrame)
        self.ui.m_ModulateFreqEdit.editingFinished.connect(self._updateFrame)
        self.ui.m_PulseWidthEdit.editingFinished.connect(self._updateFrame)
        self.ui.m_PulseReplyPeriodEdit.editingFinished.connect(self._updateFrame)
        self.ui.m_SysModeCombox.currentIndexChanged.connect(self._updateFrame)
        self.ui.m_AttEdit.editingFinished.connect(self._updateFrame)
        self.ui.m_GNEdit.editingFinished.connect(self._updateFrame)
        self.ui.m_RadioSwitchCheckBox.clicked.connect(self._rfSwitchChanged)
        self.ui.m_RadioSwitchCheckBox.stateChanged.connect(self._updateFrame)
        self.ui.m_CaliPeriodEdit.editingFinished.connect(self._updateFrame)
        self.ui.m_ChAAmpEdit.editingFinished.connect(self._updateFrame)
        self.ui.m_ChAPhaseEdit.editingFinished.connect(self._updateFrame)
        self.ui.m_ChBAmpEdit.editingFinished.connect(self._updateFrame)
        self.ui.m_ChBPhaseEdit.editingFinished.connect(self._updateFrame)
        self.ui.m_ChCAmpEdit.editingFinished.connect(self._updateFrame)
        self.ui.m_ChCPhaseEdit.editingFinished.connect(self._updateFrame)

        self.ui.m_SendCmdBtn.clicked.connect(self._sendCmd)

        brand_label = QLabel()
        brand_label.setText('<b><u>北京七星华创微波技术有限公司</u> <i>CopyRight © 2019-2029 v1.0.0</i></b>')
        brand_label.setAlignment(Qt.AlignRight)
        self.verticalLayout.addWidget(brand_label)

    def _rfSwitchChanged(self):
        if self.ui.m_RadioSwitchCheckBox.isChecked():
            self.ui.m_RadioSwitchCheckBox.setText('开')
        else:
            self.ui.m_RadioSwitchCheckBox.setText('关')

    def _initPlot(self):
        self.plot_win = pyqtgraph.GraphicsWindow()
        self.plot_temp = self.plot_win.addPlot()
        self.plot_win.nextRow()
        self.plot_bite = self.plot_win.addPlot()
        self.verticalLayout.addWidget(self.plot_win)

        self.plot_temp.vb.setMouseEnabled(False, False)
        self.plot_temp.showGrid(True, True, 0.8)
        self.plot_temp.setMenuEnabled(False)
        # self.plot_temp.vb.disableAutoRange(pyqtgraph.graphicsItems.ViewBox.ViewBox.YAxis)
        # self.plot_temp.vb.disableAutoRange(pyqtgraph.graphicsItems.ViewBox.ViewBox.XAxis)
        self.plot_temp.setYRange(-45, 100)
        self.plot_temp.setXRange(0, 5000)
        self.plot_temp.getAxis('left').setLabel('温度', units='°C')

        self.plot_bite.vb.setMouseEnabled(False, False)
        self.plot_bite.showGrid(True, True, 0.8)
        self.plot_bite.setMenuEnabled(False)
        # self.plot_bite.vb.disableAutoRange(pyqtgraph.graphicsItems.ViewBox.ViewBox.YAxis)
        # self.plot_bite.vb.disableAutoRange(pyqtgraph.graphicsItems.ViewBox.ViewBox.XAxis)
        self.plot_bite.setYRange(0, 3.3)
        self.plot_bite.setXRange(0, 5000)
        self.plot_bite.getAxis('left').setLabel('检波电压', units='V')

        self.plot_temp_curve = self.plot_temp.plot(pen='g')
        self.plot_bite_curve = self.plot_bite.plot(pen='g')
        self.plot_temp_data = numpy.empty(5000)
        self.plot_bite_data = numpy.empty(5000)
        self.plot_data_index = 0

    def _updatePlot(self):
        if self.plot_data_index == 5000:
            self.plot_temp_data[:-1] = self.plot_temp_data[1:]
            self.plot_bite_data[:-1] = self.plot_bite_data[1:]
            self.plot_data_index = 4999

        self.plot_temp_data[self.plot_data_index] = self.temp
        self.plot_bite_data[self.plot_data_index] = self.bite
        self.plot_data_index += 1

        self.plot_temp_curve.setData(self.plot_temp_data[:self.plot_data_index])
        self.plot_bite_curve.setData(self.plot_bite_data[:self.plot_data_index])

    def _enumSerialPort(self):
        self.ui.m_SerialPortCombo.clear()
        port_list = QSerialPortInfo.availablePorts()
        for port in port_list:
            self.ui.m_SerialPortCombo.addItem(port.portName())

    def _updateFrame(self):
        modulate_freq = self.ui.m_ModulateFreqEdit.text()
        modulate_freq = int(modulate_freq)
        # frame_cmd = "#KR:" + str(modulate_freq * 32768) + ";"
        frame_cmd = "#KR:" + '{:0=6}'.format(modulate_freq * 32768) + ";"

        center_freq = self.ui.m_CenterFreqEdit.text()
        center_freq = int(center_freq)
        frame_cmd += "#FRQ:" + '{:0=5}'.format(center_freq) + ";"

        pulse_width = self.ui.m_PulseWidthEdit.text()
        pulse_width = int(pulse_width)
        frame_cmd += "#PW:" + '{:0=7}'.format(pulse_width) + ";"

        pulse_reply_period = self.ui.m_PulseReplyPeriodEdit.text()
        pulse_reply_period = int(pulse_reply_period)
        frame_cmd += "#PRT:" + '{:0=7}'.format(pulse_reply_period) + ";"

        att = self.ui.m_AttEdit.text()
        att = int(att)
        frame_cmd += "#ATT:" + '{:0=2}'.format(att) + ";"

        gn = self.ui.m_GNEdit.text()
        gn = int(gn)
        frame_cmd += "#GN:" + '{:0=2}'.format(gn) + ";"

        if self.ui.m_RadioSwitchCheckBox.isChecked():
            frame_cmd += "#RF:1;"
        else:
            frame_cmd += "#RF:0;"

        sys_mode = self.ui.m_SysModeCombox.currentIndex() + 1
        frame_cmd += "#MOD:" + str(sys_mode) + ";"

        cali_period = self.ui.m_CaliPeriodEdit.text()
        cali_period = float(cali_period)
        cali_period = int(cali_period * 10)
        frame_cmd += "#CT:" + '{:0=6}'.format(cali_period) + ";"

        cha_amp = self.ui.m_ChAAmpEdit.text()
        cha_amp = int(cha_amp)
        frame_cmd += "#AAA:" + '{:0=2}'.format(cha_amp) + ";"

        cha_phase = self.ui.m_ChAPhaseEdit.text()
        cha_phase = float(cha_phase)
        cha_phase = int(cha_phase / self._PHASE_SCALE)
        frame_cmd += "#PSA:" + '{:0=2}'.format(cha_phase) + ";"

        chb_amp = self.ui.m_ChBAmpEdit.text()
        chb_amp = int(chb_amp)
        frame_cmd += "#AAB:" + '{:0=2}'.format(chb_amp) + ";"

        chb_phase = self.ui.m_ChBPhaseEdit.text()
        chb_phase = float(chb_phase)
        chb_phase = int(chb_phase / self._PHASE_SCALE)
        frame_cmd += "#PSB:" + '{:0=2}'.format(chb_phase) + ";"

        chc_amp = self.ui.m_ChCAmpEdit.text()
        chc_amp = int(chc_amp)
        frame_cmd += "#AAC:" + '{:0=2}'.format(chc_amp) + ";"

        chc_phase = self.ui.m_ChCPhaseEdit.text()
        chc_phase = float(chc_phase)
        chc_phase = int(chc_phase / self._PHASE_SCALE)
        frame_cmd += "#PSC:" + '{:0=2}'.format(chc_phase) + ";"

        self.ui.m_FrameDataEdit.setText(frame_cmd)

    def _sendCmd(self):
        if not self._serialRtx.isOpened():
            QMessageBox.information(self, '提示', '串口未打开！', QMessageBox.Yes)
            return

        self.sendFrameNum += 1
        self.ui.m_sendFrameNumLcd.display(self.sendFrameNum)

        frame = self.ui.m_FrameDataEdit.toPlainText()
        frame_bytes = frame.encode()
        self._serialRtx.send(frame_bytes, len(frame))
        return

    def _serialPortCtrl(self):
        if not self._serialRtx.isOpened():
            serial_port_name = self.ui.m_SerialPortCombo.currentText()
            if serial_port_name == '':
                QMessageBox.information(self, '提示', '无串口连接！', QMessageBox.Yes)
                return

            baud = self.ui.m_BaudEdit.text()
            baud = int(baud)
            if not self._serialRtx.openPort(serial_port_name, baud):
                QMessageBox.warning(self, '警告', '打开串口失败！串口是否已被占用？', QMessageBox.Yes)
                return
            self.ui.m_SerialPortCtrlBtn.setText('关闭串口')
        else:
            self._serialRtx.closePort()
            self.ui.m_SerialPortCtrlBtn.setText('打开串口')

    def _serialRecvHandle(self):
        data = self._serialRtx.recv()
        if len(data) == 0:
            return
        self._serial_process_buf.extend(data)
        self.recvDataProcess()

    def recvDataProcess(self):
        # if len(self._serial_process_buf) < 17 :
        #     return

        start_index = self._serial_process_buf.find(b'$sta')
        if start_index == -1:
            self._serial_process_buf.clear()
            return

        if start_index != 0:
            for i in range(start_index):
                self._serial_process_buf.pop(0)

        end_index = self._serial_process_buf.find(b'*\r\n')
        if end_index == -1:
            if len(self._serial_process_buf) > 100:
                for i in range(100):
                    self._serial_process_buf.pop(0)
                return self.recvDataProcess()
            else:
                return

        frame = self._serial_process_buf[0:end_index]
        self._frameParse(frame)
        for i in range(end_index + 1):
            self._serial_process_buf.pop(0)

        return self.recvDataProcess()

    def _frameParse(self, frame):
        self.recvFrameNum += 1
        self.ui.m_recvFrameNumLcd.display(self.recvFrameNum)

        field = frame.split(b',')
        if len(field) < 3:
            return

        temp_str = field[1].decode('utf-8', 'ignore')
        try:
            self.temp = float(temp_str)
        except ValueError:
            pass

        bite_str = field[2].decode('utf-8', 'ignore')
        try:
            self.bite = float(bite_str)
        except ValueError:
            pass

        self._updatePlot()

    def _timerHandle(self):
        self.ui.m_sendBytesNumLcd.display(self._serialRtx.sendBytesNum())
        self.ui.m_recvBytesNumLcd.display(self._serialRtx.recvBytesNum())

    def closeEvent(self, event):
        reply = QMessageBox.question(self, '提示', '是否退出应用程序？', QMessageBox.Yes | QMessageBox.No)
        if reply == QMessageBox.Yes:
            if self._serialRtx.isOpened():
                self._serialRtx.closePort()
            event.accept()
        else:
            event.ignore()
