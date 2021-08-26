#!/home/renato/anaconda2/bin/python

import numpy as np
import matplotlib.pyplot as plt
import os, sys
from scipy.interpolate import interp2d
from pylab import * 
import pandas as pd

print "--------------------------------------------------------------------------"  
print "------------------------ Start GroIMP 1.5 --------------------------------" 

os.system("java -Xmx2000m -jar /home/renato/Downloads/GroIMP-1.5/core.jar --headless /home/renato/Downloads/FSPM_BASIC-master-transpired/project.gs")

print "--------------------------------------------------------------------------"  
print "------------------------ Reading PET from GroIMP 1.5 ---------------------" 

df1 = pd.read_csv('/home/renato/groimp/transp.txt',header=0, names=['transpiration'])
PET = df1.transpiration.values

PET = np.array(PET)

print "--------------------------------------------------------------------------"  
print "--------------- Writing feddes.soi for Min3pArchiSImple ------------------" 

df2 = pd.read_csv('/home/renato/groimp/input/feddes.soi',sep='\t',names=['time','ET','canopy_int','solar_ratio','scale_tree_growth','rub1','rub2','rub3'])

df2.to_csv('/home/renato/groimp/input/feddes_original.soi',sep='\t', index=False, header=None)

ET = df2.ET.values
ET = np.array(ET)

i = len(PET)

#old_err_state = np.seterr(divide='ignore', invalid='ignore')
#ignored_states = np.seterr(**old_err_state)

beta = np.zeros(i)

try:
    np.divide(ET[:i],PET,beta)
except ZeroDivisionError:
    pass



beta[beta > 1] = 1.0

data = np.array([df2.time[:i].values,
                 PET[:i],
                 df2.canopy_int[:i].values,
                 df2.solar_ratio[:i].values,
                 df2.scale_tree_growth[:i].values]).T

df3 = pd.DataFrame(data)

df3.to_csv('/home/renato/groimp/input/feddes.soi',sep='\t', index=False, header=None )

print "--------------------------------------------------------------------------"  
print "--------------- Writing biomrac.txt for Min3pArchiSImple -----------------" 
print "--------------------- from GroIMP1.5 ArchiSImple -------------------------" 

os.system("cp /home/renato/groimp/input/biomrac.txt /home/renato/groimp/input/biomrac_ori.txt")

#df4 = pd.read_csv('/home/renato/groimp/input/biomrac_ori.txt',names=['rootbiom'],header = 0)

#data = np.array([df4.rootbiom.values/1])

#df5 = pd.DataFrame(data)

#df5.to_csv('/home/renato/groimp/input/biomrac.txt',sep='\t', index=False, header=None )


print "--------------------------------------------------------------------------"  
print "------------------------- Start Min3pArchiSImple -------------------------" 
print "--------------------------------------------------------------------------" 

os.system("cd /home/renato/groimp/input")
os.system("/home/renato/Desktop/Min3pArchi91/bin/main.exe")

print "--------------------------------------------------------------------------"  
print "------------------------- Calculating root water -------------------------" 
print "------------------------- uptake from Min3pArchi -------------------------" 

output_array = [1,2,3,4,5,6,7,8,9,10,15,20,30,40,50,60]

#for count in range(60,61):
for count in output_array:

 df1 = pd.read_csv('../feddes_%s.gsp'  %count,
      delim_whitespace=True,skiprows=3,header=None,
       names=["x", "y", "z", "h_w", "p_w", "s_w", "theta_w", "transp", "evap"])

 RSD = df1['transp'].values
 RSD_sum = np.array(RSD).astype(np.float)

 print RSD_sum







