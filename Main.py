
name = str(input("Hey whats good? what is ur name?"))

print(f"Nice to meet you {name}")
mood = str(input("how are you feeling?").lower())

if mood == "good": 
    print(("That is nice to hear."))

elif mood == "bad":
    print("Aw shucks, well dont worry its gonna be fine.")

else : 
    print("Oh well if you dont waant to talk about it, I understand.")

print(f"Well that was a good talk, see you later {name}")