# -*- coding: utf-8 -*-

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

import warnings
warnings.filterwarnings("ignore")


df=pd.read_csv(r"D:\MLTraining\ProblemStmts\day3\DemographicData.csv", header=None)#use r to escape \\(slashes otherwise should give double slash)
#plt.figure(figsize=(3,4))
sns.distplot(df.InternetAccess)
plt.show()

sns.distplot(df.InternetAccess, hist=True, kde=True, kde_kws = {'shade': True, 'lineWidth':3, "color":"Red"}, hist_kws={'edgecolor':'black'})