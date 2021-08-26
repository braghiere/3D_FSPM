#!/home/renato/anaconda2/bin/python

import numpy as np
import matplotlib.pyplot as plt
import os, sys
from scipy.interpolate import interp2d
from pylab import * 
import pandas as pd


for k in range(1,61):

  if(k == 1):
    beta = np.ones(60)
    #beta = np.empty(60)
    #beta.fill(1.0E-8)
    data = np.array([beta]).T
    df4 = pd.DataFrame(data)
    df4.to_excel("/home/renato/groimp_efficient/beta_1.xls", index=False, header=False)

    #writer = pd.ExcelWriter('/home/renato/groimp_efficient/beta_1.xls')
    #df4.to_excel(writer,'Sheet1')
    
    print ("----------------------------------------",
          "----------------------------------")
    print ("--------------- Writing feddes.soi for Min3pArchiSImple",
           " ------------------") 

    df2 = pd.read_csv('/home/renato/groimp_efficient/input/feddes.soi',sep='\t',names=['time','ET','canopy_int','solar_ratio','scale_tree_growth','rub1','rub2','rub3'])

    #ET = df2.ET.values
    #ET = np.array(ET)
    ET = np.empty(60)
    ET.fill(2.0E-8)

    i = len(ET)

    rootbiom = np.empty(60)
    rootbiom.fill(3000)

      
  print ("----------------------------------",
         "----------------------------------------"  )
  print ("------------------------ Start GroIMP 1.5 -----",
        "---------------------------")

  os.system("java -Xmx2000m -jar /home/renato/Downloads/GroIMP-1.5/core.jar --headless /home/renato/Downloads/FSPM_BASIC-master-transpired-efficient/project.gs")

  print ("---------------------------------",
         "-----------------------------------------")
  print ("------------------------ Reading PET from GroIMP 1.5",
          "---------------------")

  df1 = pd.read_csv('/home/renato/groimp_efficient/transp.txt',header=0, names=['transpiration'])
  PET = df1.transpiration.values

  PET = np.array(PET)

  for count in range(1,k):
      ET[count-1] = PET[count-1]

  print ("-------------------------------------",
         "-------------------------------------")  
  print ("------------------------ Writing update of feddes.soi ",
         "--------------------")
  
  data = np.array([df2.time[:i].values,
                 ET[:i],
                 df2.canopy_int[:i].values,
                 df2.solar_ratio[:i].values,
                 df2.scale_tree_growth[:i].values]).T

  df3 = pd.DataFrame(data)

  df3.to_csv('/home/renato/groimp_efficient/input/feddes.soi',sep='\t', index=False, header=None )

  df3.to_csv('/home/renato/groimp_efficient/output_60steps/feddes_original_%s.soi' %k,sep='\t', index=False, header=None)

  print ("--------------------------------------",
         "------------------------------------")
  print ("------------------- Reading RootBiom from GroIMP 1.5 ",
         "---------------------") 

  df1 = pd.read_csv('/home/renato/groimp_efficient/root.txt',header=0, names=['rootbiom'])
  root = df1.rootbiom.values

  root = np.array(root)

  for count in range(1,k):
      rootbiom[count-1] = root[count-1]

  print ("----------------------------------",
         "----------------------------------------")  
  print ("---------------------- Writing update of biomrac.txt",
         "---------------------") 
  
  data = np.array([rootbiom[:i]]).T

  df4 = pd.DataFrame(data)

  df4.to_csv('/home/renato/groimp_efficient/input/biomrac.txt',sep='\t', index=False, header=None)
  df4.to_csv('/home/renato/groimp_efficient/output_60steps/biomrac_%s.txt' %k ,sep='\t', index=False, header=None)

  print ("-----------------------------------",
         "---------------------------------------")  
  print ("------------------------- Start Min3pArchiSimple",
         "-------------------------") 
  print ("-------------------------------------",
         "-------------------------------------") 

  os.system("/home/renato/Desktop/Min3pArchi91_reconstruc/bin/main.exe")
  os.system("cp /home/renato/groimp_efficient/input/RSD_2D_MIN3P60.txt /home/renato/groimp/input/RSD_2D_MIN3P60_%s.txt" %k)

  print ("--------------------------------------",
          "------------------------------------")  
  print ("------------------------- Calculating root water",
         "-------------------------") 
  print ("------------------------- uptake from Min3pArchi",
         "-------------------------") 

  df0 = pd.read_csv('feddes_%s.gsp'  %k,
      delim_whitespace=True,skiprows=3,header=None,
       names=["x", "y", "z", "h_w", "p_w", "s_w", "theta_w", "transp", "evap"])

  transp = df0['transp'].values
  transp_sum = np.sum(np.array(transp).astype(np.float))

  # water uptake value
  print (transp_sum)
  ET[k-1] = transp_sum

  data = np.array([ET]).T

  df8 = pd.DataFrame(data)

  df8.to_csv('/home/renato/groimp_efficient/output_60steps/RWU_%s.txt' %k,sep='\t', index=False, header=None )

  # calculate
  if(PET[k-1] != 0.):
    beta[k-1] = ET[k-1]/PET[k-1]
  else:
    beta[k-1] = 1.0

  #try:
  #  np.divide(ET[:i],PET,beta)
  #except ZeroDivisionError:
  #  pass

  beta[beta == 0.] = 1.0
  beta[beta > 1.] = 1.0
  #beta[beta < 0.3] = 0.3

  os.system("rm /home/renato/groimp_efficient/beta_1.xls")

  data = np.array([beta[:i]]).T

  df4 = pd.DataFrame(data)
  df4.to_excel("/home/renato/groimp_efficient/beta_1.xls", index=False, header=False)


  df4.to_csv('/home/renato/groimp_efficient/output_60steps/beta_1_%s.txt' %k,sep='\t', index=False, header=None)

  print "beta_1.xls updated for time = ", k 

  print "--------------------------------------------------------------------------"  
  print "------------------------ Start GroIMP 1.5 --------------------------------" 

  #os.system("java -Xmx2000m -jar /home/renato/Downloads/GroIMP-1.5/core.jar --headless /home/renato/Downloads/FSPM_BASIC-master-transpired-efficient/project.gs")

  df0 = pd.read_csv('/home/renato/groimp_efficient/field.txt',
      delim_whitespace=True,skiprows=1,header=None,
       names=["time", "species", "LAI", "nrShoots", "fAbs", "assCO2", "biomAbove", "yield", "harvestIndex","leafArea","fieldRFR"])

  df0.to_csv('/home/renato/groimp_efficient/output_60steps/field_%s.txt' %k ,sep='\t', index=False, header=None)

  df0 = pd.read_csv('/home/renato/groimp_efficient/plant.txt',
      delim_whitespace=True,skiprows=1,header=None,
       names=["time", "tt", "plant", "strip", "row", "pos", "species", "weed",
              "age","nrbranches","leafArea","fpar","rfr","biom","yield","leafmass",
               "stemmass", "rootmass","shootrootratio","abovebiom","transpiration"])

  df0.to_csv('/home/renato/groimp_efficient/output_60steps/plant_%s.txt' %k ,sep='\t', index=False, header=None)








  
  

