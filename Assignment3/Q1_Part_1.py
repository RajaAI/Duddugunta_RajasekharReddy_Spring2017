
# coding: utf-8

# # Use ‘vehicle_collisions’ data set. 
#  # Calculate the percentage of collisions in Manhattan with total accidents in New York City for the year 2016.

# In[ ]:

import os
import pandas as pd


# In[66]:

currDir = os.getcwd()  #gives current directory


# In[67]:

df = pd.read_csv(currDir+"//"+"Assignment3"+"//"+"vehicle_collisions.csv" , parse_dates=['DATE'], usecols=[0,1,3])   # reads data from the csv file


# In[68]:

dfYear = df[df.DATE.dt.year == 2016]   # filters all date for the year 2016


# In[69]:

pd.options.mode.chained_assignment = None


# In[70]:

dfYear['Month'] = dfYear['DATE'].dt.strftime('%b')


# In[71]:

NYC = dfYear['UNIQUE KEY'].groupby(dfYear['Month']).count()


# In[72]:

NYC.index = pd.CategoricalIndex(NYC.index, 
                               categories=['Jan', 'Feb', 'Mar', 'Apr','May','Jun', 'Jul', 'Aug','Sep', 'Oct', 'Nov', 'Dec'], 
                               sorted=True)
NYC = NewYorkCity.sort_index()


# In[73]:

Manhattan = dfYear['UNIQUE KEY'][dfYear['BOROUGH'] == "MANHATTAN"].groupby(dfYear['Month']).count()


# In[74]:

Manhattan.index = pd.CategoricalIndex(Manhattan.index, 
                               categories=['Jan', 'Feb', 'Mar', 'Apr','May','Jun', 'Jul', 'Aug','Sep', 'Oct', 'Nov', 'Dec'], 
                               sorted=True)
Manhattan = Manhattan.sort_index()


# In[75]:

Columns = ["Month", "Manhattan", "NYC", "Percentage"]
dataFrame = pd.DataFrame({'Month' : NYC.index, 'Manhattan' : Manhattan, 'NYC' : NYC, 'Percentage' : Manhattan / NYC})


# In[76]:

def funCheckDir(path):
    directory = os.path.dirname(path) 
    if not os.path.exists(directory):      
        os.makedirs(directory) 
        
resultsPath = currDir+'\\output\\Q1_Part_1.csv'         # path for storing data
funCheckDir(resultsPath)


dataFrame[Columns].to_csv(resultsPath, index=False, encoding='utf-8')   # writing data to csv file


# In[ ]:



