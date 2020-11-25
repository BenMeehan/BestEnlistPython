# DAY 3

#-------------------- EXERCISE 1-------------------------

dict1={1:"hello"}
dict2={2:"world"}
dict3={}
for d in (dict1,dict2):
    dict3.update(d)

print(dict3)


#--------------------------- EXERCISE 2-----------------------

del dict3[1]
print(dict3)


#----------------------------- EXERCISE 3---------------------

key_list=[1,2,3,4]
value_list=['A','B','C','D']
dict4={}

for i in range(4):
    dict4[key_list[i]]=value_list[i]

print(dict4)


#----------------------------- EXERCISE 4------------------------

set_s1={"Hello","World","!"}
print(len(set_s1))


#-------------------------------EXERCISE 5-------------------------

set_s1={1,2,3,4,'a'}
set_s2={4,5,6,7}

s1_list=list(set_s1)
s2_list=list(set_s2)

for i in set_s2:
    if i in set_s1:
        set_s1.remove(i)

print(set_s1)
