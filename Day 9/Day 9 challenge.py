# Day 9

# Exercise 1
def demo(y):
    return lambda x: x*y


anonymous = demo(8)
print(anonymous(5))

# Exercise 2


def fibo(n):
    li = [0, 1]
    any(map(lambda x: li.append(sum(li[-2:])), range(0, n)))

    print(li)


fibo(5)


# Exercise 3
li = [1, 2, 3, 4, 5]
print(li)
n = int(input("Enter a number : "))
new_li = list(map(lambda x: x*n, li))
print(new_li)

# Exercise 4
li = [3, 9, 18, 4, 5, 7]
new_li = list(filter(lambda x: x % 9 == 0, li))
print(new_li)

# Exercise 5
li = [1, 2, 4, 6, 7, 8, 9, 15]
print(li)
count = len(list(filter(lambda x: x % 2 == 0, li)))
print(f"No of even numbers : {count}")
