import numpy as np
#import matplotlib.pyplot as plt

#Rayleigh Curve
"""
s = 1.0     # sigma = scalar parameter of the distribution

xr  = []
y   = []
rc = []

m = 49.  # number of steps
c = (m-1)/4.    # to get step only up to 4 hours

x = 0   # abscissa
for x in range(int(m)):
    y.append(x/c)
    x =+ 1

x = 0
for x in range(len(y)):
    xr.append((y[x]/(s**2))*np.exp((-y[x]**2)/(2*s**2)))
    x =+ 1
    
z = sum(xr)

x = 0
for x in range(len(xr)):
    rc.append(xr[x]/z)
    x =+ 1

print yy, "sum = ", sum(yy)

plt.plot(y,yy)
plt.show()
"""

def Rayleigh(s,m):
    #s = 1.0        # sigma = scalar parameter of the distribution
    #m = 49.        # number of steps
    c = (m-1)/4.    # to get step only up to 4 hours
    
    xr  = []
    y   = []
    rc  = []

    x = 0           # abscissa
    for x in range(int(m)):
        y.append(x/c)
        x =+ 1

    x = 0
    for x in range(len(y)):
        xr.append((y[x]/(s**2))*np.exp((-y[x]**2)/(2*s**2)))
        x =+ 1
        
    z = sum(xr)

    x = 0
    for x in range(len(xr)):
        rc.append(xr[x]/z)
        x =+ 1

    return rc

# Create Insulin by appending 0 for 15 minutes
# Need to make Carbs steeper curve
