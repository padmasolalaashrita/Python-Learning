import random 
print("Wlecome to the rock, paper, scissors game")
user = input("Enter your choice: rock, paper or scissors\n")
symbol = ["rock","paper","scissors"]
game = random.randint(0,2)
computer = symbol[game]
print(f"Computer chose {computer}")

if computer == user:
    print("It's a tie.Play again!")
elif computer == "rock" and user == "paper":
    print("You won!")
elif computer == "paper" and user == "scissors":
    print("You won!")
elif computer == "scissors" and user == "rock":
    print("You won!")
elif computer == "rock" and user == "scissors":
    print("Computer Wins! Better luck next time")
elif computer == "scissors" and user == "paper":
    print("Computer Wins! Better luck next time")
elif computer == "paper" and user =="rock":
    print("Computer Wins! Better luck next time")
