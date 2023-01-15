#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 12:22:12 2019

@author: erikdrybread
"""

import Semiamp
import numpy
import Vmod
from astropy.io import ascii
import NewPeriodogram
import matplotlib.pyplot as plt

Mstar = 1.12 #Mass of star in solar masses
P = 2.476 #period
epoch = 2458382.228
G = 6.67e-11 #Gravitational Constant
inc = 71.8 #inclination of orbit

Data=ascii.read('Combined_Data_HARPS_PFS.csv', names=('date','vel','errvel'))

for i in range(1, 41):
    mplanet = i / 2 #mass of planet in earth masses
    K = Semiamp.Semiamp(Mstar, mplanet, inc, G, P)
    #print(K)
    
    obstimes = Data['date']
    injectedRVs = numpy.zeros(len(obstimes))
    
    for j in range(0, len(obstimes)):
        injectedRVs[j] = Vmod.Vmod(K, P, epoch, obstimes[j], offset = False) + Data['vel'][j]
        print(Data['date'][j], injectedRVs[j], Data['errvel'][j])
    
    
    temp = numpy.column_stack((Data['date'], injectedRVs, Data['errvel']))
    File = 'HD30219_Combined_injected_' + str(i / 2) + '_mass_in_0.5steps_in_phase.csv'
    numpy.savetxt(File, temp, delimiter = ',')

    date = Data['date']
    vel = injectedRVs
    errvel = Data['errvel']
    filename = File
    newfile = 'HD30219_Combined_injected' + str(i / 2) + '_mass_in_0.5steps_in_phase.pdf'

    NewPeriodogram.LSP(date, vel, errvel, filename, newfile)
    
        
    