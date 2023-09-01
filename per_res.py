from config_audio import *
import os
import time

def per_res(user_input):
    match user_input:

        case'preciso de ajuda':
            speak("Sim senhor, ao seu serviço")

        case 'como você foi feita':
            speak("meu mestre me constrói em IA")

        case 'quem fez você':
            speak('Fui criado pelo meu mestre de IA em dois mil e vinte e trez')    

        case 'quem está te criando':
            speak('roger é meu mestre. Ele está me criando') 

        case 'qual é seu nome':
            speak('Meu nome é EVA')

        case 'o que significa eva':
            speak('E.V.A significa APENAS UM SISTEMA MUITO INTELIGENTE')

        case 'quem são seus amigos':
            speak('Meus amigos são assistentes do Google Alexa e Siri') 

        case "fechar":
            speak("yamete kudasai oni chan")
            speak("yaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa!!!!!!!!!!!!!!!!!!!!!!!!!!")


        case "sair":
            speak("Iniciando sequência de autodestruição!!!! Agora você vai tomar no olho da goiaba")
            contagem = ["zero!", "um!", "dois!", "três!", "desligando suporte a vida!", "quatro!", "cinco!"]

            index = len(contagem) - 1

            while index > 0:
                time.sleep(1)
                speak(contagem[index])
                index -= 1
                        


            


               