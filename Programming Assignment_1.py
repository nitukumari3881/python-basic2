#!/usr/bin/env python
# coding: utf-8

# In[1]:


#1. Write a Python Program to Check if a Number is Positive, Negative or Zero?
#2. Write a Python Program to Check if a Number is Odd or Even?
#3. Write a Python Program to Check Leap Year?
#4. Write a Python Program to Check Prime Number?
#5. Write a Python Program to Print all Prime Numbers in an Interval of 1-10000?


# # 1. Write a Python Program to Check if a Number is Positive, Negative or Zero?

# In[3]:


a=int(input())
if a>0:
    print("positive")
elif a< 0:
    print("negetive")
else:
    print("zero")


# # 2. Write a Python Program to Check if a Number is Odd or Even?
# 

# In[5]:


a=int(input())
if a%2==0:
    print("even")
else:
    print("odd")


# # 3. Write a Python Program to Check Leap Year?

# In[16]:



a=input("name of the year ")
b=int(a[2:3])
if b%4==0:
    print("leap year")
else:
    print(" not leap year")


# # 4. Write a Python Program to Check Prime Number?

# In[8]:


a=int(input())
if a>1:
    for i in range(2,a):
        if a%i==0:
            print(a,'composite')
            break
        else:
            print(a,'prime')
            break
        


# # 5. Write a Python Program to Print all Prime Numbers in an Interval of 1-10000?

# In[11]:


a = int(input("Enter the lower value:"))
b= int(input("Enter the upper value:"))
for i in range(a,b+1):
    if i>1:
        for j in range(2,i):
            if (i%j)==0:
                break
        else:
            print(i)


# In[ ]:




