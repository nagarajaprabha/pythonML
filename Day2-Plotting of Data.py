
# coding: utf-8

# In[3]:


import numpy as np
import matplotlib.pyplot as plt


# In[6]:


#FootBallGameData
#Instructions for this dataset:
# Simply copy ALL the lines in this script by pressing 
# CTRL+A on Windows 
# Once you have executed the commands the following objects
# will be created:
# Matrices:
# - Salary
# - Games
# - MinutesPlayed
# - FieldGoals
# - FieldGoalAttempts
# - Points
# Lists:
# - Players
# - Seasons
# Dictionaries:
# - Sdict
# - Pdict

#Comments:
#Seasons are labeled based on the first year in the season
#E.g. the 2012-2013 season is preseneted as simply 2012


#Import numpy
import numpy as np

#Seasons
Seasons = ["2005","2006","2007","2008","2009","2010","2011","2012","2013","2014"]
Sdict = {"2005":0,"2006":1,"2007":2,"2008":3,"2009":4,"2010":5,"2011":6,"2012":7,"2013":8,"2014":9}

#Players
Players = ["David","Joe","James","Anthony","Danny","Chris","Paul","Kevin","Derrick","Dwayne"]
Pdict = {"David":0,"Joe":1,"James":2,"Anthony":3,"Danny":4,"Chris":5,"Paul":6,"Kevin":7,"Derrick":8,"Dwayne":9}

#Salaries
David_Salary = [15946875,17718750,19490625,21262500,23034375,24806250,25244493,27849149,30453805,23500000]
Joe_Salary = [12000000,12744189,13488377,14232567,14976754,16324500,18038573,19752645,21466718,23180790]
James_Salary = [4621800,5828090,13041250,14410581,15779912,14500000,16022500,17545000,19067500,20644400]
Anthony_Salary = [3713640,4694041,13041250,14410581,15779912,17149243,18518574,19450000,22407474,22458000]
Danny_Salary = [4493160,4806720,6061274,13758000,15202590,16647180,18091770,19536360,20513178,21436271]
Chris_Salary = [3348000,4235220,12455000,14410581,15779912,14500000,16022500,17545000,19067500,20644400]
Paul_Salary = [3144240,3380160,3615960,4574189,13520500,14940153,16359805,17779458,18668431,20068563]
Kevin_Salary = [0,0,4171200,4484040,4796880,6053663,15506632,16669630,17832627,18995624]
Derrick_Salary = [0,0,0,4822800,5184480,5546160,6993708,16402500,17632688,18862875]
Dwayne_Salary = [3031920,3841443,13041250,14410581,15779912,14200000,15691000,17182000,18673000,15000000]
#Matrix
Salary = np.array([David_Salary, Joe_Salary, James_Salary, Anthony_Salary, Danny_Salary, Chris_Salary, Paul_Salary, Kevin_Salary, Derrick_Salary, Dwayne_Salary])

#Games 
David_G = [80,77,82,82,73,82,58,78,6,35]
Joe_G = [82,57,82,79,76,72,60,72,79,80]
James_G = [79,78,75,81,76,79,62,76,77,69]
Anthony_G = [80,65,77,66,69,77,55,67,77,40]
Danny_G = [82,82,82,79,82,78,54,76,71,41]
Chris_G = [70,69,67,77,70,77,57,74,79,44]
Paul_G = [78,64,80,78,45,80,60,70,62,82]
Kevin_G = [35,35,80,74,82,78,66,81,81,27]
Derrick_G = [40,40,40,81,78,81,39,0,10,51]
Dwayne_G = [75,51,51,79,77,76,49,69,54,62]
#Matrix
Games = np.array([David_G, Joe_G, James_G, Anthony_G, Danny_G, Chris_G, Paul_G, Kevin_G, Derrick_G, Dwayne_G])

#Minutes Played
David_MP = [3277,3140,3192,2960,2835,2779,2232,3013,177,1207]
Joe_MP = [3340,2359,3343,3124,2886,2554,2127,2642,2575,2791]
James_MP = [3361,3190,3027,3054,2966,3063,2326,2877,2902,2493]
Anthony_MP = [2941,2486,2806,2277,2634,2751,1876,2482,2982,1428]
Danny_MP = [3021,3023,3088,2821,2843,2935,2070,2722,2396,1223]
Chris_MP = [2751,2658,2425,2928,2526,2795,2007,2454,2531,1556]
Paul_MP = [2808,2353,3006,3002,1712,2880,2181,2335,2171,2857]
Kevin_MP = [1255,1255,2768,2885,3239,3038,2546,3119,3122,913]
Derrick_MP = [1168,1168,1168,3000,2871,3026,1375,0,311,1530]
Dwayne_MP = [2892,1931,1954,3048,2792,2823,1625,2391,1775,1971]
#Matrix
MinutesPlayed = np.array([David_MP, Joe_MP, James_MP, Anthony_MP, Danny_MP, Chris_MP, Paul_MP, Kevin_MP, Derrick_MP, Dwayne_MP])

