#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 17:28:49 2020
fitting data to exponentials (4KB exp3 (tif2 and tif5)) and ? and exp2 (tif3, tif6 and tif9)
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
    
# # #exp3 data
# 10.7 ,
# 14.6 ,
# 15.9 ,
# 16.7 ,
# 18.7 ,
# 19.8 ,
# 23.9 ,
# 24.8 ,
# 26.5 ,
# 28.1 ,
# 33.0 ,
# 35.7 ,
# 41.9 ,
# 52.2 ,
# 62.0 ,
# 70.0 ,
# 77.4 ,
# 88.1 ,
# 96.3 ,
# 105.6, 
# 115.4, 
# 132.0, 
# 12.4 ,
# 13.7 ,
# 14.4 ,
# 17.6 ,
# 21.7 ,
# 22.6 ,
# 24.3 ,
# 25.9 ,
# 30.7 ,
# 33.5 ,
# 39.6 ,
# 50.0 ,
# 59.8 ,
# 67.8 ,
# 75.2 ,
# 85.9 ,
# 94.1 ,
# 113.1, 
# 129.8, 

# # #exp2 data
17.0 ,
18.8 ,
20.6 ,
25.0 ,
28.6 ,
35.4 ,
38.0 ,
45.2 ,
48.0 ,
54.4 ,
57.0 ,
64.0 ,
68.0 ,
73.6 ,
83.6 ,
17.2 ,
25.9 ,
37.2 ,
40.0 ,
50.9 ,
17.2 ,
17.2 ,
25.9 ,
37.2 ,
40.0 ,
50.9 ,
14.6 ,
16.4 ,
18.2 ,
22.6 ,
26.2 ,
33.0 ,
35.6 ,
42.8 ,
45.6 ,
52.0 ,
54.6 ,
61.6 ,
65.6 ,
71.2 ,
74.8 ,
81.2 ,
101.4, 
110.4, 
131.8, 
177.4,

# #202004
5.0,
9.6,
12.4,
17.1,
23.0,
25.8,
30.5,
37.4,
43.4,
50.4,
56.6,
63.3,
69.9,
76.5,

#202005
4.8,
10.5,
16.8,
23.2,
29.1,
36.3,
41.5,
48.7,
55.3,
61.6,
67.4,
74.3,
81.0,
86.4,
92.8
])


y = np.array([

# #exp3 data
# 0.711 ,
# 0.557 ,
# 0.486 ,
# 0.467 ,
# 0.343 ,
# 0.311 ,
# 0.197 ,
# 0.169 ,
# 0.174 ,
# 0.099 ,
# 0.061 ,
# 0.048 ,
# 0.019 ,
# 0.012 ,
# 0.007 ,
# 0.692 ,
# 0.006 ,
# 0.003 ,
# 0.003 ,
# 0.004 ,
# 0.001 ,
# 0.003 ,
# 0.719 ,
# 0.536 ,
# 0.582 ,
# 0.420 ,
# 0.332 ,
# 0.261 ,
# 0.227 ,
# 0.177 ,
# 0.099 ,
# 0.074 ,
# 0.043 ,
# 0.020 ,
# 0.012 ,
# 0.010 ,
# 0.006 ,
# 0.008 ,
# 0.004 ,
# 0.004 ,
# 0.001 ,

# # #exp2 data
0.592 ,
0.509 ,
0.430 ,
0.253 ,
0.172 ,
0.087 ,
0.103 ,
0.043 ,
0.037 ,
0.024 ,
0.024 ,
0.016 ,
0.008 ,
0.012 ,
0.007 ,
0.574 ,
0.292 ,
0.092 ,
0.090 ,
0.046 ,
0.574 ,
0.574 ,
0.289 ,
0.092 ,
0.090 ,
0.047 ,
0.681 ,
0.562 ,
0.488 ,
0.410 ,
0.267 ,
0.169 ,
0.130 ,
0.123 ,
0.067 ,
0.042 ,
0.028 ,
0.019 ,
0.012 ,
0.034 ,
0.026 ,
0.017 ,
0.008 ,
0.006 ,
0.001 ,
0.006 ,

# #202004
0.878,
0.697,
0.471,
0.303,
0.169,
0.124,
0.093,
0.052,
0.036,
0.021,
0.012,
0.007,
0.006,
0.007,

#202005
0.732,
0.57,
0.357,
0.332,
0.244,
0.13,
0.084,
0.045,
0.03,
0.017,
0.014,
0.008,
0.005,
0.004,
0.003

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
plt.plot(xFit, model(xFit, *popt), 'b', label='fit params: a=%5.1f, b=%5.1f' % tuple(popt), lw=3.)
plt.plot(x, y, 'ko', label='experimental data (AE28)', lw=3.)
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

plt.savefig('new 4.5 kb Cherry.pdf', format='pdf')
plt.show()




