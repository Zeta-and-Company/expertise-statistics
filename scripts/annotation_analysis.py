# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 02:26:34 2024

@author: KeliDu
"""
import pandas as pd
import os
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.metrics import cohen_kappa_score

#########################################################################################################################
#########################################################################################################################
#########################################################################################################################
#Select top distinctive words for genres and measures 
    
os.chdir(r'C:\Workstation\Trier\application_study\all_results\results')
measures = ['zeta_sd2', 'welsh', 'LLR']
genres = ['policier', 'blanche', 'scifi', 'sentimental']

df_out = pd.DataFrame()

for genre in genres:
    df_name = r'results_5000-lemmata-all_' + genre + '_no-yes.csv'
    df = pd.read_csv(df_name, sep='\t')
    df.rename(columns ={'Unnamed: 0': 'word'}, inplace = True)
    for measure in measures:
        df = df.sort_values(by=[measure], ascending=False)
        distinctive_words = df['word'][:50].tolist()   
        df_out[genre + '_' + measure] = distinctive_words

df_out.to_csv(r'top_50_per_GenreMeasure.csv', sep='\t', index=False)
    
#########################################################################################################################
#########################################################################################################################
#########################################################################################################################
#Inter-annotator-Agreement ER & JR

os.chdir(r'C:\Workstation\Trier\application_study\Tabellen_IAA_JR_ER')

genres = ['blanche', 'scifi', 'policier', 'sentimental']
measures = ['welsh', 'LLR', 'zeta_sd2']

kappa_results = []

for genre in genres:
    for measure in measures:
        name = genre + '_' + measure + '.xlsx'
        df = pd.DataFrame(pd.read_excel(name)) 
        category = cohen_kappa_score(df['category_JR'], df['category_ER '])
        interpretability = cohen_kappa_score(df['interpretability_JR'], df['interpretability_ER '])
        kappa_results.append((genre, measure, category, interpretability))

kappa_df = pd.DataFrame(kappa_results, columns=['genre', 'measure', 'category', 'interpretability'])    

kappa_df = pd.read_csv(r'kappa_results.csv', sep='\t')

    
sns.set(font_scale=2)
sns.set_style("whitegrid")
f, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 14), sharex=True)
sns.barplot(x="genre", y="category", data=kappa_df, hue = 'measure', ax=ax1)
sns.barplot(x="genre", y="interpretability", data=kappa_df, hue = 'measure', ax=ax2)
        