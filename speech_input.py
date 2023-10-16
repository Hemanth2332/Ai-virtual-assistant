import speech_recognition as sr
import pyttsx3

class listener_speak:

    def __init__(self):
        self.r = sr.Recognizer()
        self.engine = pyttsx3.init()

    def take_command(self) -> str:

        with sr.Microphone() as source:
            print("Listening...")
            self.r.pause_threshold = 1
            audio = self.r.listen(source)
        try:
            print("Recognizing...")    
            query = self.r.recognize_google(audio)
            print(f"User said: {query}\n")

        except:    
            print("Say that again please...\n") 
            return "None"

        return str(query).lower()


    def speak(self, audio:str):
        voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', voices[14].id)
        self.engine.setProperty('rate', 165)
        self.engine.say(audio)
        self.engine.runAndWait()
