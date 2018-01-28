"""Unit tests using the results from report
'A COMPARISON OF THREE METHODS FOR COMPUTING THE ADDED MASS OF SHIP SECTIONS'

"""

import sys
sys.path.append("D:\\AdMarenWS\\HullCMap\\src")

import HullCmap
import numpy as np
import unittest


class IIHRTestCase(unittest.TestCase):
    def setUp(self):
        self.framepaths = [r"D:\AdMarenWS\HullCMap\tests\frame61.csv",
                           r"D:\AdMarenWS\HullCMap\tests\frame91.csv",
                           r"D:\AdMarenWS\HullCMap\tests\frame170.csv",
                           r"D:\AdMarenWS\HullCMap\tests\frame203.csv"]

        self.coeffs = [(0.235739, 0.001735),
                       (0.297847, -0.075660),
                       (0.249422, 0.044059),
                       (-0.377228, 0.125725)]

        self.TOL = 1e-4

    def test_testframes(self):
        for path, res in zip(self.framepaths, self.coeffs):
            csv = []
            with open(path) as _f:
                for l in _f:
                    csv.append([float(v) for v in l.split(",")[:2]])
            data = np.array(csv)
            rad = np.deg2rad(data[:, 0])
            r = data[:, 1]
            xp = np.multiply(r, np.cos(rad))[::-1]
            yp = np.multiply(r, np.sin(rad))[::-1]
            draft = yp[0]
            ls = HullCmap.LewisSections(x=xp, y=yp, draft=draft)
            a1, a3 = ls.GetLewisCoeffs()
            a01 = res[0]
            a03 = res[1]
            self.assertAlmostEqual(a1, a01, delta=self.TOL)


if __name__ == "__main__":
    unittest.main()
