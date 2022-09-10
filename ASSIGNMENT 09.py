#!/usr/bin/env python
# coding: utf-8

# # FIBONACCI SERIES

# In[2]:


n = int(input("Enter the number = "))
def Fibonacci(n):
    if n < 0:
        print("Wrong Input")
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)
print(Fibonacci(n))


# # CREATING CUSTOM ADD FUNTION AND ADDING ELEMENTS PRESENT IN LIST

# In[3]:


digits = []
n = int(input("Enter the number of digits = "))
for i in range(0 , n):
    x = int(input())
    digits.append(x)
    print("The list of numbers are = ",digits)
def My_Add(digits):
    for sum_ in range(0 , n):
        sum_ = 0
        sum_ = sum_ + sum(digits)
        return sum_
summation = My_Add(digits)
print(summation)


# # MATRIX PROBLEM

# In[19]:


table = [list("abcd") , list("efgh") , list("ijkl")]
def mat(table):
    x = str(input("Enter the target character = "))
    for i in range(0 , 4):
        for j in range(0 , 4):
            loc = table[i]
            if(x == loc[j]):
                return(i+1 , j+1)
            else:
                print("Not Found")
print("The position of the given character is = ",mat(table))


# # CONVERT STRING INTO A DICTIONARY OF LETTER COUNT  

# In[44]:


str1 = input("Enter a sentence = ")
str_split = str1.split()
d = {}
for word in str_split: 
    if word not in d.keys():
        d[word] = len(word)
print(d)

