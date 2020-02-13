#!/usr/bin/env python
# coding: utf-8

#Run Time Terror
#CS483 Project 1
get_ipython().run_line_magic('matplotlib', 'inline')
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

def futureValue(filePath, companyName, startDateIndex):
    '''
    futureValue(string, string, integer) -> void

    The function takes the location of the .csv file (filePath)
    and the name of the stock (companyName) in that file and the
    start date (startDateIndex) to be considered.

    The function then plots a graph and regression line for the stock
    along with a predicted closing value of the stock after 3 weeks
    '''

    #read input from file
    df = pd.read_csv(filePath)
    x = np.arange(startDateIndex,len(df))
    y = df['Close'].values
    y = y[startDateIndex:]

    # initializing a LinearRegression object
    linreg = LinearRegression()
    x = x.reshape(-1,1)
    linreg.fit(x,y)

    #printing predicted values of the stock
    print(companyName, "stock in 3 weeks:" , linreg.predict(np.array([21 + len(df) - 1]).reshape(-1,1)))
    y_pred = linreg.predict(x)
    plt.plot(x,y,color='green')
    plt.plot(x,y_pred,color='red')
    plt.show()



def getDate(filePath, startDateIndex):
    df = pd.read_csv(filePath)
    y = df['Date'].values
    print(y[startDateIndex], "-" , y[len(df)-1])


# In[31]:


futureValue("/home/caleb/CS483/csv_files/AAPL.csv","Apple", 1100)
getDate("/home/caleb/CS483/csv_files/AAPL.csv",1100)


# In[19]:


futureValue("/home/caleb/CS483/csv_files/AMD.csv", "AMD", 1150)


# In[20]:


futureValue("/home/caleb/CS483/csv_files/AMZN.csv", "Amazon",0)


# In[21]:


futureValue("/home/caleb/CS483/csv_files/DOW.csv", "Dow Jones Industrial Average",0)


# In[22]:


futureValue("/home/caleb/CS483/csv_files/IXIC.csv", "Nasdaq Composite",0)


# In[23]:


futureValue("/home/caleb/CS483/csv_files/NVDA.csv", "NVIDIA",0)


# In[24]:


futureValue("/home/caleb/CS483/csv_files/S.csv", "Sprint",0)


# In[25]:


futureValue("/home/caleb/CS483/csv_files/TMUS.csv", "T-Mobile",0)


# In[26]:


futureValue("/home/caleb/CS483/csv_files/TSLA.csv", "Tesla", 1210)


# In[27]:


futureValue("/home/caleb/CS483/csv_files/NFLX.csv", "Netflix",0)


# In[ ]:





# In[ ]:





# In[ ]:
