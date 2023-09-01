import pyttsx3
import speech_recognition as sr
import webbrowser
import os
import pyautogui


def speak(text):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.say(text)
    engine.setProperty('rate', 200)
    engine.setProperty('volume', 1)
    engine.runAndWait()


def recognize_speech():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Aguardando sua fala...")
        audio = r.listen(source)
    try:
        print("Reconhecendo...")
        query = r.recognize_google(audio, language='pt-BR')
        print(f"Usuário disse: {query}\n")
        return query
    except Exception as e:
        print("Não entendi o que você disse.")
        return "None"


webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(
    "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"))

# Loop principal
while True:

    user_input = recognize_speech().lower()

    match user_input:  # SWITCH - FUNÇÃO USADA PARA IDENTIFICAR QUAL CASO É COMPARAVEL #

        case "parar":  # CASO ComandoFalado seja "Abrir Steam" execute o código abaixo#
            speak("Até logo!")
            break

        case "fechar janela":  # CASO ComandoFalado seja "Abrir Google" execute o código abaixo#
            speak('Ok')
            pyautogui.hotkey('alt', 'f4')
            speak('Janela fechada')

        case 'esconder janela':
            pyautogui.hotkey('win', 'down')
            speak('Janela minimizada')

        case "desligar o pc em meia hora":
            speak('desligando em meia hora')
            os.system("shutdown -s -t 1800")

        case "desligar o pc em uma hora":
            speak("desligando em uma hora")
            os.system("shutdown -s -t 3600")

        case "cancelar desligamento":
            speak("cancelando o desligamento")
            os.system("shutdown -a")

            # pesquisa
        case'pesquise no google':
            speak('O que você quer procurar?')
            search = recognize_speech()
            url = 'https://www.google.com.br/search?q=' + search
            webbrowser.get('chrome').open_new_tab(url)
            speak('Aqui está o que eu encontrei para ' + search)

        case'pesquise no youtube':
            speak('O que você quer procurar?')
            search = recognize_speech()
            url = 'https://www.youtube.com/results?search_query=' + search
            webbrowser.get('chrome').open_new_tab(url)
            speak('Aqui está o que eu encontrei para ' + search)

            # sites
        case "abrir google":
            speak("Abrindo o Google...")
            webbrowser.open("https://www.google.com.br")

        case "abrir netflix":
            speak("Abrindo Netflix...")
            webbrowser.open("https://www.netflix.com")

        case "abrir facebook":
            speak("Abrirndo Facebook...")
            webbrowser.open("https://www.facebook.com")

            # programas
        case'abrir steam':
            os.startfile("C:\Program Files (x86)\Steam\steam.exe")
            speak('Abrindo Steam...')

        case'fechar steam':
            os.system("taskkill /f /im steam.exe")
            speak('Steam fechada')

        case'abrir Silhouette':
            os.startfile(
                "C:\Program Files\Silhouette America\Silhouette Studio\Silhouette Studio.exe")
            speak('Abrindo Silhouette...')

        case'fechar ':
            os.system("taskkill /f /im Silhouette.exe")
            speak(' fechada')

        # mais

        case _:  # CASO Nenhum destes rode o código abaixo#
            print("Comando não reconhecido.")
            continue
