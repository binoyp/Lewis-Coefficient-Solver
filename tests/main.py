#%%
import sys, logging

import matplotlib.pyplot as plt
sys.path.append("D:\\AdMarenWS\\HullCMap\\src")
import numpy
#%%
import numpy as np

import HullCmap

csv = []
for l in open(r'D:\AdMarenWS\HullCMap\tests\frame91.csv'):
    csv.append([float(v) for v in l.split(",")[:2]])

data = np.array(csv)
rad = np.deg2rad(data[:, 0])
r = data[:,1]

xp = np.multiply(r, np.cos(rad))[::-1]
print(xp[0])
yp = np.multiply(r, np.sin(rad))[::-1]
# yp = np.square(xp)

ls =HullCmap.LewisSections(x=xp, y =yp, draft = 19.99)

ls.plotSection()
