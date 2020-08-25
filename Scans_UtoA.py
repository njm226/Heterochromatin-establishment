#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 13:16:19 2019
Parameter scans
@author: fabio
"""

import numpy as np
#import pandas as pd
#import matplotlib.pyplot as plt
#from smaller_model_function_UtoA import simple_small as ss
from UtoA_model import simple
import multiprocessing
import time
import pickle
from scipy.optimize import curve_fit
#import uncertainties as unc

# mp
time_start = time.time()
#pool = multiprocessing.Pool(multiprocessing.cpu_count(), maxtasksperchild=None)
pool = multiprocessing.Pool(multiprocessing.cpu_count())




# Generate determin parameter x and y values
#X = [1,2,3,4,5,6,7,8,9,10] # list of all global rate S(A->U) values
#
#X = [10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29]
X = [10,20,30,40,50,60,70,80,90,100,110,120,130,140,150,160,170,180,190,200] # list of all global rate S(A->U) values
Y = [10,20,30,40,50,60,70,80,90,100,110,120,130,140,150,160,170,180,190,200] #and all local rate S(U->S) values
#Y = [50,60,70,80,90,100,110,120,130,140] #and all local rate S(U->S) values

#X = [22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,60] # list of all global rate S(A->U) values
#Y = [162,164,166,168,170,172,174,176,178,180,182,184,186,188,190,192,194,196,198,200] #and all local rate S(U->S) values


y = Y*len(X) # at the x-axis, the S value range is repeated 10 times
x = [] # and for the y-axis, each value is repeated 28 times
for i in range(len(X)):
    for j in range(len(Y)):
        x.append(X[i]) 

x = np.array(x) 
y = np.array(y) 

# #generate list with all value pairs of all system sizes
# data_pairs_small = []
# for i in X:
#     for j in Y:
#         data_pairs_small.append([i,j])


data_pairs = []
for i in X:
    for j in Y:
        data_pairs.append([153,i,j])
        
data_pairs_sm = []
for i in X:
    for j in Y:
        data_pairs_sm.append([182,i,j])
        
data_pairs_sl = []
for i in X:
    for j in Y:
        data_pairs_sl.append([191,i,j])
        
data_pairs_l = []
for i in X:
    for j in Y:
        data_pairs_l.append([203,i,j])
        
        
#state_list = pool.map(ss, data_pairs_small)

     

 
#    # save state_list
# with open('state_g_noise.txt', 'wb') as F:
#      pickle.dump(state_list, F)

    
    

        
with open ('state_g_1_x.txt', 'rb') as F:
    state_list = pickle.load(F)
     
        
        



Timing = []
all_criteria = []
Differences = []

b_value_list = []

cenH_silenced = 0
EcoRV_silenced = 0

cenH_silenced_sm = 0
EcoRV_silenced_sm = 0

cenH_silenced_sl = 0
EcoRV_silenced_sl = 0

duration=201#15

# this for loop goes through all data_pairs (list of 400) and repeats simulation reps times
for i in range(len(data_pairs)):
    
    
    #determine how often the simulation for each system and specific parameter pair should be repeated
    reps=1000

    repeat = [data_pairs[i]]*reps
    repeat_sm = [data_pairs_sm[i]]*reps
    repeat_sl = [data_pairs_sl[i]]*reps
    repeat_max = [data_pairs_l[i]]*reps
    
    
    # store the simulation results (status list of cenH and EcoRV) of each simulation
    if __name__ == '__main__':
        # 
        status_small = pool.map(simple, repeat) 
        status_m = pool.map(simple, repeat_sm) 
        status_large = pool.map(simple, repeat_sl) 
        status_max = pool.map(simple, repeat_max)

    
    # two dimensional arrays with dimensions len(repeat) and duration (pre allocation)
    cenH_list_small = np.zeros([len(repeat),duration])
    EcoRV_list_small = np.zeros([len(repeat),duration])
    
    
    cenH_list_m = np.zeros([len(repeat),duration])
    EcoRV_list_m = np.zeros([len(repeat),duration])
    
    
    cenH_list_large = np.zeros([len(repeat),duration])
    EcoRV_list_large = np.zeros([len(repeat),duration])
    
    
    cenH_list_max = np.zeros([len(repeat),duration])
    EcoRV_list_max = np.zeros([len(repeat),duration])
    
    

    
    # fill the columns with information on the status of different cells in parallel
    # at a certain (fixed) timepoint 
    for elt in range(len(repeat)):
        
        cenH_small = np.array(status_small[elt][0])
        EcoRV_small = np.array(status_small[elt][1])
        
        #switch the values of the list (1 stands now for timepoint when reporter is on)
        cenH_small=1-cenH_small
        EcoRV_small=1-EcoRV_small
        
        # stores the cenH part in a seperate two dimensional array (reps X duration)
        cenH_list_small[elt]=cenH_small
        EcoRV_list_small[elt]=EcoRV_small
        
        
        
        
            
        
        cenH_m = np.array(status_m[elt][0])
        EcoRV_m = np.array(status_m[elt][1])
        
        #switch the values of the list (1 stands now for timepoint when reporter is on)
        cenH_m=1-cenH_m
        EcoRV_m=1-EcoRV_m
        
        # stores the cenH part in a seperate two dimensional array (reps X duration)
        cenH_list_m[elt]=cenH_m
        EcoRV_list_m[elt]=EcoRV_m
        
        
        
        
        
        
        cenH_large = np.array(status_large[elt][0])
        EcoRV_large = np.array(status_large[elt][1])
        
        #switch the values of the list (1 stands now for timepoint when reporter is on)
        cenH_large=1-cenH_large
        EcoRV_large=1-EcoRV_large
        
        # stores the cenH part in a seperate two dimensional array (reps X duration)
        cenH_list_large[elt]=cenH_large
        EcoRV_list_large[elt]=EcoRV_large
        
        
        
        
        
        
        
        cenH_max = np.array(status_max[elt][0])
        EcoRV_max = np.array(status_max[elt][1])
        
        #switch the values of the list (1 stands now for timepoint when reporter is on)
        cenH_max=1-cenH_max
        EcoRV_max=1-EcoRV_max
        
        # stores the cenH part in a seperate two dimensional array (reps X duration)
        cenH_list_max[elt]=cenH_max
        EcoRV_list_max[elt]=EcoRV_max
        
        
        # print(cenH_small)
        # print(cenH_m)
        # print(cenH_large)
        # print(cenH_max)
    
    
    
    
    #output (Histograms!)
    cenH_total_small = (sum(cenH_list_small))/reps
    #
    ys = (sum(EcoRV_list_small))/reps
    
    
    
    
    cenH_total_m = (sum(cenH_list_m))/reps
    #
    ym = (sum(EcoRV_list_m))/reps
    
    
    
    
    cenH_total_large = (sum(cenH_list_large))/reps
    #
    yl = (sum(EcoRV_list_large))/reps
    
    
    
    
    cenH_total_max = (sum(cenH_list_max))/reps
    
    ymax = (sum(EcoRV_list_max))/reps
    
    

    ys = ys[3:]
    ym = ym[3:]
    yl = yl[3:]
    ymax = ymax[3:]
    x = np.array(range(duration-3))  
        
    # fitting function
    def model(x,a,b):
        return a*np.exp(-x/b)
    
    #Perform the curve fit
    popt_s, pcov_s = curve_fit(model, x, ys, p0=[1,1], maxfev=5000)
    #print(popt_s)
    
    b_s = popt_s[1]
    
    #a_s, b_s = unc.correlated_values(popt_s, pcov_s)
    
    
    
     #Perform the curve fit
    popt_m, pcov_m = curve_fit(model, x, ym, p0=[1,1], maxfev=5000)
    #print(popt_s)
    
    b_m = popt_m[1]
    
    #a_m, b_m = unc.correlated_values(popt_m, pcov_m)
    
    
    
     #Perform the curve fit
    popt_l, pcov_l = curve_fit(model, x, yl, p0=[1,1], maxfev=5000)
    #print(popt_s)
    
    b_l = popt_l[1]
    
    #a_l, b_l = unc.correlated_values(popt_l, pcov_l)
    
    
    
     #Perform the curve fit
    popt_max, pcov_max = curve_fit(model, x, ymax, p0=[1,1], maxfev=5000)
    #print(popt_s)
    
    b_max = popt_max[1]
    
    #a_max, b_max = unc.correlated_values(popt_max, pcov_max)
    
    
    b = [b_s, b_m, b_l, b_max]
    print(b)
    
    b_value_list.append(b)
    
        
    # # if cenH has been silenced within chosen intervall
    # #if cenH_Average >= 2 and cenH_Average <= 5
    # if cenH_Average >= 2.0 and cenH_Average <= 3.5:
    #     # this timing criterion has been met
    #     cenH_timing = 1
    # else:
    #     cenH_timing = 0
    
    
     
    if  b_s >= 3.5 and b_s <= 5.9:
   
        EcoRV_timing = 1
    else:
        EcoRV_timing = 0
    

    if b_m > 14.5 and b_m <= 22.5:
  
        EcoRV_timing_sm = 1
    else:
        EcoRV_timing_sm = 0
        
        
    if b_l > 35 and b_l <= 60:
    #if EcoRV_Average_sl >= 15 and EcoRV_Average_sl <= 19:
        # this timing criterion has been met
        EcoRV_timing_sl = 1
    else:
        EcoRV_timing_sl = 0
        
        
    if b_max > 90 and b_max <= 150:
    #if EcoRV_Average_sl >= 15 and EcoRV_Average_sl <= 19:
        # this timing criterion has been met
        EcoRV_timing_max = 1
    else:
        EcoRV_timing_max = 0
        
     # change color of state_list from blue to lighter blue
    if state_list[i] == 'white':
        state_list[i] = 7#'royalblue'
        
     # change color of state_list from blue to lighter blue
    if state_list[i] == 'cyan':
        state_list[i] = 0#'royalblue'
        
    # change color of state_list from blue to lighter blue
    if state_list[i] == 'blue':
        state_list[i] = 1#'royalblue'
        
    
    
    
    if b_l > 2*b_s and state_list[i]==1:
        Diff = 2#'darkblue'
    else:
        Diff = state_list[i]

    Differences.append(Diff)
    
    
    
    
    if EcoRV_timing_max == 1 and EcoRV_timing_sl == 1 and EcoRV_timing_sm == 1 and EcoRV_timing == 1:
        timing = 6
    elif EcoRV_timing_sl == 1 and EcoRV_timing_sm == 1 and EcoRV_timing == 1:
         timing = 5
    elif EcoRV_timing_sm == 1 and EcoRV_timing == 1:
         timing = 4
    elif EcoRV_timing == 1:
         timing = 3
    else:
        timing = Diff
    

    Timing.append(timing)
       
    
    
    if timing == 6 and state_list[i]==1:
        # if cenH_timing == 1:
        #    criteria = 'black'
        #else:
           criteria = 6#'gold'
    elif timing == 5 and state_list[i]==1:
        # if cenH_timing == 1:
        #    criteria = 'black'
        #else:
           criteria = 5#'red'
    elif timing == 4 and state_list[i]==1:
        # if cenH_timing == 1:
        #    criteria = 'black'
        #else:
           criteria = 4#'red'
    elif timing == 3 and state_list[i]==1:
        # if cenH_timing == 1:
        #    criteria = 'black'
        #else:
           criteria = 3#'springgreen'
    elif timing == 3 and state_list[i]==0:
        # if cenH_timing == 1:
        #    criteria = 'black'
        # else:
           criteria = 3#'springgreen'
    else:
        criteria = timing
        
    all_criteria.append(criteria)
        
# save Timing list
with open('Timing_1x.txt', 'wb') as F:
    pickle.dump(Timing, F)
    
    
# save Timing list
with open('all_criteria_1x.txt', 'wb') as F:
    pickle.dump(all_criteria, F)
    
# save Timing list
with open('Differences_1x.txt', 'wb') as F:
    pickle.dump(Differences, F)
    
# save Timing list
with open('b_list_1x.txt', 'wb') as F:
    pickle.dump(b_value_list, F)
    


# print(Differences)
# print(len(Differences))
# print(len(x))
# print(len(y))

# df = pd.DataFrame(dict(x=x, y=y, state=np.array(Differences))) # colors can be white, royalbue, cyan or darkblue
# Df = pd.DataFrame(dict(x=x, y=y, label=np.array(Timing))) # dataframe of the x and y values and labels (inner dot colors)
# #Df = pd.DataFrame(dict(x=x, y=y, label=np.array(Differences)))
# Dataframe = pd.DataFrame(dict(x=x, y=y, Label=np.array(all_criteria)))

# #prints simulation time
# print("Took {}".format(time.time() - time_start))


# # plot
    
# nuc_states = df.groupby('state')
# Timing = Df.groupby('label')
# Both = Dataframe.groupby('Label')

# fig, ax = plt.subplots(figsize=(9,9)) # a new (quadratic) figure is generated
# #fig, ax = plt.subplots(figsize=(5,5)) # a new (quadratic) figure is generated

# #ax.margins(0.05) # Optional, just adds 5% padding to the autoscaling
# for name, state in nuc_states: # goes through all  3 groups
#     if name == 0:
#         name = 'cyan'
#     elif name == 1:
#         name = 'royalblue'
#     elif name == 2:
#         name = 'darkblue'
#     else:
#         name='white'
#     ax.plot(state.x, state.y, marker = 's', color = name, linestyle='', ms = 20, label=name)
    
# for Name, label in Timing: # goes through all  3 groups
#     if Name == 0:
#         Name = 'cyan'
#     elif Name == 1:
#         Name = 'royalblue'
#     elif Name == 2:
#         Name = 'darkblue'
#     elif Name == 3:
#         Name = 'yellowgreen'
#     elif Name == 4:
#         Name = 'red'
#     elif Name == 5:
#         Name = 'silver'
#     elif Name == 6:
#         Name = 'gold'
#     ax.plot(label.x, label.y, marker = 'o', color = Name, linestyle='', ms = 18, label=Name)
    
# for NAME, Label in Both: # goes through all  3 groups
#     if NAME == 0:
#         NAME = 'cyan'
#     elif NAME == 1:
#         NAME = 'royalblue'
#     elif NAME == 2:
#          NAME = 'darkblue'
#     elif NAME == 3:
#         NAME = 'yellowgreen'
#     elif NAME == 4:
#         NAME = 'red'
#     elif NAME == 5:
#         NAME = 'silver'
#     elif NAME == 6:
#         NAME = 'gold'
#     ax.plot(Label.x, Label.y, marker = 'o', color = NAME, linestyle='', ms = 10, label=NAME)
#     ax.set_ylabel('A(S-->U) local rate', fontsize = 30)
#     ax.set_xlabel('A(U-->A) global rate', fontsize = 30)
#     ax.tick_params(labelsize='18')
    
#     #ax.set_xlabel('direct conversion', fontsize = 30)
#     #ax.set_xlabel('Special: A --> U', fontsize = 30)
    

   
#plt.savefig("fig_SUS30.pdf")
    

    
    
    
