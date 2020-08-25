
import numpy as np
cimport numpy as np
import random
import cython
from libc.math cimport log

@cython.boundscheck(False)
@cython.wraparound(False)
@cython.cdivision(True)
def t_loop(int duration, int[:] mt_region, int[:] positions, double[:] rates, int SAU):
    
    # total time (in units of generations)
    cdef double T = 0
    # time (set to 0 again after cell devides)
    cdef double t = 0
    # duration of a simulation
    cdef double p1 
    cdef double p2
    
    #sum of all rates
    cdef double total_rate = np.sum(rates)
    # array of the cumulative sums of all rates
    cdef double[:] cumsum_rates = np.cumsum(rates)
    #number of rates
    cdef int n_rates = len(rates)
    
    # borders of the cenH region
    cdef int cenHl = 60#50
    cdef int cenHr = 91#81
    
    if len(mt_region)==153:
       
        # borders of the reporter (EcoRV) located outside cenH
        EcoRVl = 118
        EcoRVr = 132
        
    elif len(mt_region)==182:
        # borders of the reporter (EcoRV) located outside cenH
        EcoRVl = 147
        EcoRVr = 161
        
    elif len(mt_region)==191:
        # borders of the reporter (EcoRV) located outside cenH
        EcoRVl = 156
        EcoRVr = 170
        
    elif len(mt_region)==203:
        # borders of the reporter (EcoRV) located outside cenH
        EcoRVl = 168
        EcoRVr = 182
        
    
    
    # silencing_threshold
    cdef int threshold1 = 14#16
    cdef int threshold2 = 9

    cdef int low_t_index
    cdef int pos_conv
    cdef int pos_rec
    cdef int i
    cdef int nuc_conv
    cdef int nn = len(mt_region)
    cdef int long_nn = 203
    cdef int nuc_rec
    cdef double ran
    cdef int x

    
    cdef int n = 100000 # large number!
    
    # generates n random integers from 0 to size of positions
    cdef int[:] random_integers = np.random.randint(len(positions), size=n, dtype=np.int32)
    cdef int[:] random_integers2 = np.random.randint(len(positions), size=n, dtype=np.int32)
    # generates 4 * n different random numbers uniformly distributed between 0 and 1
    cdef double[:] random_doubles1 = np.random.random(n)
    cdef double[:] random_doubles2 = np.random.random(n)
    cdef double[:] random_doubles3 = np.random.random(n)
    cdef double[:] random_doubles4 = np.random.random(n)
    cdef double[:] random_doubles5 = np.random.random(n)
    
    #index for generating new random uniformly distributed numbers if running out of them

    cdef int j = 0
    cdef int k
    cdef int l = 0
    cdef double rand
    
        # cenH and EcoRV are not silent (0) at the beginning
    cdef int cenH_silent = 0
    cdef int EcoRV_silent = 0
    
    # cenH and EcoRV status at each time point
    cdef int[:] cenH_status_list = np.zeros(duration, dtype=np.int32)
    cdef int[:] EcoRV_status_list = np.zeros(duration, dtype=np.int32)

    # list to store the colorcoded nucleosome states of current mt_region
    states = []
    
    S_nucleosomes = []
    A_nucleosomes = []
    U_nucleosomes = []
    S_nucleosomes_cenH = []
    
    # append the starting nucleosomes
    for nuc in mt_region:
                if nuc == 0:
                    state = 'blue'
                elif nuc == 1:
                    state = 'white'
                elif nuc == 2:
                    state = 'red'
                    
                states.append(state)
                
                
    current_states = []
    region_state = 0
    
    cdef int[:] mod_prob = np.zeros(240, dtype=np.int32)
    
    while T <= duration:
        j += 1
        #generating new random uniformly distributed numbers if running out of them
        if j >= n:
            # used for chosing a position
            random_integers = np.random.randint(len(positions), size=n, dtype=np.int32)
            random_integers2 = np.random.randint(len(positions), size=n, dtype=np.int32)
            #used for generating time_increase
            random_doubles1 = np.random.random(n)
            random_doubles2 = np.random.random(n)
            random_doubles3 = np.random.random(n)
            random_doubles4 = np.random.random(n)
            random_doubles5 = np.random.random(n)
            j = 0

        # choses the time of the fastest reaction (equivalent to generating 8 different numbers)
        time_increase = -log(random_doubles1[j]) / total_rate
        
        # generates a random number within the range of total_rate (sum of all rates)
        rand = total_rate * random_doubles2[j]

        low_t_index = n_rates - 1
        
        # goes through all rates
        for k in range(n_rates):
            # if rand is smaller then the cumsum at pos of kth rate
            if rand < cumsum_rates[k]:
                # the index of the fastest rate is chosen
                low_t_index = k
                break
        
        # increases time by the length of the 
        T += time_increase
        t += time_increase
        

        # if the spontaneous conversion-rate (direct conversion of A to U) is chosen
        if low_t_index == 0:
            # a position of a nucleosome to be converted is chosen
            pos_conv = random_integers[j]
            # the nucleosome at that posion is selected
            nuc_conv = mt_region[pos_conv]
            
            if nuc_conv == 0:
                mt_region[pos_conv]=1
                
                
        # if the spontaneous conversion-rate (direct conversion of U to A) is chosen
        elif low_t_index == 1:            
           # a position of a nucleosome to be converted is chosen
            pos_conv = random_integers[j]
            # the nucleosome at that posion is selected
            nuc_conv = mt_region[pos_conv]
            
            if nuc_conv == 1:
                mt_region[pos_conv]=0
                
                
        # if the spontaneous conversion-rate (direct conversion of U to M) is chosen
        elif low_t_index == 2:   
            # a position of a nucleosome to be converted is chosen
            pos_conv = random_integers[j]
            # the nucleosome at that posion is selected
            nuc_conv = mt_region[pos_conv]
    
            if nuc_conv == 1:
                mt_region[pos_conv]= 2
    
    
        # if the spontaneous conversion-rate (direct conversion of M to U) is chosen
        elif low_t_index == 3:      
            # a position of a nucleosome to be converted is chosen
            pos_conv = random_integers[j]
            # the nucleosome at that posion is selected
            nuc_conv = mt_region[pos_conv]
            
            if nuc_conv == 2:
                mt_region[pos_conv]=1
                
                
         # if the spontaneous conversion-rate (direct conversion in special region of A to U) is chosen
        elif low_t_index == 4:     
            # a position of a nucleosome to be converted is chosen
            pos_conv = random_integers[j]
            # the nucleosome at that posion is selected
            nuc_conv = mt_region[pos_conv]
            
            if SAU == 1:
                
                # if the nucleosome is within the special region (cenH) and in state A
                if pos_conv >= cenHl and pos_conv <= cenHr and nuc_conv == 0:
                    # the state of the nucleosome is changed to U
                        mt_region[pos_conv]=1
            
            else:
                
                # if the nucleosome is within the special region (cenH) and in state U
                if pos_conv >= cenHl and pos_conv <= cenHr and nuc_conv == 1:
                    # the state of the nucleosome is changed to S
                        mt_region[pos_conv]=2
                    
            # else, nothing happens
            
        # if the global recruitment-rate M-catalysed change of U to M (recruited conversion) is chosen
        elif low_t_index == 5:                            
            
            # a position of a nucleosome to be converted is chosen
            pos_rec = random_integers[j]
            # the nucleosome at that posion is selected
            nuc_rec = mt_region[pos_rec]
            
            pos_conv = random_integers2[j]
            nuc_conv = mt_region[pos_conv]

            #   #recruitment probability list relative to nucleosome at position x
            # ran = random_doubles4[j]
            # x = <int> (long_nn)**ran

            #   # calculates the distance between nuc_rec and nuc_conv
            # if random_doubles5[j] > 0.5:
            #     Rand = 0
            # else:
            #     Rand = 1
            # if Rand == 1:
            #     x = -x
            # pos_conv = pos_rec + x
            
            # if pos_conv < 0 or pos_conv > nn - 1:
            #     nuc_conv = -10
            # else:
            #     nuc_conv = mt_region[pos_conv]
                
            
            
            
            #recruitment probability 1/(x+10)
            # ran = random_doubles4[j]
            # x = <int> ((long_nn+10)**ran -10)

            # # calculates the distance between nuc_rec and nuc_conv
            # if random_doubles5[j] > 0.5:
            #     Rand = 0
            # else:
            #       Rand = 1
            # if Rand == 1:
            #       x = -x
            # pos_conv = pos_rec + x
            
            # if pos_conv < 0 or pos_conv > nn - 1:
            #       nuc_conv = -1
            # else:
            #       nuc_conv = mt_region[pos_conv]
        
            
                
            # and if the recruiting nucleosome is in state M (2)
            if nuc_rec == 2:
                # and the nucleosme to be converted is in state U
                if nuc_conv == 1:
                    # then the nucleosome to be converted is changed to an M
                    mt_region[pos_conv] = 2
                   
        
        # if the local recruitment-rate A-catalysed change of M to U (recruited conversion) is chosen
        elif low_t_index == 6:
          # a position of a recruiting nucleosome is chosen
            pos_rec = random_integers[j]
            # the nucleosome at that posion is selected
            nuc_rec = mt_region[pos_rec]
            
            
            if random_doubles3[j] > 0.5:
                pos_conv = pos_rec - 1
            else:
                pos_conv = pos_rec + 1
                
                    
            if pos_conv >= 0 and pos_conv <= nn-1:
                # the nucleosome at that posion is selected
                nuc_conv = mt_region[pos_conv]
            else:
                nuc_conv = -10
            
            # if the recruiting nucleosome is in state A
            if nuc_rec == 0:
                # and the nucleosome to be converted is in state M
                if nuc_conv == 2:
                    # then it is changed to an U
                   mt_region[pos_conv]= 1
                   
        # if the local recruitment-rate A-catalysed change of U to A (recruited conversion) is chosen         
        elif low_t_index == 7:            
            # a position of a recruiting nucleosome is chosen
            pos_rec = random_integers[j]
            # the nucleosome at that posion is selected
            nuc_rec = mt_region[pos_rec]
            
            
            if random_doubles3[j] > 0.5:
                pos_conv = pos_rec - 1
            else:
                pos_conv = pos_rec + 1
                
                    
            if pos_conv >= 0 and pos_conv <= nn-1:
                # the nucleosome at that posion is selected
                nuc_conv = mt_region[pos_conv]
            else:
                nuc_conv = -1
            
            # if the recruiting nucleosome is in state A
            if nuc_rec == 0:
                # and the nucleosome to be converted is in state U
                if nuc_conv == 1:
                    # then it is changed to an A
                   mt_region[pos_conv]= 0
                   
                   
        # if the local recruitment-rate (recruited conversion of A (0) to U (1)) is chosen         
        elif low_t_index == 8:  
            
            # a position of a recruiting nucleosome is chosen
            pos_rec = random_integers[j]
            # the nucleosome at that posion is selected
            nuc_rec = mt_region[pos_rec]
            
            
            if random_doubles3[j] > 0.5:
                pos_conv = pos_rec - 1
            else:
                pos_conv = pos_rec + 1
                
                    
            if pos_conv >= 0 and pos_conv <= nn-1:
                # the nucleosome at that posion is selected
                nuc_conv = mt_region[pos_conv]
            else:
                nuc_conv = -1
            
            # if the recruiting nucleosome is in state M
            if nuc_rec == 2:
                # and the nucleosome to be converted is in state A
                if nuc_conv == 0:
                    # then it is changed to an U
                   mt_region[pos_conv]= 1
                   
                   
        # # if the global recruitment-rate M-catalysed change of M to U (Epe1) (recruited conversion) is chosen
        # elif low_t_index == 9:                            
            
        #     # a position of a nucleosome to be converted is chosen
        #     pos_rec = random_integers[j]
        #     # the nucleosome at that posion is selected
        #     nuc_rec = mt_region[pos_rec]
            
        #     pos_conv = random_integers2[j]
        #     nuc_conv = mt_region[pos_conv]
            
        #     if len(mt_region)==182:
                
        #         # if the nucleosome is within the special region (cenH) and in state A
        #         if pos_conv >= 90 and pos_conv <= 119:
                    
        #              # and if the recruiting nucleosome is in state M (2)
        #             if nuc_rec == 2:
        #                 # and the nucleosme to be converted is in state U
        #                 if nuc_conv == 2:
        #                     # then the nucleosome to be converted is changed to an M
        #                     mt_region[pos_conv] = 1
                            
        #     elif len(mt_region)==191:
                
        #         # if the nucleosome is within the special region (cenH) and in state A
        #         if pos_conv >= 90 and pos_conv <= 128:
                    
        #              # and if the recruiting nucleosome is in state M (2)
        #             if nuc_rec == 2:
        #                 # and the nucleosme to be converted is in state U
        #                 if nuc_conv == 2:
        #                     # then the nucleosome to be converted is changed to an M
        #                     mt_region[pos_conv] = 1
            
        #     elif len(mt_region)==203:
                
        #         # if the nucleosome is within the special region (cenH) and in state A
        #         if pos_conv >= 90 and pos_conv <= 140:
                    
        #              # and if the recruiting nucleosome is in state M (2)
        #             if nuc_rec == 2:
        #                 # and the nucleosme to be converted is in state U
        #                 if nuc_conv == 2:
        #                     # then the nucleosome to be converted is changed to an M
        #                     mt_region[pos_conv] = 1
        
            
            
        # after each generation, half f the nucleosomes are exchanged with us
        if t >=1:
            t=0
            
            # colorcode the nucleosomes and store them in states vector
            # A = blue, U = yellow and M = red
            
            
            for nuc in mt_region:
                if nuc == 0:
                    state = 'blue'
                elif nuc == 1:
                    state = 'white'
                elif nuc == 2:
                    state = 'red'
                    
                states.append(state)
                current_states.append(state)
                
            cenH_blue = current_states[cenHl:cenHr+1].count('blue')
            cenH_red = current_states[cenHl:cenHr+1].count('red')
            
            EcoRV_blue = current_states[EcoRVl:EcoRVr+1].count('blue')
            EcoRV_red = current_states[EcoRVl:EcoRVr+1].count('red')
            
            if cenH_red - cenH_blue >= threshold1:
                cenH_silent = 1
            if EcoRV_red - EcoRV_blue >= threshold2:
                EcoRV_silent = 1
        
                    
            cenH_status_list[int(T)]=cenH_silent
            EcoRV_status_list[int(T)]=EcoRV_silent
            
            S_nucleosomes.append(current_states.count('red'))
            A_nucleosomes.append(current_states.count('blue'))
            U_nucleosomes.append(current_states.count('white'))
            
             # erase current state vector again
            current_states = []
            
            S_nucleosomes_cenH.append(cenH_red)
            
                
            # the state of the mt_region at this time point is stored 
            #mt_matrix[m]=mt_region
            for i in positions:
                rand = random.choice([0,1])
                if rand == 1:
                    mt_region[i]=1
                    
                    
        # if T>= 50 and T<= 51:
        #      for i in positions[]:
        #          mt_region[i]=2
            
    
    
    
    
    return  cenH_status_list, EcoRV_status_list, states, S_nucleosomes_cenH, S_nucleosomes, A_nucleosomes, U_nucleosomes
    
    

