# Day 4

# Exercise 1

# Create List
n=int(input("Enter the number of items in the list : "))
li=[]
for i in range(0,n):
    j=int(input(f'Enter element {i+1} : '))
    li.append(j)

# Add an element to the list
li.append(int(input("Enter the element to add : ")))
print("After Insertion : ")
print(li)

# Delete an element from list
r=int(input("Enter the element to delete : "))
if(li.count(r)==0):
    print("Element does not exist")
else:
    li.remove(r)
    print("After Deletion : ")
    print(li)

#Largest element
largest=li[0]
for i in range(0,len(li)):
    if(li[i]>largest):
        largest=li[i]

print(f"The largest element is {largest}")

#Smallest element
smallest=li[0]
for i in range(0,len(li)):
    if(li[i]<smallest):
        smallest=li[i]

print(f"The smallest element is {smallest}")


# Exercise 2

tup=tuple("hello")
print("The tuple is",end=" ")
print(tup)

rev_tup=tuple(reversed(tup))
print("The reversed tuple is",end=" ")
print(rev_tup)


# Exercise 3

tup_1=('a',4,5,"ben")
li_1=list(tup_1)

print("The tuple is",end=" ")
print(tup_1)

print("The list is",end=" ")
print(li_1)