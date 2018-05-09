
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# In[2]:


import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[3]:


#Read in csv files:
crime4 = pd.read_csv('Chicago_Crimes_2012_to_2017.csv')


# In[4]:


crime4.head()


# In[5]:


crime4.columns


# # EDA
There are currently too many columns, take long time to load. Try to get rid of some columns 
# In[6]:


crime4['Arrest'].value_counts()
#drop this column


# In[7]:


crime4['Domestic'].value_counts()
#drop this column


# In[ ]:


crime4['Location'].value_counts()
#'Location' column contains (lat,long) --> drop lat, long columns


# In[8]:


#List of columns to drop
drop_list = ['Unnamed: 0','Arrest', 'Domestic','Latitude', 'Longitude', 'Updated On']


# In[9]:


crime4.drop(drop_list, axis = 1, inplace= True)


# In[10]:


#Plot top 5 charge types ('Primary Type')
plt.figure(figsize = (15,5), dpi=70)
sns.countplot(x= crime4['Primary Type'], order = crime4['Primary Type'].value_counts().iloc[:5].index)
#https://stackoverflow.com/questions/32891211/limit-the-number-of-groups-shown-in-seaborn-countplot


# # Goal: group charges into top 5 primary type, the rest will be grouped as "OTHERS"

# In[11]:


#5 primary types:
crime4['Primary Type'].value_counts().head(5).index.tolist()
#https://stackoverflow.com/questions/35523635/extract-values-in-pandas-value-counts


# In[12]:


crime4['Primary Type'].nunique()


# In[13]:


#Total of 33 unique values, 5 top --> 33-5 = 28 tails
#List of values that will be re-assign as "OTHERS"
other_list = crime4['Primary Type'].value_counts().tail(28).index.tolist()


# In[14]:


crime4['Primary Type'].replace(to_replace = other_list, value = 'OTHERS', inplace = True)


# In[15]:


crime4['Primary Type'].value_counts()


# In[16]:


plt.figure(figsize =(15,7))
sns.countplot(crime4['Primary Type'])


# In[17]:


#Plot by Year:
plt.figure(figsize = (10,5))
sns.countplot('Year', data = crime4, palette = "muted")


# In[18]:


#Plot by year with primary type as hue:
plt.figure(figsize = (15,7))
sns.countplot('Year', data = crime4, hue = 'Primary Type', palette = "muted")


# In[ ]:


#Plot by year using pandas built-in function:
#crime4['Year'].plot.bar()
#doesn't work very well


# In[21]:


#Date column:
type(crime4['Date'].iloc[0])


# In[22]:


#Convert date column to date format:
crime4['Date'] = pd.to_datetime(crime4['Date'])
#takes awhile to load


# In[23]:


type(crime4['Date'].iloc[0])


# In[24]:


#organize data into months:
crime4['Month'] = crime4['Date'].apply(lambda time: time.month)


# In[25]:


crime.head()


# In[35]:


#Plot by month:
plt.figure(figsize = (10,4))
sns.countplot(x= 'Month', data = crime4, hue = 'Primary Type')


# In[31]:


sns.distplot(crime4['Month'], kde = False)

