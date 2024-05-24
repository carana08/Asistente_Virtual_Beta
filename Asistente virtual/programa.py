import speech_recognition as sr
import pyttsx3
import pywhatkit


name = 'alexa'
listener = sr.Recognizer()
engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    try:
        with sr.Microphone() as source:
            print('Escuchando...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice, language="es-US")
            command = command.lower()
            if name in command:
                command = command.replace(name, '')
                print(command)
    except:
        pass
    return command


def run():
    rec=listen()
    if 'reproduce' in rec:
        music = rec.replace('reproduce', '')
        talk("Reproduciendo" + music)
        pywhatkit.playonyt(music)

run()        