# Day 11

# Exercise 1
li1 = (1, 2, 3, 4)
li2 = ("Apple Juice", "Vinegar", "Baking Soda", "Flour")
print("List 1 : ", end="")
print(li1)
print("List 2 : ", end="")
print(li2)
merged = zip(li1, li2)
print("List of tuples : ", end="")
print(list(merged))

# Exercise 2
li = ["Charmander", "Cyndaquil", "Torchic", "Chimchar",
      "Tepig", "Fennekin", "Litten", "Scorbunny"]
ran = []

for i in range(1, 9):
    ran.append(i)
merged = list(zip(ran, li))
print("Given list : ", end="")
print(li)
print("Range list : ", end="")
print(ran)
print("Merged list : ", end="")
print(merged)

# Exercise 3
li = ['e', 'i', 'u', 'a', 'o']
print(sorted(li))

# Exercise 4
li = [1, 2, 3, 4, 5, 6, 7, 8, 9]
new_li = list(filter(lambda x: x % 2 != 0, li))
print(new_li)
