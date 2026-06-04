print("Welcome to Treasure Island.\nYour mission is to find the treasure.\n")
print("Which way do you choose to go?\n")
direction = input("Type 'left' or 'right' to continue\n")

if direction == "left":
    print("Game Over")
    
elif direction =="right":
    print("You have come across a river. Do you want to wait for a boat or swim across?\n")
    boat = input("Type 'wait' for boat or 'swim' for swimming across\n")
    if boat == "swim":
        print("Game Over")
    elif boat == "wait":
        print("You have safely reached the island. There are three doors in front of you.\n")
        door = input("Type 'R' for Red door, 'B' for blue door, and 'Y' for yellow road\n")
        if door == "R" or door == "B":
            print("Game Over")
        elif door == "Y":
            print("You win")
