#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 16:28:20 2020

@author: fabio

"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pickle



with open('b_list_1x05_S45.txt', 'rb') as F:
   b = pickle.load(F)
   
with open('state_g_1x05_standard_UtoS.txt', 'rb') as F:
   state_list = pickle.load(F)

Timing = []
all_criteria = []
Differences = []
   


X = [10,20,30,40,50,60,70,80,90,100,110,120,130,140,150,160,170,180,190,200] # list of all global rate S(A->U) values
Y = [10,20,30,40,50,60,70,80,90,100,110,120,130,140,150,160,170,180,190,200] #and all local rate S(U->S) values
#X = [1,2,3,4,5,6,7,8,9,10]
#Y = [60,70,80,90,100,110,120,130,140,150] #and all local rate S(U->S) values

#X = [22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,60] # list of all global rate S(A->U) values
#Y = [162,164,166,168,170,172,174,176,178,180,182,184,186,188,190,192,194,196,198,200] #and all local rate 
   
   
x = X*len(Y) # at the x-axis, the S value range is repeated 10 times
y = [] # and for the y-axis, each value is repeated 28 times
for i in range(len(Y)):
    for j in range(len(X)):
        y.append(Y[i]) 


for i in range(len(b)):
    b_s=b[i][0]
    b_m=b[i][1]
    b_l=b[i][2]
    b_max=b[i][3]
    
    if  b_s >= 2.35 and b_s <= 7.0: #mean: 4.7 (50% difference: 2.35 and 7.0) (25% difference: 3.5 and 5.9) (35% difference: 3.0 and 6.3)
       
        EcoRV_timing = 1
    else:
        EcoRV_timing = 0
    
    
    if b_m > 8.5 and b_m <= 25.6: #mean: 17.1 (50% difference: 8.5 and 25.6) (25% difference: 12.825 and 21.375)(35% difference: 11.1 and 23.1)
      
        EcoRV_timing_sm = 1
    else:
        EcoRV_timing_sm = 0
        
        
    if b_l > 24.5 and b_l <= 73.6: #mean: 49.123 (50% difference: 24.5 and 73.6845) (25% difference: 36.84 and 61.4)(35% difference: 31.9 and 66.3)
    #if EcoRV_Average_sl >= 15 and EcoRV_Average_sl <= 19:
        # this timing criterion has been met
        EcoRV_timing_sl = 1
    else:
        EcoRV_timing_sl = 0
        
        
    if b_max > 59.5 and b_max <= 178.5:#mean: 119 (50% difference: 59.5 and 178.5) (25% difference: 36.84 and 61.4)(35% difference: 77 and 160.7)
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
        
    
    
    
    if b_l > 2*b_s and state_list[i] == 1:
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


df = pd.DataFrame(dict(x=x, y=y, state=np.array(Differences))) # colors can be white, royalbue, cyan or darkblue
Df = pd.DataFrame(dict(x=x, y=y, label=np.array(Timing))) # dataframe of the x and y values and labels (inner dot colors)
#Df = pd.DataFrame(dict(x=x, y=y, label=np.array(Differences)))
Dataframe = pd.DataFrame(dict(x=x, y=y, Label=np.array(all_criteria)))

#prints simulation time
#print("Took {}".format(time.time() - time_start))


# plot
    
nuc_states = df.groupby('state')
Timing = Df.groupby('label')
Both = Dataframe.groupby('Label')

fig, ax = plt.subplots(figsize=(7,7)) # a new (quadratic) figure is generated
#fig, ax = plt.subplots(figsize=(5,5)) # a new (quadratic) figure is generated

#ax.margins(0.05) # Optional, just adds 5% padding to the autoscaling
for name, state in nuc_states: # goes through all  3 groups
    if name == 0:
        name = 'cyan'
    elif name == 1:
        name = 'royalblue'
    elif name == 2:
        name = 'darkblue'
    else:
        name='white'
    ax.plot(state.x, state.y, marker = 's', color = name, linestyle='', ms = 15, label=name)
    
for Name, label in Timing: # goes through all  3 groups
    if Name == 0:
        Name = 'cyan'
    elif Name == 1:
        Name = 'royalblue'
    elif Name == 2:
        Name = 'darkblue'
    elif Name == 3:
        Name = 'yellowgreen'
    elif Name == 4:
        Name = 'red'
    elif Name == 5:
        Name = 'silver'
    elif Name == 6:
        Name = 'gold'
    elif Name == 7:
        Name = 'white'
    ax.plot(label.x, label.y, marker = 'o', color = Name, linestyle='', ms = 13, label=Name)
    
for NAME, Label in Both: # goes through all  3 groups
    if NAME == 0:
        NAME = 'cyan'
    elif NAME == 1:
        NAME = 'royalblue'
    elif NAME == 2:
          NAME = 'darkblue'
    elif NAME == 3:
        NAME = 'yellowgreen'
    elif NAME == 4:
        NAME = 'red'
    elif NAME == 5:
        NAME = 'silver'
    elif NAME == 6:
        NAME = 'black'
    elif NAME == 7:
        NAME = 'white'
    ax.plot(Label.x, Label.y, marker = 'o', color = NAME, linestyle='', ms = 7, label=NAME)
    #ax.set_ylabel('S(A-->U) local rate', fontsize = 30)
    #ax.set_xlabel('S(U-->S) global rate', fontsize = 30)
    ax.tick_params(labelsize='30', width=4, length=4)
    #ax.tick_params(labelsize='18')
    
    #ax.set_xlabel('direct conversion', fontsize = 30)
    #ax.set_xlabel('Special: A --> U', fontsize = 30)
    

   
plt.savefig("fig_1x05_standard_S45_UtoS_50%.pdf")