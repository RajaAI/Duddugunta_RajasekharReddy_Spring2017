
# coding: utf-8

#  # Use 'employee_compensation' data set.
# # calculate the percentage of total benefits with respect to total compensation .

# In[ ]:

import pandas as pd
import os


# In[2]:

path=os.getcwd()   #gives current directory


# In[3]:

employee_data= pd.read_csv(path+"//"+"Assignment3/employee_compensation.csv") # reads data from the csv file


# In[4]:

employee_data=employee_data[employee_data['Year Type']=='Calendar']


# In[5]:

avg_sal=employee_data.groupby(['Employee Identifier']).mean().reset_index()


# In[6]:

extra_salary=employee_data[employee_data['Overtime']>0.05*employee_data['Salaries']]


# In[7]:

job_wise=pd.DataFrame(employee_data.groupby(['Job Family']).mean().reset_index())


# In[8]:

job_wise['Percentage']=(job_wise['Total Benefits']/job_wise['Total Compensation'])*100


# In[10]:

output=job_wise.drop(job_wise.columns[[1,2,3,4,5,6,7,8,9,10,11]],axis=1) 


# In[11]:

output.head()


# In[13]:

ouput_csv = path+'\\output\\Q2_Part_2.csv'    # path for storing data


# In[14]:

output.to_csv(ouput_csv, index=False, encoding='utf-8')   # writing data to csv file


# In[ ]:



