#!/usr/bin/env python
# coding: utf-8

# # DETERMINANT SOLUTION FROM MATRIX

# In[29]:


mat = []
mat = [[int(input()) for i in range(2)]for j in range(2)]
print(mat)
for i in range(0 , 2):
    for j in mat[i]:
        print(j , end = " ")
    print()
det = mat[0][0] * mat[1][1] - mat[0][1] * mat[1][0]
print("Determinant = ",det)


# # CIRCLE CONDITION

# In[24]:


x1 = int(input("Enter the x-coordinate of  centre of first circle = "))
y1 = int(input("Enter the y-coordinate of centre of first circle = "))
r1 = int(input("Enter the radius of first circle = "))
x2 = int(input("Enter the x-coordinate of centre of second circle = "))
y2 = int(input("Enter the y-coordinate of centre of second circle = "))
r2 = int(input("Enter the radius of second circle = "))
import math
if(math.dist([x1,y1],[x2,y2]) > (r1 + r2)):
    print("The circles are Intersecting")
elif(math.dist([x1,y1],[x2,y2]) == (r1 + r2)):
    print("The circles are Touching")
else:
    print("The circles are not touching")


# # MULTIPLICATION

# In[27]:


import numpy
A = [[-2,1],[0,4]]
B = [[6,5],[-7,1]]
result = [[0,0],[0,0]]
result = numpy.dot(A,B)
for r in result:
    print(r)


# # STRING VALIDATION

# In[1]:


open_list = ["[","{","("]
close_list = ["]","}",")"]
def check(mystr):
    list1 = []
    for i in mystr:
        if i in open_list:
            list1.append(i)
        elif i in close_list:
            pos = close_list.index(i)
            if (len(list1) > 0) and (open_list[pos] == list1(len(list1) - 1)):
                list1.pop()
            else:
                return "Invalid"
    if len(list1) == 0:
        return "Valid"
    else:
        return "Invalid"
str_1 = input("Enter the string = ")
print(str_1,"-",check(str_1))


# In[ ]:




