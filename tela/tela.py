from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import QMovie
from plyer import notification
from PyQt5.QtCore import QProcess
from rich import print

import sys
import datetime
import psutil
import time
import os


Thema = 'EVA/img/thau.gif'
Versao = 'Versão Beta v1.0'


class Janela (QMainWindow):
    def __init__(self):
        super().__init__()

        self.label_gif = QLabel(self)
        self.label_gif.setAlignment(QtCore.Qt.AlignCenter)
        self.label_gif.move(0, 0)
        self.label_gif.resize(400, 300)
        self.movie = QMovie(f"{Thema}")
        self.label_gif.setMovie(self.movie)
        self.movie.start()

        self.label_sara = QLabel(self)
        self.label_sara.setText("E.V.A")
        self.label_sara.setAlignment(QtCore.Qt.AlignCenter)
        self.label_sara.move(0, 0)
        self.label_sara.setStyleSheet(
            'QLabel {font:bold;font-size:50px;color:#FF1818}')
        self.label_sara.resize(400, 300)

        self.label_sara = QLabel(self)
        self.label_sara.setText("by: ROGER")
        self.label_sara.setAlignment(QtCore.Qt.AlignCenter)
        self.label_sara.move(160, 150)
        self.label_sara.setStyleSheet(
            'QLabel {font:bold;font-size:16px;color:#1F51FF}')
        self.label_sara.resize(100, 100)

        self.label_cpu = QLabel(self)
        self.label_cpu.setText("CPU: 32%")
        self.label_cpu.setAlignment(QtCore.Qt.AlignCenter)
        self.label_cpu.move(10, 270)
        self.label_cpu.setStyleSheet(
            'QLabel {font:bold;font-size:18px;color:#FFFF33}')
        self.label_cpu.resize(175, 20)
        cpu = QTimer(self)
        cpu.timeout.connect(self.MostrarCPU)
        cpu.start(1000)

        self.label_assv = QLabel(self)
        self.label_assv.setText("Assistente Virtual")
        self.label_assv.move(125, 5)
        self.label_assv.setStyleSheet(
            'QLabel {font:bold;font-size:14px;color:#39FF14}')
        self.label_assv.resize(300, 20)

        self.label_version = QLabel(self)
        self.label_version.setText(f"{Versao}")
        self.label_version.setAlignment(QtCore.Qt.AlignCenter)
        self.label_version.move(260, 270)
        self.label_version.setStyleSheet(
            'QLabel {font-size:18px;color:#BC13FE}')
        self.label_version.resize(131, 20)

        data = QDate.currentDate()
        datahoje = data.toString('dd/MM/yyyy')
        self.label_data = QLabel(self)
        self.label_data.setText(datahoje)
        self.label_data.setAlignment(QtCore.Qt.AlignCenter)
        self.label_data.move(285, 40)
        self.label_data.setStyleSheet('QLabel {font-size:20px;color:#39FF14}')
        self.label_data.resize(110, 20)

        self.label_horas = QLabel(self)
        self.label_horas.setText("22:36:09")
        self.label_horas.setAlignment(QtCore.Qt.AlignCenter)
        self.label_horas.move(3, 40)
        self.label_horas.setStyleSheet('QLabel {font-size:20px;color:#39FF14}')
        self.label_horas.resize(100, 20)
        horas = QTimer(self)
        horas.timeout.connect(self.MostrarHorras)
        horas.start(1000)

        botao_fechar = QPushButton("", self)
        botao_fechar.move(370, 5)
        botao_fechar.resize(20, 20)
        botao_fechar.setStyleSheet(
            "background-image : url(EVA/img/fechar.png);border-radius: 15px")
        botao_fechar.clicked.connect(self.fechartudo)

        botao_lista = QPushButton("", self)
        botao_lista.move(345, 3)
        botao_lista.resize(20, 20)
        botao_lista.setStyleSheet(
            "background-image : url(EVA/img/ListaIcone.png);border-radius: 0px;")
        botao_lista.clicked.connect(self.MostrarListaeva)

        botao_lista = QPushButton("", self)
        botao_lista.move(320, 3)
        botao_lista.resize(20, 20)
        botao_lista.setStyleSheet(
            "background-image : url(EVA/img/ListaIcone.png);border-radius: 0px;")
        botao_lista.clicked.connect(self.MostrarListacomandos)
        self.CarregarJanela()

    def MostrarListaeva(self):
        self.listac = QProcess()
        self.listac.start("python", ['EVA/tela/lista_comandos.py'])

    def MostrarListacomandos(self):
        self.listac = QProcess()
        self.listac.start("python", ['EVA/tela/lista_eva.py'])

    def CarregarJanela(self):
        self.setWindowFlag(Qt.FramelessWindowHint)  # sem botoes e titulo
        self.setGeometry(50, 50, 400, 300)
        self.setMinimumSize(400, 300)
        self.setMaximumSize(400, 300)
        self.setWindowOpacity(1)
        self.setWindowIcon(QtGui.QIcon('img/sara_icon.png'))
        self.setWindowTitle("Assistente Virtual")
        self.show()

    def fechartudo(self):
        print('Botao fechar presionado')
        sys.exit()

    def mousePressEvent(self, event):

        if event.buttons() == Qt.LeftButton:
            self.dragPos = event.globalPos()
            event.accept()

    def mouseMoveEvent(self, event):

        if event.buttons() == Qt.LeftButton:
            self.move(self.pos() + event.globalPos() - self.dragPos)
            self.dragPos = event.globalPos()
            event.accept()

    def MostrarHorras(self):
        hora_atual = QTime.currentTime()
        label_time = hora_atual.toString('hh:mm:ss')
        self.label_horas.setText(label_time)

    def MostrarCPU(self):
        try:
            usocpu = str(psutil.cpu_percent())
            self.label_cpu.setText("Uso da CPU: " + usocpu + "%")
        except KeyboardInterrupt:
            pass


aplicacao = QApplication(sys.argv)
j = Janela()
sys.exit(aplicacao.exec_())
