from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import QMovie
from plyer import notification
from PyQt5.QtCore import QProcess
from rich import print
import sys


class JanelaC (QMainWindow):
    def __init__(self):
        super().__init__()

        self.label_JG = QLabel(self)
        self.label_JG.setText("LISTA DE EVA")
        self.label_JG.setAlignment(QtCore.Qt.AlignRight)
        self.label_JG.move(5, 5)
        self.label_JG.setStyleSheet(
            'QLabel {font-size:18px; color: #000000;font:bold}')
        self.label_JG.resize(195, 20)

        ListaC = QListWidget(self)
        ListaC.setGeometry(5, 30, 290, 350)
        # ListaC.setStyleSheet('background-color:black;color:blue')
        ListaC.setStyleSheet("""
		QListWidget::item{
            color: #000000;
            background-color:transparent;}
            
		QScrollBar:vertical{       
            border:none;
            background: #F2B8B1;
            width:3px;
            margin:0px;}
            
        QScrollBar::handle:vertical{
            background: #F2BFB1;
            min-height:0px;}
            
        QScrollBar::add-line:vertical{
            background: #F2D3CD;
            height: 0px;
            subcontrol-position:bottom;
            subcontrol-origin:margin;}
            
        QScrollBar::sub-line:vertical{
            background: #F2D3CD;
            height:0px;
            subcontrol-position:top;
            subcontrol-origin:margin;}
        """)
        # sara
        ls = ['sara', 'silencio', 'retornar', 'voltar', 'sair',
              # funções
              'horas', 'bateria', 'aprenda', 'escreva',
              'criar pasta', 'remover pasta', 'renomear pasta', 'cadastro', 'data',
              'criar arquivo', 'remover arquivo', 'renomear arquivo', 'editar arquivo',
              'historico', 'quanto é', 'login',]

        mid = len(ls) // 2
        col1 = ls[:mid]
        col2 = ls[mid:]
        for item1, item2 in zip(col1, col2):
            # Remove todos os espaços em branco
            cleaned_item1 = item1.replace("", "")
            # Remove todos os espaços em branco
            cleaned_item2 = item2.replace("", "")
            ListaC.addItem(f"{cleaned_item1: <40} {cleaned_item2}")

        botao_fechar = QPushButton("", self)
        botao_fechar.move(270, 5)
        botao_fechar.resize(20, 20)
        botao_fechar.setStyleSheet(
            "background-image : url(EVA/img/fechar.png);border-radius: 15px;")
        botao_fechar.clicked.connect(self.fechartudo)

        self.CarregarJanela()

    def CarregarJanela(self):
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setGeometry(50, 50, 300, 400)
        self.setMinimumSize(300, 400)
        self.setMaximumSize(300, 400)
        self.setWindowOpacity(0.95)
        # self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setStyleSheet("background-color: #008000")
        self.setWindowIcon(QtGui.QIcon('img/sara_icon.png'))
        self.setWindowTitle("COMANDOS")
        self.show()

    def fechartudo(self):
        print('botao fechar presionado')
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


aplicacao = QApplication(sys.argv)
j = JanelaC()
sys.exit(aplicacao.exec_())
