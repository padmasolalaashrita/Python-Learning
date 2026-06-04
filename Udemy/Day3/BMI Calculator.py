print("=======BMI Calculator==========")
weight = float(input("Enter your weight in kgs:\n"))
height = float(input("Enter your height in m:\n"))

BMI = weight/(height **2)

if BMI <18.5:
    print("Underweight")
elif BMI>=18.5 and BMI<25:
    print("Normal weight")
elif BMI>=25:
    print("Over weight")
    
