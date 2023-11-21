from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QLabel, QHBoxLayout, QApplication, QFormLayout, QLineEdit, \
    QPushButton, QDialog, QDialogButtonBox, QVBoxLayout
from PyQt5 import QtGui, QtCore, Qt

from PyQt5.QtCore import Qt
import sys

class Ventana1(QMainWindow):

    # hacer el metodo de construccion de la ventana
    def __init__(self,parent=None):
        super(Ventana1,self).__init__(parent)

        self.setWindowTitle("Formulario de registros")
        self.setWindowIcon(QtGui.QIcon("imagenes/balon1.jpg"))
        self.setStyleSheet("background-color: #C5F9E8;")

        # Estableciendo las propiedades de ancho y alto
        self.ancho = 1000
        self.alto = 800

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

        self.imagenFondo = QPixmap()

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

        self.letrero2.setFixedWidth(360)

        self.letrero2.setText("Por favor ingrese la informacion del cliente"
                              "\nen el formulario de abajo.Los campos marcados"
                              "\ncon asterisco son obligatorios.")

        self.letrero2.setFont(QFont("Andale mono",10))

        self.letrero2.setStyleSheet("color: #000000; margin-bottom: 40px;"
                                    "margin-top:20px;"
                                    "padding-bottom: 10px;"
                                    "border: 2px solid #000000;"
                                    "border-left: none;"
                                    "boroder-right: none;"
                                    "border-top:none;"
                                    )

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

        self.botonRegistrar.setStyleSheet("background-color: #008B45;"
                                       "color: #FFFFFF;"
                                       "padding: 10px;"
                                       "margin-top: 40px;"
                                       )

        self.botonRegistrar.clicked.connect(self.accion_botonRegistrar)

        self.botonLimpiar = QPushButton("Limpiar")

        self.botonLimpiar.setFixedWidth(90)

        self.botonLimpiar.setStyleSheet("background-color: #008B45;"
                                       "color: #FFFFFF;"
                                       "padding: 10px;"
                                       "margin-top: 40px;"
                                       )

        self.botonLimpiar.clicked.connect(self.accion_botonLimpiar)

        self.ladoIzquierdo.addRow(self.botonLimpiar, self.botonRegistrar)







        self.horizontal.addLayout(self.ladoIzquierdo)

        self.ladoDerecho = QFormLayout()

        self.ladoDerecho.setContentsMargins(100,0,0,0)

        self.letrero3 = QLabel()

        self.letrero3.setText("Recuperar contraseña")

        self.letrero3.setFont(QFont("Andale mono",20))

        self.letrero3.setStyleSheet("color: #000000")

        self.ladoDerecho.addRow(self.letrero3)

        self.letrero4 = QLabel()

        self.letrero4.setText("Por favor ingrese la informacion para recuperar"
                              "\nla contraseña. Los campos marcados"
                              "\ncon asteriscos son obligatorios.")

        self.letrero4.setFont(QFont("Andale mono", 10))

        self.letrero4.setStyleSheet("color: #000000; margin-bottom: 40px;"
                                    "margin-top:20px;"
                                    "padding-bottom: 10px;"
                                    "border: 2px solid #000000;"
                                    "border-left: none;"
                                    "boroder-right: none;"
                                    "border-top:none;"
                                    )

        # 1 Prregunta y respuesta
        self.ladoDerecho.addRow(self.letrero4)

        self.labelPregunta1 = QLabel("Pregunta de verificacion 1*")

        self.ladoDerecho.addRow(self.labelPregunta1)

        self.pregunta1 = QLineEdit()

        self.pregunta1.setFixedWidth(320)

        self.ladoDerecho.addRow(self.pregunta1)

        self.labelRespuesta1 = QLabel("Respuesta de verificaion 1*")

        self.ladoDerecho.addRow(self.labelRespuesta1)

        self.respuesta1 = QLineEdit()

        self.respuesta1.setFixedWidth(320)

        self.ladoDerecho.addRow(self.respuesta1)

        # 2 Prregunta y respuesta


        self.labelPregunta2 = QLabel("Pregunta de verificacion 2*")

        self.ladoDerecho.addRow(self.labelPregunta2)

        self.pregunta2 = QLineEdit()

        self.pregunta2.setFixedWidth(320)

        self.ladoDerecho.addRow(self.pregunta2)

        self.labelRespuesta2 = QLabel("Respuesta de verificaion 2*")

        self.ladoDerecho.addRow(self.labelRespuesta2)

        self.respuesta2 = QLineEdit()

        self.respuesta2.setFixedWidth(320)

        self.ladoDerecho.addRow(self.respuesta2)

        # 3 Prregunta y respuesta


        self.labelPregunta3 = QLabel("Pregunta de verificacion 3*")

        self.ladoDerecho.addRow(self.labelPregunta3)

        self.pregunta3 = QLineEdit()

        self.pregunta3.setFixedWidth(320)

        self.ladoDerecho.addRow(self.pregunta3)

        self.labelRespuesta3 = QLabel("Respuesta de verificaion 3*")

        self.ladoDerecho.addRow(self.labelRespuesta3)

        self.respuesta3 = QLineEdit()

        self.respuesta3.setFixedWidth(320)

        self.ladoDerecho.addRow(self.respuesta3)

        self.botonBuscar = QPushButton("Buscar")

        self.botonBuscar.setFixedWidth(90)

        self.botonBuscar.setStyleSheet("background-color: #008B45;"
                                       "color: #FFFFFF;"
                                       "padding: 10px;"
                                       "margin-top: 40px;"
                                       )

        self.botonRecuperar = QPushButton("Recuperar")

        self.botonRecuperar.setFixedWidth(90)

        self.botonRecuperar.setStyleSheet("background-color: #008B45;"
                                       "color: #FFFFFF;"
                                       "padding: 10px;"
                                       "margin-top: 40px;"
                                       )

        self.ladoDerecho.addRow(self.botonRecuperar, self.botonBuscar)











        self.horizontal.addLayout(self.ladoDerecho)

        self.fondo.setLayout(self.horizontal)

    def accion_botonLimpiar(self):
        self.nombreCompleto.setText("")
        self.usuario.setText("")
        self.password.setText("")
        self.password2.setText("")
        self.documento.setText("")
        self.correo.setText("")
        self.pregunta1.setText("")
        self.respuesta1.setText("")
        self.pregunta2.setText("")
        self.respuesta2.setText("")
        self.pregunta3.setText("")
        self.respuesta3.setText("")

    def accion_botonRegistrar(self):
        self.ventanaDialogo = QDialog(None, QtCore.Qt.WindowSystemMenuHint | QtCore.Qt.WindowTitleHint)
        self.ventanaDialogo.resize(300, 150)
        self.botonAceptar = QDialogButtonBox.Ok
        self.opciones = QDialogButtonBox(self.botonAceptar)
        self.opciones.accepted.connect(self.ventanaDialogo.accept)
        self.ventanaDialogo.setWindowTitle("Formulario de registro")
        self.ventanaDialogo.setWindowModality(Qt.ApplicationModal)
        self.vertical = QVBoxLayout()
        self.mensaje = QLabel("")
        self.mensaje.setStyleSheet("background-color: #008B45; color: #FFFFFF; padding: 10px;")
        self.vertical.addWidget(self.mensaje)
        self.vertical.addWidget(self.opciones)
        self.ventanaDialogo.setLayout(self.vertical)

        self.datosCorrectos = True

        if self.password.text() != self.password2.text():
            self.datosCorrectos = False
            self.mensaje.setText("Los datos passwords no son iguales")
            self.ventanaDialogo.exec_()

        if (
                self.nombreCompleto.text() == ''
                or self.usuario.text() == ''
                or self.password.text() == ''
                or self.password2.text() == ''
                or self.documento.text() == ''
                or self.correo.text() == ''
                or self.pregunta1.text() == ''
                or self.respuesta1.text() == ''
                or self.pregunta2.text() == ''
                or self.respuesta2.text() == ''
                or self.pregunta3.text() == ''
                or self.respuesta3.text() == ''
        ):
            self.datosCorrectos = False
            self.mensaje.setText("Debe ingresar todos los campos")
            self.ventanaDialogo.exec_()

        if self.datosCorrectos:
            self.file = open('Datos/clientes.txt', 'a', encoding='UTF-8')
            self.file.write(
                f"{self.nombreCompleto.text()};{self.usuario.text()};{self.password.text()};{self.password2.text()};"
                f"{self.documento.text()};{self.correo.text()};{self.pregunta1.text()};{self.respuesta1.text()};"
                f"{self.pregunta2.text()};{self.respuesta2.text()};{self.pregunta3.text()};{self.respuesta3.text()}\n"
            )
            self.file.close()

            self.file = open('Datos/Clientes.txt', 'r', encoding='UTF-8')
            while self.file:
                linea = self.file.readline().strip()
                print(linea)
                if not linea:
                    break
            self.file.close()











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
