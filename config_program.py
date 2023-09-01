from config_audio import *
import os


def program(user_input):
    match user_input:

        case'abrir Silhouette':
            try:
                os.startfile(
                    "C:\Program Files\Silhouette America\Silhouette Studio\Silhouette Studio.exe")
                speak('Abrindo Silhouette...')
            except Exception as e:
                print(e)
                speak(e)

        case'fechar Silhouette':
            os.system("taskkill /f /im Silhouette.exe")
            speak(' fechada')

        case'abrir steam':
            os.startfile("C:\Program Files (x86)\Steam\steam.exe")
            speak('Abrindo Steam...')

        case'fechar steam':
            os.system("taskkill /f /im steam.exe")
            speak('Steam fechada')

        case'abrir cpu-z':
            os.startfile("C:\Program Files\CPUID\ASUS CPU-Z\cpuz_tuf.exe")
            speak('Abrindo c-p-u-z...')

        case'fechar cpu-z':
            os.system("taskkill /f /im cpuz_tuf.exe")
            speak('c-p-e-u-z fechada')
        # mais
        case _:  # CASO Nenhum destes rode o código abaixo#
            print(" ")
