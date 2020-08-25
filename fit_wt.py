#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 17:28:49 2020
fitting data to exponentials (WT exp1 (tif1, tif4 and tif7), exp2 (tif1 and tif4), exp3 (tif1 and tif4))
@author: fabio
"""

import matplotlib.pyplot as plt
import numpy as np
#import pandas as pd
from scipy.optimize import curve_fit
from pylab import *
import uncertainties as unc
import uncertainties.unumpy as unp

# fitting function
def model(x,a,b):
    return a*np.exp(-x/b)

#experimental data
x = np.array([
    
#exp1
13.6,
16.4,
17.5,
22.4,
23.5,
44.4,
12.0,
13.4,
14.8,
15.9,
20.8,
42.8,
45.2,
49.6,
17.0 ,

#exp2
18.8 ,
20.6 ,
25.0 ,
35.4 ,
38.0 ,
45.2 ,
48.0 ,
54.4 ,
15.8 ,
23.8 ,
34.2 ,
36.8 ,
46.8 ,
14.6 ,
16.4 ,
18.2 ,
26.2 ,
33.0 ,
35.6 ,
42.8 ,
45.6 ,
52.0 ,
61.6 ,
81.2 ,
101.4, 
131.8, 
177.4,

#exp3
10.7 ,
14.6 ,
15.9 ,
16.7 ,
19.8 ,
24.8 ,
26.5 ,
28.1 ,
33.0 ,
35.7 ,
41.9 ,
52.2 ,
62.0 ,
77.4 ,
88.1 ,
96.3 ,
105.6, 
132.0, 
12.4 ,
13.7 ,
14.4 ,
16.5 ,
21.7 ,
22.6 ,
24.3 ,
25.9 ,
30.7 ,
33.5 ,
39.6 ,
50.0 ,
59.8 ,
75.2 ,
85.9 ,
103.3, 
129.8,

#202005
10.6,
17.6,
23.8,
30.2,
37.8


])

y = np.array([

#exp1
0.183,
0.050,
0.033,
0.004,
0.010,
0.000,
0.210,
0.137,
0.093,
0.051,
0.018,
0.004,
0.007,
0.000,

#exp2
0.088, 
0.059, 
0.041, 
0.028, 
0.013, 
0.008, 
0.009, 
0.007, 
0.005, 
0.120,
0.020,
0.008,
0.014, 
0.004, 
0.105, 
0.069, 
0.055, 
0.009, 
0.009, 
0.024, 
0.010, 
0.014, 
0.007, 
0.004, 
0.005, 
0.003, 
0.000, 
0.000,

#exp3
0.233 ,
0.072 ,
0.041 ,
0.052 ,
0.028 ,
0.015 ,
0.013 ,
0.013 ,
0.011 ,
0.012 ,
0.008 ,
0.005 ,
0.004 ,
0.003 ,
0.002 ,
0.000 ,
0.001 ,
0.001 ,
0.193 ,
0.135 ,
0.102 ,
0.059 ,
0.029 ,
0.012 ,
0.015 ,
0.013 ,
0.008 ,
0.007 ,
0.009 ,
0.004 ,
0.004 ,
0.003 ,
0.002 ,
0.003 ,
0.000 ,

#202005
0.215,
0.044,
0.023,
0.006,
0.004

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
plt.plot(x, y, 'ko', label='experimental data (wt)', lw=3.)
# And the 2sigma uncertaintie lines
plt.fill_between(px, nom-2*std, nom+2*std, color='lightblue')
plt.plot(px, nom - 2 * std, c='c')
plt.plot(px, nom + 2 * std, c='c')

plt.ylim([0.001,1])
plt.yticks(fontsize=40)
plt.xticks(fontsize=40)
plt.xlim([0,200])
plt.xticks([])
plt.yscale('log')
plt.xticks([50,100,150,200],[])
plt.yticks([1,0.1,0.01],[1, 0.1, 0.01])
plt.legend(fontsize=35)
plt.tick_params(width=4,length=4)
plt.savefig('new WT mCherry.pdf', format='pdf')
#plt.savefig('WT mCherry.eps', format='eps')
plt.show()




