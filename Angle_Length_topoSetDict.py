# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 17:41:41 2021

@author: Lorenzo Vallisa
"""
import numpy as np
import io
import matplotlib.pyplot as plt
import os 
import math

#INPUT for topoSetDict settings
L_D = 1.5
L = 0.08 * L_D
angle_deg = 15

#OBTAINED QUANTITIES
angle= angle_deg/180 * np.pi
a = L/2;

x_min = 1.25 - a * math.sin(angle)
z_min = 3.1 - a*math.cos(angle)

x_max = 1.25 + a*math.sin(angle)
z_max = 3.1 + a*math.cos(angle)

print('topoSetDict features')
print('(',x_min,1.25,z_min,') ,','(',x_max,1.25,z_max,')')

#INPUT for COM settings
b = +1 #+1 above - 0 coindice - -1 below
beta = L/3


#OBTAINED QUANTITIES
x = 1.25 + b*beta*math.sin(angle)
z = 3.1 + b*beta*math.cos(angle)

print('COM')
print('(',x,1.25,z,')')


