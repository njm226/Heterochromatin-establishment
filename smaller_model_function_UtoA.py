import numpy as np
#import random
import pyximport
pyximport.install(reload_support=True, setup_args={"include_dirs":np.get_include()})
#import smaller
import smaller_UtoA
import importlib
importlib.reload(smaller)
from smaller import t_loop
import pandas as pd
import matplotlib.pyplot as plt

def simple_small(X_Y):
    #mating type region (array of 140 nucleosomes)
    mt_region = np.ones(76, dtype=np.int32)*0
    #indices of the mt_region corresponding to positions of nucleosomes
    positions = np.arange(len(mt_region), dtype=np.int32)

    # duration of a simulation
    duration = 1204#31
    
    #cenh region is lacking

    print(X_Y)
    X = X_Y[0]
    Y = X_Y[1]
    
    
    direct = 1
    
    
    # local recruitment-rate M-catalysed change of U to M (recruited conversion)
    alpha1 = 100*len(mt_region)
    # local recruitment-rate A-catalysed change of M to U (recruited conversion)
    alpha2 = Y*len(mt_region)
    # local recruitment-rate A-catalysed change of U to A (recruited conversion)
    alpha3 = X*len(mt_region)
    # global recruitment-rate (recruited conversion of A (0) to U (1))
    alpha4 = 100*len(mt_region)
    # spontaneous conversion-rate (direct conversion of A to U)
    beta1 = direct*len(mt_region)
    # spontaneous conversion-rate (direct conversion)
    beta2 = direct*len(mt_region)
    # spontaneous conversion-rate (direct conversion)
    beta3 = direct*len(mt_region)
    # spontaneous conversion-rate (direct conversion)
    beta4 = direct*len(mt_region)
    # spontaneous conversion-rate in cenH region (only A to U)
    # spontaneous conversion-rate in cenH region (only A to U)
    
    
    
    #rates = np.array([alpha1, alpha2, alpha3, alpha4, beta1, beta2, beta3, beta4], dtype=np.double)
    rates = np.array([beta1, beta2, beta3, beta4, alpha1, alpha2, alpha3, alpha4], dtype=np.double)
    
    #start the loop
    Max_blue, Max_red, states = t_loop(duration, mt_region, positions, rates)
    #print(states)

    print(Max_blue, Max_red) 


    if Max_blue >= (duration-204)/2 and Max_red >= (duration-204)/2:
        State = 'blue'
        
    elif Max_blue >= (duration-204)/10 and Max_red >= (duration-204)/10:
        State = 'cyan'
        
    else:
        State = 'white'
        
    
    # positions=list(positions)
    # x = positions*(duration-1) # at the x-axis, the position values are repeated 30 times
    # y = [] # and for the y-axis, each value is repeated 30 times
    # for i in range(duration-1):
    #     for j in range(len(positions)):
    #         y.append(positions[i]) 
    
    # x = np.array(x) # such that all PR_DUB and NURD values
    # y = np.array(y) # are paired
    
    # states = np.array(states)
    # print(len(x),len(y),len(states))

    # df = pd.DataFrame(dict(x=x, y=y, state=states))
    
    # # plot
    
    # nuc_states = df.groupby('state')
    
    # fig, ax = plt.subplots(figsize=(12,7)) # a new (quadratic) figure is generated
    # #ax.margins(0.05) # Optional, just adds 5% padding to the autoscaling
    # for name, state in nuc_states: # goes through all  3 groups
    #     ax.plot(state.x, state.y, marker = 'o', color = name, linestyle='', ms = 3.5, label=name)
    #     #ax.set_ylabel('Time (cell generations)', fontsize = 20)
    #     #ax.set_xlabel('Nucleosomes', fontsize = 20)
    #     ax.tick_params(labelsize='40')
    #     ax.set_xlim([-5,145])
        
    return(State)


# import time
# t1 = time.time()
# simple_small([100, 100])
# print(time.time() - t1)
