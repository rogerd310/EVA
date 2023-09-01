from config_audio import *
import os
import pyautogui
import psutil



def wind(user_input):
    match user_input:

        case "fechar janela":
            speak('Ok')
            pyautogui.hotkey('alt', 'f4')
            speak('Janela fechada')

        case 'esconder janela':
            speak('Ok')
            pyautogui.hotkey('win', 'down')
            speak('Janela minimizada')

        case 'abrir calculadora':
            speak('Ok')
            os.system('calc')
            speak('Calculadora aberta')

        case 'fechar calculadora':  # nao funciona
            speak('Ok')
            os.system("taskkill /im calc.exe /f")
            speak('Calculadora fechada')

        case "desligar o pc em meia hora":
            speak('desligando em meia hora')
            os.system("shutdown -s -t 1800")

        case "desligar o pc em uma hora":
            speak("desligando em uma hora")
            os.system("shutdown -s -t 3600")

        case "cancelar desligamento":
            speak("cancelando o desligamento")
            os.system("shutdown -a")

        case "cpu":
            speak("buscando...")
            cpu = psutil.cpu_percent()
            speak(f'cpu está em {cpu:.2f}porcento')

        case "memoria":
            speak("buscando...")
            memoryview = psutil.swap_memory()
            speak(f'memoria livre é {int(memoryview.free)}')



            
        case "fan":
            speak("buscando...")
            fan = psutil.sensors_fans()
            speak(f'a fan esta em {fan:.2f}rpm')



         




   





    

       

          



            

  



        case _:  # CASO Nenhum destes rode o código abaixo#
            print(" ")
