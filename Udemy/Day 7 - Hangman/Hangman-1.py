import random 
hangman_logo = r"""
 _   _    _    _   _  ____ __  __    _    _   _
| | | |  / \  | \ | |/ ___|  \/  |  / \  | \ | |
| |_| | / _ \ |  \| | |  _| |\/| | / _ \ |  \| |
|  _  |/ ___ \| |\  | |_| | |  | |/ ___ \| |\  |
|_| |_/_/   \_\_| \_|\____|_|  |_/_/   \_\_| \_|
"""

print(hangman_logo)
print("Welcome to HANGMAN. This edition is based on modes of trnasportation")
print("""
=============================
      HANGMAN RULES
=============================

1. The computer chooses a secret word.
2. You guess one letter at a time.
3. If the letter is in the word, it is revealed.
4. If the letter is not in the word, you lose a life.
5. You have 6 lives in total.
6. Guess all the letters before your lives reach 0.


Good luck!
""")
transportation_words = [
    "car",
    "bus",
    "train",
    "bicycle",
    "motorcycle",
    "airplane",
    "helicopter",
    "submarine",
    "ship",
    "boat",
    "canoe",
    "kayak",
    "ferry",
    "tram",
    "metro",
    "scooter",
    "rickshaw",
    "taxi",
    "van",
    "truck",
    "yacht",
    "jet",
    "glider",
    "hovercraft",
    "spaceship"
]
computer_choice = random.choice(transportation_words)
print(computer_choice)
length_word = len(computer_choice)
for i in range (length_word):
    print("_",end = " ")


word = []
for i in range (length_word):
    word.append("_ ")
    #print (word)

repeat = []
life_count = 6
won = False 
while life_count >0:
    guess = input("Enter your guess ").lower()
    if guess in computer_choice:
        for i in range(length_word):
            if guess == computer_choice[i]:
                word[i] = computer_choice[i]
        answer = "".join(word)
        print(answer)
        if answer == computer_choice:
            you_win = r"""
██╗   ██╗ ██████╗ ██╗   ██╗    ██╗    ██╗██╗███╗   ██╗
╚██╗ ██╔╝██╔═══██╗██║   ██║    ██║    ██║██║████╗  ██║
 ╚████╔╝ ██║   ██║██║   ██║    ██║ █╗ ██║██║██╔██╗ ██║
  ╚██╔╝  ██║   ██║██║   ██║    ██║███╗██║██║██║╚██╗██║
   ██║   ╚██████╔╝╚██████╔╝    ╚███╔███╔╝██║██║ ╚████║
   ╚═╝    ╚═════╝  ╚═════╝      ╚══╝╚══╝ ╚═╝╚═╝  ╚═══╝
"""
            print(you_win)
            won  =True 
            life_count = 0
        
            
    else:
        life_count -= 1
        print(f"You guessed wrong! You have {life_count} more choices")
        print(answer)
if life_count == 0 and not won:

    print(r"""
  ____    _    __  __ _____    _____     _______ ____
 / ___|  / \  |  \/  | ____|  / _ \ \   / / ____|  _ \
| |  _  / _ \ | |\/| |  _|   | | | \ \ / /|  _| | |_) |
| |_| |/ ___ \| |  | | |___  | |_| |\ V / | |___|  _ <
 \____/_/   \_\_|  |_|_____|  \___/  \_/  |_____|_| \_\
""")

    print(f"The word was: {computer_choice}")

