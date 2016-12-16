import numpy as np

def bolusTime(bolus, indices, Units, L):     # Indices is a moment in the days
    
    bolus1 = list(bolus)

    LL = L - len(bolus)

    x = 0
    for x in range(LL):
        bolus1.append(0)
        x += 1
    
    x = 0
    for x in range(indices):
        #bolus1.insert(0, bolus[len(bolus)-1])
        bolus1.insert(0, 0)
        bolus1.pop()
        x += 1

    bolus2 = np.array(bolus1)
    Units = float(Units)
    bolus3 = bolus2*Units

    return bolus3
 
