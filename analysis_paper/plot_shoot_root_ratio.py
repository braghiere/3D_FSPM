#! /home/renato/anaconda2/bin/ python

from __future__ import print_function, absolute_import, division

import logging
import os
import sys
import time
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

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
                        delim_whitespace=True,skiprows=0,header=None,
                        names=["time", "tt", "plant", "strip", "row", "pos",
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
                        delim_whitespace=True,skiprows=0,header=None,
                        names=["time", "tt", "plant", "strip", "row", "pos",
                               "species", "weed","age","nrbranches","leafArea",
                               "fpar","rfr","biom","yield","leafmass","stemmass",
                               "rootmass","shootrootratio","abovebiom",
                               "transpiration"])

df2_mono_beta_a = df2_mono_beta.loc[df2_mono_beta['tt'] == 1]
df2_mono_beta_b = df2_mono_beta.loc[df2_mono_beta['tt'] == 2]

df2_mono = pd.read_csv('/home/renato/groimp_efficient/run_2d/plant_60.txt',
                        delim_whitespace=True,skiprows=0,header=None,
                        names=["time", "tt", "plant", "strip", "row", "pos",
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




# ISO    ISO_BETA     MONO     MONO_BETA     INTER    INTER_BETA


# variables ISO_BETA MONOCOT

abovebiomass_run1c = df1_iso_beta['abovebiom'].values/1000
rootbiomass_run1c = df1_iso_beta['rootmass'].values/1000
biom_run1c = df1_iso_beta['biom'].values/1000
leafbiomass_run1c = df1_iso_beta['leafmass'].values/1000
stembiomass_run1c = df1_iso_beta['stemmass'].values/1000
yieldbiomass_run1c = df1_iso_beta['yield'].values/1000
shootroot_run1c = df1_iso_beta['shootrootratio']

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


plt.plot(abovebiomass_run1/rootbiomass_run1,'k',label='ISO')
plt.plot(abovebiomass_run1c/rootbiomass_run1c,'k--',label='ISO_beta')
plt.plot(abovebiomass_run1d_a/rootbiomass_run1d_a,'b',label='MONO (plant A)')
#plt.plot(abovebiomass_run1d_b/rootbiomass_run1d_b,'g--',label='MONO (plant B)')
plt.plot(abovebiomass_run1a_a/rootbiomass_run1a_a,'b--',label='MONO_beta (plant A)')
#plt.plot(abovebiomass_run1a_b/rootbiomass_run1a_b,'b--',label='MONO_beta (plant B)')
plt.plot(abovebiomass_run3_a/rootbiomass_run3_a,'r',label='INTER')
plt.plot(abovebiomass_run3c_a/rootbiomass_run3c_a,'r--',label='INTER_beta')

plt.ylabel("Shoot-root ratio", labelpad=20)
plt.xlabel("Time (days)", labelpad=20)
plt.legend()
plt.title('Monocot')
plt.tight_layout()
plt.xlim(0,60.05)
plt.ylim(0.,5.0)
plt.savefig('/home/renato/groimp_efficient/analysis_paper/shootroot_ratio_monocot.png',dpi=300)
plt.show()
plt.close("all")

plt.plot(abovebiomass_run2/rootbiomass_run2,'k',label='ISO')
plt.plot(abovebiomass_run2c/rootbiomass_run2c,'k--',label='ISO_beta')
#plt.plot(abovebiomass_run2d_a/rootbiomass_run2d_a,'g-.',label='MONO (plant A)')
plt.plot(abovebiomass_run2d_b/rootbiomass_run2d_b,'b',label='MONO (plant B)')
#plt.plot(abovebiomass_run2a_a/rootbiomass_run2a_a,'b-.',label='MONO_beta (plant A)')
plt.plot(abovebiomass_run2a_b/rootbiomass_run2a_b,'b--',label='MONO_beta (plant B)')
plt.plot(abovebiomass_run3_b/rootbiomass_run3_b,'r',label='INTER')
plt.plot(abovebiomass_run3c_b/rootbiomass_run3c_b,'r--',label='INTER_beta')

plt.ylabel("Shoot-root ratio", labelpad=20)
plt.xlabel("Time (days)", labelpad=20)
plt.legend()
plt.title('Dicot')
plt.tight_layout()
plt.xlim(0,60.05)
plt.ylim(0.,11.0)
plt.savefig('/home/renato/groimp_efficient/analysis_paper/shootroot_ratio_dicot.png',dpi=300)
plt.show()
plt.close("all")



