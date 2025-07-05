import colorama 
from colorama import (Fore,Style)
from textblob import TextBlob
history = []
colorama.init()
print(f"{Fore.BLUE}Greetings Welcome to Sentiment Spy 😀 {Style.RESET_ALL}")
name = str(input(f"{Fore.BLACK}Enter your name {Style.RESET_ALL}"))
if not name : 
    name = "Mystery Agent"
print("Nice to meet you, lets find out the sentiment of your sentence.")
print("Type exit/reset/History to quit:")

while True:
    userinput = input(f"{Fore.CYAN} >> {Style.RESET_ALL}").strip()
    if userinput.lower=="exit":
        print(f"goodbye ✌️{name}")
        break
    elif userinput.lower() == "reset":
        history.clear()
        print("all conversation history has been wiped.")
        continue
    elif userinput.lower() == "history":
        if not history:
            print("no conversation has been conducted")
            
