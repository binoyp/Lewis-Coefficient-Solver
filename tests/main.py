#%%
import sys, logging
sys.path.append("D:\\AdMarenWS\\HullCMap\\src")
logger =logging.getLogger('base')
logger.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
logger.addHandler(ch)
#%%
import numpy as np

import HullCmap

xp = np.linspace(0, 1, 20)
yp = np.square(xp)

print(HullCmap.LewisFactors(xp,yp))
