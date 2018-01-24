"""Module for mapping arbitary section to analytic functiion

Cross sections of the ship are represented by conformal mapping
Based on the paper : The Reperesentation of Ship Hulls by Conformal
Mapping Functions
By C. von Kerczek and E. O Tuck
"""

from .base import *

from ._classes import HullSection

from ._lewisfactors import LewisFactors

DEBUG = 1