print("Welcome to the tip calculator")
bill = float(input("What was the bill?\n $"))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15?\n"))
people = int(input("How many people to split the bill?\n"))

bill = (bill + (bill*(tip/100)))/people

print(bill)
