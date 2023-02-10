import sys
import math
import numpy as np


# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

lon = input()
lat = input()
n = int(input())
classeur = [[],[]]
lat = lat.replace(',','.')
lon = lon.replace(',','.')

for i in range(n):
    defib = input()
    defib = defib.split(';')

    lonB, latB = defib[4], defib[5]
    lonB = lonB.replace(',','.')
    latB = latB.replace(',','.')
    
    
    x = (float(lonB) - float(lon)) * math.cos((float(lat)+float(latB))/2)
    y = float(latB) - float(lat)
    d = math.sqrt(x * x + y * y) * 6371
    
    classeur[0].append(d)
    classeur[1].append(defib[1])     

print(classeur[1][np.argmin(classeur[0])])
