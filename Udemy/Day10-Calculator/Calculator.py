print("Welcome to the calculator program")
print("What are you calculating today?")
#Function to add
def add(number_list):
    sum = 0
    number_list = number_list.split()
    final_list = []
    for item in number_list:
        d = int(item)
        final_list.append(d)
    
    for item in final_list:
        sum = sum + item
    return sum 

    
#Function to multiply 
def multiply(number_list):
    answer = 1
    number_list = number_list.split()
    for item in number_list:
        d = float(item)
        answer = answer*d
    return answer


#Function to subtract
def subtraction(numbers_list):
    numbers_list = numbers_list.split()
    numbers_list = list(numbers_list)
    final_list = []
    for item in numbers_list:
        d = float(item)
        final_list.append(d)
    answer = final_list[0]
    final_list.pop(0)
    for item in final_list:
        answer = answer-item
    return answer


#Function to divide 
def divide(numbers_list):
    try:
        numbers_list = numbers_list.split()
        final_list = []
        for item in numbers_list:
            d = float(item)
            final_list.append(d)
        answer = final_list[0]
        final_list.pop(0)
        for item in final_list:
            answer = answer/item
        return answer
    except ZeroDivisionError:
        print("Cannot divide by zero.")
action = input("Type A to add, S to subtract, M to multiply, D to divide").lower()
if action == "a":
    numbers = input("Enter the numbers you would like to add:")
    print(add(numbers))
elif action == "s":
    numbers = input("Enter the numbers you would like to subtract:")
    print(subtraction(numbers))
elif action == "m":
    numbers = input("Enter the numbers you would like to multiply:")
    print(multiply(numbers))
elif action == "d":
    numbers = input("Enter the numbers you would like to divide:")
    print(divide(numbers))
    


        
