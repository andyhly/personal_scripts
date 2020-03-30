
# coding: utf-8

# In[3]:


import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
import pandas as pd


# In[8]:


"""The numbers were pulled from https://liquipedia.net/dota2/The_International"""
axis = [0, 1, 2, 3, 4, 5, 6, 7, 8]
raw_data = {'Prize Pool': [200000,200000,517388,3386433,6726808,6023434,7382935,7531992,11157273], 
            'First Place': [1000000,1000000,1437190,5025029,6634661,9139002,10862683,11234158,15620181], 
            'Second Place': [250000,250000,632364,1474737,2856590,3427126,3950067,4085148,4462908], 
            'Third Place': [150000,150000,287438,1037778,2211554,2180898,2592231,2680879,3089706]}
df = pd.DataFrame(raw_data)


# In[9]:


barWidth = 0.60
names = ('2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019')
totals = [a+b+c+d for a,b,c,d in zip(df['Prize Pool'], df['First Place'], df['Second Place'], df['Third Place'])]

blueBars = [a / b for a,b in zip(df['First Place'], totals)]
orangeBars = [a / b for a, b in zip(df['Second Place'], totals)]
grayBars = [a / b for a,b in zip(df['Third Place'], totals)]
greenBars = [a / b for a,b in zip(df['Prize Pool'], totals)]


# In[20]:


plt.xticks(axis, names)
plt.xlabel("Distribution of The Internationals Prize Pool Earnings")
plt.bar(axis, blueBars, color='green', edgecolor='black', width=barWidth)
plt.bar(axis, orangeBars, bottom=blueBars, color='blue', edgecolor='black', width=barWidth)
plt.bar(axis, grayBars, bottom=[a+b for a,b in zip(blueBars, orangeBars)], color='orange', edgecolor='black', width=barWidth)
plt.bar(axis, greenBars, bottom=[a+b+c for a,b,c in zip(blueBars, orangeBars, grayBars)], color='red', edgecolor='black', width=barWidth)
labels_b = ['1st place', '2nd place', '3rd place', '4th&below']
plt.legend(labels_b, loc=3)


# In[7]:


plt.show()

