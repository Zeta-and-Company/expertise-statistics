#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 10:29:15 2024

@author: kelidu
"""

import pandas as pd
import matplotlib as mpl
pd.DataFrame.iteritems = pd.DataFrame.items
import seaborn.objects as so

df = pd.read_csv(r'C:\Workstation\Trier\application_study\Github\distinctiveness_analysis_results\Figure7_1.csv', sep='\t')
df_ = pd.melt(df, id_vars=['category', 'subgenre'], value_vars=['Zeta_log', 'LLR', 'Welch'], 
              var_name='measure', value_name='no_of_words')

(
 so.Plot(df_, color="category", y='no_of_words', x="subgenre")
.add(so.Bar(), so.Stack()).layout(size=(4, 8))
.facet(row="measure")
.limit(y=(0,50))
.scale(color='viridis')#icefire
).plot()


df1 = pd.read_csv(r'C:\Workstation\Trier\application_study\Github\distinctiveness_analysis_results\Figure7_2.csv', sep='\t')
df1_ = pd.melt(df1, id_vars=['category', 'subgenre'], value_vars=['Zeta_log', 'LLR', 'Welch'], 
              var_name='measure', value_name='no_of_words')

(
 so.Plot(df1_, color="category", y='no_of_words', x="subgenre")
.add(so.Bar(), so.Stack()).layout(size=(4, 8))
.facet(row="measure")
.limit(y=(0,50))
.scale(color='viridis')#icefire
).plot()

'''
p = so.Plot(df1_, x="measure", y='no_of_words', color="category").add(so.Bar(), so.Stack()).facet("subgenre").limit(y=(0,50))
f = mpl.figure.Figure(figsize=(10, 10), layout="constrained")
sf1, sf2 = f.subfigures(2, 1)

p.on(sf2).plot()
(
    so.Plot(df_, x="measure", y='no_of_words', color="category")
    .add(so.Bars(), so.Stack())
    .facet("subgenre")
    .share(x=True)
    .scale(color='colorblind')
    .on(sf1)
)
'''

