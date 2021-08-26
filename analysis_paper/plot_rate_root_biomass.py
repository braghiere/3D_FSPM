#! /home/renato/anaconda2/bin/ python

from __future__ import print_function, absolute_import, division

import logging
import os
import sys
import time
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.interpolate import spline

def smooth(y, box_pts):
    box = np.ones(box_pts)/box_pts
    y_smooth = np.convolve(y, box, mode='same')
    return y_smooth

df1_iso = pd.read_csv('/home/renato/groimp_efficient/run_1/plant_60.txt',
                        delim_whitespace=True,skiprows=0,header=None,
                        names=["time", "tt", "plant", "strip", "row", "pos",
                               "species", "weed","age","nrbranches","leafArea",
                               "fpar","rfr","biom","yield","leafmass","stemmass",
                               "rootmass","shootrootratio","abovebiom",
                               "transpiration"])


df2_iso = pd.read_csv('/home/renato/groimp_efficient/run_2/plant_60.txt',
                        delim_whitespace=True,skiprows=0,header=None,
                        names=["time", "tt", "plant", "strip", "row", "pos",
                               "species", "weed","age","nrbranches","leafArea",
                               "fpar","rfr","biom","yield","leafmass","stemmass",
                               "rootmass","shootrootratio","abovebiom",
                               "transpiration"])

df1_iso_beta = pd.read_csv('/home/renato/groimp_efficient/run_1c/plant_60.txt',
                        delim_whitespace=True,skiprows=0,header=None,
                        names=["time", "tt", "plant", "strip", "row", "pos",
                               "species", "weed","age","nrbranches","leafArea",
                               "fpar","rfr","biom","yield","leafmass","stemmass",
                               "rootmass","shootrootratio","abovebiom",
                               "transpiration"])

df2_iso_beta = pd.read_csv('/home/renato/groimp_efficient/run_2c/plant_60.txt',
                        delim_whitespace=True,skiprows=0,header=None,
                        names=["time", "tt", "plant", "strip", "row", "pos",
                               "species", "weed","age","nrbranches","leafArea",
                               "fpar","rfr","biom","yield","leafmass","stemmass",
                               "rootmass","shootrootratio","abovebiom",
                               "transpiration"])

df1_mono_beta = pd.read_csv('/home/renato/groimp_efficient/run_1a/plant_60.txt',
                        delim_whitespace=True,skiprows=0,header=None,index_col=False,
                        names=["time","tt", "plant", "strip", "row", "pos",
                               "species", "weed","age","nrbranches","leafArea",
                               "fpar","rfr","biom","yield","leafmass","stemmass",
                               "rootmass","shootrootratio","abovebiom",
                               "transpiration"])

df1_mono_beta_a = df1_mono_beta.loc[df1_mono_beta['tt'] == 1]
df1_mono_beta_b = df1_mono_beta.loc[df1_mono_beta['tt'] == 2]

df1_mono = pd.read_csv('/home/renato/groimp_efficient/run_1d/plant_60.txt',
                        delim_whitespace=True,skiprows=0,header=None,
                        names=["time", "tt", "plant", "strip", "row", "pos",
                               "species", "weed","age","nrbranches","leafArea",
                               "fpar","rfr","biom","yield","leafmass","stemmass",
                               "rootmass","shootrootratio","abovebiom",
                               "transpiration"])



df1_mono_a = df1_mono.loc[df1_mono['tt'] == 1]
df1_mono_b = df1_mono.loc[df1_mono['tt'] == 2]


df2_mono_beta = pd.read_csv('/home/renato/groimp_efficient/run_2a/plant_60.txt',
                        delim_whitespace=True,skiprows=0,header=None,index_col=0,
                        names=["time","tt", "plant", "strip", "row", "pos",
                               "species", "weed","age","nrbranches","leafArea",
                               "fpar","rfr","biom","yield","leafmass","stemmass",
                               "rootmass","shootrootratio","abovebiom",
                               "transpiration"])

