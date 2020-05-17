import numpy as np
import pandas as pd
from datetime import datetime
import json
import matplotlib.pyplot as plt
import bokeh

with open('wyndham_data.txt', 'r+') as f:
    data = json.load(f)

df = pd.json_normalize(data['features'])
df.index = df['properties.date_stamp']
print(df)
plt.figure()
df['properties.energy_prod(KWh)'].plot()
plt.show()

