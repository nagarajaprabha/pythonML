
# coding: utf-8

# In[8]:


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
#warnings.filterwarnings("ignore")


# In[36]:


df=pd.read_csv(r"D:\MLTraining\ProblemStmts\day3\DemographicData.csv")
df.head()


# In[39]:


# df=pd.read_csv(r"D:\MLTraining\ProblemStmts\day3\DemographicData.csv", header=None)
df.columns=['CountryName','CountryCode','BirthRate','InternetAccess','IncomeGroup']
# df.BirthRate = df.BirthRate.apply(lambda x: 0.0 if x=="Null" else x)
# df.BirthRate = df.BirthRate.astype("float64")


df.info()


# In[40]:


df.describe()["BirthRate"]
#DF[DF.IncomeGroup=="High income"].describe()["BirthRate"]


# In[45]:


plt.rcParams["figure.figsize"]=(9,8)
s = sns.swarmplot(data=df, x="IncomeGroup", y = "BirthRate")
b = sns.boxplot(data=df, x="IncomeGroup", y="BirthRate", color="lightgrey")
vis3 = sns.lmplot(data=df, x="InternetAccess", y = "BirthRate", fit_reg=False, hue="IncomeGroup", size=5)


# In[46]:


j = sns.jointplot( data = df, x="InternetAccess", y = "BirthRate", color="Red", kind = "kde")

