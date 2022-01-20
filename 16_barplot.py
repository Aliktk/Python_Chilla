#package

import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('darkgrid')

x = ['A', 'B', 'C']
y = [1, 5, 3]

sns.barplot(x, y)
plt.show()

import matplotlib.pyplot as plt
import seaborn as sns

# Set Seaborn style
sns.set_style('darkgrid')
# Import Data
titanic_dataset = sns.load_dataset("titanic")

# Construct plot
sns.barplot(x = "sex", y = "survived", data = titanic_dataset)
plt.show()