df2_mono_beta_a = df2_mono_beta.loc[df2_mono_beta['tt'] == 1]
df2_mono_beta_b = df2_mono_beta.loc[df2_mono_beta['tt'] == 2]



df2_mono = pd.read_csv('/home/renato/groimp_efficient/run_2d/plant_60.txt',
                        delim_whitespace=True,skiprows=0,header=None,
                        names=["time","tt", "plant", "strip", "row", "pos",
                               "species", "weed","age","nrbranches","leafArea",
                               "fpar","rfr","biom","yield","leafmass","stemmass",
                               "rootmass","shootrootratio","abovebiom",
                               "transpiration"])

df2_mono_a = df2_mono.loc[df2_mono['tt'] == 1]
df2_mono_b = df2_mono.loc[df2_mono['tt'] == 2]

df_inter = pd.read_csv('/home/renato/groimp_efficient/run_3/plant_60.txt',
                        delim_whitespace=True,skiprows=0,header=None,
                        names=["time", "tt", "plant", "strip", "row", "pos",
                               "species", "weed","age","nrbranches","leafArea",
                               "fpar","rfr","biom","yield","leafmass","stemmass",
                               "rootmass","shootrootratio","abovebiom",
                               "transpiration"])


df1_inter = df_inter.loc[df_inter['plant'] == 1]
df2_inter = df_inter.loc[df_inter['plant'] == 2]

df_inter_beta = pd.read_csv('/home/renato/groimp_efficient/run_3c/plant_60.txt',
                        delim_whitespace=True,skiprows=0,header=None,
                        names=["time", "tt", "plant", "strip", "row", "pos",
                               "species", "weed","age","nrbranches","leafArea",
                               "fpar","rfr","biom","yield","leafmass","stemmass",
                               "rootmass","shootrootratio","abovebiom",
                               "transpiration"])

df1_inter_beta = df_inter_beta.loc[df_inter_beta['plant'] == 1]
df2_inter_beta = df_inter_beta.loc[df_inter_beta['plant'] == 2]


print(df_inter)
print(df1_mono)


# ISO    ISO_BETA     MONO     MONO_BETA     INTER    INTER_BETA

# variables ISO_BETA MONOCOT

abovebiomass_run1c = df1_iso_beta['abovebiom'].values/1000
rootbiomass_run1c = df1_iso_beta['rootmass'].values/1000
biom_run1c = df1_iso_beta['biom'].values/1000
leafbiomass_run1c = df1_iso_beta['leafmass'].values/1000
stembiomass_run1c = df1_iso_beta['stemmass'].values/1000
yieldbiomass_run1c = df1_iso_beta['yield'].values/1000

# variables ISO MONOCOT

abovebiomass_run1 = df1_iso['abovebiom'].values/1000
rootbiomass_run1 = df1_iso['rootmass'].values/1000
biom_run1 = df1_iso['biom'].values/1000
leafbiomass_run1 = df1_iso['leafmass'].values/1000
stembiomass_run1 = df1_iso['stemmass'].values/1000
yieldbiomass_run1 = df1_iso['yield'].values/1000

# variables ISO_BETA DICOT

abovebiomass_run2c = df2_iso_beta['abovebiom'].values/1000
rootbiomass_run2c = df2_iso_beta['rootmass'].values/1000
biom_run2c = df2_iso_beta['biom'].values/1000
leafbiomass_run2c = df2_iso_beta['leafmass'].values/1000
stembiomass_run2c = df2_iso_beta['stemmass'].values/1000
yieldbiomass_run2c = df2_iso_beta['yield'].values/1000

# variables ISO DICOT

abovebiomass_run2 = df2_iso['abovebiom'].values/1000
rootbiomass_run2 = df2_iso['rootmass'].values/1000
biom_run2 = df2_iso['biom'].values/1000
leafbiomass_run2 = df2_iso['leafmass'].values/1000
stembiomass_run2 = df2_iso['stemmass'].values/1000
yieldbiomass_run2 = df2_iso['yield'].values/1000
 
