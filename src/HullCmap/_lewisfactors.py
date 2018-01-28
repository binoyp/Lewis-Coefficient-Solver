"""Lewis Form factors a1, a2 and a3

"""
import numpy as np
import scipy as sp
import logging
import pdb
try:
    import matplotlib.pyplot as plt
    _MPL = 1
except ImportError as e:
    print(" Matplotlib not found: %s" % e)


class LewisSections(object):
    """Lewis conformal mapping solver

    """

    def __init__(self, *args, **kwargs):

        try:

            self.xarray = kwargs['x']
            self.yarray = kwargs['y']
            self.Ds = kwargs['draft']

            assert np.shape(self.xarray) == np.shape(self.yarray)
        except KeyError as e:
            print("Named argument %s missing in class instantiation" % e)

            return None

        if abs(self.xarray[0]) < 1e-6:  # micro meter tolerance
            print("half section ordinates detected")
            #self.xarray[0] = 0.0

            self.Bs = 2 * np.interp(self.Ds,
                                    xp=self.yarray,
                                    fp=self.xarray)

            self.As = 2 * np.trapz(self.yarray, self.xarray)

            self.sigma_s = self.As / (self.Bs * self.Ds)

        else:
            raise NotImplementedError(
                " Implementation in progress for full section")
            assert abs(self.xarray[0] + self.xarray[-1]
                       ) < 1e-3, "Symmetry check failed for input ordinates"
            print("Symmetrical sections")
            self.Bs = np.interp(self.Ds,
                                xp=self.yarray,
                                fp=self.xarray
                                )

    def GetLewisCoeffs(self, choosepos=True):

        self.h0 = (0.5 * self.Bs) / self.Ds
        self.sigma_s = self.As / (self.Bs * self.Ds)
        v0 = (4 * self.sigma_s) / np.pi
        c1 = 3 + v0 + ((1 - v0) * ((self.h0 - 1) / (self.h0 + 1))**2)
        c2 = (2 * c1) - 6
        c3 = c1 - 4

        self.a3_0 = (-c1 + 3 + np.sqrt(9 - (2 * c1))) / c1
        self.a3_1 = (-c1 + 3 - np.sqrt(9 - (2 * c1))) / c1
        if choosepos:
            self.a3 = self.a3_0
        else:
            self.a3 = self.a3_1
        self.a1 = ((self.h0 - 1) / (self.h0 + 1)) * (self.a3 + 1)

        return (self.a1, self.a3)

    def plotSection(self):
        if _MPL:
            self.GetLewisCoeffs()

            theta = np.linspace(np.pi, 0.5 * np.pi, 31)
            ms = (0.5 * self.Bs) / (1 + self.a1 + self.a3)

            x = ms * ((1 + self.a1) * np.sin(theta) -
                      (self.a3 * np.sin(3 * theta)))

            y = ms * ((1 - self.a1) * np.cos(theta) +
                      (self.a3 * np.cos(3 * theta)))

            plt.plot(x, y, 'r-+')
            plt.grid(1)
            plt.title(r"$\sigma_s$=%0.3f / $H_0$=%0.4f / $a_1$=%0.5f/$a_3$=%0.5f" %
                      (self.sigma_s, self.h0, self.a1, self.a3))
            plt.plot(self.xarray, -self.yarray)
            plt.show()
