#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


file = "Resources/budget_data.csv"


# In[3]:


df_budget = pd.read_csv(file)
df_budget.head()


# In[4]:


# df_budget.sum(axis = 1, skipna = Flase) 
Total = df_budget['Profit/Losses'].sum()
print (Total)


# In[5]:


Total_Months = df_budget['Date'].count()
print (Total_Months)


# In[6]:


#ind = pd.date_range('01/01/2010', periods = 86, freq ='M') 
#ind
#Pct_Change=df_budget['Profit/Losses'].pct_change()
#Pct_Change.mean()
#print(Pct_Change)
df_budget['Change'] = df_budget['Profit/Losses'].diff()
#print (df_budget)
df_budget['Change'].mean()


# In[7]:


#Greatest Increase in Profits: Feb-2012 ($1926159)
Greatest_Increase=df_budget.nlargest(1,['Change']) 
print(Greatest_Increase['Change'])


# In[8]:


#Greatest Decrease in Profits: Sep-2013 ($-2196167)
Greatest_Decrease=df_budget['Change'].min()
print(Greatest_Decrease)


# In[ ]:




