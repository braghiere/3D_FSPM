#!/home/renato/anaconda2/bin/python

import numpy as np
import matplotlib.pyplot as plt
import os, sys
from scipy.interpolate import interp2d
from pylab import * 
import pandas as pd

df2 = pd.read_csv('/home/renato/groimp_efficient/input_PET_impact/feddes.soi',
                 sep='\t',
                 names=['time','PET','canopy_int','solar_ratio','scale_tree_growth',
                 'rub1','rub2','rub3'])

PET = df2.PET.values
ET = np.array(PET)

ET = np.zeros(60) 
 
for k in range(1,61):

  df0 = pd.read_csv('feddes_%s.gsp'  %k,
      delim_whitespace=True,skiprows=3,header=None,
       names=["x", "y", "z", "h_w", "p_w", "s_w", "theta_w", "transp", "evap"])

  transp = df0['transp'].values
  transp_sum = np.sum(np.array(transp).astype(np.float))

  # water uptake value
  print transp_sum
  ET[k-1] = transp_sum

  data = np.array([ET]).T

  df8 = pd.DataFrame(data)

df8.to_csv('/home/renato/groimp_efficient/input_PET_impact/RWU_3.txt',sep='\t', index=True, header=None )

print df8

PET_list = ['2E-08',]
duration = ['1 min 25 sec',]

plt.plot(PET,'r-')
plt.plot(ET,'k-')
plt.show()




