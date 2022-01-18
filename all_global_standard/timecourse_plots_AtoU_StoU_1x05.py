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
#from smaller_model_function_UtoS import simple_small as ss
from AtoU_StoU_model import simple as ss
import multiprocessing
#import time
import pickle
pool = multiprocessing.Pool(multiprocessing.cpu_count())


mode = 3

if mode == 0:
    X_Y=[[153,80,70, 0]]
    X_Y_sm=[[182, 80,70, 0]]
    X_Y_sl=[[191,80,70, 0]]
    X_Y_max=[[203,80,70, 0]]
    
elif mode == 1:
    X_Y=[[153,190,170, 1]]
    X_Y_sm=[[182, 190,170, 1]]
    X_Y_sl=[[191,190,170, 1]]
    X_Y_max=[[203,190,170, 1]]
    
elif mode == 2:
    X_Y=[[153, 90, 60, 2]]
    X_Y_sm=[[182, 90, 60, 2]]
    X_Y_sl=[[191, 90, 60, 2]]
    X_Y_max=[[203, 90, 60, 2]]
    
elif mode == 3:
    X_Y=[[153, 70, 50, 3]]
    X_Y_sm=[[182, 70, 50, 3]]
    X_Y_sl=[[191, 70, 50, 3]]
    X_Y_max=[[203, 70, 50, 3]]
    


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
    
    
    
    
    # print(cenH_small)
    # print(cenH_m)
    # print(cenH_large)
    # print(cenH_max)


    
   



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







if mode == 0:
     
        # save state_list
    with open('cenH_small_full_gAtoU80_StoU70.txt', 'wb') as F:
        pickle.dump(cenH_total_small, F)
        
    # save state_list
    with open('cenH_m_full_gAtoU80_StoU70.txt', 'wb') as F:
        pickle.dump(cenH_total_m, F)
        
    # save state_list
    with open('cenH_large_full_gAtoU80_StoU70.txt', 'wb') as F:
      pickle.dump(cenH_total_large, F)
        
    # save state_list
    with open('cenH_max_full_gAtoU80_StoU70.txt', 'wb') as F:
        pickle.dump(cenH_total_max, F)
        
        
        
    
        
    # save state_list
    with open('EcoRV_small_full_gAtoU80_StoU70.txt', 'wb') as F:
        pickle.dump(EcoRV_total_small, F)
        
    # save state_list
    with open('EcoRV_m_full_gAtoU80_StoU70.txt', 'wb') as F:
        pickle.dump(EcoRV_total_m, F)
        
    # save state_list
    with open('EcoRV_large_full_gAtoU80_StoU70.txt', 'wb') as F:
        pickle.dump(EcoRV_total_large, F)
        
    # save state_list
    with open('EcoRV_max_full_gAtoU80_StoU70.txt', 'wb') as F:
        pickle.dump(EcoRV_total_max, F)



elif mode == 1:
    # save state_list
    with open('cenH_small_1x_gAtoU200_StoU170.txt', 'wb') as F:
        pickle.dump(cenH_total_small, F)
        
    # save state_list
    with open('cenH_m_1x_gAtoU200_StoU170.txt', 'wb') as F:
        pickle.dump(cenH_total_m, F)
        
    # save state_list
    with open('cenH_large_1x_gAtoU200_StoU170.txt', 'wb') as F:
      pickle.dump(cenH_total_large, F)
        
    # save state_list
    with open('cenH_max_1x_gAtoU200_StoU170.txt', 'wb') as F:
        pickle.dump(cenH_total_max, F)
        
        
        
    
        
    # save state_list
    with open('EcoRV_small_1x_gAtoU200_StoU170.txt', 'wb') as F:
        pickle.dump(EcoRV_total_small, F)
        
    # save state_list
    with open('EcoRV_m_1x_gAtoU200_StoU170.txt', 'wb') as F:
        pickle.dump(EcoRV_total_m, F)
        
    # save state_list
    with open('EcoRV_large_1x_gAtoU200_StoU170.txt', 'wb') as F:
        pickle.dump(EcoRV_total_large, F)
        
    # save state_list
    with open('EcoRV_max_1x_gAtoU200_StoU170.txt', 'wb') as F:
        pickle.dump(EcoRV_total_max, F)
        

