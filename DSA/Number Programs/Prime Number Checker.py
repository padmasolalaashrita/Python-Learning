#Prime number program in python

a = int(input("Enter the number that you would like to check: "))

b = 0
for i in range (2,a-1):
    if a%i == 0:
        b = 1
        break

if b ==1:
    print("Not Prime")
else:
    print("Prime")
