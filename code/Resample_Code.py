#!/usr/bin/env python
# coding: utf-8

# In[6]:


import pandas as pd 
import datetime as dt
import csv

industrial_consumers = pd.read_csv("D:\Study Material\DS Proejct\ds_proj-master\energy_industrial.csv")

#converting 'DateTime' column into datatype Date. 
industrial_consumers['DateTime'] =  pd.to_datetime(industrial_consumers['DateTime'], format='%Y-%m-%d')
#Selecting only Date from DateTime column, leaving the time.
industrial_consumers['Date'] = pd.to_datetime(industrial_consumers['DateTime'].dt.date)


# In[7]:


industrial_consumers['Week'] = industrial_consumers['Date'].apply(lambda x: x.week)
industrial_consumers['Month'] = industrial_consumers['Date'].apply(lambda x: x.month)
industrial_consumers['Year'] = industrial_consumers['Date'].apply(lambda x: x.year)


# In[11]:


#calculating daily consumption 
daily_consumption = industrial_consumers.groupby('Date')['Demand/Usage'].sum().reset_index()[['Date', 'Demand/Usage']]
#print(daily_consumption)

daily_consumption.to_csv("daily_consumption.csv", sep=",", index=False)


# In[12]:



weekly_consumption = industrial_consumers.groupby([(industrial_consumers.Week)])['Demand/Usage'].sum().reset_index()[['Week', 'Demand/Usage']]
#print(weekly_consumption)
#one issue which is to be solved: it calculates from week 1 instead of week 20 of 2017 (2017-05-18 is week 20)

weekly_consumption.to_csv("weekly_consumption.csv", sep=",", index=False)


# In[13]:


#calculating monthly consumption while taking into account both the month and year. Kept May 2017 and May 2018 separate. 
monthly_consumption=industrial_consumers.groupby([(industrial_consumers.Month),(industrial_consumers.Year)]).sum().reset_index()[['Month','Year', 'Demand/Usage']].sort_values(["Year"])
#print(monthly_consumption)

monthly_consumption.to_csv("monthly_consumption.csv", sep="," , index=False)


# In[198]:


import matplotlib.pyplot as plt
plt.plot(weekly_consumption)
plt.show()


# In[199]:


plt.plot(monthly_consumption)
plt.show()


# In[17]:





# In[ ]:





# In[ ]:




