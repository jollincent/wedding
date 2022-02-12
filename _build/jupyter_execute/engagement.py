#!/usr/bin/env python
# coding: utf-8

# In[1]:


import ipywidgets as widgets


# # Engagement

# ## Bridesmaids / Groomsmen

# The following is to help us calculate the costs associated with bridesmaids and groomsmen.

# In[2]:


widgets.IntSlider(
    value=7,
    min=0,
    max=10,
    step=1,
    description='Test:',
    disabled=False,
    continuous_update=False,
    orientation='horizontal',
    readout=True,
    readout_format='d'
)


# ## Food
# 
# Food we should have at the engagement:
# - Roast Pig
# - Roast Duck
# - Dessert Foods

# ## Ceremonial Events
# ... and associated estimated prices.

# ## Decorations
# 

# ## Outfits
# 
