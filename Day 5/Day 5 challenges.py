# DAY 5

# Exercise 1

def arithmetic_calculator(x,y):
    print(f"Addition of two numbers is {x+y}")
    print(f"Subtraction of two numbers is {x-y}")
    print(f"Division of two numbers is {round(x/y,2)}")
    print(f"Multiplication of two numbers is {x*y}")

x=int(input("Enter the first number : "))
y=int(input("Enter the second number : "))

arithmetic_calculator(x,y)


print("\n6-------------------------------------------\n-------------------------------------------\n")
# Exercise 2

def covid(patient_name,body_temp=98):
    print(f"The patient's name is : {patient_name}")
    print(f"Body temperature is : {body_temp}")

name=input("Enter the patient name : ")
covid(name)  # Function call with default value

print("\n-------------------------------------------\n")

temp=int(input("Enter the body temperature : "))
covid(name,temp) 
