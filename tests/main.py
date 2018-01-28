#%%
import sys, logging

import matplotlib.pyplot as plt
sys.path.append("D:\\AdMarenWS\\HullCMap\\src")
import numpy
#%%
import numpy as np

import HullCmap

csv = []
for l in open(r'D:\AdMarenWS\HullCMap\tests\frame61.csv'):
    csv.append([float(v) for v in l.split(",")[:2]])

data = np.array(csv)
rad = np.deg2rad(data[:, 0])
r = data[:,1]
print(rad)
xp = np.multiply(r, np.cos(rad))[::-1]

yp = np.multiply(r, np.sin(rad))[::-1]
# yp = np.square(xp)

for x,y in zip(xp, yp):
    print("%0.3f, %0.3f"%(x,y))

ls =HullCmap.LewisSections(x=xp, y =yp, draft = 19.99)

ls.plotSection()
