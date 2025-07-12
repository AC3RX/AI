import random
from colorama import Fore, init

# Initialize colorama
init(autoreset=True)

# Define destination categories
destinations = {
    "beaches": ["Maldives", "Bali", "Bahamas", "Maui"],
    "mountains": ["Swiss Alps", "Rocky Mountains", "Himalayas", "Andes"],
    "cities": ["New York", "Tokyo", "Barcelona", "Paris"]
}

# Sample jokes
jokes = [
    "Why don't scientists trust atoms? Because they make up everything!",
    "Why don’t skeletons fight each other? They don’t have the guts.",
    "I told my suitcase we’re not going on vacation. Now I’m dealing with emotional baggage."
]

# Packing tips
packing_tips = {
    "beaches": ["Don't forget sunscreen and flip-flops!", "Pack a hat and swimwear!"],
    "mountains": ["Take warm clothes and hiking boots!", "Pack energy bars and a first-aid kit."],
    "cities": ["Bring comfy walking shoes!", "Don’t forget a travel adapter and portable charger."]
}

def tell_joke():
    print(Fore.MAGENTA + "\nTravelBot: Here's a joke for you 😄")
    print(Fore.MAGENTA + random.choice(jokes))

def give_packing_tips(category):
    print(Fore.BLUE + f"\nTravelBot: Packing tips for {category.capitalize()}:")
    for tip in packing_tips.get(category, ["Just bring your adventurous spirit!"]):
        print(Fore.BLUE + f"- {tip}")

def normalize_input(text):
    return text.lower().strip()

def interpret_preference(user_input):
    for category in destinations.keys():
        if category in user_input or category[:-1] in user_input:
            return category
    return None

def ask_to_continue():
    print(Fore.CYAN + "\nWould you like more travel help? (yes/no)")
    try:
        response = normalize_input(input(Fore.YELLOW + "You: "))
    except Exception:
        return False
    return "yes" in response

def check_special_requests(user_input):
    if "joke" in user_input:
        tell_joke()
        return True
    for category in destinations.keys():
        if (category in user_input or category[:-1] in user_input) and ("tip" in user_input or "pack" in user_input):
            give_packing_tips(category)
            return True
    return False

def recommend():
    print(Fore.CYAN + "Hey there! 🌍 Looking to get away? I can help you pick the perfect escape.")

    while True:
        print(Fore.CYAN + "\nWhat are you in the mood for? Beaches, Mountains, or Cities?")
        print(Fore.CYAN + "(Or type something like 'give me packing tips for beaches' or 'tell me a joke')")

        try:
            preference_raw = input(Fore.YELLOW + "You: ")
        except Exception:
            print(Fore.RED + "Oops! Something went wrong with your input.")
            break

        normalized_input = normalize_input(preference_raw)

        if check_special_requests(normalized_input):
            if not ask_to_continue():
                print(Fore.CYAN + "\nTravelBot: Safe travels! 🌟 Come back when wanderlust strikes again.")
                break
            continue

        preference = interpret_preference(normalized_input)

        if preference:
            suggestion = random.choice(destinations[preference])
            print(Fore.GREEN + f"\nHow about this: {suggestion}? Sounds like your vibe. 🌴🏔️🏙️")

            print(Fore.CYAN + "Do you like this suggestion? (yes/no)")
            try:
                feedback = normalize_input(input(Fore.YELLOW + "You: "))
            except Exception:
                print(Fore.RED + "Got a bit lost there! Let's try again.")
                continue

            if "yes" in feedback:
                print(Fore.GREEN + f"\nSweet! {suggestion} it is! ✈️")
                give_packing_tips(preference)
                tell_joke()
            elif "no" in feedback:
                print(Fore.RED + "\nFair enough! Let me think of something else...")
                continue
            else:
                print(Fore.YELLOW + "\nHmm, I’ll take that as a maybe. Let’s keep exploring!")

        else:
            print(Fore.RED + "Hmm, I didn’t quite catch that. Try something like 'I want the beach' or 'I'm into cities'.")

        if not ask_to_continue():
            print(Fore.CYAN + "\nTravelBot: Safe travels! 🌟 Come back when wanderlust strikes again.")
            break

# Run the bot
if __name__ == "__main__":
    recommend()
