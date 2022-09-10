#!/usr/bin/env python
# coding: utf-8

# # NUMBER IS PRESENT IN LIST OR NOT

# In[4]:


list_1 = [1,2,3,4,5,6]
n = int(input("Enter the number = "))
if n in list_1:
    print("Element Exists")
else:
    print("Element doesn't Exist")


# # SUBSTRING IS PRESENT IN STRING WITHOUT USING in OPERATOR

# In[3]:


str1 = input("Enter a string = ")
x = input("Enter the substring = ")
if str1.find(x) == -1:
    print("Substring is not present in given string")
else:
    print("Substring present in given string")


# # REMOVING DUPLICATE VALUES RESERVING ORIGINAL ORDER

# In[2]:


list_1 = []
x = 0
n = int(input("Enter the number of element in the list = "))
for i in range (0 , n):
     x = int(input("Enter Elements = "))
     list_1.append(x)
print("Entered List is = ", list_1)
l = len(list_1)
for i in range (l-1 , 0 , -1):
    if(list_1.count(list_1[i]) > 1):
        list_1.pop(i)
    print("Modified list is = ", list_1)


# # FIND nTH LARGEST NUMBER

# In[5]:


listA = [11,36,69,24,87,2,96]
n = int(input("Enter the number = "))
listA.sort()
print(listA[-n])


# In[ ]:




