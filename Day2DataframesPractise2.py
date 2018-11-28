# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Array lengths should be consistent acrorss when forming Dataframes from dictionary
InputDataDictn1 = {
        'course_id': ['901', '902', '903', '904', '905'],
        'first_name': ['Steven', 'Alex', 'Lee', 'John', 'Greg'], 
        'last_name': ['King', 'Maden', 'Chan', 'Bruce', 'Wargus']}
DFstu1 = pd.DataFrame(InputDataDictn1 ,
		columns = ['course_id', 'first_name', 'last_name'])
DFstu1 

#---------------------------
InputDataDictn2 = {
        'course_id': ['904', '905', '906', '907', '908'],
        'first_name': ['Tina', 'Trecy', 'Andria', 'Eliza', 'Gracy'], 
        'last_name': ['Smith', 'Muller', 'Morgan', 'Johnson', 'Jordan']}

DFstu2 = pd.DataFrame(InputDataDictn2 ,columns = ['course_id', 'first_name', 'last_name'])

DFstu2

#---------------------------
InputDataDict3 = {
        'course_id': ['901', '902', '903', '904', '905', '907', '908', '909', '910', '911'],
        'exam_id': [51, 15, 15, 61, 16, 14, 15, 1, 61, 16]}
DFtest = pd.DataFrame(InputDataDict3, columns = ['course_id','exam_id'])
DFtest




#-----------------Join the two dataframes along rows------------------------

DFstudent  = pd.concat([DFstu1 , DFstu2 ])
DFstudent

#-----------------Join the two dataframes along columns-----------------

pd.concat([DFstu1 , DFstu2 ], axis=1)


#------------Merge two dataframes along the course_id value-----------------

pd.merge(DFstudent  , DFtest , on='course_id')

#---------------Merge with inner join (only matching rows) ---------------------

pd.merge(DFstu1 , DFstu2, on='course_id', how='inner')


# -------------Merge with inner join & suffix duplicate column name to understand which dataframe data belongs ---------------------
pd.merge(DFstu1 , DFstu2, on='course_id', how='inner', suffixes=('_DFstu1','_DFstu2'))


#Advance actions on Dataframe
inputArray = np.array([[1,2,3], [4,5,6]])
dfFromArray = pd.DataFrame(inputArray)
dfFromArray