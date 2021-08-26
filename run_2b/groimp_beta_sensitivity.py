#!/home/renato/anaconda2/bin/python

import numpy as np
import matplotlib.pyplot as plt
import os, sys
from scipy.interpolate import interp2d
from pylab import * 
import pandas as pd


for k in range(0,101):

  #beta = np.ones(60)
  beta = np.empty(94)
  beta.fill(k/100.0)
  data = np.array([beta]).T
  df4 = pd.DataFrame(data)
  df4.to_excel("/home/renato/groimp_efficient/beta_1.xls", index=False, header=False)
 
  os.system("java -Xmx2000m -jar /home/renato/Downloads/GroIMP-1.5/core.jar --headless /home/renato/Downloads/FSPM_BASIC-master-transpired-efficient/project.gs")


  df0 = pd.read_csv('/home/renato/groimp_efficient/field.txt',
      delim_whitespace=True,skiprows=1,header=None,
       names=["time", "species", "LAI", "nrShoots", "fAbs", "assCO2", "biomAbove", "yield", "harvestIndex","leafArea","fieldRFR"])

  df0.to_csv('/home/renato/groimp_efficient/run_2b/field_gday_%s.txt' %k ,sep='\t', index=False, header=None)

  #df0.to_csv('/home/renato/groimp_efficient/run_2b/field_clm_%s.txt' %k ,sep='\t', index=False, header=None)

  #df0.to_csv('/home/renato/groimp_efficient/run_2b/field_jules_%s.txt' %k ,sep='\t', index=False, header=None)


  df0 = pd.read_csv('/home/renato/groimp_efficient/plant.txt',
      delim_whitespace=True,skiprows=1,header=None,
       names=["time", "tt", "plant", "strip", "row", "pos", "species", "weed",
              "age","nrbranches","leafArea","fpar","rfr","biom","yield","leafmass",
               "stemmass", "rootmass","shootrootratio","abovebiom","transpiration"])

  df0.to_csv('/home/renato/groimp_efficient/run_2b/plant_gday_%s.txt' %k ,sep='\t', index=False, header=None)

  #df0.to_csv('/home/renato/groimp_efficient/run_2b/plant_clm_%s.txt' %k ,sep='\t', index=False, header=None)

  #df0.to_csv('/home/renato/groimp_efficient/run_2b/plant_jules_%s.txt' %k ,sep='\t', index=False, header=None)




  
  

