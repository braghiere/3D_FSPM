#! /home/renato/anaconda2/bin/ python

from __future__ import print_function, absolute_import, division


import os
import sys
import time
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df1_iso = pd.read_csv('/home/renato/groimp_efficient/run_1/plant.txt',
                        delim_whitespace=True,skiprows=1,header=None,
                        names=["time", "tt", "plant", "strip", "row", "pos",
                               "species", "weed","age","nrbranches","leafArea",
                               "fpar","rfr","biom","yield","leafmass","stemmass",
                               "rootmass","shootrootratio","abovebiom",
                               "transpiration"])

df1_iso_beta = pd.read_csv('/home/renato/groimp_efficient/run_1c/plant.txt',
                        delim_whitespace=True,skiprows=1,header=None,
                        names=["time", "tt", "plant", "strip", "row", "pos",
                               "species", "weed","age","nrbranches","leafArea",
                               "fpar","rfr","biom","yield","leafmass","stemmass",
                               "rootmass","shootrootratio","abovebiom",
                               "transpiration"])

df1_mono_beta = pd.read_csv('/home/renato/groimp_efficient/run_1a/plant.txt',
                        delim_whitespace=True,skiprows=1,header=None,
                        names=["time", "tt", "plant", "strip", "row", "pos",
                               "species", "weed","age","nrbranches","leafArea",
                               "fpar","rfr","biom","yield","leafmass","stemmass",
                               "rootmass","shootrootratio","abovebiom",
                               "transpiration"])

df_inter = pd.read_csv('/home/renato/groimp_efficient/run_3/plant.txt',
                        delim_whitespace=True,skiprows=1,header=None,
                        names=["time", "tt", "plant", "strip", "row", "pos",
                               "species", "weed","age","nrbranches","leafArea",
                               "fpar","rfr","biom","yield","leafmass","stemmass",
                               "rootmass","shootrootratio","abovebiom",
                               "transpiration"])

df1_inter = df1.loc[df_inter['plant'] == 1,names=["time", "tt", "plant", "strip", "row", "pos",
                               "species", "weed","age","nrbranches","leafArea",
                               "fpar","rfr","biom","yield","leafmass","stemmass",
                               "rootmass","shootrootratio","abovebiom",
                               "transpiration"]].values

df2_inter = df1.loc[df_inter['plant'] == 2,names=["time", "tt", "plant", "strip", "row", "pos",
                               "species", "weed","age","nrbranches","leafArea",
                               "fpar","rfr","biom","yield","leafmass","stemmass",
                               "rootmass","shootrootratio","abovebiom",
                               "transpiration"]].values

df_inter_beta = pd.read_csv('/home/renato/groimp_efficient/run_3c/plant.txt',
                        delim_whitespace=True,skiprows=1,header=None,
                        names=["time", "tt", "plant", "strip", "row", "pos",
                               "species", "weed","age","nrbranches","leafArea",
                               "fpar","rfr","biom","yield","leafmass","stemmass",
                               "rootmass","shootrootratio","abovebiom",
                               "transpiration"])




