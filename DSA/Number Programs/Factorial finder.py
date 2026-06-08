#Factorial Program in Python
a =int(input("Enter the number you want to find the factorial of: "))
fact = 1

while a!=0:
    fact = fact * a
    a = a-1

print(fact)
