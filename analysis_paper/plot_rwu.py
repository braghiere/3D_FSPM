#! /home/renato/anaconda2/bin/ python

from __future__ import print_function, absolute_import, division

import logging
import os
import sys
import time
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df1_iso = pd.read_csv('/home/renato/groimp_efficient/run_1/RWU_60.txt',
                        delim_whitespace=True,skiprows=0,header=None,
                        names=["transpiration"])

df2_iso = pd.read_csv('/home/renato/groimp_efficient/run_2/RWU_60.txt',
                        delim_whitespace=True,skiprows=0,header=None,
                        names=["transpiration"])

df1_iso_beta = pd.read_csv('/home/renato/groimp_efficient/run_1c/RWU_60.txt',
                        delim_whitespace=True,skiprows=0,header=None,
                        names=["transpiration"])

df2_iso_beta = pd.read_csv('/home/renato/groimp_efficient/run_2c/RWU_60.txt',
                        delim_whitespace=True,skiprows=0,header=None,
                        names=["transpiration"])

#df1_mono_beta = pd.read_csv('/home/renato/groimp_efficient/run_1a/RWU_60.txt',
#                        delim_whitespace=True,skiprows=0,header=None,
#                        names=["transpiration"])

df1_mono_beta_a = pd.read_csv('/home/renato/groimp_efficient/run_1a/RWU_1_60.txt',
                        delim_whitespace=True,skiprows=0,header=None,
                        names=["transpiration"])

df1_mono_beta_b = pd.read_csv('/home/renato/groimp_efficient/run_1a/RWU_2_60.txt',
                        delim_whitespace=True,skiprows=0,header=None,
                        names=["transpiration"])

df1_mono_a = pd.read_csv('/home/renato/groimp_efficient/run_1d/RWU_1_60.txt',
                        delim_whitespace=True,skiprows=0,header=None,
                        names=["transpiration"])

df1_mono_b = pd.read_csv('/home/renato/groimp_efficient/run_1d/RWU_2_60.txt',
                        delim_whitespace=True,skiprows=0,header=None,
                        names=["transpiration"])

#df2_mono_beta = pd.read_csv('/home/renato/groimp_efficient/run_2a/RWU_60.txt',
#                        delim_whitespace=True,skiprows=0,header=None,
#                        names=["transpiration"])

df2_mono_beta_a = pd.read_csv('/home/renato/groimp_efficient/run_2a/RWU_1_60.txt',
                        delim_whitespace=True,skiprows=0,header=None,
                        names=["transpiration"])
df2_mono_beta_b = pd.read_csv('/home/renato/groimp_efficient/run_2a/RWU_2_60.txt',
                        delim_whitespace=True,skiprows=0,header=None,
                        names=["transpiration"])

df2_mono_a = pd.read_csv('/home/renato/groimp_efficient/run_2d/RWU_1_60.txt',
                        delim_whitespace=True,skiprows=0,header=None,
                        names=["transpiration"])

df2_mono_b = pd.read_csv('/home/renato/groimp_efficient/run_2d/RWU_2_60.txt',
                        delim_whitespace=True,skiprows=0,header=None,
                        names=["transpiration"])

#df_inter = pd.read_csv('/home/renato/groimp_efficient/run_3/RWU_60.txt',
#                        delim_whitespace=True,skiprows=0,header=None,
#                        names=["transpiration"])


df1_inter = pd.read_csv('/home/renato/groimp_efficient/run_3/RWU_1_60.txt',
                        delim_whitespace=True,skiprows=0,header=None,
                        names=["transpiration"])
df2_inter = pd.read_csv('/home/renato/groimp_efficient/run_3/RWU_2_60.txt',
                        delim_whitespace=True,skiprows=0,header=None,
                        names=["transpiration"])

#df_inter_beta = pd.read_csv('/home/renato/groimp_efficient/run_3c/RWU_60.txt',
#                        delim_whitespace=True,skiprows=0,header=None,
#                        names=["transpiration"])

df1_inter_beta = pd.read_csv('/home/renato/groimp_efficient/run_3c/RWU_1_60.txt',
                        delim_whitespace=True,skiprows=0,header=None,
                        names=["transpiration"])
df2_inter_beta = pd.read_csv('/home/renato/groimp_efficient/run_3c/RWU_2_60.txt',
                        delim_whitespace=True,skiprows=0,header=None,
                        names=["transpiration"])





# ISO    ISO_BETA     MONO     MONO_BETA     INTER    INTER_BETA


# variables ISO_BETA MONOCOT