# variables MONO_BETA MONOCOT (PLANT A )

abovebiomass_run1a_a = df1_mono_beta_a['abovebiom'].values/1000
rootbiomass_run1a_a = df1_mono_beta_a['rootmass'].values/1000
biom_run1a_a = df1_mono_beta_a['biom'].values/1000
leafbiomass_run1a_a = df1_mono_beta_a['leafmass'].values/1000
stembiomass_run1a_a = df1_mono_beta_a['stemmass'].values/1000
yieldbiomass_run1a_a = df1_mono_beta_a['yield'].values/1000

# variables MONO_BETA MONOCOT (PLANT B )

abovebiomass_run1a_b = df1_mono_beta_b['abovebiom'].values/1000
rootbiomass_run1a_b = df1_mono_beta_b['rootmass'].values/1000
biom_run1a_b = df1_mono_beta_b['biom'].values/1000
leafbiomass_run1a_b = df1_mono_beta_b['leafmass'].values/1000
stembiomass_run1a_b = df1_mono_beta_b['stemmass'].values/1000
yieldbiomass_run1a_b = df1_mono_beta_b['yield'].values/1000

# variables MONO MONOCOT (PLANT A )

abovebiomass_run1d_a = df1_mono_a['abovebiom'].values/1000
rootbiomass_run1d_a = df1_mono_a['rootmass'].values/1000
biom_run1d_a = df1_mono_a['biom'].values/1000
leafbiomass_run1d_a = df1_mono_a['leafmass'].values/1000
stembiomass_run1d_a = df1_mono_a['stemmass'].values/1000
yieldbiomass_run1d_a = df1_mono_a['yield'].values/1000

# variables MONO MONOCOT (PLANT B )

abovebiomass_run1d_b = df1_mono_b['abovebiom'].values/1000
rootbiomass_run1d_b = df1_mono_b['rootmass'].values/1000
biom_run1d_b = df1_mono_b['biom'].values/1000
leafbiomass_run1d_b = df1_mono_b['leafmass'].values/1000
stembiomass_run1d_b = df1_mono_b['stemmass'].values/1000
yieldbiomass_run1d_b = df1_mono_b['yield'].values/1000

# variables MONO_BETA DICOT (PLANT A )

abovebiomass_run2a_a = df2_mono_beta_a['abovebiom'].values/1000
rootbiomass_run2a_a = df2_mono_beta_a['rootmass'].values/1000
biom_run2a_a = df2_mono_beta_a['biom'].values/1000
leafbiomass_run2a_a = df2_mono_beta_a['leafmass'].values/1000
stembiomass_run2a_a = df2_mono_beta_a['stemmass'].values/1000
yieldbiomass_run2a_a = df2_mono_beta_a['yield'].values/1000

# variables MONO_BETA DICOT (PLANT B )

abovebiomass_run2a_b = df2_mono_beta_b['abovebiom'].values/1000
rootbiomass_run2a_b = df2_mono_beta_b['rootmass'].values/1000
biom_run2a_b = df2_mono_beta_b['biom'].values/1000
leafbiomass_run2a_b = df2_mono_beta_b['leafmass'].values/1000
stembiomass_run2a_b = df2_mono_beta_b['stemmass'].values/1000
yieldbiomass_run2a_b = df2_mono_beta_b['yield'].values/1000

# variables MONO DICOT (PLANT A )

abovebiomass_run2d_a = df2_mono_a['abovebiom'].values/1000
rootbiomass_run2d_a = df2_mono_a['rootmass'].values/1000
biom_run2d_a = df2_mono_a['biom'].values/1000
leafbiomass_run2d_a = df2_mono_a['leafmass'].values/1000
stembiomass_run2d_a = df2_mono_a['stemmass'].values/1000
yieldbiomass_run2d_a = df2_mono_a['yield'].values/1000
transp_run2d_a = df2_mono_a['transpiration'].values*(1000*24*60*60)