#Field Goals
David_FG = [978,813,775,800,716,740,574,738,31,266]
Joe_FG = [632,536,647,620,635,514,423,445,462,446]
James_FG = [875,772,794,789,768,758,621,765,767,624]
Anthony_FG = [756,691,728,535,688,684,441,669,743,358]
Danny_FG = [468,526,583,560,510,619,416,470,473,251]
Chris_FG = [549,543,507,615,600,524,393,485,492,343]
Paul_FG = [407,381,630,631,314,430,425,412,406,568]
Kevin_FG = [306,306,587,661,794,711,643,731,849,238]
Derrick_FG = [208,208,208,574,672,711,302,0,58,338]
Dwayne_FG = [699,472,439,854,719,692,416,569,415,509]
#Matrix
FieldGoals  = np.array([David_FG, Joe_FG, James_FG, Anthony_FG, Danny_FG, Chris_FG, Paul_FG, Kevin_FG, Derrick_FG, Dwayne_FG])

#Field Goal Attempts
David_FGA = [2173,1757,1690,1712,1569,1639,1336,1595,73,713]
Joe_FGA = [1395,1139,1497,1420,1386,1161,931,1052,1018,1025]
James_FGA = [1823,1621,1642,1613,1528,1485,1169,1354,1353,1279]
Anthony_FGA = [1572,1453,1481,1207,1502,1503,1025,1489,1643,806]
Danny_FGA = [881,873,974,979,834,1044,726,813,800,423]
Chris_FGA = [1087,1094,1027,1263,1158,1056,807,907,953,745]
Paul_FGA = [947,871,1291,1255,637,928,890,856,870,1170]
Kevin_FGA = [647,647,1366,1390,1668,1538,1297,1433,1688,467]
Derrick_FGA = [436,436,436,1208,1373,1597,695,0,164,835]
Dwayne_FGA = [1413,962,937,1739,1511,1384,837,1093,761,1084]
#Matrix
FieldGoalAttempts = np.array([David_FGA, Joe_FGA, James_FGA, Anthony_FGA, Danny_FGA, Chris_FGA, Paul_FGA, Kevin_FGA, Derrick_FGA, Dwayne_FGA])

#Points
David_PTS = [2832,2430,2323,2201,1970,2078,1616,2133,83,782]
Joe_PTS = [1653,1426,1779,1688,1619,1312,1129,1170,1245,1154]
James_PTS = [2478,2132,2250,2304,2258,2111,1683,2036,2089,1743]
Anthony_PTS = [2122,1881,1978,1504,1943,1970,1245,1920,2112,966]
Danny_PTS = [1292,1443,1695,1624,1503,1784,1113,1296,1297,646]
Chris_PTS = [1572,1561,1496,1746,1678,1438,1025,1232,1281,928]
Paul_PTS = [1258,1104,1684,1781,841,1268,1189,1186,1185,1564]
Kevin_PTS = [903,903,1624,1871,2472,2161,1850,2280,2593,686]
Derrick_PTS = [597,597,597,1361,1619,2026,852,0,159,904]
Dwayne_PTS = [2040,1397,1254,2386,2045,1941,1082,1463,1028,1331]
#Matrix
Points = np.array([David_PTS, Joe_PTS, James_PTS, Anthony_PTS, Danny_PTS, Chris_PTS, Paul_PTS, Kevin_PTS, Derrick_PTS, Dwayne_PTS])             
#FootBallGameData
#Instructions for this dataset:
# Simply copy ALL the lines in this script by pressing 
# CTRL+A on Windows 
# Once you have executed the commands the following objects
# will be created:
# Matrices:
# - Salary
# - Games
# - MinutesPlayed
# - FieldGoals
# - FieldGoalAttempts
# - Points
# Lists:
# - Players
# - Seasons
# Dictionaries:
# - Sdict
# - Pdict

#Comments:
#Seasons are labeled based on the first year in the season
#E.g. the 2012-2013 season is preseneted as simply 2012


#Import numpy
import numpy as np

#Seasons
Seasons = ["2005","2006","2007","2008","2009","2010","2011","2012","2013","2014"]
Sdict = {"2005":0,"2006":1,"2007":2,"2008":3,"2009":4,"2010":5,"2011":6,"2012":7,"2013":8,"2014":9}

#Players
Players = ["David","Joe","James","Anthony","Danny","Chris","Paul","Kevin","Derrick","Dwayne"]
Pdict = {"David":0,"Joe":1,"James":2,"Anthony":3,"Danny":4,"Chris":5,"Paul":6,"Kevin":7,"Derrick":8,"Dwayne":9}

#Salaries
David_Salary = [15946875,17718750,19490625,21262500,23034375,24806250,25244493,27849149,30453805,23500000]
Joe_Salary = [12000000,12744189,13488377,14232567,14976754,16324500,18038573,19752645,21466718,23180790]
James_Salary = [4621800,5828090,13041250,14410581,15779912,14500000,16022500,17545000,19067500,20644400]
Anthony_Salary = [3713640,4694041,13041250,14410581,15779912,17149243,18518574,19450000,22407474,22458000]
Danny_Salary = [4493160,4806720,6061274,13758000,15202590,16647180,18091770,19536360,20513178,21436271]
Chris_Salary = [3348000,4235220,12455000,14410581,15779912,14500000,16022500,17545000,19067500,20644400]
Paul_Salary = [3144240,3380160,3615960,4574189,13520500,14940153,16359805,17779458,18668431,20068563]
Kevin_Salary = [0,0,4171200,4484040,4796880,6053663,15506632,16669630,17832627,18995624]
Derrick_Salary = [0,0,0,4822800,5184480,5546160,6993708,16402500,17632688,18862875]
Dwayne_Salary = [3031920,3841443,13041250,14410581,15779912,14200000,15691000,17182000,18673000,15000000]
#Matrix
Salary = np.array([David_Salary, Joe_Salary, James_Salary, Anthony_Salary, Danny_Salary, Chris_Salary, Paul_Salary, Kevin_Salary, Derrick_Salary, Dwayne_Salary])

#Games 
David_G = [80,77,82,82,73,82,58,78,6,35]
Joe_G = [82,57,82,79,76,72,60,72,79,80]
James_G = [79,78,75,81,76,79,62,76,77,69]
Anthony_G = [80,65,77,66,69,77,55,67,77,40]
Danny_G = [82,82,82,79,82,78,54,76,71,41]
Chris_G = [70,69,67,77,70,77,57,74,79,44]
Paul_G = [78,64,80,78,45,80,60,70,62,82]
Kevin_G = [35,35,80,74,82,78,66,81,81,27]
Derrick_G = [40,40,40,81,78,81,39,0,10,51]
Dwayne_G = [75,51,51,79,77,76,49,69,54,62]
#Matrix
Games = np.array([David_G, Joe_G, James_G, Anthony_G, Danny_G, Chris_G, Paul_G, Kevin_G, Derrick_G, Dwayne_G])

#Minutes Played
David_MP = [3277,3140,3192,2960,2835,2779,2232,3013,177,1207]
Joe_MP = [3340,2359,3343,3124,2886,2554,2127,2642,2575,2791]
James_MP = [3361,3190,3027,3054,2966,3063,2326,2877,2902,2493]
Anthony_MP = [2941,2486,2806,2277,2634,2751,1876,2482,2982,1428]
Danny_MP = [3021,3023,3088,2821,2843,2935,2070,2722,2396,1223]
Chris_MP = [2751,2658,2425,2928,2526,2795,2007,2454,2531,1556]
Paul_MP = [2808,2353,3006,3002,1712,2880,2181,2335,2171,2857]
Kevin_MP = [1255,1255,2768,2885,3239,3038,2546,3119,3122,913]
Derrick_MP = [1168,1168,1168,3000,2871,3026,1375,0,311,1530]
Dwayne_MP = [2892,1931,1954,3048,2792,2823,1625,2391,1775,1971]
#Matrix
MinutesPlayed = np.array([David_MP, Joe_MP, James_MP, Anthony_MP, Danny_MP, Chris_MP, Paul_MP, Kevin_MP, Derrick_MP, Dwayne_MP])

#Field Goals
David_FG = [978,813,775,800,716,740,574,738,31,266]
Joe_FG = [632,536,647,620,635,514,423,445,462,446]
James_FG = [875,772,794,789,768,758,621,765,767,624]
Anthony_FG = [756,691,728,535,688,684,441,669,743,358]
Danny_FG = [468,526,583,560,510,619,416,470,473,251]
Chris_FG = [549,543,507,615,600,524,393,485,492,343]
Paul_FG = [407,381,630,631,314,430,425,412,406,568]
Kevin_FG = [306,306,587,661,794,711,643,731,849,238]
Derrick_FG = [208,208,208,574,672,711,302,0,58,338]
Dwayne_FG = [699,472,439,854,719,692,416,569,415,509]
#Matrix
FieldGoals  = np.array([David_FG, Joe_FG, James_FG, Anthony_FG, Danny_FG, Chris_FG, Paul_FG, Kevin_FG, Derrick_FG, Dwayne_FG])

#Field Goal Attempts
David_FGA = [2173,1757,1690,1712,1569,1639,1336,1595,73,713]
Joe_FGA = [1395,1139,1497,1420,1386,1161,931,1052,1018,1025]
James_FGA = [1823,1621,1642,1613,1528,1485,1169,1354,1353,1279]
Anthony_FGA = [1572,1453,1481,1207,1502,1503,1025,1489,1643,806]
Danny_FGA = [881,873,974,979,834,1044,726,813,800,423]
Chris_FGA = [1087,1094,1027,1263,1158,1056,807,907,953,745]
Paul_FGA = [947,871,1291,1255,637,928,890,856,870,1170]
Kevin_FGA = [647,647,1366,1390,1668,1538,1297,1433,1688,467]
Derrick_FGA = [436,436,436,1208,1373,1597,695,0,164,835]
Dwayne_FGA = [1413,962,937,1739,1511,1384,837,1093,761,1084]
#Matrix
FieldGoalAttempts = np.array([David_FGA, Joe_FGA, James_FGA, Anthony_FGA, Danny_FGA, Chris_FGA, Paul_FGA, Kevin_FGA, Derrick_FGA, Dwayne_FGA])

#Points
David_PTS = [2832,2430,2323,2201,1970,2078,1616,2133,83,782]
Joe_PTS = [1653,1426,1779,1688,1619,1312,1129,1170,1245,1154]
James_PTS = [2478,2132,2250,2304,2258,2111,1683,2036,2089,1743]
Anthony_PTS = [2122,1881,1978,1504,1943,1970,1245,1920,2112,966]
Danny_PTS = [1292,1443,1695,1624,1503,1784,1113,1296,1297,646]
Chris_PTS = [1572,1561,1496,1746,1678,1438,1025,1232,1281,928]
Paul_PTS = [1258,1104,1684,1781,841,1268,1189,1186,1185,1564]
Kevin_PTS = [903,903,1624,1871,2472,2161,1850,2280,2593,686]
Derrick_PTS = [597,597,597,1361,1619,2026,852,0,159,904]
Dwayne_PTS = [2040,1397,1254,2386,2045,1941,1082,1463,1028,1331]
#Matrix
Points = np.array([David_PTS, Joe_PTS, James_PTS, Anthony_PTS, Danny_PTS, Chris_PTS, Paul_PTS, Kevin_PTS, Derrick_PTS, Dwayne_PTS])             


# In[8]:


Salary


# In[10]:


# Simple display of data
plt.plot(Salary)
plt.show()


# In[13]:


plt.plot(Salary, c='Red', ls="-", marker='*', label=Players)
plt.show()


# In[19]:


plt.plot(Salary, c='Black', ls="-", marker='*', label=Players)
plt.plot(Salary, c='Yellow', ls="-", marker='*', label=Players)
plt.ticklabel_format(style='plain')
plt.xticks(list(range(len(Seasons))), Seasons, rotation=19)
plt.xlabel("Season")
plt.ylabel("Salary")
plt.title("Salary vs Season")
plt.legend(bbox_to_anchor=(1,1)) #shift+tab to check parameters
plt.show()


# In[22]:


def Analyze(aspect, playersList):
    for p in playersList:
        plt.plot(aspect, ls="--", marker=".", label=playersList)
    plt.ticklabel_format(style="plain")
    plt.xticks(list(range(len(Seasons))), Seasons, rotation=17)
    plt.xlabel("Season")
    plt.title("Salary Vs Season")
    plt.legend(bbox_to_anchor=(1,1)) #shift+tab to check parameters
    plt.show()


# In[23]:


Analyze(Games, ["James"])
Analyze(Salary, ["James", "David"])
Analyze(FieldGoals, Players)
Analyze(np.nan_to_num(FieldGoals/Games), Players)


# In[29]:


#Solution for Dynamic Markers
def Analyze(aspect, playersList):
    markerList = ["o", "p", "d", "h", "s", "D", "H", "p", "d", "*", "."]
    for p in playersList:
        plt.plot(aspect[Pdict[p]], ls="--", marker=markerList[Pdict[p]], label=playersList)
    plt.ticklabel_format(style="plain")
    plt.xticks(list(range(len(Seasons))), Seasons, rotation=17)
    plt.xlabel("Season")
    plt.title("Salary Vs Season")
    plt.legend(bbox_to_anchor=(1,1)) #shift+tab to check parameters
    plt.show()
Analyze(Games, ["James"])
Analyze(Salary, ["James", "David"])
Analyze(FieldGoals, Players)
Analyze(np.nan_to_num(FieldGoals/Games), Players)


# In[30]:


#Seasons
Seasons = ["2005","2006","2007","2008","2009","2010","2011","2012","2013","2014"]

#Players
Players = ["David","Joe","James","Anthony","Danny","Chris","Paul","Kevin","Derrick","Dwayne"]

#Free Kicks Vectors
David_FK = [696,667,623,483,439,483,381,525,18,196]
Joe_FK = [261,235,316,299,220,195,158,132,159,141]
James_FK = [601,489,549,594,593,503,387,403,439,375]
Anthony_FK = [573,459,464,371,508,507,295,425,459,189]
Danny_FK = [356,390,529,504,483,546,281,355,349,143]
Chris_FK = [474,463,472,504,470,384,229,241,223,179]
Paul_FK = [394,292,332,455,161,337,260,286,295,289]
Kevin_FK = [209,209,391,452,756,594,431,679,703,146]
Derrick_FK = [146,146,146,197,259,476,194,0,27,152]
Dwayne_FK = [629,432,354,590,534,494,235,308,189,284]

#Create Matrix Free Kicks
FreeKicks = np.array([David_FK, Joe_FK, James_FK, Anthony_FK, Danny_FK, Chris_FK, Paul_FK, Kevin_FK, Derrick_FK, Dwayne_FK])
# delete the vectors/list

#Free Kick Attempts Vectors
David_FKA = [819,768,742,564,541,583,451,626,21,241]
Joe_FKA = [330,314,379,362,269,243,186,161,195,176]
James_FKA = [814,701,771,762,773,663,502,535,585,528]
Anthony_FKA = [709,568,590,468,612,605,367,512,541,237]
Danny_FKA = [598,666,897,849,816,916,572,721,638,271]
Chris_FKA = [581,590,559,617,590,471,279,302,272,232]
Paul_FKA = [465,357,390,524,190,384,302,323,345,321]
Kevin_FKA = [256,256,448,524,840,675,501,750,805,171]
Derrick_FKA = [205,205,205,250,338,555,239,0,32,187]
Dwayne_FKA = [803,535,467,771,702,652,297,425,258,370]

#Create Matrix FreeKickAttempts 
FreeKickAttempts = np.array([David_FKA, Joe_FKA, James_FKA, Anthony_FKA, Danny_FKA, Chris_FKA, Paul_FKA, Kevin_FKA, Derrick_FKA, Dwayne_FKA])

# delete the vectors/list


# In[43]:


#Solution for Freekicks
def FootballAnalyze(aspect, playersList, xlabel, title):
    markerList = ["o", "p", "d", "h", "s", "D", "H", "p", "d", "*", "."]
    for p in playersList:
        plt.plot(aspect[Pdict[p]], ls="--", marker=markerList[Pdict[p]], label=playersList)
    plt.ticklabel_format(style="plain")
    plt.xticks(list(range(len(Games))), Seasons, rotation=17)
    plt.xlabel(xlabel)
    plt.title(title)
    plt.legend(bbox_to_anchor=(1,1)) #shift+tab to check parameters
    plt.show()

FreeKickAttemptsPerGame = np.round(np.nan_to_num(FreeKickAttempts/Games),0).astype("int64")
FootballAnalyze(FreeKickAttemptsPerGame, Players, "Goals", "Goals Vs Game")

#2. 2- Accuracy of Free Kicks
FootballAnalyze(np.round(np.nan_to_num(FreeKicks/FreeKickAttemptsPerGame)).astype("int64"), Players, "Free Kickts", "FreeKicks Vs Attemps")


#3Player playing style excluding Free Kicks
FootballAnalyze((Points - FreeKicks) / FieldGoals, Players, "Points" , " Player Style ")

