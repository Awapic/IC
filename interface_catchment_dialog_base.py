# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interface_catchment_dialog_base.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_interface_catchment_DialogBase(object):
    def setupUi(self, interface_catchment_DialogBase):
        interface_catchment_DialogBase.setObjectName("interface_catchment_DialogBase")
        interface_catchment_DialogBase.resize(451, 433)
        self.verticalLayout = QtWidgets.QVBoxLayout(interface_catchment_DialogBase)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollArea = QtWidgets.QScrollArea(interface_catchment_DialogBase)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 431, 413))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.mMapLayerComboBox = gui.QgsMapLayerComboBox(self.scrollAreaWidgetContents)
        self.mMapLayerComboBox.setObjectName("mMapLayerComboBox")
        self.horizontalLayout.addWidget(self.mMapLayerComboBox)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_9 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_8.addWidget(self.label_9)
        self.verticalLayout_2.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.checkBox = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkBox.setChecked(False)
        self.checkBox.setTristate(False)
        self.checkBox.setObjectName("checkBox")
        self.horizontalLayout_9.addWidget(self.checkBox)
        self.mQgsDoubleSpinBox_2 = gui.QgsDoubleSpinBox(self.scrollAreaWidgetContents)
        self.mQgsDoubleSpinBox_2.setMaximum(99999999999.0)
        self.mQgsDoubleSpinBox_2.setProperty("value", 40.0)
        self.mQgsDoubleSpinBox_2.setObjectName("mQgsDoubleSpinBox_2")
        self.horizontalLayout_9.addWidget(self.mQgsDoubleSpinBox_2)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem)
        self.verticalLayout_2.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.checkBox_2 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkBox_2.setChecked(True)
        self.checkBox_2.setObjectName("checkBox_2")
        self.horizontalLayout_10.addWidget(self.checkBox_2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_10)
        self.line = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_2.addWidget(self.line)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.mMapLayerComboBox_2 = gui.QgsMapLayerComboBox(self.scrollAreaWidgetContents)
        self.mMapLayerComboBox_2.setAllowEmptyLayer(True)
        self.mMapLayerComboBox_2.setObjectName("mMapLayerComboBox_2")
        self.horizontalLayout_2.addWidget(self.mMapLayerComboBox_2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_3 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_11.addWidget(self.label_3)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem1)
        self.pushButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_11.addWidget(self.pushButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_4 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_5.addWidget(self.label_4)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_5 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_4.addWidget(self.label_5)
        self.lineEdit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.lineEdit.setInputMask("")
        self.lineEdit.setClearButtonEnabled(True)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_4.addWidget(self.lineEdit)
        spacerItem2 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.label_6 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_4.addWidget(self.label_6)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_2.setClearButtonEnabled(True)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_4.addWidget(self.lineEdit_2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_8 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_8.setEnabled(True)
        self.label_8.setText("")
        self.label_8.setWordWrap(True)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_7.addWidget(self.label_8)
        self.verticalLayout_2.addLayout(self.horizontalLayout_7)
        self.line_2 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_2.addWidget(self.line_2)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_7 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_6.addWidget(self.label_7)
        self.mQgsDoubleSpinBox = gui.QgsDoubleSpinBox(self.scrollAreaWidgetContents)
        self.mQgsDoubleSpinBox.setProperty("showGroupSeparator", False)
        self.mQgsDoubleSpinBox.setMaximum(1e+16)
        self.mQgsDoubleSpinBox.setProperty("value", 400.0)
        self.mQgsDoubleSpinBox.setShowClearButton(True)
        self.mQgsDoubleSpinBox.setClearValue(False)
        self.mQgsDoubleSpinBox.setObjectName("mQgsDoubleSpinBox")
        self.horizontalLayout_6.addWidget(self.mQgsDoubleSpinBox)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem3)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem4)
        self.button_box = QtWidgets.QDialogButtonBox(self.scrollAreaWidgetContents)
        self.button_box.setOrientation(QtCore.Qt.Horizontal)
        self.button_box.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.button_box.setObjectName("button_box")
        self.verticalLayout_2.addWidget(self.button_box)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        self.statusBar = QtWidgets.QStatusBar()
        self.addWidget(self.statusBar)

        self.retranslateUi(interface_catchment_DialogBase)
        self.mMapLayerComboBox_2.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(interface_catchment_DialogBase)

    def retranslateUi(self, interface_catchment_DialogBase):
        _translate = QtCore.QCoreApplication.translate
        interface_catchment_DialogBase.setWindowTitle(_translate("interface_catchment_DialogBase", "InterfaceCatchment"))
        self.label.setText(_translate("interface_catchment_DialogBase", "Blocks layer:"))
        self.label_9.setText(_translate("interface_catchment_DialogBase", "Dead-end removal:"))
        self.checkBox.setText(_translate("interface_catchment_DialogBase", "yes, max. street width"))
        self.mQgsDoubleSpinBox_2.setSuffix(_translate("interface_catchment_DialogBase", " m"))
        self.checkBox_2.setText(_translate("interface_catchment_DialogBase", "no"))
        self.label_2.setText(_translate("interface_catchment_DialogBase", "Starting point layer:"))
        self.label_3.setText(_translate("interface_catchment_DialogBase", "Click on map to select starting point:"))
        self.pushButton.setText(_translate("interface_catchment_DialogBase", "SELECT"))
        self.label_4.setText(_translate("interface_catchment_DialogBase", "Starting point coordinates:"))
        self.label_5.setText(_translate("interface_catchment_DialogBase", "X:"))
        self.label_6.setText(_translate("interface_catchment_DialogBase", "Y:"))
        self.label_7.setText(_translate("interface_catchment_DialogBase", "Max walking distance:"))
        self.mQgsDoubleSpinBox.setSuffix(_translate("interface_catchment_DialogBase", " m"))

from qgis import gui
