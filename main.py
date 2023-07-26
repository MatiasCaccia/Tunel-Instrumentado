import sys
import paho.mqtt.client as mqtt
import csv
from PyQt5.QtWidgets import QApplication, QMainWindow 
from PyQt5.QtCore import QTimer
import socket
import time
from interfaz import Ui_MainWindow

class Form(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.sendSincro) #Asociar la funcion enviar epoch para sincronizar
        # self.ui.pushButton.clicked.connect(self.on_message) #Asociar la funcion enviar epoch para sincronizar
        #self.ui.ei.text()
        self.ui.pushButton_stop.clicked.connect(self.sendStop) #Asociar la funcion enviar cero para frenar
        
        self.ui.lcdN1P_e.display(128)
        self.ui.lcdN1P_t.display(64)
        self.ui.lcdN1P_t.display(256)
        self.show()
        
        # Configurar broker MQTT
        self.broker_address = socket.gethostbyname(socket.gethostname()) #Obtener el IP de la maquina = IP del broker
        self.topic_1 = "Sincro" #Tópico donde se publica el epoch de sincronismo
        self.topic_2 = "Sincro2" #Tópico donde se publica el epoch de sincronismo
        self.topic_3 = "Sincro3" #Tópico donde se publica el epoch de sincronismo
        self.subscribe_topic_1 = "/Sensor/1" #Tópico al que se suscribe con información del nodo 1 (Aguas Abajo)
        self.subscribe_topic_2 = "/Sensor/2" #Tópico al que se suscribe con información del nodo 2 (Aguas Arriba)
        self.subscribe_topic_3 = "/Sensor/3" #Tópico al que se suscribe con información del nodo 3 (Exterior)
        # Configuracion del cliente MQTT
        self.client = mqtt.Client()
        self.client.on_message = self.on_message #Ejecución de la funcion "on_message" cuando hay una lectura
        self.client.on_connect = self.on_connect #Conexión al Ejecución de la funcion "on_message" cuando hay una lectura
        self.client.connect(self.broker_address) #Conexión al Broker
        self.client.subscribe(self.subscribe_topic_1) #Suscripción al tópico Sensor1
        self.client.subscribe(self.subscribe_topic_2) #Suscripción al tópico Sensor2
        self.client.subscribe(self.subscribe_topic_3) #Suscripción al tópico Sensor3
        self.client.loop_start()
        # Archivo Logger CSV
        self.csv_filename = "datos.csv"
        self.csv_fieldnames = ["Timestamp","Nodo","V1","V2","V3"]
        # nodo | V1 | V2 | V3
        #  N1  |P_e |P_t | T
        #  N2  |P_e |P_t | T
        #  N3  |P_atm|%H | T
        
    # MQTT message handler y actualizador del Loggers
    def on_message(self, client, userdata, message):
        #self.ui.lcdNumberMax.display(12)
        payload_str = message.payload.decode("utf-8")
        payload_str = payload_str.split(' | ') #Separa el string que viene con el caracter |
        topic_str = message.topic
        type(topic_str)
        # Nodo 1
        if(message.topic == self.subscribe_topic_1): 
            self.ui.lcdTimestamp.display(payload_str[0])
            self.ui.lcdN1P_e.display(payload_str[2])
            self.ui.lcdN1P_t.display(payload_str[3])
            self.ui.lcdN1T.display(payload_str[4])
        # Nodo 2
        elif(message.topic == self.subscribe_topic_2): 
            self.ui.lcdN2P_e.display(payload_str[2])
            self.ui.lcdN2P_t.display(payload_str[3])
            self.ui.lcdN2T.display(payload_str[4])
        # Nodo 3
        elif(message.topic == self.subscribe_topic_3):
            self.ui.lcdN3P_atm.display(payload_str[2])
            self.ui.lcdN3T.display(payload_str[3])
            self.ui.lcdN3H.display(payload_str[4])
        # Escribir los datos en el logger
        with open(self.csv_filename, "a", newline="") as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=self.csv_fieldnames)
            writer.writerow({
                "Timestamp": payload_str[0],
                "Nodo": payload_str[1],
                "V1": payload_str[2],
                "V2": payload_str[3],
                "V3": payload_str[4]
            })
    # Conexión al broker MQTT
    def on_connect(self,client, userdata, flags, rc):
        print("Conectado al broker MQTT con código " + str(rc))
        self.client.subscribe(self.subscribe_topic_1)
        self.client.subscribe(self.subscribe_topic_2)

    #Funcion para enviar cero para frenar
    def sendStop(self):
        self.client.publish(self.topic_1, 0)
        self.client.publish(self.topic_2, 0)
        self.client.publish(self.topic_3, 0)
    
    #Funcion para enviar epoch para sincronizar
    def sendSincro(self):
        #self.ui.ei.text()
        #self.client.publish(self.topic, self.ui.ei.text())
        self.client.publish(self.topic_1, int(time.time()))
        self.client.publish(self.topic_2, int(time.time()))
        self.client.publish(self.topic_3, int(time.time()))

    def startTimer(self):    
        if self.ui.pushButton.text() == "Start Timer":
            self.timer.start(1000) 
            self.ui.pushButton.setText("Stop Timer")            
        else:
            self.ui.pushButton.setText("Start Timer")
            self.timer.stop() 

if __name__ == '__main__':
    app = QApplication(sys.argv)
    frm = Form()
    sys.exit(app.exec_())
