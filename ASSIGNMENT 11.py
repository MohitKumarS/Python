#!/usr/bin/env python
# coding: utf-8

# # Q1

# In[15]:


import random
list1 = [random.randint(1 , 6) for i in range(501)]
dict1 = {i : list1.count(i) for i in range(1 , 7)}
print(dict1)


# # Q2

# In[17]:


import random
mat = [[random.randint(1,10) for i in range(4)]for row in range(4)]
print(mat)
for i in range(0 , 4):
    for j in mat[i]:
        print(j , end = " ")
    print()
for i in mat:
    for j in i:
        if j%2 == 0:
            print("The even numbers are = ",j)


# # Q3

# In[36]:


from math import sqrt
n = int(input("Enter a number = "))
if n > 1:
    x = int(sqrt(n))
    for i in range(2 , x + 1):
        if n%i == 0:
            print("Not a Prime Number")
            break
        else:
            print("Prime Number")
else:
    print("Not a Prime Number")


# # Q4

# In[13]:


import string
import random 
print(random.choice(string.ascii_letters))


# # Q5

# In[44]:


import random 
x = random.sample(range(1 , 100), 9)
print(x)


# In[ ]:




