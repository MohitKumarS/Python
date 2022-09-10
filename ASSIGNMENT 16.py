#!/usr/bin/env python
# coding: utf-8

# In[10]:


try:
    x = float(input("Enter the x-coordinate of circle = "))
    y = float(input("Enter the y-coordinate of circle = "))
    r = float(input("Enter the radius of circle = "))
    import math
    class Circle:
        def _init_(cl,r,ci_co):
            cl.x = x
            cl.y = y
            cl.r = r
            cl.ci_co = ci_co
        def area_(cl,a):
            cl.a = math.pi*cl.r**2
            return area_(cl.a)
        def perimeter_(self,p):
            cl.p = 2*math.pi*cl.r
            return perimeter_(cl.a)
        def centre_origin_dist(cl,cd):
            cl.cd = math.dist(origin,cl.ci_co)
            return centre_origin_dist(cl.cd) 
        def circum_dist_origin(cl,ci_co):
            if(math.dist(origin,cl.ci_co)) > cl.r:
                return math.dist(origin,c.ci_co) - c.r
            else:
                return cl.r - math.dist(origin,cl.ci_co)
    ci_co = (x,y)
    origin = (0,0)
    c = Circle(r,ci_co)
    print("Area of circle = ",c.area_())
    print("Perimeter of circle = ",c.perimeter_())
    print("Distance of centre of circle to origin = ",c.centre_origin_dist())
    print("Distance of outside of circle to origin = ",c.circum_dist_origin())
except ValueError:
    print("PLEASE ENTER A VALID NUMBER")
except NameError:
    print("PLEASE ENTER A VALID NAME")
except TypeError:
    print("NOT POSSIBLE")


# # SUBSET OF A SET

# In[4]:


class sets:
    import itertools
    def subsets(list1 , n):
        n = int(input("Enter the number of elements = "))
        for i in range(0 , n):
            x = int(input())
            list1.append(x)
            print("The list of elements = ",list1)
        return itertools.combinations(list1 , n)


# In[19]:


try:
    class subset:
        def sub_lists(self,l1):
            lists=[[]]
            for i in range(len(l1)+1):
                for j in range(i):
                    lists.append(l1[j:i])
            return lists
except ValueError:
    print("PLEASE ENTER A VALID NUMBER")
else:
    l1=[4,5,6]
    print(subset().sub_lists(l1))


# In[16]:


#Q-3
class triplet:
    def threesum(self ,lst):
        found = False
        a= []
        for i in range(n-2):
            b= []
            for j in range(i+1,n-1):
                for k in range(j+1,n):
                    if(lst[i]+lst[j]+lst[k] == 0):
                        found =True
                        b.append(lst[i])
                        b.append(lst[j])
                        b.append(lst[k])
                        a.append(b)
        if found==True:
            return a
        if found==False:
            return("Not found")
lst=[]
n=int(input("Enter number of elements of list: "))
for i in range(0,n):
    b=int(input("Enter  element: "))
    lst.append(b)
print(triplet().threesum(lst))


#  
