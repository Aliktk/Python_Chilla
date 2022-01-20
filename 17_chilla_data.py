import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
import seaborn as sns
# chilla = pd.read_csv('Chilla_data.csv')
# sns.set_theme(style="ticks", color_codes=True)
# p = sns.countplot(x='Gender', hue="Age", data=chilla)
# plt.show()

chilla = pd.read_csv('data_viz.csv')
sns.set_theme(style="ticks", color_codes=True)
p = sns.countplot(x='Gender', hue="Age", data=chilla)
plt.show()