#!/usr/bin/env python
# coding: utf-8

# In[6]:


file_obj = open("sowpods.txt","r")
words = file_obj.readlines()
print(type(words))
print(str(words[0]).strip())
file_obj.close()


# # TO CHECK HOW MANY WORDS WITH 2 CONSECUTIVE U's

# In[5]:


file_obj = open("sowpods.txt","r")
words = file_obj.readlines()
for w in words:
    if 'UU' in w:
        print(w.strip())
file_obj.close()


# # NO 2 WORDS MUST BE REPEATED 

# In[1]:


import string
import time
file_obj = open("sowpods.txt","r")
words = file_obj.readlines()
start = time.time()
for alpha in string.ascii_uppercase:
    f = False
    for w in words:
        if alpha*2 in w:
            f = True
            break
    if (f == False):
        print(alpha)
print("Total Time Taken = ",time.time()-start)


# # VOWELS IN SOWPODS

# In[2]:


file_obj = open("sowpods.txt","r")
words = file_obj.readlines()
vowels = 'AEIOU'
print("Words are = ")
for w in words:
    x = 0
    for v in vowels:
        if v not in w:
            x = 1
            break
    if(x == 0):
        print(w)


# In[ ]:


file_obj = open("sowpods.txt","r")
words = file_obj.readlines()
for i in words:
    if('A' in i and 'E' in i and 'I' in i and 'O' in i and 'U' in i):
        print(i)
file_obj.close()


# # PALINDROME FROM BOTH SOWPOD AND SONNET

# In[3]:


file_obj = open("sowpods.txt","r")
words = file_obj.readlines()
print("Palindrome words of sowpods are = ")
for i in words:
    i = i.strip()
    if(i == i[::-1]):
        print(i)
file_obj.close()

file_obj2 = open("sonnet_words.txt","r")
words2 = file_obj2.readlines()
print("Palindrome words of sonnet_words are = ")
for i in words:
    i = i.strip()
    if(i == i[::-1]):
        print(i)
file_obj2.close()


# # LONGEST PALINDROME

# In[2]:


file_obj = open("sowpods.txt","r")
words = file_obj.readlines()
print("Longest Palindrome of sowpods are = ")
max = ""
for i in words:
    i = i.strip()
    if(i == i[::-1]):
        if len(i) >= len(max):
            max = i
print(max)
file_obj.close()


# # WORDS THAT ARE PRESENT IN SOWPODS BUT NOT IN SONNET

# In[4]:


file_obj = open("sowpods.txt","r")
words = file_obj.readlines()
file_obj2 = open("sonnet_words.txt","r")
words2 = file_obj2.readlines()
print("Words that are prsent in sonnet_words.txt but not in sowpods.txt are = ")
for i in words:
    i = i.strip()
    if(i == i[::-1]):
        print(i)
file_obj.close()
file_obj2.close()


# In[ ]:




