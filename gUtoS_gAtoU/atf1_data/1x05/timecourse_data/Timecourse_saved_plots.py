#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 14:35:05 2020

timecourse saved plots

@author: fabio
"""
import pickle
import matplotlib.pyplot as plt
import numpy as np

duration = 201

## save state_list
with open('cenH_small_1x05_gUtoM100_AtoU110_S55.txt', 'rb') as F:
    cenH_total_small = pickle.load(F)

## save state_list
with open('cenH_m_1x05_gUtoM100_AtoU110_S55.txt', 'rb') as F:
    cenH_total_m = pickle.load(F)

## save state_list
with open('cenH_large_1x05_gUtoM100_AtoU110_S55.txt', 'rb') as F:
    cenH_total_large = pickle.load(F)
    
## save state_list
with open('cenH_max_1x05_gUtoM100_AtoU110_S55.txt', 'rb') as F:
    cenH_total_max = pickle.load(F)


    
    
## save state_list
with open('EcoRV_small_1x05_gUtoM100_AtoU140_S55.txt', 'rb') as F:
    EcoRV_total_small = pickle.load(F)
    
## save state_list
with open('EcoRV_m_1x05_gUtoM100_AtoU140_S55.txt', 'rb') as F:
    EcoRV_total_m = pickle.load(F)
    
## save state_list
with open('EcoRV_large_1x05_gUtoM100_AtoU140_S55.txt', 'rb') as F:
    EcoRV_total_large = pickle.load(F)
    
## save state_list
with open('EcoRV_max_1x05_gUtoM7100_AtoU140_S55.txt', 'rb') as F:
    EcoRV_total_max = pickle.load(F)
    
    
# # #comparison EcoRV data sets

# ## save state_list
# with open('EcoRV_small_g41.txt', 'rb') as F:
#     EcoRV_total_small2 = pickle.load(F)
    
# ## save state_list
# with open('EcoRV_m_g41.txt', 'rb') as F:
#     EcoRV_total_m2 = pickle.load(F)
    
# ## save state_list
# with open('EcoRV_large_g41.txt', 'rb') as F:
#     EcoRV_total_large2 = pickle.load(F)
    
# ## save state_list
# with open('EcoRV_max_g41.txt', 'rb') as F:
#     EcoRV_total_max2 = pickle.load(F)
    
    
    
# ## save state_list
# with open('EcoRV_small_g39.txt', 'rb') as F:
#     EcoRV_total_small3 = pickle.load(F)
    
# ## save state_list
# with open('EcoRV_m_g39.txt', 'rb') as F:
#     EcoRV_total_m3 = pickle.load(F)
    
# ## save state_list
# with open('EcoRV_large_g39.txt', 'rb') as F:
#     EcoRV_total_large3 = pickle.load(F)
    
# ## save state_list
# with open('EcoRV_max_g39.txt', 'rb') as F:
#     EcoRV_total_max3 = pickle.load(F)
    

time = np.array(range(duration))

y_axis = np.array([cenH_total_small, EcoRV_total_small,  cenH_total_m, EcoRV_total_m, cenH_total_large, EcoRV_total_large,cenH_total_max, EcoRV_total_max,])
        
#fig, (ax1, ax2, ax3) = plt.subplots(nrows=1, ncols=3, figsize=((36, 12)))
fig, (ax1) = plt.subplots(nrows=1, ncols=1, figsize=((11.5, 10)))
#default line colors and styles
ax1.plot(time,EcoRV_total_small, color='yellowgreen', label='mCherry 23 kb region')
ax1.plot(time,cenH_total_small, color='cyan', label='cenH 23 kb region')
ax1.plot(time,EcoRV_total_m, color='black', label='mCherry 27.5 kb region')
#ax1.plot(time,cenH_total_m,'ro', label='cenH 24 kb region')
ax1.plot(time,EcoRV_total_large, color='red', label='mCherry 29 kb region')
#ax1.plot(time,cenH_total_large, color='blue', label='cenH 26 kb region')
ax1.plot(time,EcoRV_total_max, color='gold', label='mCherry 31 kb region')
#ax1.plot(time,cenH_total_max, color='purple', label='cenH 28 kb region')
ax1.fill_between(time, cenH_total_max, color='cyan')
ax1.legend(loc='upper left')
#ax1.set_ylabel("fraction of 'ON' cells", fontsize = 35)  
#ax1.set_xlabel('t (generations)', fontsize = 35)  
ax1.set_yscale('log')    
ax1.tick_params(labelsize='15')
ax1.set_ylim([0.001,1])
ax1.set_xlim([1,200])
#ax1.legend(fontsize='35')
ax1.legend([])
ax1.set_yticks([0.01, 0.1, 1])
ax1.set_yticklabels([0.01, 0.1, 1])
#ax1.set_yticklabels([])
ax1.set_xticks([50,100,150,200])
#ax1.set_xticklabels([50,100,150,200])
#ax1.set_xticklabels([])
ax1.tick_params(labelsize='30', width=4, length=4)

plt.savefig("timecourse_big_1x05.pdf")
    

# #fig, (ax1, ax2, ax3) = plt.subplots(nrows=1, ncols=3, figsize=((36, 12)))
# fig, (ax1) = plt.subplots(nrows=1, ncols=1, figsize=((12, 10)))
# #default line colors and styles
# ax1.plot(time,EcoRV_total_small, color='yellowgreen', label='EcoRV 20 kb region')
# ax1.plot(time,cenH_total_small, color='cyan', label='cenH 20 kb region')
# ax1.plot(time,EcoRV_total_m, color='black', label='EcoRV 24 kb region')
# #ax1.plot(time,cenH_total_m,'ro', label='cenH 24 kb region')
# ax1.plot(time,EcoRV_total_large, color='gold', label='EcoRV 26 kb region')
# #ax1.plot(time,cenH_total_large, color='blue', label='cenH 26 kb region')
# ax1.plot(time,EcoRV_total_max, color='red', label='EcoRV 28 kb region')
# #ax1.plot(time,cenH_total_max, color='purple', label='cenH 28 kb region')
# #ax1.legend(loc='upper left')
# ax1.set_ylabel('fraction of ''ON'' cells', fontsize = 25)  
# ax1.set_xlabel('t (generations)', fontsize = 25)  
# ax1.set_yscale('log')    
# ax1.tick_params(labelsize='30')
# ax1.set_ylim([0.01,1])
# ax1.set_xlim([1,46])
# ax1.legend(fontsize='35')

# #plt.savefig("timecourse_small_SAU24_local110")






# #fig, (ax1, ax2, ax3) = plt.subplots(nrows=1, ncols=3, figsize=((36, 12)))
# fig, (ax1) = plt.subplots(nrows=1, ncols=1, figsize=((15, 10)))
# #default line colors and styles
# #ax1.plot(time,EcoRV_total_small, color='red', label='EcoRV 23 kb region')
# #ax1.plot(time,cenH_total_small, color='grey', label='cenH 23 kb region')
# #ax1.plot(time,EcoRV_total_m, color='red', label='EcoRV 27.5 kb region')
# #ax1.plot(time,cenH_total_m,'grey', label='cenH 27.5 kb region')
# #ax1.plot(time,EcoRV_total_large, color='red', label='EcoRV 29 kb region')
# #ax1.plot(time,cenH_total_large, color='grey', label='cenH 29 kb region')
# ax1.plot(time,EcoRV_total_max, color='red', label='EcoRV 31 kb region')
# ax1.plot(time,cenH_total_max, color='grey', label='cenH 31 kb region')
# ax1.fill_between(time, cenH_total_max, color='grey')
# #ax1.legend(loc='upper left')
# #ax1.set_ylabel("fraction of 'ON' cells", fontsize = 35)  
# #ax1.set_xlabel('time (generations)', fontsize = 35)  
# ax1.set_yscale('log')    
# ax1.tick_params(labelsize='40', width=4, length=4)
# ax1.set_ylim([0.001,1])
# ax1.set_xlim([1,200])
# #ax1.set_xticklabels([])
# ax1.set_yticklabels([])
# ax1.legend(fontsize='35')

# plt.savefig("timecourse_big_l186.pdf")


# fig, (ax1, ax2, ax3) = plt.subplots(nrows=1, ncols=3, figsize=((36, 12)))
# fig, (ax1) = plt.subplots(nrows=1, ncols=1, figsize=((15, 10)))
# #default line colors and styles
# #ax1.plot(time,EcoRV_total_small, color='lightgreen')
# #ax1.plot(time,EcoRV_total_small2, color='lightgreen')
# #ax1.plot(time,EcoRV_total_small3, color='lightgreen', label='EcoRV 23 kb region')
# ax1.plot(time,EcoRV_total_m, color='grey')
# ax1.plot(time,EcoRV_total_m2,'grey')
# ax1.plot(time,EcoRV_total_m3,'grey', label='EcoRV 27.5 kb region')
# #ax1.plot(time,EcoRV_total_large, color='lightsalmon')
# #ax1.plot(time,EcoRV_total_large2, color='lightsalmon')
# #ax1.plot(time,EcoRV_total_large3, color='lightsalmon', label='EcoRV 29 kb region')
# #ax1.plot(time,EcoRV_total_max, color='yellow')
# #ax1.plot(time,EcoRV_total_max2, color='yellow')
# #ax1.plot(time,EcoRV_total_max3, color='yellow', label='EcoRV 31 kb region')
# #ax1.fill_between(time, EcoRV_total_small2, EcoRV_total_small3, color='lightgreen')
# ax1.fill_between(time, EcoRV_total_m2, EcoRV_total_m3, color='grey')
# #ax1.fill_between(time, EcoRV_total_max2, EcoRV_total_max3, color='yellow')
# #ax1.fill_between(time, EcoRV_total_max, EcoRV_total_max2, color='yellow')
# ax1.legend(loc='upper left')
# #ax1.set_ylabel("fraction of 'ON' cells", fontsize = 35)  
# #ax1.set_xlabel('time (generations)', fontsize = 35)  
# ax1.set_yscale('log')    
# ax1.tick_params(labelsize='40', width=4, length=4)
# ax1.set_ylim([0.001,1])
# ax1.set_xlim([1,200])
# ax1.set_xticklabels([])
# ax1.set_yticklabels([])
# #ax1.set_yticks([0.01, 0.1, 1])
# #ax1.set_yticklabels([0.01, 0.1, 1])
# ax1.legend(fontsize='35')

# plt.savefig("sensitivity_max.pdf")
    
    

