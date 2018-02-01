"""data structures for section mapping

"""

from .base import *

class HullSection(object):
    """Hull Section Class

    Class to represent typical hull represented by x,y points
    in cartesian coordinates
    """

    def __init__(self, xp, yp):
        """initialisation

        Args:
            xp (numpy array) :

        """
        self.x = xp
        self.y = yp

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        # TODO: implement type check and list conversions
        self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, x):
        self.__y = x

    @property
    def N(self):
        assert self.__y.shape[0] == self.__x.shape[0], "Oops something wrong\
        x and y are not of same size"
        return self.__n
