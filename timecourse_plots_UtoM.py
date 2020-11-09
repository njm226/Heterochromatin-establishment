#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 13:16:19 2019
histogramm and timecourse data
@author: fabio
"""

import numpy as np
#import pandas as pd
import matplotlib.pyplot as plt
#from smaller_model_function_UtoM import simple_small as ss
from UtoM_model import simple as ss
import multiprocessing
#import time
#import pickle
pool = multiprocessing.Pool(multiprocessing.cpu_count())



X_Y=[[153,87,110]]
X_Y_sm=[[182,87,110]]
X_Y_sl=[[191,87,110]]
X_Y_max=[[203,87,110]]

reps=10000

repeat=reps*X_Y
repeat_sm=reps*X_Y_sm
repeat_sl=reps*X_Y_sl
repeat_max=reps*X_Y_max

duration=201

if __name__ == '__main__':
    status_small = pool.map(ss, repeat) 
    status_m = pool.map(ss, repeat_sm) 
    status_large = pool.map(ss, repeat_sl) 
    status_max = pool.map(ss, repeat_max)

# status_small = []
# for i in repeat:
#     status_small.append(ss(i))
    
# print(status_small)
# #
# status_large = []
# for i in repeat:
#     status_large.append(sl(i))

# status_m = []
# for i in repeat:
#     status_m.append(sl(i))

#small system
reporters_diff_small = np.zeros([len(repeat),duration])
reporters_off_small = np.zeros([len(repeat),duration])
reporters_on_small = np.zeros([len(repeat),duration])


cenH_list_small = np.zeros([len(repeat),duration])
EcoRV_list_small = np.zeros([len(repeat),duration])



#medium system
reporters_diff_m = np.zeros([len(repeat),duration])
reporters_off_m = np.zeros([len(repeat),duration])
reporters_on_m = np.zeros([len(repeat),duration])


cenH_list_m = np.zeros([len(repeat),duration])
EcoRV_list_m = np.zeros([len(repeat),duration])



#large system
reporters_diff_large = np.zeros([len(repeat),duration])
reporters_off_large = np.zeros([len(repeat),duration])
reporters_on_large = np.zeros([len(repeat),duration])


cenH_list_large = np.zeros([len(repeat),duration])
EcoRV_list_large = np.zeros([len(repeat),duration])



#max system
reporters_diff_max = np.zeros([len(repeat),duration])
reporters_off_max = np.zeros([len(repeat),duration])
reporters_on_max = np.zeros([len(repeat),duration])


cenH_list_max = np.zeros([len(repeat),duration])
EcoRV_list_max = np.zeros([len(repeat),duration])



#wt system
                   
cenH_average = np.zeros(len(repeat))
EcoRV_average = np.zeros(len(repeat))

#4.5kb insert system

cenH_average_m = np.zeros(len(repeat))
EcoRV_average_m = np.zeros(len(repeat))

#6kb insert system

cenH_average_large = np.zeros(len(repeat))
EcoRV_average_large = np.zeros(len(repeat))


for elt in range(len(repeat)):
    
    cenH_small = np.array(status_small[elt][0])
    EcoRV_small = np.array(status_small[elt][1])
    
    
    
    # generate list with cenH and EcoRV states being both at different states (1)
    reporter_diff_small = cenH_small != EcoRV_small
    #transform that vector into a int vector
    reporter_diff_small = reporter_diff_small.astype(int)
    # copy this vector into reporter_states vector
    reporters_diff_small[elt]=reporter_diff_small
    
    
    
    # generate list with cenH and EcoRV states being both switched off
    reporter_off_small = np.zeros(len(cenH_small),'int')
    for index in range(len(cenH_small)):
        if cenH_small[index]==1 and EcoRV_small[index]==1:
            reporter_off_small[index]=1
        else:
            reporter_off_small[index]=0
            
    reporters_off_small[elt]=reporter_off_small
    
    
    
    # generate list with cenH and EcoRV states being both switched on
    reporter_on_small = np.zeros(len(cenH_small),'int')
    for Index in range(len(cenH_small)):
        if cenH_small[Index]==0 and EcoRV_small[Index]==0:
            reporter_on_small[Index]=1
        else:
            reporter_on_small[Index]=0
            
    reporters_on_small[elt]=reporter_on_small
    
    
    #switch the values of the list (1 stands now for timepoint when reporter is on)
    cenH_small=1-cenH_small
    EcoRV_small=1-EcoRV_small
    
    cenH_list_small[elt]=cenH_small
    EcoRV_list_small[elt]=EcoRV_small
    
    
    
    
    
    
    
    
    cenH_m = np.array(status_m[elt][0])
    EcoRV_m = np.array(status_m[elt][1])
    
    
    
    # generate list with cenH and EcoRV states being both at different states (1)
    reporter_diff_m = cenH_m != EcoRV_m
    #transform that vector into a int vector
    reporter_diff_m = reporter_diff_m.astype(int)
    # copy this vector into reporter_states vector
    reporters_diff_m[elt]=reporter_diff_m
    
    
    # generate list with cenH and EcoRV states being both switched off
    reporter_off_m = np.zeros(len(cenH_m),'int')
    for index in range(len(cenH_m)):
        if cenH_m[index]==1 and EcoRV_m[index]==1:
            reporter_off_m[index]=1
        else:
            reporter_off_m[index]=0
            
    reporters_off_m[elt]=reporter_off_m
    
    
    # generate list with cenH and EcoRV states being both switched on
    reporter_on_m = np.zeros(len(cenH_m),'int')
    for Index in range(len(cenH_m)):
        if cenH_m[Index]==0 and EcoRV_m[Index]==0:
            reporter_on_m[Index]=1
        else:
            reporter_on_m[Index]=0
            
    reporters_on_m[elt]=reporter_on_m
    
    #switch the values of the list (1 stands now for timepoint when reporter is on)
    cenH_m=1-cenH_m
    EcoRV_m=1-EcoRV_m
    
    cenH_list_m[elt]=cenH_m
    EcoRV_list_m[elt]=EcoRV_m
    
    
    
    
    
    
    cenH_large = np.array(status_large[elt][0])
    EcoRV_large = np.array(status_large[elt][1])
    
    
    
    # generate list with cenH and EcoRV states being both at different states (1)
    reporter_diff_large = cenH_large != EcoRV_large
    #transform that vector into a int vector
    reporter_diff_large = reporter_diff_large.astype(int)
    # copy this vector into reporter_states vector
    reporters_diff_large[elt]=reporter_diff_large
    
    
    # generate list with cenH and EcoRV states being both switched off
    reporter_off_large = np.zeros(len(cenH_large),'int')
    for index in range(len(cenH_large)):
        if cenH_large[index]==1 and EcoRV_large[index]==1:
            reporter_off_large[index]=1
        else:
            reporter_off_large[index]=0
            
    reporters_off_large[elt]=reporter_off_large
    
    
    # generate list with cenH and EcoRV states being both switched on
    reporter_on_large = np.zeros(len(cenH_large),'int')
    for Index in range(len(cenH_large)):
        if cenH_large[Index]==0 and EcoRV_large[Index]==0:
            reporter_on_large[Index]=1
        else:
            reporter_on_large[Index]=0
            
    reporters_on_large[elt]=reporter_on_large
    
    #switch the values of the list (1 stands now for timepoint when reporter is on)
    cenH_large=1-cenH_large
    EcoRV_large=1-EcoRV_large
    
    cenH_list_large[elt]=cenH_large
    EcoRV_list_large[elt]=EcoRV_large
    
    
    
    
    
    
    
    cenH_max = np.array(status_max[elt][0])
    EcoRV_max = np.array(status_max[elt][1])
    
    
    
    # generate list with cenH and EcoRV states being both at different states (1)
    reporter_diff_max = cenH_max != EcoRV_max
    #transform that vector into a int vector
    reporter_diff_max = reporter_diff_max.astype(int)
    # copy this vector into reporter_states vector
    reporters_diff_max[elt]=reporter_diff_max
    
    
    # generate list with cenH and EcoRV states being both switched off
    reporter_off_max = np.zeros(len(cenH_max),'int')
    for index in range(len(cenH_max)):
         if cenH_max[index]==1 and EcoRV_max[index]==1:
             reporter_off_max[index]=1
         else:
             reporter_off_max[index]=0
            
    reporters_off_max[elt]=reporter_off_max
    
   
    # generate list with cenH and EcoRV states being both switched on
    reporter_on_max = np.zeros(len(cenH_max),'int')
    for Index in range(len(cenH_max)):
         if cenH_max[Index]==0 and EcoRV_max[Index]==0:
             reporter_on_max[Index]=1
         else:
             reporter_on_max[Index]=0
            
    reporters_on_max[elt]=reporter_on_max
    
    #switch the values of the list (1 stands now for timepoint when reporter is on)
    cenH_max=1-cenH_max
    EcoRV_max=1-EcoRV_max
    
    cenH_list_max[elt]=cenH_max
    EcoRV_list_max[elt]=EcoRV_max
    
    
    
    
    print(cenH_small)
    print(cenH_m)
    print(cenH_large)
    print(cenH_max)
    
    
    
    
    
    
    
    
    
#     #calculate the average switch off time off all system sizes
    
    
#     #wt system
#     CENH = np.array(status_small[elt][0])
#     ECORV = np.array(status_small[elt][1])
    
#     if 1 in CENH:
#         # tell me when
#         cenH_silenced = list(CENH).index(1)
    
#     if 1 in ECORV:
#         # tell me when
#         EcoRV_silenced = list(ECORV).index(1)
        
        
    
#     #4.5kb insert system
#     CENH_m = np.array(status_m[elt][0])
#     ECORV_m = np.array(status_m[elt][1])
    
#     if 1 in CENH_m:
#         # tell me when
#         cenH_silenced_m = list(CENH_m).index(1)
    
#     if 1 in ECORV_m:
#         # tell me when
#         EcoRV_silenced_m = list(ECORV_m).index(1)
    
    
    
#     #6kb insert system
#     CENH_large = np.array(status_large[elt][0])
#     ECORV_large = np.array(status_large[elt][1])
    
#     if 1 in CENH_large:
#         # tell me when
#         cenH_silenced_large = list(CENH_large).index(1)
    
#     if 1 in ECORV_large:
#         # tell me when
#         EcoRV_silenced_large = list(ECORV_large).index(1)
        
        
        
    
#     #wt system
#     cenH_average[elt] = cenH_silenced
#     EcoRV_average[elt] = EcoRV_silenced

    
    
    
#     #4.5kb insert system
#     cenH_average_m[elt] = cenH_silenced_m
#     EcoRV_average_m[elt] = EcoRV_silenced_m
    
    
    
#     #6kb insert system
#     cenH_average_large[elt] = cenH_silenced_large
#     EcoRV_average_large[elt] = EcoRV_silenced_large



# #wt system
# cenH_Average = sum(cenH_average)/len(repeat)
# EcoRV_Average = sum(EcoRV_average)/len(repeat)

# #4.5kb insert system
# cenH_Average_m = sum(cenH_average_m)/len(repeat)
# EcoRV_Average_m = sum(EcoRV_average_m)/len(repeat)


# #6kb insert system
# cenH_Average_large = sum(cenH_average_large)/len(repeat)
# EcoRV_Average_large = sum(EcoRV_average_large)/len(repeat)
    
# print(cenH_Average)
# print(cenH_Average_m)
# print(cenH_Average_large)

# print(EcoRV_Average)
# print(EcoRV_Average_m)
# print(EcoRV_Average_large)


    

diff_small = (sum(reporters_diff_small))/reps
off_small = (sum(reporters_off_small))/reps
on_small = (sum(reporters_on_small))/reps




diff_m = (sum(reporters_diff_m))/reps
off_m = (sum(reporters_off_m))/reps
on_m = (sum(reporters_on_m))/reps




diff_large = (sum(reporters_diff_large))/reps
off_large = (sum(reporters_off_large))/reps
on_large = (sum(reporters_on_large))/reps




diff_max = (sum(reporters_diff_max))/reps
off_max = (sum(reporters_off_max))/reps
on_max = (sum(reporters_on_max))/reps





#output
cenH_total_small = (sum(cenH_list_small))/reps
#
EcoRV_total_small = (sum(EcoRV_list_small))/reps




cenH_total_m = (sum(cenH_list_m))/reps
#
EcoRV_total_m = (sum(EcoRV_list_m))/reps




cenH_total_large = (sum(cenH_list_large))/reps
#
EcoRV_total_large = (sum(EcoRV_list_large))/reps




cenH_total_max = (sum(cenH_list_max))/reps

EcoRV_total_max = (sum(EcoRV_list_max))/reps



    
    
    
    



    
# # save state_list
# with open('cenH_small_1x.txt', 'wb') as F:
#     pickle.dump(cenH_total_small, F)
    
# # save state_list
# with open('cenH_m_1x.txt', 'wb') as F:
#     pickle.dump(cenH_total_m, F)
    
# # save state_list
# with open('cenH_large_1x.txt', 'wb') as F:
#   pickle.dump(cenH_total_large, F)
    
# # save state_list
# with open('cenH_max_1x.txt', 'wb') as F:
#     pickle.dump(cenH_total_max, F)
    
    
    

    
# # save state_list
# with open('EcoRV_small_1x.txt', 'wb') as F:
#     pickle.dump(EcoRV_total_small, F)
    
# # save state_list
# with open('EcoRV_m_1x.txt', 'wb') as F:
#     pickle.dump(EcoRV_total_m, F)
    
# # save state_list
# with open('EcoRV_large_1x.txt', 'wb') as F:
#     pickle.dump(EcoRV_total_large, F)
    
# # save state_list
# with open('EcoRV_max_1x.txt', 'wb') as F:
#     pickle.dump(EcoRV_total_max, F)



# ## save state_list
# with open('cenH_small_SAU24_new.txt', 'rb') as F:
#     cenH_total_small = pickle.load(F)

# ## save state_list
# with open('cenH_m_SAU24_new.txt', 'rb') as F:
#     cenH_total_m = pickle.load(F)

# ## save state_list
# with open('cenH_large_SAU24_new.txt', 'rb') as F:
#     cenH_total_large = pickle.load(F)
    
# ## save state_list
# with open('cenH_max_SAU24_new.txt', 'rb') as F:
#     cenH_total_max = pickle.load(F)

    
    
# ## save state_list
# with open('EcoRV_small_SAU24_new.txt', 'rb') as F:
#     EcoRV_total_small = pickle.load(F)
    
# ## save state_list
# with open('EcoRV_m_SAU24_new.txt', 'rb') as F:
#     EcoRV_total_m = pickle.load(F)
    
# ## save state_list
# with open('EcoRV_large_SAU24_new.txt', 'rb') as F:
#     EcoRV_total_large = pickle.load(F)
    
# ## save state_list
# with open('EcoRV_max_SAU24_new.txt', 'rb') as F:
#     EcoRV_total_max = pickle.load(F)
    
    

time = np.array(range(duration))

y_axis = np.array([cenH_total_small, EcoRV_total_small,  cenH_total_m, EcoRV_total_m, cenH_total_large, EcoRV_total_large,cenH_total_max, EcoRV_total_max,])
        
#fig, (ax1, ax2, ax3) = plt.subplots(nrows=1, ncols=3, figsize=((36, 12)))
fig, (ax1) = plt.subplots(nrows=1, ncols=1, figsize=((15, 10)))
#default line colors and styles
ax1.plot(time,EcoRV_total_small, color='yellowgreen', label='mCherry 23 kb region')
ax1.plot(time,cenH_total_small, color='cyan', label='cenH 23 kb region')
ax1.plot(time,EcoRV_total_m, color='black', label='mCherry 27.5 kb region')
#ax1.plot(time,cenH_total_m,'ro', label='cenH 24 kb region')
ax1.plot(time,EcoRV_total_large, color='red', label='mCherry 29 kb region')
#ax1.plot(time,cenH_total_large, color='blue', label='cenH 26 kb region')
ax1.plot(time,EcoRV_total_max, color='gold', label='mCherry 31 kb region')
#ax1.plot(time,cenH_total_max, color='purple', label='cenH 28 kb region')
ax1.legend(loc='upper left')
#ax1.set_ylabel("fraction of 'ON' cells", fontsize = 35)  
#ax1.set_xlabel('t (generations)', fontsize = 35)  
ax1.set_yscale('log')    
ax1.tick_params(labelsize='30')
ax1.set_ylim([0.001,1])
ax1.set_xlim([1,200])
ax1.legend(fontsize='25')

plt.savefig("timecourse_UtoM.pdf")
    

# #fig, (ax1, ax2, ax3) = plt.subplots(nrows=1, ncols=3, figsize=((36, 12)))
# fig, (ax1) = plt.subplots(nrows=1, ncols=1, figsize=((12, 10)))
# #default line colors and styles
# ax1.plot(time,EcoRV_total_small, color='yellowgreen', label='EcoRV 20 kb region')
# ax1.plot(time,cenH_total_small, color='cyan', label='cenH 20 kb region')
# ax1.plot(time,EcoRV_total_m, color='red', label='EcoRV 24 kb region')
# #ax1.plot(time,cenH_total_m,'ro', label='cenH 24 kb region')
# ax1.plot(time,EcoRV_total_large, color='black', label='EcoRV 26 kb region')
# #ax1.plot(time,cenH_total_large, color='blue', label='cenH 26 kb region')
# ax1.plot(time,EcoRV_total_max, color='gold', label='EcoRV 28 kb region')
# #ax1.plot(time,cenH_total_max, color='purple', label='cenH 28 kb region')
# #ax1.set_title('Combined debt growth over time')
# #ax1.legend(loc='upper left')
# ax1.set_ylabel('fraction of ''ON'' cells', fontsize = 25)  
# ax1.set_xlabel('t (generations)', fontsize = 25)  
# ax1.set_yscale('log')    
# ax1.tick_params(labelsize='18')
# ax1.set_ylim([0.01,1])
# ax1.set_xlim([1,46])
# ax1.legend(fontsize='20')

#plt.savefig("timecourse_small_SUS55_g90")

# ax2.plot(time, off_small, color='k')
# ax2.plot(time, on_small, color='b')
# ax2.plot(time, diff_small, color='r')
# #ax1.set_title('Combined debt growth over time')
# #ax1.legend(loc='upper left')
# ax2.set_ylabel('fraction of cells (small system)', fontsize = 26)  
# ax2.set_xlabel('t (generations)', fontsize = 25)   
# ax2.tick_params(labelsize='18') 
# ax2.set_ylim([0,1])
# ax2.set_xlim([1,100])

# ax3.plot(time, off_large, color='k')
# ax3.plot(time, on_large, color='b')
# ax3.plot(time, diff_large, color='r')
# #ax1.set_title('Combined debt growth over time')
# #ax1.legend(loc='upper left')
# ax3.set_ylabel('fraction of cells (large system)', fontsize = 25)  
# ax3.set_xlabel('t (generations)', fontsize = 25)   
# ax3.tick_params(labelsize='18') 
# ax3.set_ylim([0,1])
# ax3.set_xlim([1,100])

















