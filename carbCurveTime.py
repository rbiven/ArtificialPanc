# Jonswap Curve used for representing carbs.
# This was done to have control of curve shape and its shape is steeper
# than the rayliegh which is used for boluses

import numpy as np
from carbCurve import Carbs

"""

carb = Carbs(5.5, 5.0) # bolus is calculated for an entire day = 288 indices
print carb

indices = 100
grams  = 5.     # grams of carbs

carb = carb
x = 0
for x in range(indices):
    carb.insert(0, carb[len(carb)-1])
    carb.pop()
    x += 1

carb = np.array(carb)

grams = float(grams)

Carb = carb*grams
"""


def CarbTIME(carb, indices, grams):     # Indices is a moment in the days
    
    carb1 = list(carb)
    x = 0
    for x in range(indices):
        carb1.insert(0, 0)
        carb1.pop()
        x += 1

    carb2 = np.array(carb1)
    grams = float(grams)
    Carb = carb2*grams

    return Carb
 
