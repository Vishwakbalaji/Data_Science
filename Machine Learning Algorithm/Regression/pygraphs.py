#!/usr/bin/env python
# coding: utf-8

# # PYTHON GRAPHS PACKAGES
# 
# **DONE BY**
# 
# **VISHWAK BALAJI - E21026**

# In[1]:


# this fucntion is for creating a data frame

import os                                                 # os module
import pandas as pd                                       # importing pandas module

def DFrame(data,directory=os.getcwd()):                   # x represents the data
    if dir != os.getcwd():                                # if the getcwd is true then directory = os.getcwd, if not equal
        directory = os.chdir(directory)                   # the input directory will take place here
        data = pd.read_csv(data)                          # it will automatically read the file
    x = data
    return (pd.DataFrame(x))                              # convert it into pandas dataframe

# Spliting the entier dataset into its data types:

# graphs function consists of hist,box,bar. which plot for any datasets
import pandas as pd                                        # importing the pandas module
import matplotlib.pyplot as plt                            # importing the matplotlib to plot the graph
import seaborn as sns                                      # importing seaborn to plot the graph
import os                                                  # importing os for directory changing

# Spliting the entier dataset into its data types:

def graphs(data,variable = 0,directory= os.getcwd()):     # function with name graphs
    
    if dir != os.getcwd():                                # if the getcwd is true then directory = os.getcwd, if not equal
        directory = os.chdir(directory)                   # the input directory will take place here
        data = pd.read_csv(data)                          # it will automatically read the file
        
    # below is one line code for if and else
    x = data if variable == 0 else data[variable]  # if the variable=0 then it takes entier dataset or else takes variable
    
    a = list(x.columns)                    # this list of entier datset columns
    b = []                                 # this named as f list
    c = []                                 # this named as g list
    d = {}                                 # this named as d dictionary
    p = round(len(x)*0.05)                 # taking the length of the datset and multiplying with 5% and rounding it up
    for i in x.columns:                    # for loop iterates the datasets columns
        uni = len(pd.unique(x[i]))         # now taking length of the unique dataset columns iterate
        
    # below is one line code for if and else:    
        b.append(i) if p <= uni else c.append(i)      # if the numerical value is larger append in b or else append in c
        
# if suppose numerical variable contain object of large no. of unique value, then we have to append it in catagorical list

    for i in range(len(b)):                      # so, we using for loop to iterates            
        d[b[i]]=str(x.dtypes[i])                 # finding the data types for numerical and putting it in dictionary 
    
        if d[b[i]] == ('object'):                # if the dictionary contain object then     
            c.append(b[i])                       # it will append it into catagorical varible
            e = b.index(b[i])                    # finding index for object in numerical variable
            b.pop(e)                             # delete the particular index
        else:                                    # if there is no object
            break                                # leave this loop and go to next
    
    # histogram:
    for i in b:                                                           # using for to plot continuously
        x.hist(column=str(i),bins=25,grid=False,edgecolor="black")        # histogram function to plot the graph
        plt.savefig(i+" hist.png")                                        # to save the figure in the directory
        plt.show()                                                        # this helps to show the ploting
        
    # boxplot:
    for i in b:                                                           # using for loop to plot continuosly
        sns.boxplot(x=x[i]).set(title='%s Plot'%i)                        # boxplot function to plot the graph
        plt.savefig(i+" box.png")                                         # to save the figure in the directory
        plt.show()                                                        # this helps to show the plotting
        
    # histogram for catagorical:
    for i in c:
        plt.subplots(figsize=(10,5))               # it streches the fig, the way we want it to look like
        plt.ylabel('count',fontsize=12)
        sns.countplot(x[i],color='steelblue').set(title='%s Plot'%i)
        plt.savefig(i+" bar.png")                                          # to save the figure in the directory
        plt.show()                                                         # this helps to show the plotting
      
    return                                                                 # returning all the outputs

