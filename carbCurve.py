# Log-Normal Distribution Curve used for representing carbs.
# This was done to have control of curve shape

import numpy as np

###################################################################################
# NOTES TO ADD
###################################################################################

"""
import matplotlib.pyplot as plt

m = 4.*60/5         # number of steps in 4 hours (including 0 - initial step)
c = (m-1)/4.        # to get step only up to 4 hours

# set up arrays  

xj   = []
y    = []        
LND  = []

x = 0               # abscissa (Wave frequency)
for x in range(int(m)):
    y.append(x/c)
    x =+ 1

print y

sigma = 0.25    # standard deviation
mu = 0.1        # mean

# Log-Normal Distribution 
#LND = ((1)/(y[x]*sigma*(2*Pi)**(0.5)))*np.exp(((-ln(y[x])-mu)**2)/(2*sigma**2))

x = 1
while x < len(y):
    LND.append((1/(y[x]*sigma*((2*np.pi)**(0.5))))*np.exp((-(np.log(y[x])-mu)**2)/(2*sigma**2)))
    x += 1

z = sum(LND)

LND1 = []

for x in range(len(LND)):
    LND1.append(LND[x]/z)
    x =+ 1

z1 = sum(LND1)

print "sum = ", z1

y.pop(0)

print "Length =", len(LND)

plt.plot(y,LND1)
plt.show()
#"""
#"""
#mu = 0.1       # mean
#sigma = 0.25   # standard deviation

def Carbs(sigma, mu, L):
    m = 6.*60/5         # number of steps in 4 hours (including 0 - initial step)
    #m = L         # number of steps in 4 hours (including 0 - initial step)
    c = (m-1)/6.        # to get step only up to 4 hours

    # set up arrays  

    xj   = []
    y    = []        
    LND  = []
    LND1 = []

    x = 0               # abscissa (Wave frequency)
    for x in range(int(m)):
        y.append(x/c)
        x =+ 1

    # Log-Normal Distribution 
    #LND = ((1)/(y[x]*sigma*(2*Pi)**(0.5)))*np.exp(((-ln(y[x])-mu)**2)/(2*sigma**2))

    x = 1
    while x < len(y):
        LND.append((1/(y[x]*sigma*((2*np.pi)**(0.5))))*np.exp((-(np.log(y[x])-mu)**2)/(2*sigma**2)))
        x += 1

    z = sum(LND)

    for x in range(len(LND)):
        LND1.append(LND[x]/z)
        x =+ 1

    z1 = sum(LND1)

    x = 0
    for x in range(L-len(LND1)):
        LND1.append(0.0)

    return LND1
#"""
