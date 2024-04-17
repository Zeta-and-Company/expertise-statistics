# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 18:54:15 2023

@author: KeliDu
"""

import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

df = pd.read_csv(r'C:\Workstation\Trier\application_study\70s_80s_90s_corpus\metadata.csv', sep='\t')

df.columns

sns.set(font_scale=2)
sns.set_style("whitegrid")
f, ax = plt.subplots(figsize = (14,10))#12
ax.grid(False)
g = sns.histplot(data=df, hue="author-gender", x="subgenre", multiple="stack", shrink=.8)


sns.set(font_scale=2)
sns.set_style("whitegrid")
f, ax = plt.subplots(figsize = (14,16))#12
g = sns.histplot(data=df, y="publisher", hue="subgenre", multiple="stack", shrink=.8)
ax.set_xscale('log')
ax.grid(False)

sns.set(font_scale=2)
sns.set_style("whitegrid")
f, ax = plt.subplots(figsize = (25,10))#12
g = sns.histplot(data=df, x="publ-ref", shrink=.8, kde=True, discrete=True)
plt.xticks(rotation=30)






