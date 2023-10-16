import speech_recognition as sr
import urllib.parse,pyperclip
import pyautogui

class Search:

    def search_engine_remover(self, query:str, search_engine:str) -> str:
        result = query.lower().split()
        for i,j in enumerate(result):
            if j == search_engine.lower():
                result.pop(i)

        result = " ".join(result)
        return result

    def get_youtube(self, user_query:str) -> str:
        output = urllib.parse.quote(self.search_engine_remover(user_query,"youtube"))
        return f"https://www.youtube.com/results?search_query={output}"

    def get_google(self, user_query:str) -> str:
        output = urllib.parse.quote(self.search_engine_remover(user_query,"google"))
        return f"https://www.google.com/search?q={output}"


    def get_wikipedia(self, user_query:str) -> str:
        output = self.search_engine_remover(user_query,"wikipedia")
        return f"https://en.wikipedia.org/wiki/{urllib.parse.quote(output)}"


    def clipboard(self) -> str:
        output =  pyperclip.paste()
        return f"https://www.google.com/search?q={urllib.parse.quote(output)}"
        


class Keystroke:

    def pressdown(self, n:int):
        for _ in range(n+1):
            pyautogui.press("down")

    def pressup(self, n:int):
        for _ in range(n+1):
            pyautogui.hotkey("up")
