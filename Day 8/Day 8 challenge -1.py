# Day 8

# Exercise 1

# import error : importing a module that does not exist
from random import abc

# index error : when index is out of range
li = [1, 2, 3, 4]
print(li[6])

# key error : when dictionary key is not found
diction = {1: 'a', 2: 'b'}
print(diction[4])

# unbound local error : when a variable is referenced before assignment


def func():
    a = a+1
    print(a)


func()

# indentation error : incorrect indentation
if True:
    a = 1
    # b = 1

# zero division error : dividing by zero

print(10/0)
