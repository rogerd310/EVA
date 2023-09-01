from config_audio import *
from config_sites import *
from config_program import *
from config_win import *
from per_res import *
from PyQt5.QtCore import QProcess


if __name__ == "__main__":

    speak("oi! sou a eva, como posso te ajudar?")
    print("Iniciando o programa ...")
    p = QProcess()
    p.start("python", ["EVA/tela/tela.py"])
    while True:
        user_input = recognize_speech().lower()
        program(user_input)
        sites(user_input)
        wind(user_input)
        per_res(user_input)
