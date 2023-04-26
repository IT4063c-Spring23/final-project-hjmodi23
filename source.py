#!/usr/bin/env python
# coding: utf-8

# # STREAMING SERVICE COMPARISON📝
# 
# ![Banner](./assets/banner.jpeg)

# **CHECKPOINT 1**
# ## Topic
# *What problem are you (or your stakeholder) trying to address?*
# 📝 <!-- Answer Below -->
# The problem I'm trying to address is that there is no need to have a number of streaming services that require subscriptions to watch shows/movies as it can be financially constraining to customers and businesses and it'd be more beneficial to just have it all in one spot.

# ## Project Question
# *What specific question are you seeking to answer with this project?*
# *This is not the same as the questions you ask to limit the scope of the project.*
# 📝 <!-- Answer Below -->
# Why so many streaming services when there can be all-in-one?

# ## What would an answer look like?
# *What is your hypothesized answer to your question?*
# 📝 <!-- Answer Below -->
# Hypothetical answer would be that all the streaming services merge into one service so there can only be one subscription and that way customers can access everything in one spot.

# ## Data Sources
# *What 3 data sources have you identified for this project?*
# *How are you going to relate these datasets?*
# 📝 <!-- Answer Below -->
# I've identified 3 APIs using RapidAPI to provide statistics and context to the issue using various streaming related APIs.

# ## Approach and Analysis
# *What is your approach to answering your project question?*
# *How will you use the identified data to answer your project question?*
# 📝 <!-- Start Discussing the project here; you can add as many code cells as you need -->
# I'll be using these API endpoints to extract data relating to streaming including traffic, subscriptions, availability and more to provide statistics on how having multiple streaming services can hamper profit in a business and it's financial impact on customer due to multiple subscriptions.

# In[ ]:


# Start your code here
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sklearn 


# **CHECKPOINT 2**
# ### Exploartory Data Analysis
# I will be able to pull different insights from this dataset which will justify which streaming is worth it. There are few correlations between variables, but they should add value by themselves. The issue in my dataset is merging two different data sets and fixing nulls or errors. I did find some outliers, but I was able to fact check and fix them. I changed the missing values to '0' or 'unknown', based on the data type of the column. Luckily, there were no duplicates that came to my attention. Data types were good the way they were.

# ### Data Cleaning and Transformations
# I've tried to be as thorough as possible in my code to showcase what process I went through to clean the data, process it as well as analyze it. Overall, I've spent 50% of my time scraping data and cleaning it to provide a better understanding of the data structure. The visualizations also have write-up below them to explain what insights were gained and a detailed summary in the end to help explain better.

# ### Machine Learning Plan
# From a machine learning standpoint, I really wanted to wait for the clean and processed data to see what made the most sense in terms of building a model. I think a multiple linear regression model is appropriate as I'll be working with more than one variable. A potential issue that I see happening is not getting the output that I expect as my variables are a mixture of string and numerical values. 

# **CHECKPOINT 3**
# 

# ## Resources and References
# *What resources and references have you used for this project?*
# 📝 <!-- Answer Below -->
# url: 'https://streaming-availability.p.rapidapi.com/v2/services',
# url: 'https://netflix54.p.rapidapi.com/search',
# url: 'https://streamlinewatch-streaming-guide.p.rapidapi.com/search'
# url: 'https://www.kaggle.com/code/armintalic/quality-and-quantity-of-streaming-services-content/input'

# In[3]:


# ⚠️ Make sure you run this cell at the end of your notebook before every submission!
get_ipython().system('jupyter nbconvert --to python source.ipynb')

