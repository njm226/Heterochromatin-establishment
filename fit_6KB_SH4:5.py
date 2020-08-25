#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 17:28:49 2020
fitting data to exponentials ( 202004 and 202005)
@author: fabio
"""

import matplotlib.pyplot as plt
import numpy as np
#import pandas as pd
from scipy.optimize import curve_fit
from pylab import *
from scipy import stats
import uncertainties as unc
import uncertainties.unumpy as unp

# fitting function
def model(x,a,b):
    return a*np.exp(-x/b)

#experimental data
x = np.array([

11.3,
17.7,
24.2,
30.7,
38.1,
44.8,
51.8,
58.2,
65.4,
72.5,
78.2,
85.6,
92.3,
99.3,
105.7,
112.8,
119.2,
125.9,
132.7,
139.1,
146.5,
152.8,

10.9,
18.0,
24.6,
31.2,
38.7,
45.4,
52.5,
59.0,
66.2,
73.5,
79.2,
86.7,
93.5,
100.5,
106.9,
114.2,
120.7,
127.7,
134.6,

10.2,
17.1,
23.4,
30.9,
36.7,
43.5,
50.0,
57.9,
63.7,
70.3,
76.3,
83.4,
89.9,
96.9,
103.1,
110.2,
117.1,
122.9,
130.7


])


y = np.array([

0.864,
0.813,
0.669,
0.569,
0.433,
0.384,
0.366,
0.324,
0.302,
0.249,
0.209,
0.175,
0.154,
0.13,
0.101,
0.087,
0.074,
0.064,
0.063,
0.051,
0.046,
0.042,

0.847,
0.706,
0.595,
0.497,
0.392,
0.333,
0.322,
0.313,
0.281,
0.249,
0.213,
0.174,
0.14,
0.124,
0.103,
0.087,
0.072,
0.073,
0.058,


0.802,
0.643,
0.512,
0.522,
0.502,
0.441,
0.381,
0.355,
0.323,
0.288,
0.258,
0.208,
0.181,
0.146,
0.125,
0.103,
0.086,
0.069,
0.063

 ])




#Perform the curve fit
popt, pcov = curve_fit(model, x, y)
print(popt)

a, b = unc.correlated_values(popt, pcov)

# Plot data and best fit curve.
plt.scatter(x, y, s=3, linewidth=0, alpha=0.3)

px = np.linspace(1, 200, 200)
# use unumpy.exp
py = a * unp.exp(-px/b)

nom = unp.nominal_values(py)
std = unp.std_devs(py)

# plot the nominal value
plt.plot(px, nom, c='r')

#fx values for the fitted function
xFit = np.arange(0.0, 200, 0.001)

#plot the fitted function
plt.figure(figsize=[15,10])
plt.plot(xFit, model(xFit, *popt), 'b', label='fit params: a=%5.3f, b=%5.3f' % tuple(popt), lw=3.)
plt.plot(x, y, 'ko', label='experimental data (SH4 and SH5)', lw=3.)
# And the 2sigma uncertaintie lines
plt.fill_between(px, nom-2*std, nom+2*std, color='lightblue')
plt.plot(px, nom - 2 * std, c='c')
plt.plot(px, nom + 2 * std, c='c')

plt.ylim([0.001,1])
plt.yticks(fontsize=40)
plt.xticks(fontsize=40)
plt.xlim([0,200])
plt.yscale('log')
plt.xticks([50,100,150,200],[])
plt.yticks([1,0.1,0.01],[1, 0.1, 0.01])
plt.legend(fontsize=35)
plt.tick_params(width=4,length=4)
plt.savefig('5.9 kb SH5_4 mCherry.pdf', format='pdf')
#plt.savefig('6kb mCherry.eps', format='eps')
plt.show()




