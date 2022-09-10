#!/usr/bin/env python
# coding: utf-8

# # BINARY SEARCH

# In[ ]:


list1 = []
n = int(input("Enter the number of elements of list = "))
for i in range(0 , n):
    x = int(input())
    list1.append(x)
print("The list of elements are = ",list1)
low = 0
high = len(list1) - 1
y = int(input("Enter the required target element = "))
while low <= high:
    mid = low + (high - low) // 2
    if y == list1[mid]:
        print("The element is found ",list1.index(y))
        break
    elif y < list1[mid]:
        high = mid - 1
    else:
        low = mid + 1
else:
    print("Element not found")


# In[ ]:


def Binary_Search(list1,low,high,y):
    if low <= high:
        mid = low + (high - low) // 2
        if y == list1[mid]:
            return mid
        elif y < list1[mid]:
            return Binary_Search(list1,low,mid - 1,y)
        else:
            return Binary_Search(list1,mid + 1,high,y) 
    else:
        return -1
list1 = []
n = int(input("Enter the number of elements of list = "))
for i in range(0 , n):
    x = int(input())
    list1.append(x)
print("The list of elements are = ",list1)
list1.sort()
print("The sorted list is = ",list1)
low = 0
high = len(list1) - 1
y = int(input("Enter the required target element = "))
result = Binary_Search(list1,0,len(list1)-1,y)
if result != -1:
    print("The element is present at index = ",str(result))
else:
    print("The element is not present")


# # MAXIMUM WEIGHT

# In[1]:


list1 = [(60,10),(100,20),(120,30)]
new_list = [((i//j),j)for (i,j) in list1]
print(new_list)
n = 50
t = 0
for k in new_list:
    if n >= k[1]:
        t += k[1]*k[0]
        n = n - k[1]
    else:
        t += n*k[0]
        break
print(t)


# In[4]:


x = int(input("Enter the number = "))
Expression = lambda a,b,c : 2**a * 3**b * 5**c
for n in range(1 , x+1):
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if(Expression(i,j,k) == n):
                    print("Expression for {} is = 2**{} * 3**{} * 5**{}".format(x,i,j,k))


# In[5]:


x = int(input("Enter the number = "))
Expression = lambda a,b,c : 2**a * 3**b * 5**c
a = b = c = 0
for i in range(x):
    for j in range(x):
        for k in range(x):
            if(Expression(i,j,k) == x):
                print("Expression for {} is = 2**{} * 3**{} * 5**{}".format(x,i,j,k))
if (a == 0):
    print("No such expression for {} is found".format(x))


# In[ ]:




