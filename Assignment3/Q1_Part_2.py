
# coding: utf-8

# # Use ‘vehicle_collisions’ data set. 
# # Find out distribution of each collision scale from 2015 to present

# In[ ]:

import os
import pandas as pd


# In[2]:

current = os.getcwd()    #gives current directory


# In[5]:

data = pd.read_csv(current+"//"+"Assignment3"+"//"+"vehicle_collisions.csv")   # reads data from the csv file


# In[6]:

location = data[['UNIQUE KEY','BOROUGH']]
vehicletype = data[['VEHICLE 1 TYPE','VEHICLE 2 TYPE','VEHICLE 3 TYPE','VEHICLE 4 TYPE','VEHICLE 5 TYPE']]
vehicletype = vehicletype.notnull()


# In[7]:

vehicletype = vehicletype.applymap(lambda x:1 if x else 0)
required_data = pd.concat([location,vehicletype],axis=1)


# In[8]:

total_no_of_collision = required_data.groupby('BOROUGH').sum()


# In[18]:

ordered_data = ['Borough', 'One_Vehicle', 'Two_Vehicles', 'Three_Vehicles', 'more_vehicles']
collisions_data = pd.DataFrame({'Borough' : total_no_of_collision.index, 'One_Vehicle' : total_no_of_collision['VEHICLE 1 TYPE']-total_no_of_collision['VEHICLE 2 TYPE'], 
                           'Two_Vehicles' : total_no_of_collision['VEHICLE 2 TYPE']-total_no_of_collision['VEHICLE 3 TYPE'], 'Three_Vehicles' : total_no_of_collision['VEHICLE 3 TYPE']-total_no_of_collision['VEHICLE 4 TYPE'],
                           'more_vehicles' : total_no_of_collision['VEHICLE 4 TYPE'] })


# In[13]:

ouput_csv = current+'\\output\\Q1_Part_2.csv'      # path for storing data


# In[14]:

collisions_data[ordered_data].to_csv(ouput_csv, index=False, encoding='utf-8')       # writing data to csv file


# In[ ]:



