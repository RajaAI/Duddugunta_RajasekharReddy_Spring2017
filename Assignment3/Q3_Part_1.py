
# coding: utf-8

# # Use ‘cricket_matches’ data set. 
# # Calculate the average score for each team which host the game and win the game.

# In[ ]:

import pandas as pd
import os


# In[2]:

current = os.getcwd()   #gives current directory


# In[3]:

data_cricket = pd.read_csv(current+"//"+"Assignment3"+"//"+"cricket_matches.csv")  # reads data from the csv file


# In[4]:

data_required=data_cricket[data_cricket.home==data_cricket.winner]


# In[5]:

win_host=pd.DataFrame(data_required.groupby('home').size().reset_index()) 
win_host.columns=['Home','Number']


# In[6]:

firstinnings=data_required.groupby('home').apply(lambda x: x[x['winner']==x['innings1']]['innings1_runs'].sum())
secondinnings=data_required.groupby('home').apply(lambda x: x[x['winner']==x['innings2']]['innings2_runs'].sum())


# In[7]:

runs=firstinnings+secondinnings
runs=pd.DataFrame(runs.reset_index())
runs.columns=['Home','Score']


# In[8]:

avg_runs=pd.merge(win_host,runs)
avg_runs['Average Score']=(avg_runs['Score']/avg_runs['Number'])


# In[9]:

avg_runs=avg_runs.drop(avg_runs.columns[[1,2]],axis=1)


# In[10]:

avg_runs.head()


# In[11]:

ouput_csv = current+'\\output\\Q3_Part_1.csv'     # path for storing data


# In[12]:

avg_runs.to_csv(ouput_csv, index=False, encoding='utf-8')   # writing data to csv file


# In[ ]:



