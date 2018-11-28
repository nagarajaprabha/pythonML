# -*- coding: utf-8 -*-

import numpy as np
revenueList = [14574.49, 7606.46, 8611.41, 9175.41, 8058.65, 8105.44, 11496.28, 9766.09, 10305.32, 14379.96, 10713.97, 15433.50]
revenues = np.array(revenueList)

expensesList = [12051.82, 5695.07, 12319.20, 12089.72, 8658.57, 840.20, 3285.73, 5821.12, 6976.93, 16618.61, 10054.37, 3803.96]
expenses = np.array(expensesList)

profit=revenues-expenses

pAfTax=profit*30/100
pAfTax = np.round(pAfTax/1000,2)

np.round((profit-pAfTax)/1000,2)

gm=profit>(np.mean(pAfTax))
#good months

los=pAfTax<(np.mean(revenues))
#bad months

bestMonth= pAfTax == pAfTax.max()
print(bestMonth)

worstMonth=pAfTax == min(pAfTax)

print("best month {0},worstMonth {1} ".format(bestMonth,worstMonth))

a1 = np.arange(20)
print(type(a1), a1.ndim, a1.shape, len(a1))

# matrix from a1 row,column row*col=20
m1=np.reshape(a1,(5,4))
m1

m1
print(type(m1), m1.ndim, m1.shape, len(m1))
#To order matrix, default order is column
m2=np.reshape(a1,(5,4),order='F')

#matrix multiplication
m1*m2

#matrices addition
m1+m2

#handling nan
#handling nans
mDiv = np.nan_to_num(m1/m2)
mDiv

  