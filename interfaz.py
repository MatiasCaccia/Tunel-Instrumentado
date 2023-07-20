from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        # Pantalla Principal
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(0, 0, 990, 590))
        self.groupBox.setObjectName("groupBox")
        # -------- NODO 1 --------
        self.lcdN1P_e = QtWidgets.QLCDNumber(10, self.groupBox)
        self.lcdN1P_e.setGeometry(QtCore.QRect(200, 20, 300, 41))
        self.lcdN1P_e.setObjectName("lcdN1P_e")
        self.lcdN1P_t = QtWidgets.QLCDNumber(10, self.groupBox)
        self.lcdN1P_t.setGeometry(QtCore.QRect(200, 80, 300, 41))
        self.lcdN1P_t.setObjectName("lcdN1P_t")
        self.lcdN1T = QtWidgets.QLCDNumber(10, self.groupBox)
        self.lcdN1T.setGeometry(QtCore.QRect(200, 140, 300, 41))
        self.lcdN1T.setObjectName("lcdN1T")

        # -------- NODO 2 --------
        self.lcdN2P_e = QtWidgets.QLCDNumber(10, self.groupBox)
        self.lcdN2P_e.setGeometry(QtCore.QRect(200, 260, 300, 41))
        self.lcdN2P_e.setObjectName("lcdN2P_e")
        self.lcdN2P_t = QtWidgets.QLCDNumber(10, self.groupBox)
        self.lcdN2P_t.setGeometry(QtCore.QRect(200, 325, 300, 41))
        self.lcdN2P_t.setObjectName("lcdN2P_t")
        self.lcdN2T = QtWidgets.QLCDNumber(10, self.groupBox)
        self.lcdN2T.setGeometry(QtCore.QRect(200, 390, 300, 41))
        self.lcdN2T.setObjectName("lcdN2T")
        # -------- NODO 3 --------
        self.lcdN3P_atm = QtWidgets.QLCDNumber(10, self.groupBox)
        self.lcdN3P_atm.setGeometry(QtCore.QRect(670, 20, 300, 41))
        self.lcdN3P_atm.setObjectName("lcdN3P_atm")
        self.lcdN3T = QtWidgets.QLCDNumber(10, self.groupBox)
        self.lcdN3T.setGeometry(QtCore.QRect(670, 80, 300, 41))
        self.lcdN3T.setObjectName("lcdN3T")
        self.lcdN3H = QtWidgets.QLCDNumber(10, self.groupBox)
        self.lcdN3H.setGeometry(QtCore.QRect(670, 140, 300, 41))
        self.lcdN3H.setObjectName("lcdN3H")
        # -------- Timestamp --------
        self.lcdTimestamp = QtWidgets.QLCDNumber(self.groupBox)
        self.lcdTimestamp.setGeometry(QtCore.QRect(670, 315, 300, 41))
        self.lcdTimestamp.setObjectName("lcdTimestamp")

        # -------- TEXTOS --------
        # Izquierda del display
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(20, 50, 150, 50))
        self.label.setObjectName("label")
        # Nodo 1
        self.labelN1P_e = QtWidgets.QLabel(self.groupBox)
        self.labelN1P_e.setGeometry(QtCore.QRect(15, 10, 150, 50))
        self.labelN1P_e.setObjectName("labelN1P_e")
        self.labelN1P_t = QtWidgets.QLabel(self.groupBox)
        self.labelN1P_t.setGeometry(QtCore.QRect(15, 75, 150, 50))
        self.labelN1P_t.setObjectName("labelN1P_t")
        self.labelN1T = QtWidgets.QLabel(self.groupBox)
        self.labelN1T.setGeometry(QtCore.QRect(15, 140, 160, 50))
        self.labelN1T.setObjectName("labelN1T")
        # Nodo 2
        self.labelN2P_e = QtWidgets.QLabel(self.groupBox)
        self.labelN2P_e.setGeometry(QtCore.QRect(15, 250, 150, 50))
        self.labelN2P_e.setObjectName("labelN2P_e")
        self.labelN2P_t = QtWidgets.QLabel(self.groupBox)
        self.labelN2P_t.setGeometry(QtCore.QRect(15, 315, 150, 50))
        self.labelN2P_t.setObjectName("labelN2P_t")
        self.labelN2T = QtWidgets.QLabel(self.groupBox)
        self.labelN2T.setGeometry(QtCore.QRect(15, 380, 160, 50))
        self.labelN2T.setObjectName("labelN2T")
        # Nodo 3
        self.labelN3P_atm = QtWidgets.QLabel(self.groupBox)
        self.labelN3P_atm.setGeometry(QtCore.QRect(530, 10, 150, 50))
        self.labelN3P_atm.setObjectName("labelN3P_atm")
        self.labelN3T = QtWidgets.QLabel(self.groupBox)
        self.labelN3T.setGeometry(QtCore.QRect(530, 75, 150, 50))
        self.labelN3T.setObjectName("labelN3T")
        self.labelN3H = QtWidgets.QLabel(self.groupBox)
        self.labelN3H.setGeometry(QtCore.QRect(530, 140, 160, 50))
        self.labelN3H.setObjectName("labelN3H")
        # Timestamp
        self.labelTimestamp = QtWidgets.QLabel(self.groupBox)
        self.labelTimestamp.setGeometry(QtCore.QRect(570, 310, 150, 50))
        self.labelTimestamp.setObjectName("labelTimestamp")
        
        # Boton de envio de sincronia
        self.pushButton = QtWidgets.QPushButton("pushButton", self.groupBox) 
        self.pushButton.setGeometry(QtCore.QRect(100, 500, 100, 50))
        self.pushButton.setObjectName("pushButton")

        # Boton de envio de STOP
        self.pushButton_stop = QtWidgets.QPushButton("pushButton_stop", self.groupBox) 
        self.pushButton_stop.setGeometry(QtCore.QRect(750, 500, 100, 50))
        self.pushButton_stop.setObjectName("pushButton_stop")

        # Entrada de texto para la presión de referencia
        #self.ei = QtWidgets.QLineEdit(self.groupBox)
        #self.ei.setGeometry(QtCore.QRect(600, 20, 300, 41))
        #self.ei.setObjectName("ValorReferencia")

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Datos Tunel de Viento"))
        # Nodo 1
        self.labelN1P_e.setText(_translate("MainWindow", "P. Estática Nodo 1 [Pa]"))
        self.labelN1P_t.setText(_translate("MainWindow", "P. Total Nodo 1 [Pa]"))
        self.labelN1T.setText(_translate("MainWindow", "T. Nodo 1 [°C]"))
        # Nodo 2
        self.labelN2P_e.setText(_translate("MainWindow", "P. Estática Nodo 2 [Pa]"))
        self.labelN2P_t.setText(_translate("MainWindow", "P. Total Nodo 2 [Pa]"))
        self.labelN2T.setText(_translate("MainWindow", "T. Nodo 2 [°C]"))
        # Nodo 3
        self.labelN3P_atm.setText(_translate("MainWindow", "P. Atmosf. Nodo 3[Pa]"))
        self.labelN3T.setText(_translate("MainWindow", "T. Nodo 3 [°C]"))
        self.labelN3H.setText(_translate("MainWindow", "Humedad Nodo 3 [%]"))
        # Timestamp
        self.labelTimestamp.setText(_translate("MainWindow","Timestamp"))
        # Botones
        self.pushButton.setText(_translate("MainWindow", "Comenzar"))
        self.pushButton_stop.setText(_translate("MainWindow", "STOP"))
        #self.ei.setText(_translate("MainWundow", ""))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())