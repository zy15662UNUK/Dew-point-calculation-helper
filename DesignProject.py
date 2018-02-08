"""
Created on Sat Oct 21 19:35:05 2017

@author: zy156
"""

'''
How to use it?
For example:
    type in the below codes in console:


    In [20]: CH4(temperature in celcius degree).enthalpy()

    Then you will see:

    Out[20]: 1084.4963653361813

    this is the enthalpy value in kJ/kg


CH4: low <= 1300k
CO2: low <= 1200k
N2: low <= 500k
NH3: low <= 1400K
HCN : low <= 1200K
NO2: low <= 1200K
NO: low <= 1200K
CO: low <= 1300K

'''
class gas(object):
    def __init__(self,temp):
        self.t = temp
        self.k = temp + 273.15
        self.T = float(self.t+273.15)/1000
    def enthalpy(self):
        dh_mole = self.T*self.data[0]+(self.T**2)*self.data[1]/2+(self.T**3)*self.data[2]/3+(self.T**4)*self.data[3]/4-self.data[4]/self.T+self.data[5]-self.data[7]
        return dh_mole/(self.data[-1]*10**(-3))+self.ini
    def high(self):
        self.data = self.high_T
    def low(self):
        self.data = self.low_T
class CH4(gas):
    def __init__(self,temp):
        super().__init__(temp)
        self.ini = 909.95
        self.low_T = [-0.703029, 108.4773,-42.52157,5.862788,0.678565,-76.84376,158.7163,-74.87310,16]
        self.high_T = [85.81217, 11.26467,-2.114146,0.138190,-26.42221,-153.5327,224.4143,-74.87310,16]
        if self.k <= 1300:
            self.data = self.low_T
        else:
            self.data = self.high_T

class CO2(gas):
    def __init__(self, temp):
        super().__init__(temp)
        self.ini = 505.84
#        low for T <= 1200k
        self.low_T = [24.99735,55.18696,-33.69137,7.948387,-0.136638,-403.6075,228.2431,-393.5224,44]
        self.high_T = [58.16639,2.720074,-0.492289,0.038844,-6.447293,-425.9186,263.6125,-393.5224,44]
        if self.k <= 1200:
            self.data = self.low_T
        else:
            self.data = self.high_T

class NH3(gas):
    def __init__(self, temp):
        super().__init__(temp)
        self.ini = 1689.8
        self.low_T = [19.99563,49.77119,-15.37599,1.921168,0.189174,-53.30667,203.8591,-45.89806,17]
        self.high_T = [52.02427,18.48801,-3.765128,0.248541,-12.45799,-85.53895,223.8022,-45.89806,17]
        if self.k <= 1400:
            self.data = self.low_T
        else:
            self.data = self.high_T

class HCN(gas):
    def __init__(self, temp):
        super().__init__(temp)
        self.low_T = [32.69373, 22.59205, -4.369142, -0.407697, -0.282399, 123.4811, 233.2597, 135.1432,27.0253]
        self.high_T = [52.36527, 5.563298, -0.953224, 0.056711, -7.564086, 103.8523, 244.8448, 135.1432,27.0253]
        self.ini = 135.1432/(self.low_T[-1]*10**(-3))
        if self.k <= 1200:
            self.data = self.low_T
        else:
            self.data = self.high_T
class N2(gas):
    def __init__(self, temp):
        super().__init__(temp)
        self.ini = 309.27
        self.low_T = [28.98641,1.853978,-9.647459,16.63537,0.000117,-8.671914,226.4168,0,28]
        self.high_T = [19.50583,19.88705,-8.598535,1.369784,0.527601,-4.935202,212.3900,0,28]
        if self.k <= 500:
            self.data = self.low_T
        else:
            self.data = self.high_T
class NO2(gas):
    def __init__(self, temp):
        super().__init__(temp)
        self.low_T = [16.10857,75.89525,-54.38740,14.30777,0.239423,26.17464,240.5386,33.09502, 46.0055]
        self.high_T = [56.82541,0.738053,-0.144721,0.009777,-5.459911,2.846456,290.5056,33.09502,46.0055]
        self.ini = 33.17912/(self.low_T[-1]*10**(-3))
        if self.k <= 1200:
            self.data = self.low_T
        else:
            self.data = self.high_T
class NO(gas):
    def __init__(self, temp):
        super().__init__(temp)
        self.low_T = [23.83491,12.58878,-1.139011,-1.497459,0.214194,83.35783,237.1219,90.29114,30.0061]
        self.high_T = [35.99169,0.957170,-0.148032,0.009974,-3.004088,73.10787,246.1619,90.29114,30.0061]
        self.ini = 90.24888/(self.low_T[-1]*10**(-3))
        if self.k <= 1200:
            self.data = self.low_T
        else:
            self.data = self.high_T
class CO(gas):
    def __init__(self, temp):
        super().__init__(temp)
        self.low_T = [25.56759,6.096130,4.054656,-2.671301,0.131021,-118.0089,227.3665,-110.5271,28.0101]
        self.high_T = [35.15070,1.300095,-0.205921,0.013550,-3.282780,-127.8375,231.7120,-110.5271,28.0101]
        self.ini = 442.40
        if self.k <= 1300:
            self.data = self.low_T
        else:
            self.data = self.high_T
class O2(gas):
    def __init__(self, temp):
        super().__init__(temp)
        self.low_T = [31.32234,-20.23531,57.86644,-36.50624,-0.007374,-8.903471,246.7945,0,31.9988]
        self.medium_T = [30.03235,8.772972,-3.988133,0.788313,-0.741599,-11.32468,236.1663,0,31.9988]
        self.high_T = [20.91111,10.72071,-2.020498,0.146449,9.245722,5.337651,237.6185,0,31.9988]
        self.ini = 271.01
        if self.k <= 700:
            self.data = self.low_T
        elif self.k <= 2000:
            self.data = self.medium_T
        else:
            self.data = self.high_T

A=CH4(110)
print(A)
