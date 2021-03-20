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


# save Timing list
with open('Timing_S300.txt', 'rb') as F:
    Timing = pickle.load(F)
    
    
# save Timing list
with open('all_criteria_S300.txt', 'rb') as F:
    all_criteria = pickle.load(F)
    
# save Timing list
with open('Differences_S300.txt', 'rb') as F:
    Differences = pickle.load(F)

# save Timing list
with open('b_list_S300.txt', 'rb') as F:
   b = pickle.load(F)

X = [10,20,30,40,50,60,70,80,90,100,110,120,130,140,150,160,170,180,190,200] # list of all global rate S(A->U) values
Y = [10,20,30,40,50,60,70,80,90,100,110,120,130,140,150,160,170,180,190,200] #and all local rate S(U->S) values
#X = [1,2,3,4,5,6,7,8,9,10]
#Y = [60,70,80,90,100,110,120,130,140,150] #and all local rate S(U->S) values

#X = [22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,60] # list of all global rate S(A->U) values
#Y = [162,164,166,168,170,172,174,176,178,180,182,184,186,188,190,192,194,196,198,200] #and all local rate 
   
   
y = Y*len(X) # at the x-axis, the S value range is repeated 10 times
x = [] # and for the y-axis, each value is repeated 28 times
for i in range(len(X)):
    for j in range(len(Y)):
        x.append(X[i]) 

print(b)
print(Differences)
print(all_criteria)
print(len(Differences))
print(len(x))
print(len(y))


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
    

   
plt.savefig("fig_S300.pdf")