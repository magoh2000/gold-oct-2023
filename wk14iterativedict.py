"""
Your module description
"""
sample_dict = {
    "mouth": "Mund",
    "finger": "Finger",
    "leg": "Bein",
    "hand": "Hand",
    "face": "Gesicht",
    "nose": "Nase"
}

while True:
    user_input = input("Enter a word in English or EXIT: ")
    if user_input == "EXIT":
        print("Bye!")
        break
    else:
        if user_input in sample_dict:
            print(f"Translation: {sample_dict[user_input]}")
        else:
            print("No match!")