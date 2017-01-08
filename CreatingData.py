"""
Created on Tue Jan 03 10:55:39 2017

@author: Ricky
"""

#####################################################################
"""
Importing program modules
"""
#####################################################################

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from scipy.signal import savgol_filter

from datetime import datetime
from datetime import timedelta
from datetime import time
from datetime import date

from basal import Basal 
from bolusTime import bolusTime
from dailyBasal1 import Dbasal
from maxBasal import maxBasal
from carbCurve import Carbs
from carbCurveTime import CarbTIME

from dexTime import dexTime
from omniTime import omniTime
from carbTime import carbTime
from Flags import flags
from normalTime import normaltime
from oneday import oneday
from separateBGs import usableBasal
from gradientBG import gradientBG

#####################################################################
TDD = 49.0     # Total Daily Dosage. Pull from pump - Average should work for meow

upper = 160     # High glucose limit
lower = 70      # Low glucose limit
#####################################################################
"""
Importing Dexcom Data from TXT file
"""
#####################################################################

f = open("pyDexBH.txt")  # pyData2 is manually modified from Dexcom export 
lines = f.readlines()   # Read data from .txt file 
f.close()

f = open("omniBolusNew.txt")   # omniBolus is manually modified from Dexcom export
lines2 = f.readlines()      # Read data from .txt file 
f.close()

f = open("carbsEaten.txt")
lines3 = f.readlines()
f.close()

Dates, timeofday, BG = dexTime(lines)

####################################################################
"""
fig, ax1 = plt.subplots()
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter("%m/%d/%Y %H:%M"))
ax1.plot(Dates[:20], BG[:20])
ax1.set_xlabel('Date & Time')
ax1.set_ylabel('Blood Glucose Level [mg/dl]')
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter("%m/%d/%Y %H:%M"))
ax1.set_xlim(min(Dates),Dates[20])
plt.gcf().autofmt_xdate()
plt.grid(True)
plt.title('Dataset - Time Series of BG')
plt.show()
#"""


L = len(BG)
print "Lenght of BG =", L
sumBG = sum(BG)

DatesB, timeofdayB, BolusV = omniTime(lines2) 
DatesC, timeofdayC, CarbV = carbTime(lines3)

# Create Smooth BG
SBG = savgol_filter(BG, 5, 2)

print "Smooth SGBG =", len(SBG)

#####################################################################

basal, bolus = Basal(1,49)
#print "bolus sum =", sum(bolus)

Bolus = bolusTime(bolus, 0, 1, L)
#print Bolus

programBasalTime  = [ 0.0,  4.0,  5.0,  6.0, 6.5, 15.0, 18.5, 19.0, 22.5, 24.0]
programBasalValue = [1.05, 1.30, 1.45, 1.30, 1.35, 1.25, 1.40, 1.50, 1.05, 1.05]

TL = timeday = 24*60/5  # minutes in the day / 5 minute intervals

delta = (1./TL)*24.

PBV24 = [0]*TL
y = 1
for x in range(TL):
    if x*delta < programBasalTime[y]:
        PBV24.insert(x,y-1)
        x += 1
    else:
        PBV24.insert(x,y)
        x += 1
        y += 1

PBV24 = PBV24[:287]
    
PBV24.append(len(programBasalTime)-2)


PBR = [0]*288
y = 0
for x in range(len(PBR)):
    if PBV24[x] == y:
        PBR.insert(x,programBasalValue[y]*(5/60.))
    elif PBV24[x] == y+1:
        PBR.insert(x,programBasalValue[y+1]*(5/60.))
    elif PBV24[x] == y+2:
        PBR.insert(x,programBasalValue[y+2]*(5/60.))
    elif PBV24[x] == y+3:
        PBR.insert(x,programBasalValue[y+3]*(5/60.))
    elif PBV24[x] == y+4:
        PBR.insert(x,programBasalValue[y+4]*(5/60.))
    elif PBV24[x] == y+5:
        PBR.insert(x,programBasalValue[y+5]*(5/60.))
    elif PBV24[x] == y+6:
        PBR.insert(x,programBasalValue[y+6]*(5/60.))
    elif PBV24[x] == y+7:
        PBR.insert(x,programBasalValue[y+7]*(5/60.))
    elif PBV24[x] == y+8:
        PBR.insert(x,programBasalValue[y+8]*(5/60.))
    else:
        PBR.insert(x,programBasalValue[y+9]*(5/60.))

PBR = PBR[:287]
PBR.append(PBR[-1])

#add one extra value for midnight
basalActual = Dbasal(PBR)

#####################################################################
from carbCurve import Carbs

carb = Carbs(0.4, 0.0, L) # carb is calculated for an entire time
#print "carb sum =", sum(carb), carb

CarbsT = CarbTIME(carb, 3, 1)
#print CarbsT 

#####################################################################
"""
Analysis: Part 1 - Setting up low and high BG flags
"""
#####################################################################
addIns, addInsBG, hyperglycemia, lessIns, lessInsBG, hypoglycemia, normal, normalBG, NoActionReq, TimeNorm = flags(BG, Dates, upper, lower)
#####################################################################
"""
Analysis: Part 2 - Remove times from Normal when Carbs or Bolus are used.
"""
#####################################################################
BolusTime, CarbTime, carbsUsed, bolusUsed, greatJob, greatJobBG, greatJobTime = normaltime(Dates, DatesB, DatesC, normal, BG)
#####################################################################

"""
Analysis: Part 3 - Is Normal acceptable with current Basal Rate
"""
#####################################################################
# Data for Plotting
#####################################################################
t, d = oneday(1)    # t = time for one day in minutes, no date
                    # d = time for one day with date added (today)
#####################################################################
# Need to set up time
y = range(len(basalActual))
y = np.array(y)

z   = y*5/60.

# Get Carb to Day Indices
oneDayCarb = []

for x in range(len(d)):
    oneDayCarb.append(CarbsT[x])

####################################################################
# Caclulate Liver Basal Rate 
####################################################################

ISF  = 1800/TDD  # 1800 rule - Insulin Sensitivity Factor (ISF)
print "Insulin Sensitivity Factor (how much 1 unit[mg/dl] lowers BG = ",ISF

C2RBG   = 2.0 # Amount 1 carb raising BG - Ref: "Think Like a Pancreas"

####################################################################
# 1 - BOLUS
# Create array for all the boluses that take place
ABTD = []
x = 0
for x in range(len(BolusV)):
    ABTD.append(bolusTime(bolus, BolusTime[x], BolusV[x], L))
    x += 1
ABTD = np.array(ABTD)
ABTD = sum(ABTD)

####################################################################
# 2 - CARBS
# Create array for all the Carbs that take place
ACarbsT = []
for x in range(len(CarbV)):
    ACarbsT.append((CarbTIME(carb, CarbTime[x], CarbV[x])))
    x += 1
ACarbsT = np.array(ACarbsT)
ACarbsT = sum(ACarbsT)

####################################################################
# 3 - Basal Insulin
BI = basalActual + basalActual + basalActual
BI = np.array(BI)

####################################################################
# 4 - Dexcom Values
SBG = list(SBG)
SBG.insert(0,SBG[0])
SBG = np.array(SBG)

DBG = []
for x in range(1,len(SBG)):
    DBG.append(SBG[x]-SBG[x-1])

BGDex = np.array(DBG)
print "Differential Dexcom Values =", len(BGDex)
print "Carbs =", len(ACarbsT)
print "Differential Dexcom Values =", len(BGDex)
print "Actual Basal Insulin =",len(BI)
print "Boluses =", len(ABTD) 

####################################################################
# 5 - Basal Carbs
BL = ((ABTD*ISF) - (ACarbsT*C2RBG) + (BI*ISF) + BGDex)/C2RBG

# 6 - Change in Basal Carbs
BL = list(BL)
BL.insert(0,BL[0])

DBL = []
for x in range(1,len(BL)):
    DBL.append(BL[x]-BL[x-1])

DBL = np.array(DBL)

#<---------- 
# Make array for when carbs are eaten and how much 
#<----------

CarbsEaten = [0]*len(ACarbsT)

for x in range(len(CarbV)):
    CarbsEaten[CarbTime[x]] = CarbV[x]

#<---------- 
# Make array for when carbs are eaten and how much 
#<----------

BolusTaken = [0]*len(ACarbsT)

for x in range(len(BolusV)):
    BolusTaken[BolusTime[x]] = BolusV[x]

#<---------- 
# Export for Capstone 
#<----------

SBG = list(SBG)

SBG.pop(0)
BL.pop(0)

DFCarbs = (ACarbsT*C2RBG)
DFBolus = (ABTD*ISF)
DFBI = (BI*ISF)
DFBGChange = BGDex
DFBL = BL
DFBG = SBG
DFDBL = DBL


import pandas as pd
columnTitle = ['Date&Time','DFBGChange','Bolus Taken', 'Bolus Ingested', 'Basal Carbs (Liver)', 'Basal Insulin', 'Carbs Eaten', 'Carbs Ingested', 'BG']
DF = {'Date&Time':Dates,'BG':DFBG, 'DFBGChange': DFBGChange, 'Bolus Taken': BolusTaken, 'Bolus Ingested':DFBolus, 'Basal Carbs (Liver)':DFBL, 'Basal Insulin':DFBI, 'Carbs Eaten':CarbsEaten, 'Carbs Ingested':DFCarbs, 'Delta BL':DFDBL}
df = pd.DataFrame(DF, columns=columnTitle)

#df.to_csv(r'C:\Users\Ricky\Documents\Udacity\MLND\machine-learning-master\projects\capstone\DiabeathisSet.txt', header=columnTitle, index=None, sep=' ', mode='a')
#print df
