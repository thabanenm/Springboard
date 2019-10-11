#!/usr/bin/env python
# coding: utf-8

# In[1]:


## Data Story for Online Shopping Dataset


# In[2]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
data = pd.read_csv('C:/Users/michael.thabane/Documents/Springboard/Capstone1/online_shoppers_intention.csv')
data.head()


# In[3]:


# Run descriptive analysis on Data


# In[4]:


data.describe()


# In[5]:


# Examine the Variables which are harder to determine if they are Categorical and Continuous


# In[6]:


data['Administrative'].value_counts()


# In[7]:


data['Informational'].value_counts()


# In[8]:


data['SpecialDay'].value_counts()


# In[9]:


data['ProductRelated'].value_counts()


# In[10]:


### CLASSIFACTION OF VARIABLES

##### Administrative - Categorical
##### Administrative_Duration - Continuous
##### Informational - Categorical 
##### Informational_Duration - Continuous
##### ProductRelated - Continuous
##### ProductRelated_Duration - Continuous
##### BounceRates - Continuous (Percentage)
##### ExitRates - Continuous (Percentage)
##### PageValues - Continuous
##### SpecialDay - Categorical 
##### Month - Categorical
##### OperatingSystems - Categorical
##### Browser - Categorical
##### Region - Categorical
##### TrafficType - Categorical
##### VisitorType - Categorical
##### Weekend - Categorical (Boolean)
##### Revenue - Categorical (Boolean)


# In[11]:


# Convert Boolen Column to String Categorical Variable
daytype = {True : 'Weekend', False : 'Weekday'}
UserResult = {True: 'Purchase', False: 'Browse'}
data['Weekend'].map(daytype)
data['Revenue'].map(UserResult)


# In[12]:


# Count the number of Missing Values per column
data.isnull().sum()


# In[13]:


# Split the data into 2 different groups of Revenue and examine the difference in the descriptive statistics
Purchase = data[data.Revenue == True]
Browse = data[data.Revenue == False]
Purchase.describe()


# In[14]:


Browse.describe()


# In[15]:


# Histograms to see the relationship between Categorical variables and outcome of interest (Revenue)
sns.countplot(x='Weekend', hue='Revenue', data=data, palette='Set1')


# In[16]:


sns.countplot(x='Region', hue='Revenue', data=data, palette='Set1')


# In[17]:


sns.countplot(x='Browser', hue='Revenue', data=data, palette='Set1')


# In[18]:


sns.countplot(x='OperatingSystems', hue='Revenue', data=data, palette='Set1')


# In[19]:


sns.countplot(x='VisitorType', hue='Revenue', data=data, palette='Set1')


# In[20]:


sns.countplot(x='TrafficType', hue='Revenue', data=data, palette='Set1')


# In[21]:


sns.countplot(x='Month', hue='Revenue', data=data, palette='Set1')


# In[22]:


sns.countplot(x='SpecialDay', hue='Revenue', data=data, palette='Set1')


# In[23]:


# Scatter plot to see relationships between (Administrative, Administrative_Duration), (Informational, Informational_Duration), 
# (ProductRelated, ProductRelated_Duration) and the outcome of interest ------ Revenue


# In[24]:


_ = plt.scatter(x= Purchase['Administrative'], y=Purchase['Administrative_Duration'], color='b',s=6)
_ = plt.scatter(x= Browse['Administrative'], y=Browse['Administrative_Duration'], color='r',s=6)
_ = plt.xlabel('Administrative')
_ = plt.ylabel('Administrative_Duration')
plt.show()


# In[25]:


_ = plt.scatter(x= Purchase['Informational'], y=Purchase['Informational_Duration'], color='b',s=6)
_ = plt.scatter(x= Browse['Informational'], y=Browse['Informational_Duration'], color='r',s=6)
_ = plt.xlabel('Informational')
_ = plt.ylabel('Informational_Duration')
plt.show()


# In[26]:


_ = plt.scatter(x= Purchase['ProductRelated'], y=Purchase['ProductRelated_Duration'], color='b',s=6)
_ = plt.scatter(x= Browse['ProductRelated'], y=Browse['ProductRelated_Duration'], color='r',s=6)
_ = plt.xlabel('ProductRelated')
_ = plt.ylabel('ProductRelated_Duration')
plt.show()


# In[27]:


# Use bloxplots to determine if the BounceRates, ExitRates & PageValues have an effect on Revenue


# In[30]:


sns.boxplot(x='Revenue',y='BounceRates',data=data)


# In[31]:


sns.boxplot(x='Revenue',y='ExitRates',data=data)


# In[32]:


sns.boxplot(x='Revenue',y='PageValues',data=data)


# In[ ]:




