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
import pickle

# fitting function
def model(x,a,b):
    return a*np.exp(-x/b)




## save state_list
with open('EcoRV_small_full_gAtoU50_UtoM130_S300.txt', 'rb') as F:
    EcoRV_total_small = pickle.load(F)
    
## save state_list
with open('EcoRV_m_full_gAtoU50_UtoM130_S300.txt', 'rb') as F:
    EcoRV_total_m = pickle.load(F)
    
## save state_list
with open('EcoRV_large_full_gAtoU50_UtoM130_S300.txt', 'rb') as F:
    EcoRV_total_large = pickle.load(F)
    
## save state_list
with open('EcoRV_max_full_gAtoU50_UtoM130_S300.txt', 'rb') as F:
    EcoRV_total_max = pickle.load(F)


duration=198
y = EcoRV_total_small[3:]
x = np.array(range(duration))


#Perform the curve fit
popt, pcov = curve_fit(model, x, y)
print(popt[1])

a, b = unc.correlated_values(popt, pcov)

# Plot data and best fit curve.
#plt.scatter(x,y, s=3, linewidth=0, alpha=0.3)

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
plt.plot(x, y, 'r', label='experimental data', lw=3.)
# And the 2sigma uncertaintie lines
#plt.fill_between(px, nom-2*std, nom+2*std, color='lightblue')
plt.plot(px, nom - 2 * std, c='c')
plt.plot(px, nom + 2 * std, c='c')

plt.ylim([0.001,1])
plt.yticks(fontsize=40)
plt.xticks(fontsize=40)
plt.xlim([0,200])
plt.yscale('log')
#plt.xticks([50,100,150,200],[])
plt.yticks([1,0.1,0.01],[1, 0.1, 0.01])
plt.legend(fontsize=35)
plt.tick_params(width=4,length=4)

#plt.savefig('new 4.5 kb Cherry.pdf', format='pdf')
plt.show()