# variables MONO DICOT (PLANT B )

abovebiomass_run2d_b = df2_mono_b['abovebiom'].values/1000
rootbiomass_run2d_b = df2_mono_b['rootmass'].values/1000
biom_run2d_b = df2_mono_b['biom'].values/1000
leafbiomass_run2d_b = df2_mono_b['leafmass'].values/1000
stembiomass_run2d_b = df2_mono_b['stemmass'].values/1000
yieldbiomass_run2d_b = df2_mono_b['yield'].values/1000
transp_run2d_b = df2_mono_b['transpiration'].values*(1000*24*60*60)

# variables INTER MONOCOT

abovebiomass_run3_a = df1_inter['abovebiom'].values/1000
rootbiomass_run3_a = df1_inter['rootmass'].values/1000
biom_run3_a = df1_inter['biom'].values/1000
leafbiomass_run3_a = df1_inter['leafmass'].values/1000
stembiomass_run3_a = df1_inter['stemmass'].values/1000
yieldbiomass_run3_a = df1_inter['yield'].values/1000

# variables INTER_BETA MONOCOT

abovebiomass_run3c_a= df1_inter_beta['abovebiom'].values/1000
rootbiomass_run3c_a = df1_inter_beta['rootmass'].values/1000
biom_run3c_a = df1_inter_beta['biom'].values/1000
leafbiomass_run3c_a = df1_inter_beta['leafmass'].values/1000
stembiomass_run3c_a = df1_inter_beta['stemmass'].values/1000
yieldbiomass_run3c_a = df1_inter_beta['yield'].values/1000


# variables INTER DICOT

abovebiomass_run3_b = df2_inter['abovebiom'].values/1000
rootbiomass_run3_b = df2_inter['rootmass'].values/1000
biom_run3_b = df2_inter['biom'].values/1000
leafbiomass_run3_b = df2_inter['leafmass'].values/1000
stembiomass_run3_b = df2_inter['stemmass'].values/1000
yieldbiomass_run3_b = df2_inter['yield'].values/1000

# variables INTER_BETA DICOT

abovebiomass_run3c_b= df2_inter_beta['abovebiom'].values/1000
rootbiomass_run3c_b = df2_inter_beta['rootmass'].values/1000
biom_run3c_b = df2_inter_beta['biom'].values/1000
leafbiomass_run3c_b = df2_inter_beta['leafmass'].values/1000
stembiomass_run3c_b = df2_inter_beta['stemmass'].values/1000
yieldbiomass_run3c_b = df2_inter_beta['yield'].values/1000


rate_rootbiomass_run1=[]
rate_rootbiomass_run1c=[]
rate_rootbiomass_run1a_a=[]
rate_rootbiomass_run1a_b=[]
rate_rootbiomass_run1d_a=[]
rate_rootbiomass_run1d_b=[]
rate_rootbiomass_run3_a=[]
rate_rootbiomass_run3c_a=[]

print(df1_iso['time'].values[0],df1_mono['time'].values[0],df1_mono_beta['time'].values[0])

for i in range(0,len(rootbiomass_run1c)):

   rate_rootbiomass_run1.append(rootbiomass_run1[i]-rootbiomass_run1[i-1])
   rate_rootbiomass_run1c.append(rootbiomass_run1c[i]-rootbiomass_run1c[i-1])
   rate_rootbiomass_run1a_a.append(rootbiomass_run1a_a[i]-rootbiomass_run1a_a[i-1])
   rate_rootbiomass_run1a_b.append(rootbiomass_run1a_b[i]-rootbiomass_run1a_b[i-1])
   rate_rootbiomass_run1d_a.append(rootbiomass_run1d_a[i]-rootbiomass_run1d_a[i-1])
   rate_rootbiomass_run1d_b.append(rootbiomass_run1d_b[i]-rootbiomass_run1d_b[i-1])
   rate_rootbiomass_run3_a.append(rootbiomass_run3_a[i]-rootbiomass_run3_a[i-1])
   rate_rootbiomass_run3c_a.append(rootbiomass_run3c_a[i]-rootbiomass_run3c_a[i-1])

