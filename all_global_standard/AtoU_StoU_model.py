
import numpy as np
import pyximport
pyximport.install(reload_support=True, setup_args={"include_dirs":np.get_include()})
from AtoU_StoU import t_loop
import AtoU_StoU
import importlib
importlib.reload(AtoU_StoU)
import pandas as pd
import matplotlib.pyplot as plt

def simple(X_Y):
    
    
    N=X_Y[0]
    #mating type region (array of 140 nucleosomes) starting all with silent nucs (0)
    mt_region = np.zeros(N, dtype=np.int32)
    #indices of the mt_region corresponding to positions of nucleosomes
    positions = np.arange(len(mt_region), dtype=np.int32)
    

    duration = 101#201#15#101#15#101#15#101#15#101#10#61#15
    
    
    # rates
#    
#    print(glo_loc)
#    glo = glo_loc[0]
#    loc = glo_loc[1]
    
        
    
    
    X= X_Y[1]
    Y = X_Y[2]
    
   
    print(X_Y)
    
    direct = 1
    
    global_mode = X_Y[3]
    
    # local recruitment-rate M-catalysed change of U to M (recruited conversion)
    alpha1 = 50*len(mt_region)
    # local recruitment-rate A-catalysed change of M to U (recruited conversion)
    alpha2 = Y*len(mt_region)
    # local recruitment-rate A-catalysed change of U to A (recruited conversion)
    alpha3 = 50*len(mt_region)
    # global recruitment-rate (recruited conversion of A (0) to U (1))
    alpha4 = X*len(mt_region)
    # spontaneous conversion-rate (direct conversion of A to U)
    beta1 = direct*len(mt_region)
    # spontaneous conversion-rate (direct conversion)
    beta2 = direct*len(mt_region)
    # spontaneous conversion-rate (direct conversion)
    beta3 = direct*len(mt_region)
    # spontaneous conversion-rate (direct conversion)
    beta4 = direct*len(mt_region)
    # spontaneous conversion-rate in cenH region (only A to U)
    
    # global mode full
    if global_mode==0:
        beta5 = 450*len(mt_region)
    
    # global mode 1/x
    if global_mode==1:
        beta5 = 100*len(mt_region)#13.5*len(mt_region)#15*len(mt_region)#13.5 for SAU
    
    # global mode 1/(X^0.75)
    elif global_mode==2:
        beta5 = 250*len(mt_region)
    
    # global mode 1/(X^0.5)
    elif global_mode==3:
        beta5 = 300*len(mt_region)
        
    # global mode 1/(X^0.25)
    elif global_mode==4:
        beta5 = 150*len(mt_region)
        
        
        
    SAU = 0

    #rates = np.array([alpha1, alpha2, alpha3, alpha4, beta1, beta2, beta3, beta4, beta5])
    rates = np.array([beta1, beta2, beta3, beta4, beta5, alpha1, alpha2, alpha3, alpha4], dtype=np.double)

    #print(cenH_status_list)
    cenH_status_list, EcoRV_status_list, states, S_nucleosomes_cenH, S_nucleosomes, A_nucleosomes, U_nucleosomes= t_loop(duration, mt_region, positions, rates, SAU, global_mode)
    
    
    
    positions = list(positions)
    x = positions*(duration) # at the x-axis, the position values are repeated 30 times
    y = [] # and for the y-axis, each value is repeated 30 times
    for i in range(duration):
        for j in range(len(positions)):
            y.append(positions[i]) 
    
    
    x = np.array(x) # such that all PR_DUB and NURD values
    y = np.array(y) # are paired
    states = np.array(states)
    #print(len(x),len(y),len(states))
    df = pd.DataFrame(dict(x=x, y=y, state=states))
    
    # plot
    
    nuc_states = df.groupby('state')
    
    fig, ax = plt.subplots(figsize=(30,30)) # a new (quadratic) figure is generated
    #ax.margins(0.05) # Optional, just adds 5% padding to the autoscaling
    for name, state in nuc_states: # goes through all  3 groups
        ax.plot(state.x, state.y, marker = 'o', color = name, linestyle='', ms = 2.5, label=name)
        #ax.set_ylabel('Time (cell generations)', fontsize = 20)
        #ax.set_xlabel('Nucleosomes', fontsize = 20)
        ax.tick_params(labelsize='50')
        ax.set_title("23 kb system", fontsize ='60')
    
    #plt.savefig("timecourse_203_new.pdf")
        
    
    # fig, ax2 = plt.subplots(figsize=(12,12))

    # ax2.plot(S_amount[0], 'black')
    # ax2.plot(S_amount[1], 'grey')
    # ax2.plot(S_amount[2], 'red')
    # ax2.plot(S_amount[3], 'blue')
    # ax2.plot(S_amount[4], 'yellow')
    # ax2.set_xlim([-1,100 ])
    # #ax2.set_ylim([-1,20 ])
    # ax2.set_ylabel('number of S nucleosomes', fontsize=30)
    # ax2.set_xlabel('time (generations)', fontsize=30)
    # ax2.set_yticks([0,50, 100, 150, 200])
    # ax2.tick_params(labelsize = '20')

    return list(cenH_status_list), list(EcoRV_status_list)

# #values for full(special set to 300)
# if __name__ == '__main__':
#     import time
#     #import cProfile
#     t1 = time.time()
#     simple([203, 50, 70, 0])
#     print(time.time() - t1)



#values for 1/X (special set to 80)
if __name__ == '__main__':
    import time
    #import cProfile
    t1 = time.time()
    simple([203, 50, 40, 1])
    print(time.time() - t1)


# # #values for 1/(X^0.75) (special set to 200)
# if __name__ == '__main__':
#     import time
#     #import cProfile
#     t1 = time.time()
#     simple([203, 40, 50, 2])
#     print(time.time() - t1)


# # #values for 1/(X^0.5) (special set to 200)
# if __name__ == '__main__':
#     import time
#     #import cProfile
#     t1 = time.time()
#     simple([203, 40, 50, 3])
#     print(time.time() - t1)
    
 
