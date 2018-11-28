
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


revList = [14574.49, 7606.46, 8611.41, 9175.41, 8058.65, 8105.44, 11496.28, 9766.09, 10305.32, 14379.96, 10713.97, 15433.50]


# In[3]:


revAr = np.array(revList)


# In[4]:


expensesList = [12051.82, 5695.07, 12319.20, 12089.72, 8658.57, 840.20, 3285.73, 5821.12, 6976.93, 16618.61, 10054.37, 3803.96]
expAr = np.array(expensesList)


# In[5]:


profit=revAr-expAr


# In[6]:


profit


# In[35]:


pAfTax=profit*30/100
pAfTax = np.round(pAfTax/1000,2)


# In[36]:


np.round((profit-pAfTax)/1000,2)


# In[37]:


gm=profit>(np.mean(pAfTax))
#good months


# In[38]:


los=pAfTax<(np.mean(revAr))
#bad months


# In[39]:


los


# In[40]:


bestMonth= pAfTax == pAfTax.max()
print(bestMonth)


# In[43]:


worstMonth=pAfTax == min(pAfTax)


# In[44]:


print("best month {0},worstMonth {1} ".format(bestMonth,worstMonth))


# In[46]:


a1 = np.arange(20)
print(type(a1), a1.ndim, a1.shape, len(a1))


# In[47]:


a1


# In[55]:


# matrix from a1 row,column row*col=20
m1=np.reshape(a1,(5,4))
m1


# In[53]:


m1
print(type(m1), m1.ndim, m1.shape, len(m1))


# In[51]:


#To order matrix, default order is column
m2=np.reshape(a1,(5,4),order='F')


# m2

# In[52]:


m2


# In[56]:


m1*m2


# In[57]:


m1+m2


# In[58]:


m1>10


# In[63]:


#handling nans
mDiv = np.nan_to_num(m1/m2)
mDiv


# In[66]:


score = np.array([[90,77,88,90], #steven
                [55,65,87,67], #allen
                [65,77,65,88],#alex
                [55,75,75,87],#lee
                [87,87,87,87]])# Neena
print(score.ndim, score.shape)


# In[81]:


studentList = ["Steven", "Allen", "Alex", "Lee", "Neena"]
studIndx = list(range(len(studentList)))#[0, 1, 2, 3, 4]
stuZip = zip(studentList,studIndx) #creates tupple, iterates through loop
studDict = dict(stuZip)

semList = ["sem1", "sem2", "sem3", "sem4"]
semInx = list(range(len(semList)))
semDict = dict(zip(semList, semInx))


# In[85]:


print(studDict)
print(semDict)


# In[86]:


np.where(score == score.min())


# In[87]:


np.where(score==score.min())[0][0]


# In[88]:


studentList[np.where(score==score.max())[0][0]]

