
# coding: utf-8

# In[2]:


print("hello") #ctrl + Enter (run the cell)
               #shift + Enter     
               # to create blank cell ESC + A (above), ESC + B 


# In[3]:


dummyVariable = 20.2
type(dummyVariable)


# In[4]:


id(dummyVariable)


# In[6]:


city = '22.2'
type(city)


# In[7]:


indicator = True
type(indicator)


# In[8]:


print(dummyVariable, city, indicator)


# In[9]:


print(type(city
          ))


# In[10]:


print(type(city))


# In[11]:


num1 = 20
num2=10
result = num1+num2
print("Addition of {0} and {1} is {2}".format(num1,num2,result))


# In[16]:


dummy = input("please enter your name")


# In[14]:


age = int(input("Please enter u r age"))


# In[15]:


type(age)


# In[17]:


print("Your name is {0} and age is {1}".format(dummy, age))


# In[ ]:


cnt = 0
while cnt < 10:
    cnt= cnt + 1
    print(cnt)


# In[19]:


cnt = 1
while cnt<10:
    cnt=cnt+1
    print(cnt)


# In[20]:


range(1,10)


# In[21]:


for i in range(1,10):
    print(i)


# In[22]:


for i in range(10):
    print(i)
    


# In[23]:


#              start,stop,step(can include expressions step*2)
for i in range(1,100,10):
    print(i)
    


# In[24]:


for i in range(10, 1 , -2):
    print(i)


# In[26]:


city = "dummb"
for a in city:
    if(a == "m"):
        print(a)
    print(a)


# In[27]:


ip = input("Enter ip address")


# In[45]:


cntCharacters = 0
segLength = 0
for p in ip:
    if(p!="."):
        cntCharacters=cntCharacters+1
        #segLength = 0
        continue
    else:
        segLength = segLength+1
    print("segment {0} contains {1} characters".format(segLength, cntCharacters))
    cntCharacters = 0

#to print last segment details
print("segment {0} contains {1} characters".format(segLength+1, cntCharacters))


# In[46]:


#importing packages
from numpy.random import randint,randn


# In[59]:


randint(10)


# In[69]:


winNumber = randint(10)


# In[70]:


userGuess = int(input("Enter u r number"))


# In[71]:


if winNumber == userGuess:
    print("Kudos")
else:
    print("you loose as win number was {0}".format(winNumber))


# In[87]:


from numpy.random import randn
N = randint(100000)
cnt = 0
for i in range(N):
    num = randn()
    if num >= -1 and num <= 1:
        cnt+=1
percentage = cnt/N * 100
print(percentage)


# In[88]:


#List function extend would explode and add elements 
sampleList = [1,2,4,65]


# In[103]:


sl = [23,'a',3,True]
sl.extend(sampleList)


# In[92]:


sl


# In[93]:


sl=range(10)


# In[94]:


type(sl)


# In[95]:


sl=list(sl)


# In[96]:


type(sl)


# In[97]:


sl


# In[99]:


sl.sort()


# In[100]:


sl


# In[104]:


li = ['A','B','C','D','E','F']


# In[106]:


li[::]


# In[107]:


li[1:]


# In[115]:


li[:-2]


# In[118]:


import scrapy

