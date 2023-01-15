#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 12:22:30 2019

@author: erikdrybread
"""

import matplotlib.pyplot as plt
from astropy.io import ascii
from astropy.stats import LombScargle as AP_LS

#——————————

Data=ascii.read('Combined_Data_HARPS_PFS.csv',names=('date','vel','errvel'))
starname='HD30219'

#——————————

#S-index Periodograms

plt.figure(1,[12,9])   #initialize figure dimensions
ax1=plt.subplot(111)   #initialize the figure itself

minfreq=0.001 #set min frequency of the LS periodogram: corresponds to a maximum period of 1/f, or 1000 days
maxfreq=2.0   #set max frequency of the LS periodogram: corresponds to a minimum period of 1/f, or 0.5 days

ls = AP_LS(Data['date'], Data['vel'])  #Analyze our dates and s-index data using the AstroPy Lomb Scargle module
frequency,power = ls.autopower(minimum_frequency=minfreq,maximum_frequency=maxfreq) #Determine the LS periodogram

ax1.semilogx(1/frequency,power,color='blue')  #Plot the resulting periods (1/the freq from the LS result) and LS power

ax1.set(xlim=([0.5,1000]),ylim=([0,power.max()*1.1]))                 #Set y-axis to go from 0 to 10% above the max peak height
ax1.set_title(starname+' RV Data',fontsize=16)                 #Set the plot title
ax1.set_ylabel('L-S power',fontsize=20,fontweight='bold')       #Set the y-axis
ax1.set_xlabel('Period [days]',fontsize=20,fontweight='bold')   #Set the x-axis
ax1.tick_params(axis='both',which='major',labelsize=15)         #Set the size of the tick marks

#Figure out the L-S Power levels that correspond to some FAP values
FAP_probabilities = [0.5, 0.1, 0.01]                                        #Enter FAP values you want to determine
FAP_levels=ls.false_alarm_level(FAP_probabilities)               #Get corresponding LS Power values
ax1.hlines(FAP_levels,0.5,1000,color='grey',linewidth=1,)    #Plot the result as horizontal lines on the figure
ax1.vlines(2.476, 0, 1, colors='red')
ax1.text(2e2,FAP_levels[0],'0.5% FAP',fontsize=14)             #Add some labels, so we know what the lines correspond to
ax1.text(2e2,FAP_levels[1],'0.1% FAP',fontsize=14)
ax1.text(2e2,FAP_levels[2],'0.01% FAP',fontsize=14)
#print('L-S power for FAPs of 0.5, 0.5, 0.01',FAP_levels)      #Print out the results if you want
#See what the FAP is for the peak we see in the data
FAP=ls.false_alarm_probability(power.max())                             #Calculate the FAP for the highest peak in the power array
peak_loc=round(float(1/frequency[power == power.max()]),2)   #Get the period of the highest peak, rounded to 0.01 days
ax1.plot(peak_loc, power.max(), marker='d', markersize=12, color="red")                      #add a red diamond to mark the highest peak
ax1.text(peak_loc*1.2,power.max(),'Peak Period: '+str(peak_loc)+' days',fontsize=14)   #add text to figure with details
ax1.text(peak_loc*1.2,power.max()*.95,'FAP: '+str(FAP),fontsize=14)                               #about the highest LS peak

#print('Period of tallest peak: ',peak_loc)       #Print out period of the highest peak, here it's 44.8 days
#print('FAP of tallest peak: ',FAP)                   #Print out that FAP number, here it's 6*10^-15.
plt.tight_layout()                                              #Set the figure to have no extra white space on the borders
plt.savefig('HD30219_Combined.pdf')                     #Save the figure 