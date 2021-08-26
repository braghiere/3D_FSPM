import numpy as np
import matplotlib.pyplot as plt
import pandas as pd




df1 = pd.read_csv('/home/renato/groimp_efficient/output_60steps/feddes_original_1.soi',sep='\t',names=['time','PET','canopy_int','solar_ratio','scale_tree_growth','rub1','rub59','rub3'])

df59 = pd.read_csv('/home/renato/groimp_efficient/output_60steps/feddes_original_60.soi',sep='\t',names=['time','PET','canopy_int','solar_ratio','scale_tree_growth','rub1','rub59','rub3'])

dfofi = pd.read_csv('/home/renato/groimp_efficient/transp.txt',sep='\t',names=['PET'],skiprows=1,header=None)


time = df1.time.values
time = np.array(time)

PET1 = df1.PET.values
PET1 = np.array(PET1)

PET59 = df59.PET.values
PET59 = np.array(PET59)

PET = df59.PET.values
PET = np.array(PET)

print(PET1,PET59)

plt.scatter(time, PET1)
plt.plot(time, PET59,'r-')
plt.plot(time, PET,'k-')
plt.ylim(0,1.0E-6)

plt.show()


