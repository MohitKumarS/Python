#!/usr/bin/env python
# coding: utf-8

# # NAME AND HANDLING THE EXCEPTION OF THE GIVEN PROGRAM

# In[1]:


a = 3
try:
    if a < 4:
        a = a / (a - 3)
        print(a)
except ZeroDivisionError:
    print("IT SEEMS THERE IS AN ERROR! PLEASE TRY AGAIN.")


# # NAME AND HANDLING THE EXCEPTION OF THE GIVEN PROGRAM

# In[11]:


l = [1,2,3]
try:
    print(l[3])
except IndexError:
    print("INDEX OF LIST IS OUT OF RANGE!")


# # HANDLING EXCEPTIONS FOR A GIVEN FUNTION 

# In[2]:


def my_fun(a , b):
    c = ((a+b)/(a-b))
    return c
a = int(input("Enter the value of a = "))
b = int(input("Enter the value of b = "))
try:
    void = my_fun(a , b)
except ZeroDivisionError:
    print("NOT POSSIBLE")
except TypeError:
    print("SOMETHING WENT WRONG")
except ValueError:
    print("PLEASE ENTER A VALID NUMBER")
else:
    print("Results is = ",void)


# # IMPORT ERROR AND VALUE ERROR

# In[2]:


# Import Error
try:
    import meth
except ImportError:
    print("PLEASE IMPORT A VALID MODULE!")


# In[16]:


a = input("Enter the value of a = ")
b = input("Enter the value of b = ")
try:
    c = (a + b)
    print("Results is = ",int(c))    
except ValueError:
    print("SOMETHING'S WRONG! PLEASE TRY AGAIN.")


# In[ ]:




