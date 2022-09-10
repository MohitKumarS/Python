#!/usr/bin/env python
# coding: utf-8

# # NUMBER OF ALPHABETS IN A STRING

# In[4]:


xyz = 'A69B420C'
count = 0
for i in xyz:
    if i.isalpha():
        count = count+1
print(count)


# # PRINT STRING WITH MAXIMUM LENGTH

# In[2]:


a = input("Enter 1st string = ")
b = input("Enter 2nd string = ")
c = "The largest string is = "
if len(a) > len(b) :
    print(c,a)
elif len(b) > len(a) :
    print(c,b)
else :
    print("Both string have equal length so = \n{}\n{}".format(a,b))


# # LEAP YEAR PROGRAM

# In[8]:


year = int(input("Enter the year = "))
if(((year % 4) == 0) and ((year % 100) != 0)) or ((year % 400) == 0):
    print("Leap year")
else:
    print("Not a leap year")


# # CALCULATION OF NUMBER OF ALPHABETS AND DIGITS 

# In[16]:


sentence = 'There are 28 States in India'
digit = letter = 0
for i in sentence:
    if i.isdigit():
        digit = digit + 1
    elif i.isalpha():
        letter = letter + 1
print("Digits = ", digit)
print("Letter = ", letter)


# In[ ]:




