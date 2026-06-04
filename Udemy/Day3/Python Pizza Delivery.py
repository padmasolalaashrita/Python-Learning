print("Welcome to the python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L:")
pepperoni = input("Do you wat pepperoni on your pizza? Y for yes and N for no:")
cheese = input("Do you want extra cheese? Y or N:")

bill = 0
if size == "S":
    bill = 15
    if pepperoni =="Y":
        bill+=2
    if cheese == "Y":
        bill+=1
elif size == "M":
    bill = 20
    if pepperoni =="Y":
        bill+=3
    if cheese == "Y":
        bill+=1
elif size == "L":
    bill = 25
    if pepperoni =="Y":
        bill+=3
    if cheese == "Y":
        bill+=1

print(f"Your total bill for the pizza is {bill}")

