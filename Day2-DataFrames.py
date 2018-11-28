
# coding: utf-8

# In[44]:


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

import warnings
warnings.filterwarnings("ignore")


# In[6]:


empdf = pd.read_csv(r"D:\MLTraining\ProblemStmts\day2\Empexport.csv", header=None)#use r to escape \\(slashes otherwise should give double slash)
empdf.columns = (["employee_id", "first_name", "last_name", "job_id", "salary", "commision_pct", "manager_id", "department_id"])


# In[8]:


empdf
empdf.head() # default first 5 rows
empdf.head(10) # first 10rows
empdf.tail() #default last5 rows
empdf.tail(10) # last 10 rows
len(empdf) # num of rows
empdf.columns # list of columns
len(empdf.columns) # number of columns


# In[9]:


empdf.info() #data frame information given


# In[10]:


empdf.describe() # returns statistical information about numerical columns


# In[12]:


type(empdf.describe())


# In[13]:


empdf.job_id.unique() #Unique list of values from jobId column


# In[14]:


empdf["job_id"].unique()


# In[15]:


# Slicing of DataFrame DF[rowlable][columnLabel]
              #DF[start:stop:step][start:stop:step]
    
empdf[:]    


# In[18]:


empdf[::10] # Every 10th Row


# In[19]:


empdf[10:200:5] #Starts=10 stop=200 every 5 th row


# In[20]:


empdf[:]["employee_id"] #all rows only employee_id column


# In[21]:


empdf[:][ ["employee_id", "last_name", "salary"] ]


# In[22]:


empdf[::-1][:] #last to first row all columns


# In[23]:


empdf[:][::-1] # al rows and all columns in reverse order


# In[24]:


empdf[:][ [ "employee_id", "last_name", "salary"]].head()


# In[25]:


empdf.describe()["salary"]


# In[27]:


empdf.sort_values(by="salary").head() # ascending order of salary


# In[30]:


empdf.sort_values(by="salary", ascending=False).head(20)


# In[32]:


empdf.sort_values(["job_id", "salary"])[ ["job_id", "salary"]] #nested sorting within jobid and within that Salary


# In[33]:


#Filter Dataframes

empdf[empdf.salary>10000][ ["employee_id", "last_name", "salary"]]


# In[35]:


#Nested conditions
empdf[(empdf.salary>10000) &(empdf.department_id=='90')][ ["employee_id", "last_name", "salary"]]


# In[36]:


filteredEmpDf = empdf[(empdf.salary>10000) &(empdf.department_id=='90')][ ["employee_id", "last_name", "salary"]]
filteredEmpDf


# In[39]:


#using in values
empdf[(empdf.job_id.isin(["SA_REP", "ST_CLERK", "IT_PROG", "AD_PRES"]))][ ["employee_id", "last_name", "salary"]]


# In[41]:


empdf[empdf.job_id.str.contains('CLERK')]["job_id"].head(10)


# In[48]:


df=pd.read_csv(r"D:\MLTraining\ProblemStmts\day3\DemographicData.csv", header=None)#use r to escape \\(slashes otherwise should give double slash)

mydf = pd.DataFrame(data={1,22,-3,444,51,6,77,888,29,10}, columns=['x'])


# In[47]:


sns.distplot(df.Int)
plt.show()


# In[51]:


def lawOfLargeNum(samples):
    from numpy.random import randn
    N=samples
    numList=[]
    for i in range(N):
        numList.append(randn())
    ldf = pd.DataFrame(numList)
    ldf.columns=(['x'])
    sns.distplot(ldf.x, kde_kws={'shade':True, 'linewidth': 3, "color":"Red"}, hist_kws={'edgecolor':'black'})
    hist_kws = {'edgecolor':'black'}
    plt.show()


# In[54]:


lawOfLargeNum(10)

lawOfLargeNum(1000)

lawOfLargeNum(10000)


# In[64]:


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
#warnings.filterwarnings("ignore")


# In[73]:


DF=pd.read_csv(r"D:\MLTraining\ProblemStmts\day3\DemographicData.csv", header=None)
DF.columns=['CountryName','CountryCode','BirthRate','InternetAccess','IncomeGroup']

#vis2 = sns.boxplot(data=DF, x="IncomeGroup", y = "BirthRate")

DF[DF.IncomeGroup=="High income"].describe()["BirthRate"]


# In[72]:


#DF[DF.IncomeGroup=="High income"].sort_values(by="BirthRate")["BirthRate"]

