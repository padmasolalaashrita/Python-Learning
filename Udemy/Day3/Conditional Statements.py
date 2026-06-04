print("Welcome to the rollercoaster!")
height = int(input("What is your height in cms?\n"))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster. Have a fun ride !")
    age = int(input("Enter your age\n"))
    if age<= 12:
        bill = 5
        print("Child ticket is $5")
    elif age>12 and age<18:
        bill = 7
        print("Youth ticket is $7")
    elif age>=18:
        bill =12
        print("Adult ticket is $12")
    print("Do you want your photo taken?")
    photo_taken = input("Enter n for no photo and y for taking a photo\n")
    if(photo_taken != "n"):
            bill+=3
            print(f"Your total bill is{bill}") 
    else:
            print(f"Your total bill is{bill}")
        
    
    
else:
    print("Sorry you have to grow taller before you can ride")
