import colorama
from colorama import Fore, Style
from textblob import TextBlob
from datetime import datetime

# Initialize colorama
colorama.init(autoreset=True)

# Greeting
print(f"{Fore.BLUE}Greetings! Welcome to Sentiment Spy 😀{Style.RESET_ALL}")
name = input(f"{Fore.BLACK}Enter your name: {Style.RESET_ALL}").strip()
if not name:
    name = "Mystery Agent"

print(f"\nNice to meet you, {name}! Let's find out the sentiment of your sentence.")
print("Type 'exit', 'reset', 'history', or 'export' to perform special actions.\n")

# History log
history = []

while True:
    user_input = input(f"{Fore.CYAN}>> {Style.RESET_ALL}").strip()

    if user_input.lower() == "exit":
        print(f"{Fore.YELLOW}Goodbye ✌️, {name}! Stay curious.{Style.RESET_ALL}")
        break

    elif user_input.lower() == "reset":
        history.clear()
        print(f"{Fore.RED}All conversation history has been wiped.{Style.RESET_ALL}")
        continue

    elif user_input.lower() == "history":
        if not history:
            print(f"{Fore.YELLOW}No conversation has been conducted yet.{Style.RESET_ALL}")
        else:
            print(f"{Fore.GREEN}Conversation History:{Style.RESET_ALL}")
            for item in history:
                print(f"[{item['time']}] {item['text']} → Sentiment: {item['sentiment']} (Polarity: {item['polarity']:.2f})")
        continue

    elif user_input.lower() == "export":
        if not history:
            print(f"{Fore.YELLOW}Nothing to export! History is empty.{Style.RESET_ALL}")
        else:
            filename = f"sentiment_history_{name.replace(' ', '_')}.txt"
            with open(filename, 'w') as f:
                for item in history:
                    f.write(f"[{item['time']}] {item['text']} → Sentiment: {item['sentiment']} (Polarity: {item['polarity']:.2f})\n")
            print(f"{Fore.GREEN}History exported successfully to {filename}{Style.RESET_ALL}")
        continue

    # Analyze sentiment
    blob = TextBlob(user_input)
    polarity = blob.sentiment.polarity

    if polarity > 0.1:
        sentiment = "Positive 😊"
    elif polarity < -0.1:
        sentiment = "Negative 😞"
    else:
        sentiment = "Neutral 😐"

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    history.append({
        'text': user_input,
        'sentiment': sentiment,
        'polarity': polarity,
        'time': timestamp
    })

    print(f"{Fore.MAGENTA}Sentiment Detected: {sentiment}")
    print(f"Polarity Score: {polarity:.2f}{Style.RESET_ALL}\n")

            