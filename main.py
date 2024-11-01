import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia



listener = sr.Recognizer()
engine = pyttsx3.init()

def talk(text):
    engine.say(text)
    engine.runAndWait()

def check_command():
    try:
        with sr.Microphone() as source:
            print('listening......')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'vision' in command:
                command = command.replace('vision', '')
                print(command)
    except:
        pass
    return command

def run_vision():
    command = check_command()
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('current time is '+ time)
    elif 'get me information' in command:
        person = command.replace('get me information', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'how are you' in command:
        talk('i am doing just great sir')
    elif 'look alive' in command:
        talk('alive and healthy sir.')
    elif 'nice job well done' in command:
        talk('Happy to impress you sir, just doing my job.')
    elif 'good morning' in command:
        talk('morning sir, all system is a go.')
    elif 'good afternoon' in command:
        talk('afternoon sir, all system is looking great.')
    elif 'shutdown' in command:
        talk('shutting down.')
    elif 'evening' in command:
        talk('good evening sir, the weather looks suitable to get jobs done sir.')
    else:
        talk('sorry i did not get the sir.')

while True:
    run_vision()





run_vision()