#!/usr/bin/ python
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  2 18:33:10 2016

Modified from https://stackoverflow.com/questions/38076682/how-to-add-colors-to-each-individual-face-of-a-cylinder-using-matplotlib
to add "end caps" and to undo fancy coloring.

@author: astrokeat
"""

import numpy as np
from matplotlib import pyplot as plt
from matplotlib import cm
from scipy.linalg import norm
from mpl_toolkits.mplot3d import Axes3D
import pandas as pd
import sys

biomrsd1= []
biomrsd2= []

df1 = pd.read_csv('/home/renato/groimp_efficient/run_3/seg60.txt',
                  delim_whitespace=True,skiprows=0,header=0)


NumAxe = np.array(df1['NumAxe'].values)
Jour = np.array(df1['Jour'].values)
Diam = np.array(df1['Diam'].values)
x1 = np.array(df1['X1'].values)
y1 = np.array(df1['Y1'].values)
z1 = np.array(df1['Z1'].values)
x2 = np.array(df1['X2'].values)
y2 = np.array(df1['Y2'].values)
z2 = np.array(df1['Z2'].values)


biomass = 0.0
pi = 3.1415926539

for j in range(1,61):
   biomass = 0.0
   for i in range(0,len(Jour)):
      if Jour[i] == j:
        biomass = biomass + (0.25*pi*0.1*np.sqrt((x1[i]-x2[i])**2 + (y1[i]-y2[i])**2+ (z1[i]-z2[i])**2)*(Diam[i]**2))/1000.
   #print j,biomass
   biomrsd1.append(biomass)


df2 = pd.read_csv('/home/renato/groimp_efficient/run_3/seg60_2.txt',
                  delim_whitespace=True,skiprows=0,header=0)


NumAxe = np.array(df2['NumAxe'].values)
Jour = np.array(df2['Jour'].values)
Diam = np.array(df2['Diam'].values)
x1 = np.array(df2['X1'].values)
y1 = np.array(df2['Y1'].values)
z1 = np.array(df2['Z1'].values)
x2 = np.array(df2['X2'].values)
y2 = np.array(df2['Y2'].values)
z2 = np.array(df2['Z2'].values)


biomass = 0.0
pi = 3.1415926539

for j in range(1,61):
   biomass = 0.0
   for i in range(0,len(Jour)):
      if Jour[i] == j:
        biomass = biomass + (0.25*pi*0.1*np.sqrt((x1[i]-x2[i])**2 + (y1[i]-y2[i])**2+ (z1[i]-z2[i])**2)*(Diam[i]**2))/1000.
   #print j,biomass
   biomrsd2.append(biomass)


#with open ('/home/renato/groimp_efficient/run_1c/paper_fig/RSD/biomass_run1.txt','w') as f:
 #  for item in biomrsd1:
 #      f.write("%s\n" % item)

#with open ('/home/renato/groimp_efficient/run_1c/paper_fig/RSD/biomass_run1c.txt','w') as f:
 #  for item in biomrsd2:
 #      f.write("%s\n" % item)

df3 = pd.read_csv('/home/renato/groimp_efficient/run_3/root.txt',
                  delim_whitespace=True,skiprows=0,header=0)


plant_groimp = np.array(df3['plant#'].values)
root_groimp = np.array(df3['rootMass(mg)'].values)

root_groimp_monocot = df3[df3['plant#'] == 1]
root_groimp_dicot = df3[df3['plant#'] == 2]

root_groimp_monocot = np.array(root_groimp_monocot['rootMass(mg)'].values)
root_groimp_dicot = np.array(root_groimp_dicot['rootMass(mg)'].values)

biomass_tot1 = []
biomass_tot1.append(0.0)
for i in range(1,len(biomrsd1)):
   biomass_tot1.append(biomass_tot1[i-1] + biomrsd1[i])

#plt.plot(biomrsd1,label='With Beta')
plt.plot(biomass_tot1,label='Monocot')

biomass_tot2 = []
biomass_tot2.append(0.0)
for i in range(1,len(biomrsd2)):
   biomass_tot2.append(biomass_tot2[i-1] + biomrsd2[i])


#plt.plot(biomrsd2,label='Without Beta')
plt.plot(biomass_tot2,label='Dicot')

#plt.plot(biomrsd2,label='Without Beta')
plt.plot(root_groimp_monocot/1000.,label='GroIMP Monocot')
plt.plot(root_groimp_dicot/1000.,label='GroIMP Dicot')

plt.xlabel("Time (days)", labelpad=20)
plt.ylabel("Root biomass (g)", labelpad=20)
# plt.title('DAY = 94')
plt.legend()
plt.title('Cereal')
plt.tight_layout()
plt.savefig('/home/renato/groimp_efficient/run_3/figures/RSD/biomass.png')
#plt.show()

   
sys.exit()
