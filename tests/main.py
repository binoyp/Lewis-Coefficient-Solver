#%%
import sys, logging
sys.path.append("D:\\AdMarenWS\\HullCMap\\src")

#%%
import numpy as np

import HullCmap

xp = np.linspace(0, 1, 20)
yp = np.square(xp)

ls =HullCmap.LewisSections(x=xp, y =yp, draft = 0.6)

ls.plotSection()
