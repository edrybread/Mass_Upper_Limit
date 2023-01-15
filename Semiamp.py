#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 08:01:49 2019

@author: erikdrybread
"""

import math

def Semiamp(M, m, inc, G, P):
    
    P_sec = P * 86400   #input P is assumed to be in days
    M_kg = M * 1.9891e30   #input M is assumed to be in Solar Masses
    m_kg = m * 5.972e24   #input m is assumed to be in Earth Masses
    
    a = ((2 * math.pi * G) / P_sec) ** (1/3)
    b = (m_kg * math.sin(math.radians(inc))) / ((M_kg + m_kg) ** (2/3))
    
    K = a * b
    return K

#Test Client
def main():
    M = 1         #mass of star in solar masses
    m = 10          #mass of planet in earth masses
    inc = 90         #inclination of planet orbit
    G = 6.67408e-11   #gravitational constant
    P = 10         #period of planet
    
    
    K = Semiamp(M, m, inc, G, P)
    print(K)
    
if __name__ == '__main__':
    main()    
    


