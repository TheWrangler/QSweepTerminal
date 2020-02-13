# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1160, 810)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(MainWindow)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox_3 = QtWidgets.QGroupBox(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy)
        self.groupBox_3.setMinimumSize(QtCore.QSize(260, 0))
        self.groupBox_3.setMaximumSize(QtCore.QSize(260, 16777215))
        self.groupBox_3.setObjectName("groupBox_3")
        self.formLayout_3 = QtWidgets.QFormLayout(self.groupBox_3)
        self.formLayout_3.setObjectName("formLayout_3")
        self.label_16 = QtWidgets.QLabel(self.groupBox_3)
        self.label_16.setObjectName("label_16")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_16)
        self.label_17 = QtWidgets.QLabel(self.groupBox_3)
        self.label_17.setObjectName("label_17")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_17)
        self.m_BaudEdit = QtWidgets.QLineEdit(self.groupBox_3)
        self.m_BaudEdit.setStyleSheet("")
        self.m_BaudEdit.setObjectName("m_BaudEdit")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.m_BaudEdit)
        self.m_SerialPortCombo = QtWidgets.QComboBox(self.groupBox_3)
        self.m_SerialPortCombo.setObjectName("m_SerialPortCombo")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.m_SerialPortCombo)
        self.m_SerialPortCtrlBtn = QtWidgets.QPushButton(self.groupBox_3)
        self.m_SerialPortCtrlBtn.setObjectName("m_SerialPortCtrlBtn")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.m_SerialPortCtrlBtn)
        self.verticalLayout.addWidget(self.groupBox_3)
        self.groupBox = QtWidgets.QGroupBox(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setMinimumSize(QtCore.QSize(260, 0))
        self.groupBox.setMaximumSize(QtCore.QSize(260, 16777215))
        self.groupBox.setObjectName("groupBox")
        self.formLayout_2 = QtWidgets.QFormLayout(self.groupBox)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.m_CenterFreqEdit = QtWidgets.QLineEdit(self.groupBox)
        self.m_CenterFreqEdit.setObjectName("m_CenterFreqEdit")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.m_CenterFreqEdit)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.m_ModulateFreqEdit = QtWidgets.QLineEdit(self.groupBox)
        self.m_ModulateFreqEdit.setObjectName("m_ModulateFreqEdit")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.m_ModulateFreqEdit)
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.m_PulseWidthEdit = QtWidgets.QLineEdit(self.groupBox)
        self.m_PulseWidthEdit.setObjectName("m_PulseWidthEdit")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.m_PulseWidthEdit)
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setObjectName("label_4")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.m_PulseReplyPeriodEdit = QtWidgets.QLineEdit(self.groupBox)
        self.m_PulseReplyPeriodEdit.setObjectName("m_PulseReplyPeriodEdit")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.m_PulseReplyPeriodEdit)
        self.label_11 = QtWidgets.QLabel(self.groupBox)
        self.label_11.setObjectName("label_11")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_11)
        self.m_SysModeCombox = QtWidgets.QComboBox(self.groupBox)
        self.m_SysModeCombox.setObjectName("m_SysModeCombox")
        self.m_SysModeCombox.addItem("")
        self.m_SysModeCombox.addItem("")
        self.m_SysModeCombox.addItem("")
        self.m_SysModeCombox.addItem("")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.m_SysModeCombox)
        self.label_12 = QtWidgets.QLabel(self.groupBox)
        self.label_12.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_12.setObjectName("label_12")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_12)
        self.m_AttEdit = QtWidgets.QLineEdit(self.groupBox)
        self.m_AttEdit.setObjectName("m_AttEdit")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.m_AttEdit)
        self.label_13 = QtWidgets.QLabel(self.groupBox)
        self.label_13.setObjectName("label_13")
        self.formLayout_2.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_13)
        self.m_GNEdit = QtWidgets.QLineEdit(self.groupBox)
        self.m_GNEdit.setObjectName("m_GNEdit")
        self.formLayout_2.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.m_GNEdit)
        self.label_14 = QtWidgets.QLabel(self.groupBox)
        self.label_14.setObjectName("label_14")
        self.formLayout_2.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.label_14)
        self.m_RadioSwitchCheckBox = QtWidgets.QCheckBox(self.groupBox)
        self.m_RadioSwitchCheckBox.setObjectName("m_RadioSwitchCheckBox")
        self.formLayout_2.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.m_RadioSwitchCheckBox)
        self.label_15 = QtWidgets.QLabel(self.groupBox)
        self.label_15.setObjectName("label_15")
        self.formLayout_2.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.label_15)
        self.m_CaliPeriodEdit = QtWidgets.QLineEdit(self.groupBox)
        self.m_CaliPeriodEdit.setObjectName("m_CaliPeriodEdit")
        self.formLayout_2.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.m_CaliPeriodEdit)
        self.verticalLayout.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setMinimumSize(QtCore.QSize(260, 0))
        self.groupBox_2.setMaximumSize(QtCore.QSize(260, 16777215))
        self.groupBox_2.setObjectName("groupBox_2")
        self.formLayout = QtWidgets.QFormLayout(self.groupBox_2)
        self.formLayout.setObjectName("formLayout")
        self.label_5 = QtWidgets.QLabel(self.groupBox_2)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.m_ChAAmpEdit = QtWidgets.QLineEdit(self.groupBox_2)
        self.m_ChAAmpEdit.setObjectName("m_ChAAmpEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.m_ChAAmpEdit)
        self.label_6 = QtWidgets.QLabel(self.groupBox_2)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.m_ChAPhaseEdit = QtWidgets.QLineEdit(self.groupBox_2)
        self.m_ChAPhaseEdit.setObjectName("m_ChAPhaseEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.m_ChAPhaseEdit)
        self.label_7 = QtWidgets.QLabel(self.groupBox_2)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.m_ChBAmpEdit = QtWidgets.QLineEdit(self.groupBox_2)
        self.m_ChBAmpEdit.setObjectName("m_ChBAmpEdit")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.m_ChBAmpEdit)
        self.label_8 = QtWidgets.QLabel(self.groupBox_2)
        self.label_8.setObjectName("label_8")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.m_ChBPhaseEdit = QtWidgets.QLineEdit(self.groupBox_2)
        self.m_ChBPhaseEdit.setObjectName("m_ChBPhaseEdit")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.m_ChBPhaseEdit)
        self.label_9 = QtWidgets.QLabel(self.groupBox_2)
        self.label_9.setObjectName("label_9")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.m_ChCAmpEdit = QtWidgets.QLineEdit(self.groupBox_2)
        self.m_ChCAmpEdit.setObjectName("m_ChCAmpEdit")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.m_ChCAmpEdit)
        self.label_10 = QtWidgets.QLabel(self.groupBox_2)
        self.label_10.setObjectName("label_10")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_10)
        self.m_ChCPhaseEdit = QtWidgets.QLineEdit(self.groupBox_2)
        self.m_ChCPhaseEdit.setObjectName("m_ChCPhaseEdit")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.m_ChCPhaseEdit)
        self.verticalLayout.addWidget(self.groupBox_2)
        spacerItem = QtWidgets.QSpacerItem(20, 108, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.brand_label = QtWidgets.QLabel(MainWindow)
        self.brand_label.setObjectName("brand_label")
        self.verticalLayout.addWidget(self.brand_label)
        self.copyright_label = QtWidgets.QLabel(MainWindow)
        self.copyright_label.setObjectName("copyright_label")
        self.verticalLayout.addWidget(self.copyright_label)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.m_PlotFrame = QtWidgets.QFrame(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.m_PlotFrame.sizePolicy().hasHeightForWidth())
        self.m_PlotFrame.setSizePolicy(sizePolicy)
        self.m_PlotFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.m_PlotFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.m_PlotFrame.setObjectName("m_PlotFrame")
        self.verticalLayout_2.addWidget(self.m_PlotFrame)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.m_FrameDataEdit = QtWidgets.QTextEdit(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.m_FrameDataEdit.sizePolicy().hasHeightForWidth())
        self.m_FrameDataEdit.setSizePolicy(sizePolicy)
        self.m_FrameDataEdit.setMinimumSize(QtCore.QSize(0, 60))
        self.m_FrameDataEdit.setMaximumSize(QtCore.QSize(16777215, 60))
        self.m_FrameDataEdit.setObjectName("m_FrameDataEdit")
        self.horizontalLayout.addWidget(self.m_FrameDataEdit)
        self.m_SendCmdBtn = QtWidgets.QPushButton(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.m_SendCmdBtn.sizePolicy().hasHeightForWidth())
        self.m_SendCmdBtn.setSizePolicy(sizePolicy)
        self.m_SendCmdBtn.setMinimumSize(QtCore.QSize(0, 60))
        self.m_SendCmdBtn.setMaximumSize(QtCore.QSize(16777215, 60))
        self.m_SendCmdBtn.setObjectName("m_SendCmdBtn")
        self.horizontalLayout.addWidget(self.m_SendCmdBtn)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.groupBox_4 = QtWidgets.QGroupBox(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_4.sizePolicy().hasHeightForWidth())
        self.groupBox_4.setSizePolicy(sizePolicy)
        self.groupBox_4.setMinimumSize(QtCore.QSize(0, 0))
        self.groupBox_4.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.groupBox_4.setObjectName("groupBox_4")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox_4)
        self.gridLayout.setObjectName("gridLayout")
        self.label_18 = QtWidgets.QLabel(self.groupBox_4)
        self.label_18.setObjectName("label_18")
        self.gridLayout.addWidget(self.label_18, 0, 0, 1, 1)
        self.m_sendBytesNumLcd = QtWidgets.QLCDNumber(self.groupBox_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.m_sendBytesNumLcd.sizePolicy().hasHeightForWidth())
        self.m_sendBytesNumLcd.setSizePolicy(sizePolicy)
        self.m_sendBytesNumLcd.setFrameShape(QtWidgets.QFrame.Box)
        self.m_sendBytesNumLcd.setLineWidth(1)
        self.m_sendBytesNumLcd.setMidLineWidth(0)
        self.m_sendBytesNumLcd.setSmallDecimalPoint(False)
        self.m_sendBytesNumLcd.setDigitCount(18)
        self.m_sendBytesNumLcd.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.m_sendBytesNumLcd.setObjectName("m_sendBytesNumLcd")
        self.gridLayout.addWidget(self.m_sendBytesNumLcd, 0, 1, 1, 1)
        self.label_19 = QtWidgets.QLabel(self.groupBox_4)
        self.label_19.setObjectName("label_19")
        self.gridLayout.addWidget(self.label_19, 0, 2, 1, 1)
        self.m_recvBytesNumLcd = QtWidgets.QLCDNumber(self.groupBox_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.m_recvBytesNumLcd.sizePolicy().hasHeightForWidth())
        self.m_recvBytesNumLcd.setSizePolicy(sizePolicy)
        self.m_recvBytesNumLcd.setDigitCount(18)
        self.m_recvBytesNumLcd.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.m_recvBytesNumLcd.setObjectName("m_recvBytesNumLcd")
        self.gridLayout.addWidget(self.m_recvBytesNumLcd, 0, 3, 1, 1)
        self.label_20 = QtWidgets.QLabel(self.groupBox_4)
        self.label_20.setObjectName("label_20")
        self.gridLayout.addWidget(self.label_20, 0, 4, 1, 1)
        self.m_sendFrameNumLcd = QtWidgets.QLCDNumber(self.groupBox_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.m_sendFrameNumLcd.sizePolicy().hasHeightForWidth())
        self.m_sendFrameNumLcd.setSizePolicy(sizePolicy)
        self.m_sendFrameNumLcd.setDigitCount(18)
        self.m_sendFrameNumLcd.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.m_sendFrameNumLcd.setObjectName("m_sendFrameNumLcd")
        self.gridLayout.addWidget(self.m_sendFrameNumLcd, 0, 5, 1, 1)
        self.label_21 = QtWidgets.QLabel(self.groupBox_4)
        self.label_21.setObjectName("label_21")
        self.gridLayout.addWidget(self.label_21, 0, 6, 1, 1)
        self.m_recvFrameNumLcd = QtWidgets.QLCDNumber(self.groupBox_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.m_recvFrameNumLcd.sizePolicy().hasHeightForWidth())
        self.m_recvFrameNumLcd.setSizePolicy(sizePolicy)
        self.m_recvFrameNumLcd.setDigitCount(18)
        self.m_recvFrameNumLcd.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.m_recvFrameNumLcd.setObjectName("m_recvFrameNumLcd")
        self.gridLayout.addWidget(self.m_recvFrameNumLcd, 0, 7, 1, 1)
        self.verticalLayout_2.addWidget(self.groupBox_4)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PSTR17R5A控制软件"))
        self.groupBox_3.setTitle(_translate("MainWindow", "通信参数配置"))
        self.label_16.setText(_translate("MainWindow", "端口号:"))
        self.label_17.setText(_translate("MainWindow", "波特率:"))
        self.m_SerialPortCtrlBtn.setText(_translate("MainWindow", "打开串口"))
        self.groupBox.setTitle(_translate("MainWindow", "发射通道参数配置"))
        self.label.setText(_translate("MainWindow", "中心频率(MHz):"))
        self.label_2.setText(_translate("MainWindow", "调频率(MHz/us):"))
        self.label_3.setText(_translate("MainWindow", "脉冲宽度(us):"))
        self.label_4.setText(_translate("MainWindow", "脉冲重复周期(us):"))
        self.label_11.setText(_translate("MainWindow", "系统模式:"))
        self.m_SysModeCombox.setItemText(0, _translate("MainWindow", "一发一收"))
        self.m_SysModeCombox.setItemText(1, _translate("MainWindow", "一发两收(切换)"))
        self.m_SysModeCombox.setItemText(2, _translate("MainWindow", "一发两收(固定)"))
        self.m_SysModeCombox.setItemText(3, _translate("MainWindow", "一发三收"))
        self.label_12.setText(_translate("MainWindow", "衰减(dB):"))
        self.label_13.setText(_translate("MainWindow", "增益(dB):"))
        self.label_14.setText(_translate("MainWindow", "射频开关:"))
        self.m_RadioSwitchCheckBox.setText(_translate("MainWindow", "关"))
        self.label_15.setText(_translate("MainWindow", "校准时长(s):"))
        self.groupBox_2.setTitle(_translate("MainWindow", "接收通道参数配置"))
        self.label_5.setText(_translate("MainWindow", "通道A幅度衰减(dB):"))
        self.label_6.setText(_translate("MainWindow", "通道A相位偏置(°):"))
        self.label_7.setText(_translate("MainWindow", "通道B幅度衰减(dB):"))
        self.label_8.setText(_translate("MainWindow", "通道B相位偏置(°):"))
        self.label_9.setText(_translate("MainWindow", "通道C幅度衰减(dB):"))
        self.label_10.setText(_translate("MainWindow", "通道C相位偏置(°):"))
        self.brand_label.setText(_translate("MainWindow", "TextLabel"))
        self.copyright_label.setText(_translate("MainWindow", "TextLabel"))
        self.m_SendCmdBtn.setText(_translate("MainWindow", "发送命令"))
        self.groupBox_4.setTitle(_translate("MainWindow", "工作状态"))
        self.label_18.setText(_translate("MainWindow", "发送字节数:"))
        self.label_19.setText(_translate("MainWindow", "接收字节数:"))
        self.label_20.setText(_translate("MainWindow", "发送帧数:"))
        self.label_21.setText(_translate("MainWindow", "接收帧数:"))
