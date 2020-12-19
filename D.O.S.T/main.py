import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
# engine.say("Hello I am Dost the virtual assistant of Dostam")
def talk(text):
    engine.say(text)
    # engine.say("What can I do for you?")
    engine.runAndWait()

def your_commands():
    try:
        with sr.Microphone() as source:
            print("DOSTAMMMMM")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'dost' in command:
                command = command.replace('dost','')
                print(command)
    except:
        pass
    return command

def run_dost():
    command = your_commands()
    print(command)
    if 'play' in command:
        song = command.replace('play','')
        talk("playing"+song)
        pywhatkit.playonyt(song)

    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M:%S %p')
        print(time)
        talk('The time now is' + time)

    elif 'who is' in command:
        person = command.replace('who is','')
        info = wikipedia.summary(person, 4)
        talk(info)

    elif 'tell me a joke' in command:
        joke = command.replace('tell me a joke','')
        talk(pyjokes.get_joke())
        # talk(joke)
        return (pyjokes.get_joke)


while True:
    run_dost()