rate_rootbiomass_run2=[]
rate_rootbiomass_run2c=[]
rate_rootbiomass_run2a_a=[]
rate_rootbiomass_run2a_b=[]
rate_rootbiomass_run2d_a=[]
rate_rootbiomass_run2d_b=[]
rate_rootbiomass_run3_b=[]
rate_rootbiomass_run3c_b=[]

for i in range(0,len(rootbiomass_run2c)):

   rate_rootbiomass_run2.append(rootbiomass_run2[i]-rootbiomass_run2[i-1])
   rate_rootbiomass_run2c.append(rootbiomass_run2c[i]-rootbiomass_run2c[i-1])
   rate_rootbiomass_run2a_a.append(rootbiomass_run2a_a[i]-rootbiomass_run2a_a[i-1])
   rate_rootbiomass_run2a_b.append(rootbiomass_run2a_b[i]-rootbiomass_run2a_b[i-1])
   rate_rootbiomass_run2d_a.append(rootbiomass_run2d_a[i]-rootbiomass_run2d_a[i-1])
   rate_rootbiomass_run2d_b.append(rootbiomass_run2d_b[i]-rootbiomass_run2d_b[i-1])
   rate_rootbiomass_run3_b.append(rootbiomass_run3_b[i]-rootbiomass_run3_b[i-1])
   rate_rootbiomass_run3c_b.append(rootbiomass_run3c_b[i]-rootbiomass_run3c_b[i-1])



plt.plot(rate_rootbiomass_run1,'k',label='ISO')
plt.plot(rate_rootbiomass_run1c,'k--',label='ISO_beta')
plt.plot(rate_rootbiomass_run1d_a,'b',label='MONO (plant A)')
#plt.plot(rate_rootbiomass_run1d_b,'g--',label='MONO (plant B)')
plt.plot(rate_rootbiomass_run1a_a,'b--',label='MONO_beta (plant A)')
#plt.plot(rate_rootbiomass_run1a_b,'b--',label='MONO_beta (plant B)')
plt.plot(rate_rootbiomass_run3_a,'r',label='INTER')
plt.plot(rate_rootbiomass_run3c_a,'r--',label='INTER_beta')

plt.ylabel("Root biomass production (g.day-1)", labelpad=20)
plt.xlabel("Time (days)", labelpad=20)
plt.legend()
plt.title('Monocot')
plt.tight_layout()
plt.xlim(0,60.05)
plt.ylim(0.,0.07)
plt.savefig('/home/renato/groimp_efficient/analysis_paper/production_root_biomass_monocot.png',dpi=300)
plt.show()
plt.close("all")


plt.plot(rate_rootbiomass_run2,'k',label='ISO')
plt.plot(rate_rootbiomass_run2c,'k--',label='ISO_beta')
#plt.plot(rate_rootbiomass_run2d_a,'g-.',label='MONO (plant A)')
plt.plot(rate_rootbiomass_run2d_b,'b',label='MONO (plant B)')
#plt.plot(rate_rootbiomass_run2a_a,'b-.',label='MONO_beta (plant A)')
plt.plot(rate_rootbiomass_run2a_b,'b--',label='MONO_beta (plant B)')
plt.plot(rate_rootbiomass_run3_b,'r',label='INTER')
plt.plot(rate_rootbiomass_run3c_b,'r--',label='INTER_beta')

plt.ylabel("Root biomass production (g.day-1)", labelpad=20)
plt.xlabel("Time (days)", labelpad=20)
plt.legend()
plt.title('Dicot')
plt.tight_layout()
plt.xlim(0,60.05)
plt.ylim(0.,0.07)
plt.savefig('/home/renato/groimp_efficient/analysis_paper/production_root_biomass_dicot.png',dpi=300)
plt.show()
plt.close("all")


