#!/usr/bin/env python
# coding: utf-8

# In[2]:


conda install numpy


# In[5]:


pip install np


# In[7]:


import numpy as np


# In[15]:


a = np.arange(100).reshape(10,10)
a


# In[16]:


a = np.arange(27).reshape(3,3,3)
a


# In[17]:


a = np.arange(27).reshape(3,3,3)
print(a.ndim) # number of dimension/rank 3d
print(a.shape)# number of axis in each dimension
print(a.size)# number elements
a


# In[18]:


a = np.arange(3*3*3).reshape(3,3,3)
print(a.ndim) # number of dimension/rank 3d
print(a.shape)# number of axis in each dimension
print(a.size)# number elements
a


# In[19]:


# 4 pictures resoulation 8x8
a = np.arange(4*8*8).reshape(4,8,8)
a


# In[20]:


np.random.randint(0,255,10*8*8)


# In[21]:


np.random.randint(0,255,(10,10,10))


# In[22]:


a = np.array((1,2,3))
print(a)
display(a)


# # How to create a basic array

# * np.array()
# * np.zeros()
# * np.ones()
# * np.empty()
# * np.arange()
# * np.linspace()

# In[26]:


display(np.zeros(10))
display(np.ones(10))
display(np.empty(10))


# In[30]:


np.linspace(1,60,3) #60 = km and 2 = hours


# In[31]:


np.ones((10,10),dtype="str")


# In[33]:


arr = np.array([1,2,3,4,5,69,7,55,3,4,44])
np.sort(arr)


# # arg

# In[34]:


#    0 1 2 3 4 5
a = np.array([1,7,20,0,4,3])
print(np.argmax(a))
print(np.argmin(a))
print(np.argsort(a))


# In[37]:


labels = ['cat','dog','apple','orange']
prediction = [15,10,70,5]
index = np.argmax(prediction) # max index probablity
print(labels[index])


# # concatinatio

# In[39]:


a = np.arange(1,11).reshape(5,2)
b = np.arange(11,21).reshape(5,2)
np.concatenate((a,b))


# In[40]:


np.stack((a,b),axis=1)


# In[41]:


np.hstack((a,b))


# In[42]:


np.vstack((a,b))


# In[ ]:




