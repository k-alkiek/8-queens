# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './ui/ui_main_window.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(777, 494)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 541, 401))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.resetButton = QtWidgets.QPushButton(self.centralwidget)
        self.resetButton.setGeometry(QtCore.QRect(10, 420, 90, 32))
        self.resetButton.setObjectName("resetButton")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(580, 170, 171, 241))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.runningTimeLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.runningTimeLabel.setObjectName("runningTimeLabel")
        self.verticalLayout.addWidget(self.runningTimeLabel)
        self.runningTimeLineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.runningTimeLineEdit.setEnabled(False)
        self.runningTimeLineEdit.setObjectName("runningTimeLineEdit")
        self.verticalLayout.addWidget(self.runningTimeLineEdit)
        self.costLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.costLabel.setObjectName("costLabel")
        self.verticalLayout.addWidget(self.costLabel)
        self.costLineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.costLineEdit.setEnabled(False)
        self.costLineEdit.setObjectName("costLineEdit")
        self.verticalLayout.addWidget(self.costLineEdit)
        self.expandedNodesLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.expandedNodesLabel.setObjectName("expandedNodesLabel")
        self.verticalLayout.addWidget(self.expandedNodesLabel)
        self.expandedNodesLineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.expandedNodesLineEdit.setEnabled(False)
        self.expandedNodesLineEdit.setObjectName("expandedNodesLineEdit")
        self.verticalLayout.addWidget(self.expandedNodesLineEdit)
        self.optimalKLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.optimalKLabel.setObjectName("optimalKLabel")
        self.verticalLayout.addWidget(self.optimalKLabel)
        self.optimalKLineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.optimalKLineEdit.setEnabled(False)
        self.optimalKLineEdit.setObjectName("optimalKLineEdit")
        self.verticalLayout.addWidget(self.optimalKLineEdit)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(580, 10, 171, 101))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.algorithmComboBox = QtWidgets.QComboBox(self.verticalLayoutWidget_2)
        self.algorithmComboBox.setObjectName("algorithmComboBox")
        self.verticalLayout_2.addWidget(self.algorithmComboBox)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.solveButton = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.solveButton.setObjectName("solveButton")
        self.horizontalLayout.addWidget(self.solveButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 777, 28))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.actionLoad = QtWidgets.QAction(MainWindow)
        self.actionLoad.setObjectName("actionLoad")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.menuFile.addAction(self.actionLoad)
        self.menuFile.addAction(self.actionSave)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.resetButton.setText(_translate("MainWindow", "Reset"))
        self.runningTimeLabel.setText(_translate("MainWindow", "Running Time"))
        self.costLabel.setText(_translate("MainWindow", "Cost"))
        self.expandedNodesLabel.setText(_translate("MainWindow", "Expanded Nodes"))
        self.optimalKLabel.setText(_translate("MainWindow", "Optimal K"))
        self.solveButton.setText(_translate("MainWindow", "Solve"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionLoad.setText(_translate("MainWindow", "Load From File"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))