#Statistics

x = np.linspace(1,60,60)
xnew = np.linspace(1,60,12) #300 represents number of points to make between T.min and T.max

y1 = np.nan_to_num(np.array(rate_rootbiomass_run1c)/np.array(rate_rootbiomass_run1))*100.
y2 = np.nan_to_num(np.array(rate_rootbiomass_run1a_a)/np.array(rate_rootbiomass_run1d_a))*100.
y3 = np.nan_to_num(np.array(rate_rootbiomass_run3c_a)/np.array(rate_rootbiomass_run3_a))*100.


#power_smooth1 = spline(x,y1,xnew)
#power_smooth2 = smooth(y1,45)
power_smooth1 = np.poly1d(np.polyfit(x, y1, 2))
power_smooth2 = np.poly1d(np.polyfit(x, y2, 3))
power_smooth3 = np.poly1d(np.polyfit(x, y3, 3))

plt.plot(x,(np.array(rate_rootbiomass_run1c)/np.array(rate_rootbiomass_run1))*100.,c='k',label='ISO_beta/ISO')
#plt.plot(xnew,power_smooth1,'k',label='ISO_beta/ISO')
#plt.plot(x,power_smooth2,'k--',label='ISO_beta/ISO')
#plt.plot(x,power_smooth1(x),'k',label='ISO_beta/ISO')

plt.plot(x,(np.array(rate_rootbiomass_run1a_a)/np.array(rate_rootbiomass_run1d_a))*100.,c='b',label='MONO_beta/MONO')
#plt.plot(x,power_smooth2(x),'b',label='MONO_beta/MONO')

plt.plot(x,(np.array(rate_rootbiomass_run3c_a)/np.array(rate_rootbiomass_run3_a))*100.,c='r',label='INTER_beta/INTER')
#plt.plot(x,power_smooth3(x),'r',label='INTER_beta/INTER')

plt.ylabel("Root biomass production (BETA)/  \n Root biomass production (Default) (%)", labelpad=10)
plt.xlabel("Time (days)", labelpad=20)
plt.legend()
plt.grid()
plt.title('BETA IMPACT - MONOCOT')
plt.tight_layout()
plt.xlim(0,60.05)
plt.ylim(0.,105.)
plt.savefig('/home/renato/groimp_efficient/analysis_paper/beta_difference_production_root_biomass_monocot.png',dpi=300)
plt.show()
plt.close("all")

plt.plot(x,(np.array(rate_rootbiomass_run2c)/np.array(rate_rootbiomass_run2))*100.,c='k',label='ISO_beta/ISO')
#plt.plot(xnew,power_smooth1,'k',label='ISO_beta/ISO')
#plt.plot(x,power_smooth2,'k--',label='ISO_beta/ISO')
#plt.plot(x,power_smooth1(x),'k',label='ISO_beta/ISO')

plt.plot(x,(np.array(rate_rootbiomass_run2a_b)/np.array(rate_rootbiomass_run2d_b))*100.,c='b',label='MONO_beta/MONO')
#plt.plot(x,power_smooth2(x),'b',label='MONO_beta/MONO')

plt.plot(x,(np.array(rate_rootbiomass_run3c_b)/np.array(rate_rootbiomass_run3_b))*100.,c='r',label='INTER_beta/INTER')
#plt.plot(x,power_smooth3(x),'r',label='INTER_beta/INTER')

plt.ylabel("Root biomass production (BETA)/  \n Root biomass production (Default) (%)", labelpad=10)
plt.xlabel("Time (days)", labelpad=20)
plt.legend()
plt.grid()
plt.title('BETA IMPACT - DICOT')
plt.tight_layout()
plt.xlim(0,60.05)
plt.ylim(0.,105.)
plt.savefig('/home/renato/groimp_efficient/analysis_paper/beta_difference_production_root_biomass_dicot.png',dpi=300)
plt.show()
plt.close("all")

