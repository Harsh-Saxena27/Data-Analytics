#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Import the python libraries for analysis

import pandas as pd
import matplotlib.pyplot as plt


# In[2]:


#Import source file

data=pd.read_excel('Visualizationdata.xlsx')


# In[4]:


data.info()


# In[5]:


data.columns


# In[6]:


data.head(3)


# In[8]:


#For check the null values in source file

data.isnull().sum()


# In[9]:


data['DESCRIPTION'].unique()


# In[13]:


update_fruit=data['DESCRIPTION']=='Dry fruits'
data.loc[update_fruit, 'DESCRIPTION']='Dryfruits'


# In[14]:


data['DESCRIPTION'].unique()


# In[15]:


data['DESCRIPTION'].value_counts()


# In[16]:


# Plot the bar graph for check the most selling product from the source

data['DESCRIPTION'].value_counts().plot(kind='bar')


# In[18]:


#Pie chart vie of the most selling product

data['DESCRIPTION'].value_counts().plot(kind='pie')


# In[20]:


data['PLACE'].value_counts().plot(kind='bar')


# In[ ]:




