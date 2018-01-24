# -*- coding: utf-8 -*-
"""base equations for hull maps


"""
import numpy as np
import scipy as sp


def xp(an,phip, n):
    
    if an.shape[0] != phip.shape[0]:
        print("length of an must match phip's")
        return None

    return np.product(an, np.cos)
    