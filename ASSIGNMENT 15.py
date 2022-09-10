#!/usr/bin/env python
# coding: utf-8

# # SEQUENTIAL SEARCH

# In[6]:


list_1 = []
n = int(input("Enter the number of elements of list = "))
print("Enter the elements = ")
for i in range(0 , n):
    x = int(input())
    list_1.append(x)
print("The list of elements are = ",list_1)
y = int(input("Enter the target element = "))
for i in range(n):
    if list_1[i] == y:
        print("The element is found at position = ",list_1.index(y))
else:
    print("Element not found")


# # WIGGLE SORT

# In[3]:


list_1 = []
n = int(input("Enter the number of elements of list = "))
print("Enter the numbers = ")
for i in range(0 , n):
    x = int(input())
    list_1.append(x)
print("The list of elements are = ",list_1)
l = list_1.sort()
print("The Sorted list = ",l)
for i in range(0 , n-1 , 2):
    list_1[i] , list_1[i + 1] = list_1[i + 1] , list_1[i]
    print("Wiggle List = ",list_1)


# # INSERTION SORT

# In[10]:


list_1 = []
n = int(input("Enter the number of elements of list = "))
print("Enter the elements = ")
def in_sort_tion(list_1):
    for i in range(0 , n):
        x = int(input())
        list_1.append(x)
    print("The list of elements are = ",list_1)
    for i in range(1 , len(list_1)):
        key = list_1[i]
        j = i - 1
        while j >= 0 and key < list_1[j]:
            list_1[j + 1] = list_1[j]
            j = j- 1
            list_1[j + 1] = key
in_sort_tion(list_1)
for i in range(len(list_1)):
    print("",list_1[i])


#  

# In[ ]:





# In[ ]:




