# DAY 6

# Exercise 1
li=[1,2,3,4]
print("The original list is : ",end=" ")
print(li)
for i in range(0,len(li)):
    li[i]=li[i]+2

print("List after adding 2 to each element : ",end=" ")
print(li)

# Exercise 2
n=int(input("Enter a number : "))
while (n>0):
    t=n
    for i in range(0,n):
        print(t,end="")
        t-=1
    print("\n")
    n-=1

# Exercise 3
n=int(input("Enter the number : "))
a=0
b=1
print(a,end=", ")
print(b, end=", ")
while(n>0):
    a=a+b
    b=a+b
    print(a,end=", ")
    print(b, end=", ")
    n-=1

# Exercise 4
def amstrong(temp):
    sum=0
    while(temp>0):
        digit=temp%10
        sum=sum+(digit**3)
        temp=temp//10
    return sum

n=int(input("Enter a number : "))
sum=amstrong(n)

if(sum==n):
    print(f"{n} is a amstrong number")
else:
    print(f"{n} is not a amstrong number")


# Exercise 5
n=int(input("Enter how many multiples of 9 : "))
print("The multiplication table for 9 is : ")
for i in range(1,n+1):
    print(f"{i} x 9 = {i*9}")


# Exercise 6
n=int(input("Enter a number to check : "))
if(n<0):
    print("It is negative")
else:
    print("It is positive")


# Exercise 7
days=int(input("Enter the number of days : "))
years=days//365
months=(days%365)//30
weeks=((days%365)%30)//7
print(f"The age is {years} years, {months} months and {weeks} weeks")


# Exercise 8
import math

n=int(input("Enter a degree : "))

print(f"The sin of {n} is {round(math.sin(math.radians(n)),1)}")
print(f"The cos of {n} is {round(math.cos(math.radians(n)),1)}")


# Exercise 9
a=int(input("Enter the first number : "))
b=int(input("Enter the second number : "))
op=input("Enter the operation + , - , * , / , % : ")

if(op=='+'):
    print(f"{a} + {b} = {a+b}")
elif(op=='-'):
    print(f"{a} - {b} = {a-b}")
elif(op=='*'):
    print(f"{a} * {b} = {a*b}")
elif(op=='/'):
    print(f"{a} / {b} = {a/b}")
elif(op=='%'):
    print(f"{a} % {b} = {a%b}")


