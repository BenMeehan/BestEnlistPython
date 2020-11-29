# Day 7

# Exercise 1
import sys
import random_number as rn
import pandas as pd
import numpy as np
import list_module as l

print("List Before : ", end='')
print(l.li)
l.li[0] = 100
print("List After : ", end='')
print(l.li)

# Exercise 2

s = pd.Series(np.random.randn(4))
print(s)

# Exercise 3

print(f"The random number is {rn.get_random()}")

# Exercise 4

print(sys.path)
