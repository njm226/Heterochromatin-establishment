#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 17:28:49 2020
fitting data to exponentials (8KB exp1 (tif2 and tif5) and exp2 (tif2, tif5 and tif8))
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

#exp1 data
13.6,
15.0,
16.4,
17.5,
22.4,
23.5,
24.4,
33.8,
46.8,
51.2 ,
60.8 ,
72.0 ,
92.4 ,
101.4 ,
111.0 ,
120.4 ,
129.2 ,
138.6,
12.8,
13.9,
15.2,
16.2,
20.8,
41.1,
43.3,
47.4,
66.7,
85.6,
93.9,
102.8,
119.6,
128.3,
183.9,

#exp2 data
18.5,
20.4,
22.4,
27.2,
31.1,
38.5,
41.3,
49.1,
23.8,
34.2,
36.8,
46.8,
14.6,
16.4,
18.2,
26.2,
33.0,
35.6,
42.8,
61.6,
65.6,
71.2,
74.8,
81.2,
101.4,
110.4,
119.4,
131.8,
148.6,
177.4,

#unknown data
5.0,
9.8,
12.7,
17.5,
23.5,
26.4,
30.8,
38.3,
44.5,
51.2,
58.0,
64.6,
71.8,
78.7,
85.6,
91.4,
98.3,
105.4,
111.2,
119.4,
126.1,

#202005
5.1,
10.9,
17.4,
24.3,
31.6,
38.1,
43.6,
51.2,
58.1,
64.7,
70.8,
78.2,
84.8,
90.9,
98.5,
105.0,
111.0,
118.3,
124.5,
131.0,
137.7
])

y = np.array([
    
#exp1 data
0.884,
0.841,
0.786 ,
0.831,
0.824 ,
0.753,
0.771,
0.735,
0.000,
0.647,
0.576,
0.541,
0.479,
0.431,
0.397,
0.368,
0.415,
0.372,
0.892,
0.910,
0.876,
0.799,
0.834,
0.628,
0.714,
0.634,
0.529,
0.480,
0.392,
0.409,
0.511,
0.426,
0.000,

#exp2 data
0.999,
0.916,
0.900,
0.864,
0.822,
0.725,
0.714,
0.669,
0.828,
0.713,
0.700,
0.674,
0.937,
0.898,
0.903,
0.802,
0.759,
0.728,
0.663,
0.547,
0.543,
0.612,
0.564,
0.510,
0.429,
0.400,
0.373,
0.328,
0.307,
0.284,

#unknown data
0.871,
0.888,
0.848,
0.785,
0.718,
0.681,
0.643,
0.585,
0.547,
0.516,
0.486,
0.462,
0.472,
0.489,
0.48,
0.439,
0.433,
0.42,
0.379,
0.354,
0.313,

#202005
0.914,
0.847,
0.801,
0.852,
0.804,
0.766,
0.729,
0.676,
0.622,
0.604,
0.547,
0.512,
0.479,
0.44,
0.40,
0.385,
0.384,
0.348,
0.325,
0.309,
0.306
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
plt.plot(x, y, 'ko', label='experimental data (AE14)', lw=3.)
# And the 2sigma uncertaintie lines
plt.fill_between(px, nom-2*std, nom+2*std, color='lightblue')
plt.plot(px, nom - 2 * std, c='c')
plt.plot(px, nom + 2 * std, c='c')

plt.ylim([0.001,1])
plt.yticks(fontsize=40)
plt.xticks(fontsize=40)
plt.xticks([50,100,150,200])
plt.xlim([0,200])
plt.yscale('log')
plt.xticks([50,100,150,200])
plt.yticks([1,0.1,0.01],[1, 0.1, 0.01])
plt.legend(fontsize=35)
plt.tick_params(width=4,length=4)
#plt.xticks([])
plt.savefig('new 8Kb mCherry.pdf', format='pdf')
#plt.savefig('8kb mCherry.eps', format='eps')
plt.show()




