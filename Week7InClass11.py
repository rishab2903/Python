
# coding: utf-8

# In[11]:


import plotly.graph_objs as go
from plotly.offline import iplot,plot
import numpy as np
x = np.random.randn(2000)
y = np.random.randn(2000)
plot([go.Scatter(x=[95, 77, 84], y=[75, 67, 56])])

