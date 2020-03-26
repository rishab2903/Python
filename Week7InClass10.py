
# coding: utf-8

# In[10]:


import plotly.graph_objs as go
from plotly.offline import iplot,plot
import numpy as np
x = np.random.randn(2000)
y = np.random.randn(2000)
plot({'data': [{'y': [14, 22, 30,44]}], 'layout': {'title': 'Offline Plotly', 'font':dict(size=16)}}, image='png')

