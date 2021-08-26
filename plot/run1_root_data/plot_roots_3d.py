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


day_list = []
day = 1


count = 0
X = []
Y = []
Z = []



df1 = pd.read_csv('/home/renato/groimp_efficient/run_1/seg60.txt',
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

while day <= 30:

     print day_list
     ax = plt.subplot(111, projection='3d')
     day_list.append(day)

     #for j in range(len(NumAxe)):

     #print NumAxe[i],Jour[i],Diam[i],X1[i], Y1[i], Z1[i],X2[i], Y2[i], Z2[i]
     df1 = pd.read_csv('/home/renato/groimp_efficient/plot/run1_root_data/seg%s.txt'%(day),
                   delim_whitespace=True,skiprows=0,header=0)

     #if Jour[j] in day_list:


     NumAxe = np.array(df1['NumAxe'].values)
     Jour = np.array(df1['Jour'].values)
     Diam = np.array(df1['Diam'].values)
     x1 = np.array(df1['X1'].values)
     y1 = np.array(df1['Y1'].values)
     z1 = np.array(df1['Z1'].values)
     x2 = np.array(df1['X2'].values)
     y2 = np.array(df1['Y2'].values)
     z2 = np.array(df1['Z2'].values)

     for j in range(len(x1)):

       #axis and radius
       p0 = np.array([x1[j], y1[j], -z1[j]]) #point at one end
       p1 = np.array([x2[j], y2[j], -z2[j]]) #point at other end
       R = Diam[j]

       #vector in direction of axis
       v = p1 - p0

       #find magnitude of vector
       mag = norm(v)

       #unit vector in direction of axis
       v = v / mag

       #make some vector not in the same direction as v
       not_v = np.array([1, 0, 0])
       if (v == not_v).all():
          not_v = np.array([0, 1, 0])

       #make vector perpendicular to v
       n1 = np.cross(v, not_v)
       #normalize n1
       n1 /= norm(n1)

       #make unit vector perpendicular to v and n1
       n2 = np.cross(v, n1)

       #surface ranges over t from 0 to length of axis and 0 to 2*pi
       t = np.linspace(0, mag, 2)
       theta = np.linspace(0, 2 * np.pi, 100)
       rsample = np.linspace(0, R, 2)

       #use meshgrid to make 2d arrays
       t, theta2 = np.meshgrid(t, theta)

       rsample,theta = np.meshgrid(rsample, theta)

       #generate coordinates for surface
       # "Tube"
       #X, Y, Z = [p0[i] + v[i] * t + R * np.sin(theta2) * n1[i] + R * np.cos(theta2) *       n2[i] for i in [0, 1, 2]]
       X.append(p0[0] + v[0] * t + R * np.sin(theta2) * n1[0] + R * np.cos(theta2) *       n2[0]) 
       Y.append(p0[1] + v[1] * t + R * np.sin(theta2) * n1[1] + R * np.cos(theta2) *       n2[1])
       Z.append(p0[2] + v[2] * t + R * np.sin(theta2) * n1[2] + R * np.cos(theta2) *       n2[2])


       #T = (X[j]**2+Y[j]**2+Z[j]**2)**(1/2)
       my_col = cm.jet_r(Z[j]/float(Z[j].max()))

       ax.plot_surface(X[j], Y[j], Z[j], facecolors = my_col)
       #ax.plot_surface(X_diff, X_diff, X_diff, facecolors = my_col)
       #ax.plot_surface(X, Y, Z, color = cm.rainbow(255*Jour[i]/60))
       #ax.contourf(X, Y, Z, zdir='y', offset=max(y2),cmap=cm.rainbow, vmin=0, vmax=60)
       # Tweaking display region and labels
       ax.set_xlim(-250, 250)
       ax.set_ylim(-250, 250)
       ax.set_zlim(-1000, 0)
       ax.set_xlabel('X axis')
       ax.set_ylabel('Y axis')
       ax.set_zlabel('Z axis')
       #ax.plot_surface(X2, Y2, Z2, color='black')
       #ax.plot_surface(X3, Y3, Z3, color='black')
       count = count + 1


     m = cm.ScalarMappable(cmap=cm.jet)
     m.set_array(range(61))
     cbar = plt.colorbar(m)
     cbar.ax.set_ylabel('Root age (days)', rotation=270, labelpad=20)
     #plt.colorbar(m)

 
     plt.title('DAY = %i' %(day))
     plt.tight_layout()
     plt.show()

     #plt.savefig('/home/renato/groimp_efficient/run_2/figures/root_3d_%i.png'%(day))
     #ax=plt.subplot(111, projection='3d')
     day = day + 1


