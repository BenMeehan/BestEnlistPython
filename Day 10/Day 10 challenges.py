import re

# Exercise 1
s1 = "Intresting Facts"
s2 = "FACT 1 !@: The goldenrod crab spider can change colors between white and yellow depending on the color of the flowers on which it lives"


def check_regex(txt):
    if(("".join(re.findall("[a-zA-Z0-9]", txt)) == txt.replace(" ", ""))):
        print("The string only contains a-z, A-Z, 0-9")
    else:
        print("The string contains characters other than a-z, A-Z, 0-9")


check_regex(s1)
check_regex(s2)

# Exercise 2
s1 = "Hello abcdefg"
match = re.search("[ab]", s1)
print(match.span())


# Exercise 3
s1 = "keywords = 31"
print(re.findall("[0-9]$", s1))

# Exercise 4
s1 = "thousand 1000 hundred 100 ten 10 one 1"
pattern = ""
for i in range(1, 4):
    pattern += "[0-9]"
    print(f"Numbers of length {i}")
    print(re.search(pattern, s1))

# Exercise 5
s1 = "ABCEDE"


def cap(txt):
    x = re.search('^[A-Z]*$', txt)
    if(x):
        print("It is all upper case")
    else:
        print("It is not all upper case")


cap(s1)
cap("Abdshbh")
