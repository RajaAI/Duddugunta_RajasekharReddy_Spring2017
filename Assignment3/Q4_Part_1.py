
# coding: utf-8

# 
# # Use ‘movies_awards’ data set
# # Display win and nominated column and other columns that extract the number of wins and nominations for each category of award. 
# 

# In[ ]:

import pandas as pd
import os


# In[2]:

current_path = os.getcwd() #gives current directory


# In[6]:

movie_data = pd.read_csv(current_path+"//"+"Assignment3"+"//"+"movies_awards.csv") # reads data from the csv file


# In[7]:

awards=pd.DataFrame(movie_data.groupby('Awards').size())
awards.columns=['count']


# In[8]:

movies=awards.reset_index()


# In[9]:

movies.head()


# In[46]:

new_movies = pd.DataFrame({'AWARDS':['abc'],'AWARDS WON' : [0],'AWARDS NOMINATED' : [0],
                       'GOLDEN GLOBE WON' : [0],'GOLDEN GLOBE NOMINATED' : [0],
                       'OSCAR WON' : [0],'OSCAR NOMINATED' : [0],
                      'PRIMETIME EMMY WON' : [0],'PRIMETIME EMMY NOMINATED' : [0],
                      'BAFTA FILM WON' : [0],'BAFTA FILM NOMINATED' : [0]})


# In[47]:

for i in movies.index:
    new_movies.loc[i] = [movies.ix[i]['Awards'], 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    str = movies.ix[i]['Awards'].upper()
    index = str.find("WON")
    if index != -1:
        str = str[(index + 4):]
        splits = str.split()
        clm_name = splits[1].replace("OSCARS", "OSCAR")
        if(splits[1] == "BAFTA" or splits[1] == "GOLDEN" or splits[1] == "PRIMETIME"):
            clm_name += (" " + splits[2]).replace("GLOBES", "GLOBE").replace("EMMYS", "EMMY").replace("FILMS", "FILM")
        if(clm_name[-1] == '.'):
            clm_name = clm_name[:-1]
        
        new_movies.set_value(i, clm_name + ' WON', splits[0])
        new_movies.set_value(i, 'AWARDS WON', int(new_df.ix[i]['AWARDS WON']) + int(splits[0]))
    
    str = movies.ix[i]['Awards'].upper()
    index = str.find("NOMINATED FOR")
    if index != -1:
        str = str[(index + 14):]
        splits = str.split()
        clm_name = splits[1].replace("OSCARS", "OSCAR")
        if(splits[1] == "BAFTA" or splits[1] == "GOLDEN" or splits[1] == "PRIMETIME"):
            clm_name += (" " + splits[2]).replace("GLOBES", "GLOBE").replace("EMMYS", "EMMY").replace("FILMS", "FILM")
        if(clm_name[-1] == '.'):
            clm_name = clm_name[:-1]
        
        new_movies.set_value(i, clm_name + ' NOMINATED', splits[0])
        new_movies.set_value(i, 'AWARDS NOMINATED', int(new_movies.ix[i]['AWARDS NOMINATED']) + int(splits[0]))
    
    str = movies.ix[i]['Awards'].upper()
    index = str.find("NOMINATION")
    if index != -1:
        str = str[:(index - 1)]
        splits = str.split()
        
        new_movies.set_value(i, 'AWARDS NOMINATED', int(new_movies.ix[i]['AWARDS NOMINATED']) + int(splits[len(splits) - 1]))
    
    str = movies.ix[i]['Awards'].upper()
    index = str.find("WIN")
    if index != -1:
        str = str[:(index - 1)]
        splits = str.split()
        
        new_movies.set_value(i, 'AWARDS WON', int(new_movies.ix[i]['AWARDS WON']) + int(splits[len(splits) - 1]))   


# In[48]:

new_movies.head()


# In[49]:

ouput_csv = current_path+'\\output\\Q4_Part_1.csv'     # path for storing data


# In[50]:

new_movies.to_csv(ouput_csv, index=False, encoding='utf-8')    # writing data to csv file


# In[ ]:



