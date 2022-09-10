#!/usr/bin/env python
# coding: utf-8

# # NAME ALL PRODUCTS WITH PRICES MORE THAN 10

# In[4]:


products = [{'name':'Orange','price':20},{'name':'Apple','price':8},{'name':'Banana','price':10},{'name':'Kiwi','price':30}]
print("The products with prices higher than 10 are = ")
for i in products:
    if i['price'] >= 10:
        print(i['name'])


# # FIND TOTAL PRICE OF THE LIST OF ITEMS

# In[11]:


product_quantities = []
x = 0
prices = []
y = 0
n = int(input("Enter the number of products and prices respectively = "))
for i in range(0 , n):
    x = int(input())
    product_quantities.append(x)
    print("The number of products are = ",product_quantities)
for i in range(0 , n):
    y = float(input())
    prices.append(y)
    print("The prices of products are = ",prices)
total_price = [product_quantities[i] * prices[i] for i in range(n)]
print("The total price list is = ",total_price)
total = 0
total = sum(total_price)
print("Total price of the list = ",total)


# # WINNER CANDIDATE

# In[10]:


a = input("Enter the 1st candidate ")
b = input("Enter the 2nd candidate ")
c = input("Enter the 3rd candidate ")
votes_list = []
x = 0
n = int(input("Enter the number of votes = "))
for i in range(0 , n):
    x = str(input())
    votes_list.append(x)
    print("The list of votes are = ",votes_list)
winner = min(votes_list)
print("The winner is = ",winner)

