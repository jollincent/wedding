#!/usr/bin/env python
# coding: utf-8

# In[1]:


import ipywidgets as widgets


# # Engagement

# ## Bridesmaids / Groomsmen

# The following is to help us calculate the costs associated with bridesmaids and groomsmen.

# In[2]:


numBridesmaids = widgets.IntSlider(
    value=7,
    min=0,
    max=10,
    step=1,
    description='Number:',
    disabled=False,
    continuous_update=False,
    orientation='horizontal',
    readout=True,
    readout_format='d'
)
display(numBridesmaids)


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

# ## Estimated Running Total
# 
# The following is the estimated running total. Please run the code cell below to calculate the current running total based on the sliders above.

# In[3]:


print("With {} bridesmaids and groomsmen at a price of ${} for each:".format(numBridesmaids.value, 100))
print("${:.2f}".format(numBridesmaids.value * 100.192))

