#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 08:24:15 2019

@author: erikdrybread
"""

from astropy.io import ascii
import numpy

Data=ascii.read('HD30219_HARPS_f2.vels', names=('date','vel','errvel'))

temp = numpy.column_stack((Data['date'], Data['vel'], Data['errvel']))
File = 'HD30219_HARPS_f2.csv'
numpy.savetxt(File, temp, delimiter = ',')