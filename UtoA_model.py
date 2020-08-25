
import numpy as np
import pyximport
pyximport.install(reload_support=True, setup_args={"include_dirs":np.get_include()})
from UtoA import t_loop
import UtoA
import importlib
importlib.reload(UtoA)
#import pandas as pd
#import matplotlib.pyplot as plt

def simple(X_Y):
    
    
    N=X_Y[0]
    #mating type region (array of 140 nucleosomes) starting all with silent nucs (0)
    mt_region = np.zeros(N, dtype=np.int32)
    #indices of the mt_region corresponding to positions of nucleosomes
    positions = np.arange(len(mt_region), dtype=np.int32)
    

    duration = 201#201#15#101#15#101#15#101#15#101#10#61#15
    
    
    # rates
#    
#    print(glo_loc)
#    glo = glo_loc[0]
#    loc = glo_loc[1]
    
        
    
    
    X = X_Y[1]
    Y = X_Y[2]
    
   
    print(X_Y)
    
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
    beta5 = 30*len(mt_region)#13.5*len(mt_region)#15*len(mt_region)#
    
    SAU = 0

    #rates = np.array([alpha1, alpha2, alpha3, alpha4, beta1, beta2, beta3, beta4, beta5])
    rates = np.array([beta1, beta2, beta3, beta4, beta5, alpha1, alpha2, alpha3, alpha4], dtype=np.double)

    #print(cenH_status_list)
    cenH_status_list, EcoRV_status_list, states = t_loop(duration, mt_region, positions, rates, SAU)
    
    
    
    # positions = list(positions)
    # x = positions*(duration) # at the x-axis, the position values are repeated 30 times
    # y = [] # and for the y-axis, each value is repeated 30 times
    # for i in range(duration):
    #     for j in range(len(positions)):
    #         y.append(positions[i]) 
    
    
    # x = np.array(x) # such that all PR_DUB and NURD values
    # y = np.array(y) # are paired
    # states = np.array(states)
    # #print(len(x),len(y),len(states))
    # df = pd.DataFrame(dict(x=x, y=y, state=states))
    
    # # plot
    
    # nuc_states = df.groupby('state')
    
    # fig, ax = plt.subplots(figsize=(12,15)) # a new (quadratic) figure is generated
    # #ax.margins(0.05) # Optional, just adds 5% padding to the autoscaling
    # for name, state in nuc_states: # goes through all  3 groups
    #     ax.plot(state.x, state.y, marker = 'o', color = name, linestyle='', ms = 3.5, label=name)
    #     #ax.set_ylabel('Time (cell generations)', fontsize = 20)
    #     #ax.set_xlabel('Nucleosomes', fontsize = 20)
    #     ax.tick_params(labelsize='50')
    #     ax.set_title("23.5 kb system", fontsize ='60')
    
        
    
#    fig, ax1 = plt.subplots(figsize=(12,5))
#    
#    ax1.plot(mod_prob)
#    ax1.set_xlim([-1,140 ])

    return list(cenH_status_list), list(EcoRV_status_list)
 
# if __name__ == '__main__':
#     import time
#     #import cProfile
#     t1 = time.time()
#     simple([203, 40, 170])
#     print(time.time() - t1)

