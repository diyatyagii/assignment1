#!/usr/bin/env python
# coding: utf-8

# In[27]:


n=int(input("enter a number:"))
sum=0
while n>0:
    sum=sum+n%10
    n=n//10
print("sum of digits is:",sum)


# In[ ]:




