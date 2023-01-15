#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 11:35:31 2019

@author: erikdrybread
"""

import math

def Vmod(K, P, epoch, obs, offset):
    dT = obs - epoch             #delta time
    dPh = (dT % P) / P           #delta phase 
    Phase = dPh * 2 * math.pi
    if offset == True:
        K = K * (-1)
    NewRV = K * math.sin(-Phase)
    
    return NewRV

#Test Client
def main():
    K = 10                       #Semiamplitude
    P = 10                       #Period of planet
    epoch = 1                    #transit epoch
    obs = 10                     #observation time or JD
    offset = True
    
    NewRV = Vmod(K, P, epoch, obs, offset)
    print(NewRV)
if __name__ == '__main__':
    main()