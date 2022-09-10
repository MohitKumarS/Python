#!/usr/bin/env python
# coding: utf-8

# # RABBIT AND CHICKEN

# In[4]:


numheads = 35 
numlegs = 94
for i in range(0 , 35):
    for j in range(0 , 35):
        if 2*i + 4*j == numlegs and i + j == numheads:
            print('The number of chickens and rabbits are {0} and {1} respectively'.format(str(i),str(j)))


# # NO 2 NUMBERS IN THE LIST ARE EQUAL

# In[ ]:


x = input("Enter the 1st list = ").split()
y = input("Enter the 2nd list = ").split()
output = [(a,b) for a in x for b in y if a != b]
print(output)


# # FREQUENCY OF WORDS IN A SENTENCE

# In[22]:


str1 = input("Enter the Sentence = ")
print(str1)
str_list = str1.split()
print(str_list)
str2 = []
for i in str_list:
    if i not in str2:
        str2.append(i)
count = 0
for i in str2:
    for j in str_list:
        if i == j:
            count = count + 1
    print("{} is {}".format(i , count))
    count = 0


# In[ ]:




