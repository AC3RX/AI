while True:
    # 1st Component: Greet and ask for name
    name = input("Hey there, welcome to the Enhanced Chatbot Interface. What is your name? ")
    print(f"Nice to meet you, {name}!\n")

    # 2nd Component: Ask how the user is feeling
    mood = input("How are you feeling today? ").lower()

    if mood == "good":
        print("That is nice to hear.\n")
    elif mood == "bad":
        print("Aw shucks, well don't worry, it's going to be fine.\n")
    else:
        print("Oh well, if you don't want to talk about it, I understand.\n")

    # 3rd Component: Ask for hobby
    hobby = input("So, what is your hobby? ").lower()
    print(f"Well, that sounds nice. {hobby} definitely sounds fun!\n")

    # 4th Component: Ask what the user is currently doing
    activity = input("What are you doing currently?").lower()

    if activity == "scrolling through social media":
        print("That's nice to hear that you're scrolling through social media.\n")
    elif activity == "chatting with me":
        print("That's nice to hear that you're chatting with me.\n")
    elif activity == "playing games":
        print("That's nice to hear that you're playing games.\n")
    else:
        print("Hmm, that sure sounds interesting.\n")

    # 5th Component: Ask if the user wants to continue
    while True:
        continue_chat = input("Would you like to continue chatting? (yes or no): ").lower()
        if continue_chat == "yes":
            print("\nAwesome! Let's keep going!\n")
            break  # Continue the outer loop
        elif continue_chat == "no":
            print(f"\nAlright, it was nice talking to you, {name}! Have a great day! 👋")
            exit()  # Ends the program
        else:
            print("Hmm, I didn't quite catch that. Please type 'yes' or 'no'.\n")