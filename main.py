import speech_input
import additional_function
import webbrowser,random,os

goodbye_msg = ["goodbye for now!", "see ya later!", "pleasure to help you"]
hello_msg = ["hi","hello","hey Jarvis"]

if __name__ == "__main__":

    si = speech_input.listener_speak()
    search = additional_function.Search()
    key = additional_function.Keystroke()

    os.system("clear")

    while True:
        query = si.take_command()

        if query in ['exit', 'goodbye']:
            si.speak(goodbye_msg[random.randint(0,len(goodbye_msg)-1)])
            os.system("clear")
            exit()

        elif query in hello_msg:
            si.speak("hello there")

        if "open google" in query:
            webbrowser.open("https://www.google.com")

        elif "google" in query:
            webbrowser.open(search.get_google(query))

        elif "youtube" in query:
            webbrowser.open(search.get_youtube(query))

        elif "wikipedia" in query:
            webbrowser.open(search.get_wikipedia(query))

        elif "search this" in query:
            webbrowser.open(search.clipboard())
        
        elif "whatsapp" in query:
            webbrowser.open_new_tab("https://web.whatsapp.com/")
        
        elif "down" in query:
            key.pressdown(6)

        elif "up" in query:
            key.pressup(6)
