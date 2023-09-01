from elevenlabs import set_api_key, generate, play
import pyttsx3
import speech_recognition as sr
set_api_key("sua key")


def speak(text):
  # engine = pyttsx3.init('sapi5')
  # voices = engine.getProperty('voices')
  # engine.setProperty('voice', voices[0].id)
  # engine.say(text)
  # engine.setProperty('rate', 200)
  # engine.setProperty('volume', 1)
  # engine.runAndWait()

    audio = generate(
        text=text,
        voice="Bella",
        model='eleven_multilingual_v1'
    )
    play(audio)


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
