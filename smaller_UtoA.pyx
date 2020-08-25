#cython: language_level=3
import numpy as np
cimport numpy as np
import random
import cython
from libc.math cimport log

@cython.boundscheck(False)
@cython.wraparound(False)
@cython.cdivision(True)
def t_loop(double duration, int[:] mt_region, int[:] positions, double[:] rates):
    cdef double T = 0
    cdef double t = 0
    cdef double total_rate = np.sum(rates)
    cdef double[:] cumsum_rates = np.cumsum(rates)
    cdef int n_rates = len(rates)
    cdef double p1 
    cdef double p2

    cdef int low_t_index
    cdef long pos_conv
    cdef long pos_rec
    cdef int i
    cdef int nuc_conv
    cdef int nn = len(mt_region)
    cdef int long_nn = 203
    cdef int nuc_rec
    cdef double ran
    cdef int x

    cdef int n = 100000 # large number!
    cdef int[:] random_integers = np.random.randint(len(positions), size=n, dtype=np.int32)
    cdef int[:] random_integers2 = np.random.randint(len(positions), size=n, dtype=np.int32)
    cdef double[:] random_doubles1 = np.random.random(n)
    cdef double[:] random_doubles2 = np.random.random(n)
    cdef double[:] random_doubles3 = np.random.random(n)
    cdef double[:] random_doubles4 = np.random.random(n)
    cdef double[:] random_doubles5 = np.random.random(n)

    cdef int j = 0
    cdef int k
    cdef int l = 0
    cdef double rand

    # list to store the colorcoded nucleosome states of current mt_region
    states = []
    current_states = []
    
    region_state_blue=0
    region_state_red=0
    region_state = 0
    red = []
    blue = []
    
    switched = 0
    while T <= duration:
        
        if T >= duration/2 and switched == 0:
            switched = 1
            #cdef int[:] mt_region = np.zeros(70, dtype=np.int32)
            mt_region = np.ones(76, dtype=np.int32)*2
#        
        j += 1
        # if running out of numbers, generate new ones and set counter to zero again
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
        
        if low_t_index == 0:
            # a position of a nucleosome to be converted is chosen
            pos_conv = random_integers[j]
            # the nucleosome at that posion is selected
            nuc_conv = mt_region[pos_conv]

            if nuc_conv == 0:
                mt_region[pos_conv] = 1


        elif low_t_index == 1:
            # a position of a nucleosome to be converted is chosen
            pos_conv = random_integers[j]
            # the nucleosome at that posion is selected
            nuc_conv = mt_region[pos_conv]

            if nuc_conv == 1:
                mt_region[pos_conv] = 0


        elif low_t_index == 2:
            # a position of a nucleosome to be converted is chosen
            pos_conv = random_integers[j]
            # the nucleosome at that posion is selected
            nuc_conv = mt_region[pos_conv]

            if nuc_conv == 1:
                mt_region[pos_conv] = 2


        elif low_t_index == 3:
            # a position of a nucleosome to be converted is chosen
            pos_conv = random_integers[j]
            # the nucleosome at that posion is selected
            nuc_conv = mt_region[pos_conv]

            if nuc_conv == 2:
                mt_region[pos_conv] = 1
                

        # if the global recruitment-rate M-catalysed change of U to M (recruited conversion) is chosen
        elif low_t_index == 4:                            
            
            # a position of a nucleosome to be converted is chosen
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
            
            # if the recruiting nucleosome is in state M
            if nuc_rec == 2:
                # and the nucleosome to be converted is in state U
                if nuc_conv == 1:
                    # then it is changed to an M
                   mt_region[pos_conv]= 2
            
            
                   
        
        # if the local recruitment-rate A-catalysed change of M to U (recruited conversion) is chosen
        elif low_t_index == 5:
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
                # and the nucleosome to be converted is in state M
                if nuc_conv == 2:
                    # then it is changed to an U
                   mt_region[pos_conv]= 1
                   
        # if the local recruitment-rate A-catalysed change of U to A (recruited conversion) is chosen         
        elif low_t_index == 6:            
            # a position of a recruiting nucleosome is chosen
            pos_rec = random_integers[j]
            # the nucleosome at that posion is selected
            nuc_rec = mt_region[pos_rec]
            
            pos_conv = random_integers2[j]
            nuc_conv = mt_region[pos_conv]

            # #recruitment probability list relative to nucleosome at position x
            # ran = random_doubles4[j]
            # x = <int> (long_nn)**ran

            # # calculates the distance between nuc_rec and nuc_conv
            # if random_doubles5[j] > 0.5:
            #     Rand = 0
            # else:
            #     Rand = 1
            # if Rand == 1:
            #     x = -x
            # pos_conv = pos_rec + x
            
            # if pos_conv < 0 or pos_conv > nn - 1:
            #     nuc_conv = -1
            # else:
            #     nuc_conv = mt_region[pos_conv]
                
            
            
            
            # #recruitment probability 1/(x+10)
            # ran = random_doubles4[j]
            # x = <int> ((long_nn+10)**ran -10)

            # # calculates the distance between nuc_rec and nuc_conv
            # if random_doubles5[j] > 0.5:
            #     Rand = 0
            # else:
            #     Rand = 1
            # if Rand == 1:
            #     x = -x
            # pos_conv = pos_rec + x
            
            # if pos_conv < 0 or pos_conv > nn - 1:
            #     nuc_conv = -1
            # else:
            #     nuc_conv = mt_region[pos_conv]
            
            
            # if the recruiting nucleosome is in state A
            if nuc_rec == 0:
                # and the nucleosome to be converted is in state U
                if nuc_conv == 1:
                    # then it is changed to an A
                   mt_region[pos_conv]= 0
                   
                   
        # if the local recruitment-rate (recruited conversion of A (0) to U (1)) is chosen         
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
                nuc_conv = -10
        
            
                
            # and if the recruiting nucleosome is in state M (2)
            if nuc_rec == 2:
                # and the nucleosme to be converted is in state A
                if nuc_conv == 0:
                    # then the nucleosome to be converted is changed to a U
                    mt_region[pos_conv] = 1

        # after each generation, half f the nucleosomes are exchanged with us
        if t >= 1:
            t = 0

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


            blue_nucs = current_states.count('blue')
            red_nucs = current_states.count('red')
            current_states=[]
            
            blue.append(blue_nucs)
            red.append(red_nucs)
                         

            # the state of the mt_region at this time point is stored
            # mt_matrix[m]=mt_region
            for i in positions:
                rand = random.choice([0, 1])
                if rand == 1:
                    mt_region[i] = 1
                    
    
    count_blue=[]

    for number in blue:
        if number > 38:#40
            region_state_blue+=1
            
        else:
            count_blue.append(region_state_blue)
            region_state_blue=0
               
            
    count_red=[]
    
    for number in red:
        if number > 38:#40
            region_state_red+=1
            
        else:
            count_red.append(region_state_red)
            region_state_red=0
               
            
    
    count_red.append(region_state_red)
    count_blue.append(region_state_blue)
    
    
    Max_blue=max(count_blue)
    Max_red=max(count_red)
    
    
    
    
        
        
        
   
    return Max_blue, Max_red, list(states)
