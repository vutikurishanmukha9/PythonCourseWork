import speech_recognition as sr
import pyttsx3


engine = pyttsx3.init()
def speak(text):
    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[0].id)
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print(" Listening...")
        recognizer.pause_threshold = 1

        audio = recognizer.listen(source)

        try:
            command = recognizer.recognize_google(audio,language='en-in')
            print("🗣️🗣️ You Said:", command)
            return command.lower()
        except sr.UnknownValueError:
            print("❌❌ sorry, I did'nt understand")
            speak("Sorry, I didn't cath that")
            return
        except sr.RequestError:
            print("❌❌ Speech service error.")
            speak("Sorry, my speech service is down")
            return
    
speak("Hi, this is Your virtual Assistant. How can I help you.")
while True:
    command = listen()
    if 'play music' in command:
        speak("okay, Music is Playing...")
    elif 'reminder' in command:
        speak("reminder set to push code at 5pm")
    elif 'Geo Politic' in command:
        speak("The Indonesian government and its regional partners must respond to recent Jakarta protests with radical transparency, expanded civic pathways, and a program to restore economic opportunity. This is not only politically prudent in avoiding future conflict; it’s also a moral necessity.")

    elif 'music' in command:
        speak("Saregama padhanisa")
        
    
    elif 'exit' or 'stop' or 'bye' in command:
        speak("okay, Have good day")
        break
    else:
        speak("I don't have that access yet.")