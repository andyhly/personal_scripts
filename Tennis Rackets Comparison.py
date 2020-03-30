
# coding: utf-8

# In[45]:


import matplotlib.pyplot as plt
import pandas as pd
from math import pi


# In[46]:


df = pd.DataFrame({
    'rackets': ['Slazenger X1', 'Wilson Blade 98 v7', 'Babolat Pure Drive Team', 'Wilson PS Tour 95 Hyper Carbon'],
    
    'HEADSIZE': [5, 8, 10, 5],
    
    'STIFFNESS': [2, 4, 10, 2],
    
    'STRUNG WEIGHT': [9.75, 7.25, 4.25, 7.25],
    
    'SWINGWEIGHT': [3, 9, 7.5, 7.5],
    
    'BALANCE HL': [10, 9.375, 7.5, 7.5]
})


# In[47]:


def make_spider(row, title, color):
    #variables
    categories=list(df)[1:]
    N = len(categories)
    
    angles = [n / float(N) * 2 * pi for n in range(N)]
    angles += angles[:1]
    
    ax = plt.subplot(2, 2, row+1, polar=True, )
    
    ax.set_theta_offset(pi / 2)
    ax.set_theta_direction(-1)
    
    #Sets the font size of 5 categories
    plt.xticks(angles[:-1], categories, color='grey', size=23)
    
    #draw ylabels
    ax.set_rlabel_position(0)
    plt.yticks([1.5, 5, 10.5], [], color='grey', size=7)
    #setting so that value of 10 doesn't touch edge of circle
    plt.ylim(0,10.5)
    
    values=df.loc[row].drop('rackets').values.flatten().tolist()
    values += values[:1]
    ax.plot(angles, values, color=color, linewidth=2, linestyle='solid')
    ax.fill(angles, values, color=color, alpha=0.4)
    
    #title
    plt.title(title, size=38, color=color, y=1.1)
    


# In[60]:


my_dpi=34
plt.figure(figsize=(1000/my_dpi, 1000/my_dpi), dpi=my_dpi)
    
#creating color palette
my_palette = plt.cm.get_cmap("Set2", len(df.index))

#looping plots
for row in range(0, len(df.index)):
    make_spider(row=row, title=''+df['rackets'][row], color=my_palette(row))
    