elif mode == 2:
    # save state_list
    with open('cenH_small_1x075_gAtoU90_StoU60.txt', 'wb') as F:
        pickle.dump(cenH_total_small, F)
        
    # save state_list
    with open('cenH_m_1x075_gAtoU90_StoU60.txt', 'wb') as F:
        pickle.dump(cenH_total_m, F)
        
    # save state_list
    with open('cenH_large_1x075_gAtoU90_StoU60.txt', 'wb') as F:
      pickle.dump(cenH_total_large, F)
        
    # save state_list
    with open('cenH_max_1x075_gAtoU90_StoU60.txt', 'wb') as F:
        pickle.dump(cenH_total_max, F)
        
        
        
    
        
    # save state_list
    with open('EcoRV_small_1x075_gAtoU90_StoU60.txt', 'wb') as F:
        pickle.dump(EcoRV_total_small, F)
        
    # save state_list
    with open('EcoRV_m_1x075_gAtoU90_StoU60.txt', 'wb') as F:
        pickle.dump(EcoRV_total_m, F)
        
    # save state_list
    with open('EcoRV_large_1x075_gAtoU90_StoU60.txt', 'wb') as F:
        pickle.dump(EcoRV_total_large, F)
        
    # save state_list
    with open('EcoRV_max_1x075_gAtoU90_StoU60.txt', 'wb') as F:
        pickle.dump(EcoRV_total_max, F)
        
        
        
        
elif mode == 3:
     
      # save state_list
    with open('cenH_small_1x05_gAtoU70_StoU50.txt', 'wb') as F:
        pickle.dump(cenH_total_small, F)
        
    # save state_list
    with open('cenH_m_1x05_gAtoU70_StoU50.txt', 'wb') as F:
        pickle.dump(cenH_total_m, F)
        
    # save state_list
    with open('cenH_large_1x05_gAtoU70_StoU50.txt', 'wb') as F:
      pickle.dump(cenH_total_large, F)
        
    # save state_list
    with open('cenH_max_1x05_gAtoU70_StoU50.txt', 'wb') as F:
        pickle.dump(cenH_total_max, F)
        
        
        
    
        
    # save state_list
    with open('EcoRV_small_1x05_gAtoU70_StoU50.txt', 'wb') as F:
        pickle.dump(EcoRV_total_small, F)
        
    # save state_list
    with open('EcoRV_m_1x05_gAtoU70_StoU50.txt', 'wb') as F:
        pickle.dump(EcoRV_total_m, F)
        
    # save state_list
    with open('EcoRV_large_1x05_gAtoU70_StoU50.txt', 'wb') as F:
        pickle.dump(EcoRV_total_large, F)
        
    # save state_list
    with open('EcoRV_max_1x05_gAtoU70_StoU50.txt', 'wb') as F:
        pickle.dump(EcoRV_total_max, F)
        
        
        


time = np.array(range(duration))

#y_axis = np.array([cenH_total_small, EcoRV_total_small,  cenH_total_m, EcoRV_total_m, cenH_total_large, EcoRV_total_large,cenH_total_max, EcoRV_total_max])
        
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

plt.fill_between(time,cenH_total_small, color='lightblue')
ax1.set_yscale('log')    
ax1.tick_params(labelsize='30')
ax1.set_ylim([0.001,1])
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

if mode == 1:
    plt.savefig("timecourse_1x_gAtoU190_StoU170.pdf")
    
elif mode == 2:
    plt.savefig("timecourse_075x_gAtoU90_StoU60.pdf")
    
elif mode == 3:
    plt.savefig("timecourse_05x_gAtoU70_StoU50.pdf")
    
elif mode == 0:
    plt.savefig("timecourse_full_gUtoM80_AtoU70.pdf")
    
















