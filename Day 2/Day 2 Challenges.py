# EXERCISE 1

print("Enter the values of a,b and c")
a=int(input())
b=int(input())
c=int(input())

print("a / 10 = {0}".format(a/10))
print("b * 50 = {0}".format(b*50))
print("c + 60 = {0}".format(c+60))

# EXERCISE 2

print("Enter a string with more than 2 characters : ")
str=input()
str_list=list(str)
str_list[2]='G'
new_str="".join(str_list)
print(new_str)

# EXERCISE 3

print("Enter a as an integer : ",end="")
a=int(input())
print("Enter b as a float : ",end="")
b=float(input())

a=float(a)
b=int(b)

print("Float a = {0}".format(a))
print("Integer b = {0}".format(b))