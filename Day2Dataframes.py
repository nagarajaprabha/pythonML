# -*- coding: utf-8 -*-
"""
Created on Tue Nov 27 12:05:16 2018

@author: nprabha
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

empdf = pd.read_csv(r"D:\MLTraining\ProblemStmts\day2\Empexport.csv", header=None)#use r to escape \\(slashes otherwise should give double slash)
empdf.columns = (["employee_id", "first_name", "last_name", "job_id", "salary", "commision_pct", "manager_id", "department_id"])

empdf
empdf.head() # default first 5 rows
empdf.head(10) # first 10rows
empdf.tail() #default last5 rows
empdf.tail(10) # last 10 rows
len(empdf) # num of rows
empdf.columns # list of columns
len(empdf.columns) # number of columns

empdf.info() #data frame information given

empdf.describe() # returns statistical information about numerical columns

empdf.job_id.unique() #Unique list of values from jobId column

empdf["job_id"].unique()
# Slicing of DataFrame DF[rowlable][columnLabel]
              #DF[start:stop:step][start:stop:step]
    
empdf[:]    

empdf[::10] # Every 10th Row

empdf[10:200:5] #Starts=10 stop=200 every 5 th row

empdf[:]["employee_id"] #all rows only employee_id column

empdf[:][ ["employee_id", "last_name", "salary"] ]

empdf[::-1][:] #last to first row all columns

empdf[:][::-1] # al rows and all columns in reverse order


empdf[:][ [ "employee_id", "last_name", "salary"]].head()

#verify
empdf.describe()["salary"]


empdf.sort_values(by="salary").head() # ascending order of salary
empdf.sort_values(by="salary", ascending=False).head(20)
empdf.sort_values(["job_id", "salary"])[ ["job_id", "salary"]] #nested sorting within jobid and within that Salary

#Filter Dataframes
empdf[empdf.salary>10000][ ["employee_id", "last_name", "salary"]]

#Nested conditions
empdf[(empdf.salary>10000) &(empdf.department_id=='90')][ ["employee_id", "last_name", "salary"]]
filteredEmpDf = empdf[(empdf.salary>10000) &(empdf.department_id=='90')][ ["employee_id", "last_name", "salary"]]
filteredEmpDf


#using in values
empdf[(empdf.job_id.isin(["SA_REP", "ST_CLERK", "IT_PROG", "AD_PRES"]))][ ["employee_id", "last_name", "salary"]]

#contains value
empdf[empdf.job_id.str.contains('CLERK')]["job_id"].head(10)

#convert the column to int
empdf.department_id = empdf.department_id.apply(lambda x: 0 if x=="Null" else int(x))
empdf.info()

#First Check for Null values then explicity convert into int64
empdf.manager_id = empdf.manager_id.apply(lambda x: 0 if x=="Null" else x)
empdf.manager_id = empdf.manager_id.astype('int64')
empdf.info()

def comm(x):
    if x== "Null":
        return 0.0
    else:
        return float(x)

#using function
empdf.commission_pct = empdf.commision_pct.apply(comm )
empdf.info()

gResult = empdf.groupby("department_id")["salary"].sum()
gResult.plot.bar()
plt.show()

gResult = empdf.groupby("department_id")["salary"].min()
gResult.plot.bar()
plt.show()

#To add column dynamically
empdf["annual_salary"] = empdf.salary*12;
empdf.columns
empdf.head()

#to drop column appraoch 1. This would drop from inmemory but will not apply for empdf object.
#so either assign or use parameter inplace
empdf = empdf.drop("annual_salary", axis=1)
empdf

#OR

empdf.drop("annual_salary", axis=1, inplace=True)

#Copy Dataframe
empdfCopy = empdf[:15][ ["employee_id", "last_name", "salary"] ].copy()
empdfCopy

#Drop understand indexes or list of labels
#Drop from copy
empdfCopy.drop([1,2,3], inplace=True)
empdfCopy

empdfCopy.drop(list(range(6,7)), inplace=True)
empdfCopy

#to get indexes on condition based
empdfCopy[empdfCopy.salary < 7500].index

empdfCopy.drop(empdfCopy[empdfCopy.salary<7500].index, inplace=True)
empdfCopy
empdfCopy.at[11, "last_name"]

#.at[rowlabel, collLabel] renaming of value
empdfCopy.at[11, "last_name"]="Teena"
empdfCopy

#index based renaming using iat
empdfCopy.iat[4,1] = "Steeven"
empdfCopy

# iat() function would Also get data from the cell
empdfCopy.iat[4,1]

#iloc()
empdfCopy.iloc[0:10, 0:4]
#all rows and except last column
empdfCopy.iloc[:, :-1]

#all rows but selected columns
#empdf.iloc[:,[2,4,6]]
empdfCopy.iloc[:,[2]]

#print all columns
empdfCopy.columns

# Extracting 2d-Array(with [] in second parameter serves as 2D array) from Dataframe
#matrix=empdf.iloc[:,:-1].values
matrix = empdf.iloc[:,[1,2]].values
type(matrix)

#2D -Array with one column
twoD = empdf.iloc[:,[4]].values

#Extracting 1D-Array
oneDMatrix = empdf.iloc[:2].values
oneDMatrix

print(type(twoD), twoD.ndim, twoD.shape)

