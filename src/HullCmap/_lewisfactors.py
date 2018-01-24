"""Lewis Form factors a1, a2 and a3

"""
import numpy as np
import scipy as sp
import logging

lewislogger = logging.getLogger('LewisFUncion')
lewislogger.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
lewislogger.addHandler(ch)


def LewisFactors(xp, yp, **kwargs):
    """Calculate Lewis form factors a1, a2, a3


    Args:
        xp (array): array of sectional x coordinates
        yp (array): array of sectional y coordinates
        **kwargs (optional args):
            b (float): Half breadth of the section 
            H (float): Draft fo the section
    """
    assert np.abs(xp[0]) < 1e6, "Starting x coordinate to be zero"

    if 'b' in kwargs:
        b = kwargs['b']
    else:
        b = np.max(xp) - np.min(xp)
        lewislogger.info("b calculated to be %0.3f" % b)

    if 'H' in kwargs:
        H = kwargs['H']
    else:
        H = np.max(yp) - np.min(yp)
        lewislogger.info("H calculated to be %0.3f" % H)

    a2 = 0.5 * (b - H)
    _bh = b + H
    S = 2 * np.trapz(yp, x=xp)
    a3 = 0.25 * (np.sqrt((_bh * _bh) + 8 * ((b * H - (2 * S) / np.pi)) - _bh))
    a1 = (0.5 * _bh) - a3
    return (a1, a2, a3)
