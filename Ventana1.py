from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QLabel, QHBoxLayout, QApplication, QFormLayout, QLineEdit, \
    QPushButton
from PyQt5 import QtGui, QtCore
import sys

class Ventana1(QMainWindow):

    # hacer el metodo de construccion de la ventana
    def __init__(self,parent=None):
        super(Ventana1,self).__init__(parent)

        self.setWindowTitle("Formulario de registros")
        self.setWindowIcon(QtGui.QIcon("imagenes/balon1.jpg"))
        self.setStyleSheet("background-color: #C5F9E8;")

        # Estableciendo las propiedades de ancho y alto
        self.ancho = 900
        self.alto = 600

        # Establecer el tamaño de la ventana:
        self.resize(self.ancho, self.alto)

        # Estas lineas hacen que la ventana se vea en el centro:
        self.pantalla = self.frameGeometry()
        self.centro = QDesktopWidget().availableGeometry().center()
        self.pantalla.moveCenter(self.centro)
        self.move(self.pantalla.topLeft())

        # Para que la ventana no se pueda cambiar de tamaño
        # Se fija el ancho y el alto
        self.setFixedWidth(self.ancho)
        self.setFixedHeight(self.alto)

        self.fondo = QLabel(self)

        self.imagenFondo = QPixmap("imagenes/escudo.png")

        self.fondo.setPixmap(self.imagenFondo)

        self.fondo.setScaledContents(True)

        self.resize(self.imagenFondo.width(),self.imagenFondo.height())

        self.setCentralWidget(self.fondo)

        self.horizontal = QHBoxLayout()

        self.horizontal.setContentsMargins(30,30,30,30)

        # Layout izquierdo

        self.ladoIzquierdo = QFormLayout()

        self.letrero1 = QLabel()

        self.letrero1.setText("Informacion del cliente")

        self.letrero1.setFont(QFont("Andale mono",20))

        self.letrero1.setStyleSheet("color: #000000")

        self.ladoIzquierdo.addRow(self.letrero1)

        self.horizontal.addLayout(self.ladoIzquierdo)

        self.letrero2 = QLabel()

        self.letrero2.setFixedWidth(340)

        self.letrero2.setText("Por favor ingrese la informacion del cliente"
                              "\nen el formulario de abajo.Los campos marcados"
                              "\ncon asterisco son obligatorios.")

        self.letrero2.setFont(QFont("Andale mono",10))

        self.letrero2.setStyleSheet("color: #000000; margin-bottom: 40px;"
                                    "margin-top:20px"
                                    "padding-bottom: 10px"
                                    "border: 2px solid #000000"
                                    "border-left: none;"
                                    "boroder-right: none"
                                    "border-top:none;")

        self.ladoIzquierdo.addRow(self.letrero2)

        self.nombreCompleto = QLineEdit()
        self.nombreCompleto.setFixedWidth(250)

        self.ladoIzquierdo.addRow("Nombre Completo*", self.nombreCompleto)

        self.horizontal.addLayout(self.ladoIzquierdo)

        self.usuario = QLineEdit()
        self.usuario.setFixedWidth(250)

        self.ladoIzquierdo.addRow("Usuario*", self.usuario)

        self.password = QLineEdit()
        self.password.setFixedWidth(250)
        self.password.setEchoMode(QLineEdit.Password)
        self.ladoIzquierdo.addRow("Password*", self.password)

        self.password2 = QLineEdit()
        self.password2.setFixedWidth(250)
        self.password2.setEchoMode(QLineEdit.Password)
        self.ladoIzquierdo.addRow("Password*", self.password2)

        self.documento = QLineEdit()
        self.documento.setFixedWidth(250)

        self.ladoIzquierdo.addRow("Documento* ", self.documento)
        self.correo = QLineEdit()
        self.correo.setFixedWidth(250)

        self.ladoIzquierdo.addRow("Correo* ", self.correo)

        self.botonRegistrar = QPushButton("Registrar")

        self.botonRegistrar.setFixedWidth(90)

        self.botonRegistrar.setStyleSheet("background-color: # 008B45"
                                          "color: #FFFFFF"
                                          "padding: 10px;"
                                          "margin-top: 40px;")

        self.botonRegistrar.clicked.connect(self.accion_botonRegistrar)

        self.botonLimpiar = QPushButton("Limpiar")

        self.botonLimpiar.setFixedWidth(90)

        self.botonLimpiar.setStyleSheet("background-color: # 008B45"
                                          "color: #FFFFFF"
                                          "padding: 10px;"
                                          "margin-top: 40px;")

        self.botonLimpiar.clicked.connect(self.accion_botonRegistrar)

        self.ladoIzquierdo.addRow(self.botonLimpiar, self.botonRegistrar)







        self.horizontal.addLayout(self.ladoIzquierdo)


        self.fondo.setLayout(self.horizontal)

    def accion_botonLimpiar(self):
        pass
    def accion_botonRegistrar(self):
        pass

# Este if de decision se llama si se ejecuta el archivo
if __name__ == '__main__':
    # creamos una aplicacion pyqt5
    aplicacion1 = QApplication(sys.argv)
    # creamos una ventana
    v1 = Ventana1()
    # indicamos que la ventana se deje observar
    v1.show()
    # indicamos que la ventana se deje cerrar

    sys.exit(aplicacion1.exec_())

