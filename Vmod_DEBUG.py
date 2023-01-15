#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 24 13:03:51 2019

@author: erikdrybread
"""

import math
import matplotlib.pyplot as plt
import numpy

def Vmod(K, P, epoch, obs):
    dT = obs - epoch             #delta time
    dPh = (dT % P) / P           #delta phase 
    Phase = dPh * 2 * math.pi
    NewRV = K * math.sin(-Phase)
    
    return NewRV

#Test Client
def main():
    K = 10   #Semiamplitude
    P = 100                      #Period of planet
    epoch = 0                    #transit epoch
    RVarray = numpy.zeros(100)
    
    for i in range(0, 100):
        obs = i                     #observation time or JD
        NewRV = Vmod(K, P, epoch, obs)
        RVarray[i] = NewRV
        #print(RVarray[i])
    plt.plot(numpy.arange(100), RVarray, 'o')
    plt.show()
if __name__ == '__main__':
    main()