#!/usr/bin/env python
# coding: utf-8

# # LONGEST COMMON PREFIX

# In[3]:


str1 = input("Enter the 1st string = ")
str2 = input("Enter the 2nd string = ")
z = zip(str1 , str2)
for i,j in list(z):
    if i == j:
        print(i , end = '')


# # TO FIND LIST OF SPEEDS FROM LISTS OF DISTANCES AND TIME

# In[4]:


dist = []
time = []
n1 = int(input("Enter the number of distances in the list = "))
for i in range(0 , n1):
    x = int(input())
    dist.append(x)
    print("The entered distance list are = ", dist)
n2 = int(input("Enter the number of time in the list = "))
for i in range(0 , n2):
    y = int(input())
    time.append(y)
    print("The entered time list are = ", time)
speed = []
for i,j in zip(dist , time):
    speed.append(i/j)
print("The required list of speeds are = ",speed)


# # TRIANGLE PROBLEM

# In[5]:


a = int(input("Enter the side of triangle = "))
b = int(input("Enter the side of triangle = "))
c = int(input("Enter the side of triangle = "))
if (a+b) > c  or (b+c) > a or (c+a) > b:
    print("Triangle is Valid")
    if a==b and b==c:
        print("Triangle is Equilateral")
    elif a==b or b==c or c==a:
        print("Triangle is Isosceles")
    elif a*a+b*b == c*c or a*a+c*c == b*b or b*b+c*c == a*a:
        print("Triangle is Right Angled")
    else:
        print("Triangle is Scalene")
else:
    print("Triangle is Invalid")

