
# coding: utf-8

# # Use 'employee_compensation' data set. 
# #  Find out the highest paid departments in each organization group by calculating mean of total compensation for every department. 

# In[ ]:

import pandas as pd
import os


# In[2]:

current_path=os.getcwd()   #gives current directory


# In[6]:

employee_data = pd.read_csv(current_path+"//"+"Assignment3//employee_compensation.csv") # reads data from the csv file


# In[7]:

employee_data.head()


# In[8]:

grouped_data = employee_data.groupby(['Organization Group','Department']).mean().reset_index()


# In[9]:

required_data = grouped_data[['Organization Group','Department','Total Compensation']]


# In[10]:

sorted_info = required_data.sort_values(['Organization Group','Total Compensation'],ascending = [True, False])


# In[12]:

ouput_csv = current_path+'\\output\\Q2_Part_1.csv'      # path for storing data


# In[13]:

sorted_info.to_csv(ouput_csv, index=False, encoding='utf-8')     # writing data to csv file


# In[ ]:



