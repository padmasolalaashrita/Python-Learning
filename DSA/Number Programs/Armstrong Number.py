# Armstrong number program in python
a = int(input("Enter the number you would like to check: "))

b = a
sum = 0
while b!=0:
    c = b%10
    d = c ** 3
    sum = sum + d
    b = b//10

if sum == a:
    print("Armstrong Number")
else:
    print("Not Armstrong number")
    
    
