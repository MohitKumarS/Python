#!/usr/bin/env python
# coding: utf-8

# # TO CHECK THE STRING IS PALLINDROME OR NOT

# In[6]:


str1 = input("Enter the string = ")
if(str1 == str1[:: -1]):
    print("The String is Pallindrome")
else:
    print("The String is not a Pallindrome")


# # CAPITALIZE WHOLE SENTENCE

# In[15]:


str1 = input("Enter the string = ") 
if(str1.isupper()) == False:
    str1 = str1.upper()
    print(str1)
else:
    print("The string is already in capitalized form")
    print(str1)


# # TO FIND CONSONANT IN A STRING

# In[22]:


str_1 = input("Enter the string = ")
for i in str_1:
    if(i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u' or i == 'A' or i == 'E' or i == 'I' or i == 'O' or i == 'U') == False:
        print("Consonant Letter = ",i)


# # TO CHECK PERFECT SQUARE CONDITION

# In[38]:


import math
x = int(input("Enter a digit = "))
r = math.sqrt(x)
if int(r + 0.5) ** 2 == x:
    print("Perfect Square")
else:
    print("Not a Perfect Square")


# In[ ]:




