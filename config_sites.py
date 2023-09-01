from config_audio import *
import webbrowser
import pyautogui


webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(
    "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"))


def sites(user_input):
    match user_input:

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

        case "abrir google":
            speak("Abrindo o Google...")
            webbrowser.open("https://www.google.com.br")

        case "abrir netflix":
            speak("Abrindo Netflix...")
            webbrowser.open("https://www.netflix.com")

        case "abrir youtube":
            speak("Abrindo youtube...")
            webbrowser.open("https://www.youtube.com")


        case "abrir facebook":
            speak("Abrirndo Facebook...")
            webbrowser.open("https://www.facebook.com")

        case "abrir instagram":
            speak("Abrindo Instagram...")
            webbrowser.open("https://www.instagram.com")

        case "fechar instagram":
            speak("Fechando aba do Instagram...")
        

        case _:  # CASO Nenhum destes rode o código abaixo#
            print(" ")


   



    