transp_run1c = df1_iso_beta['transpiration'].values*(1000*24*60*60)

# variables ISO MONOCOT


transp_run1 = df1_iso['transpiration'].values*(1000*24*60*60)

# variables ISO_BETA DICOT


transp_run2c = df2_iso_beta['transpiration'].values*(1000*24*60*60)

# variables ISO DICOT


transp_run2 = df2_iso['transpiration'].values*(1000*24*60*60)
 
# variables MONO_BETA MONOCOT (PLANT A )


transp_run1a_a = df1_mono_beta_a['transpiration'].values*(1000*24*60*60)

# variables MONO_BETA MONOCOT (PLANT B )


transp_run1a_b = df1_mono_beta_b['transpiration'].values*(1000*24*60*60)

# variables MONO MONOCOT (PLANT A )


transp_run1d_a = df1_mono_a['transpiration'].values*(1000*24*60*60)

# variables MONO MONOCOT (PLANT B )


transp_run1d_b = df1_mono_b['transpiration'].values*(1000*24*60*60)

# variables MONO_BETA DICOT (PLANT A )


transp_run2a_a = df2_mono_beta_a['transpiration'].values*(1000*24*60*60)

# variables MONO_BETA DICOT (PLANT B )


transp_run2a_b = df2_mono_beta_b['transpiration'].values*(1000*24*60*60)

# variables MONO DICOT (PLANT A )


transp_run2d_a = df2_mono_a['transpiration'].values*(1000*24*60*60)

# variables MONO DICOT (PLANT B )


transp_run2d_b = df2_mono_b['transpiration'].values*(1000*24*60*60)

# variables INTER MONOCOT


transp_run3_a = df1_inter['transpiration'].values*(1000*24*60*60)

# variables INTER_BETA MONOCOT


transp_run3c_a = df1_inter_beta['transpiration'].values*(1000*24*60*60)


# variables INTER DICOT


transp_run3_b = df2_inter['transpiration'].values*(1000*24*60*60)

# variables INTER_BETA DICOT


transp_run3c_b = df2_inter_beta['transpiration'].values*(1000*24*60*60)


print(transp_run1[59],transp_run1c[59],transp_run1d_a[59],transp_run1a_a[59],
      transp_run3_a[59],transp_run3c_a[59])
print(transp_run2[59],transp_run2c[59],transp_run2d_b[59],transp_run2a_b[59],
      transp_run3_b[59],transp_run3c_b[59])

sys.exit()

plt.plot(transp_run1,'k',label='ISO')
plt.plot(transp_run1c,'k--',label='ISO_beta')
plt.plot(transp_run1d_a,'b',label='MONO (plant A)')
#plt.plot(transp_run1d_b,'g--',label='MONO (plant B)')
plt.plot(transp_run1a_a,'b--',label='MONO_beta (plant A)')
#plt.plot(transp_run1a_b,'b--',label='MONO_beta (plant B)')
plt.plot(transp_run3_a,'r',label='INTER')
plt.plot(transp_run3c_a,'r--',label='INTER_beta')

plt.ylabel("Root water uptake (mm.day-1)", labelpad=20)
plt.xlabel("Time (days)", labelpad=20)
plt.legend()
plt.title('Monocot')
plt.tight_layout()
plt.xlim(0,60.05)
plt.ylim(0.,4.0)
plt.savefig('/home/renato/groimp_efficient/analysis_paper/rwu_monocot.png',dpi=300)
plt.show()
plt.close("all")



plt.plot(transp_run2,'k',label='ISO')
plt.plot(transp_run2c[:-1],'k--',label='ISO_beta')
#plt.plot(transp_run2d_a,'g-.',label='MONO (plant A)')
plt.plot(transp_run2d_b,'b',label='MONO (plant B)')
#plt.plot(transp_run2a_a[:-1],'b-.',label='MONO_beta (plant A)')
plt.plot(transp_run2a_b[:-1],'b--',label='MONO_beta (plant B)')
plt.plot(transp_run3_b[:-1],'r',label='INTER')
plt.plot(transp_run3c_b[:-1],'r--',label='INTER_beta')

plt.ylabel("Root water uptake (mm.day-1)", labelpad=20)
plt.xlabel("Time (days)", labelpad=20)
plt.legend()
plt.title('Dicot')
plt.tight_layout()
plt.xlim(0,60.05)
plt.ylim(0.,4.0)
plt.savefig('/home/renato/groimp_efficient/analysis_paper/rwu_dicot.png',dpi=300)
plt.show()
plt.close("all")



