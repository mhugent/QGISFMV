# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui\ui_FmvMultiplexer.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_VideoMultiplexer(object):

    def setupUi(self, VideoMultiplexer):
        VideoMultiplexer.setObjectName("VideoMultiplexer")
        VideoMultiplexer.resize(425, 402)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/imgFMV/images/multiplexer.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        VideoMultiplexer.setWindowIcon(icon)
        self.verticalLayout = QtWidgets.QVBoxLayout(VideoMultiplexer)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(VideoMultiplexer)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.ln_inputVideo = QtWidgets.QLineEdit(VideoMultiplexer)
        self.ln_inputVideo.setReadOnly(True)
        self.ln_inputVideo.setObjectName("ln_inputVideo")
        self.horizontalLayout_4.addWidget(self.ln_inputVideo)
        self.pushButton = QtWidgets.QPushButton(VideoMultiplexer)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/imgFMV/images/opened-folder.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_4.addWidget(self.pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.label_2 = QtWidgets.QLabel(VideoMultiplexer)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.ln_inputMeta = QtWidgets.QLineEdit(VideoMultiplexer)
        self.ln_inputMeta.setReadOnly(True)
        self.ln_inputMeta.setObjectName("ln_inputMeta")
        self.horizontalLayout.addWidget(self.ln_inputMeta)
        self.pushButton_2 = QtWidgets.QPushButton(VideoMultiplexer)
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setText("")
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.label_3 = QtWidgets.QLabel(VideoMultiplexer)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.cmb_drone = QtWidgets.QComboBox(VideoMultiplexer)
        self.cmb_drone.setObjectName("cmb_drone")
        self.cmb_drone.addItem("")
        self.verticalLayout.addWidget(self.cmb_drone)
        self.widget_2 = QtWidgets.QWidget(VideoMultiplexer)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_4 = QtWidgets.QLabel(self.widget_2)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        self.sp_hfov = QtWidgets.QSpinBox(self.widget_2)
        self.sp_hfov.setProperty("value", 81)
        self.sp_hfov.setObjectName("sp_hfov")
        self.horizontalLayout_3.addWidget(self.sp_hfov)
        self.label_5 = QtWidgets.QLabel(self.widget_2)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_3.addWidget(self.label_5)
        self.sp_vfov = QtWidgets.QSpinBox(self.widget_2)
        self.sp_vfov.setProperty("value", 66)
        self.sp_vfov.setObjectName("sp_vfov")
        self.horizontalLayout_3.addWidget(self.sp_vfov)
        self.verticalLayout.addWidget(self.widget_2)
        self.bt_createCSV = QtWidgets.QPushButton(VideoMultiplexer)
        self.bt_createCSV.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.bt_createCSV.setObjectName("bt_createCSV")
        self.verticalLayout.addWidget(self.bt_createCSV)
        self.gb_telemetry = QtWidgets.QGroupBox(VideoMultiplexer)
        self.gb_telemetry.setObjectName("gb_telemetry")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.gb_telemetry)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_6 = QtWidgets.QLabel(self.gb_telemetry)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_3.addWidget(self.label_6)
        self.cmb_telemetry = QtWidgets.QComboBox(self.gb_telemetry)
        self.cmb_telemetry.setObjectName("cmb_telemetry")
        self.verticalLayout_3.addWidget(self.cmb_telemetry)
        self.verticalLayout.addWidget(self.gb_telemetry)
        self.bt_createMISB = QtWidgets.QPushButton(VideoMultiplexer)
        self.bt_createMISB.setEnabled(False)
        self.bt_createMISB.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.bt_createMISB.setObjectName("bt_createMISB")
        self.verticalLayout.addWidget(self.bt_createMISB)

        self.retranslateUi(VideoMultiplexer)
        self.bt_createMISB.clicked.connect(VideoMultiplexer.CreateMISB)
        self.pushButton.clicked.connect(VideoMultiplexer.OpenVideoFile)
        self.pushButton_2.clicked.connect(VideoMultiplexer.OpenCsvFile)
        self.bt_createCSV.clicked.connect(VideoMultiplexer.CreateCSV)
        QtCore.QMetaObject.connectSlotsByName(VideoMultiplexer)

    def retranslateUi(self, VideoMultiplexer):
        _translate = QtCore.QCoreApplication.translate
        VideoMultiplexer.setWindowTitle(_translate("VideoMultiplexer", "Video Multiplexer"))
        self.label.setText(_translate("VideoMultiplexer", "Input Video File (e.g video.ts)"))
        self.label_2.setText(_translate("VideoMultiplexer", "Input Metadata File (e.g video_metadata.csv)"))
        self.label_3.setText(_translate("VideoMultiplexer", "Select drone"))
        self.cmb_drone.setItemText(0, _translate("VideoMultiplexer", "DJI Mavic Pro"))
        self.label_4.setText(_translate("VideoMultiplexer", "Horizontal FOV"))
        self.label_5.setText(_translate("VideoMultiplexer", "Vertical FOV"))
        self.bt_createCSV.setText(_translate("VideoMultiplexer", "Extract Recordings"))
        self.gb_telemetry.setTitle(_translate("VideoMultiplexer", "Available telemetry"))
        self.label_6.setText(_translate("VideoMultiplexer", "Select the correct one if there is more than one"))
        self.bt_createMISB.setText(_translate("VideoMultiplexer", "Create MISB"))


from QGIS_FMV.gui import resources_rc
