# libraries and data
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import sys, os
 
file_name_plant = 'plant_{}.txt'
file_name_field = 'field_{}.txt'

file_name_plant_clm = 'plant_clm_{}.txt'
file_name_field_clm = 'field_clm_{}.txt'

file_name_plant_gday = 'plant_gday_{}.txt'
file_name_field_gday = 'field_gday_{}.txt'


df1 = pd.concat([pd.read_csv(file_name_plant.format(i),sep='\t', names=["time", "tt", "plant", "strip", "row", "pos", "species", "weed",
              "age","nrbranches","leafArea","fpar","rfr","biom","yields","leafmass",
               "stemmass", "rootmass","shootrootratio","abovebiom","transpiration"]) for i in range(1, 21)])

df2 = pd.concat([pd.read_csv(file_name_field.format(i),sep='\t', names=["time", "species", "LAI", "nrShoots", "fAbs", "assCO2", "biomAbove", "yield", "harvestIndex","leafArea","fieldRFR"]) for i in range(1, 21)])

df3 = pd.concat([pd.read_csv(file_name_plant_clm.format(i),sep='\t', names=["time", "tt", "plant", "strip", "row", "pos", "species", "weed",
              "age","nrbranches","leafArea","fpar","rfr","biom","yields","leafmass",
               "stemmass", "rootmass","shootrootratio","abovebiom","transpiration"]) for i in range(1, 21)])

df4 = pd.concat([pd.read_csv(file_name_field_clm.format(i),sep='\t', names=["time", "species", "LAI", "nrShoots", "fAbs", "assCO2", "biomAbove", "yield", "harvestIndex","leafArea","fieldRFR"]) for i in range(1, 21)])

df5 = pd.concat([pd.read_csv(file_name_plant_gday.format(i),sep='\t', names=["time", "tt", "plant", "strip", "row", "pos", "species", "weed",
              "age","nrbranches","leafArea","fpar","rfr","biom","yields","leafmass",
               "stemmass", "rootmass","shootrootratio","abovebiom","transpiration"]) for i in range(1, 21)])

df6 = pd.concat([pd.read_csv(file_name_field_gday.format(i),sep='\t', names=["time", "species", "LAI", "nrShoots", "fAbs", "assCO2", "biomAbove", "yield", "harvestIndex","leafArea","fieldRFR"]) for i in range(1, 21)])



# Initialize the figure
plt.style.use('seaborn-darkgrid')

#plt.plot(df1['age'], df1['transpiration'], marker='', color='grey', linewidth=0.6, alpha=0.3)
plt.show()

df_early = df1.loc[df1['age'] == 30]
df_heading = df1.loc[df1['age'] == 45]
df_dough = df1.loc[df1['age'] == 60]
df_hard = df1.loc[df1['age'] == 75]

print df_early['time'],df_heading['time'],df_dough['time'],df_hard['time']

df2_early = df2.loc[df2['time'] == 31]
df2_heading = df2.loc[df2['time'] == 46]
df2_dough = df2.loc[df2['time'] == 61]
df2_hard = df2.loc[df2['time'] == 76]

print df2_early['time']



df3_early = df3.loc[df3['age'] == 30]
df3_heading = df3.loc[df3['age'] == 45]
df3_dough = df3.loc[df3['age'] == 60]
df3_hard = df3.loc[df3['age'] == 75]


df4_early = df4.loc[df4['time'] == 31]
df4_heading = df4.loc[df4['time'] == 46]
df4_dough = df4.loc[df4['time'] == 61]
df4_hard = df4.loc[df4['time'] == 76]


df5_early = df5.loc[df5['age'] == 30]
df5_heading = df5.loc[df5['age'] == 45]
df5_dough = df5.loc[df5['age'] == 60]
df5_hard = df5.loc[df5['age'] == 75]


df6_early = df6.loc[df6['time'] == 31]
df6_heading = df6.loc[df6['time'] == 46]
df6_dough = df6.loc[df6['time'] == 61]
df6_hard = df6.loc[df6['time'] == 76]




areaplant = df1.leafArea.values
areaplant = np.array(areaplant)

areafield = 2*2

areaplant = df_early['leafArea'].values
areaplant = np.array(areaplant)
transp = df_early['transpiration'].values
transp = np.array(transp)
y1 = transp*(10e2*60*60*24*areaplant/2.54)/areafield

areaplant = df_heading['leafArea'].values
areaplant = np.array(areaplant)
transp = df_heading['transpiration'].values
transp = np.array(transp)
y2 = transp*(10e2*60*60*24*areaplant/2.54)/areafield

areaplant = df_dough['leafArea'].values
areaplant = np.array(areaplant)
transp = df_dough['transpiration'].values
transp = np.array(transp)
y3 = transp*(10e2*60*60*24*areaplant/2.54)/areafield

areaplant = df_hard['leafArea'].values
areaplant = np.array(areaplant)
transp = df_hard['transpiration'].values
transp = np.array(transp)
y4 = transp*(10e2*60*60*24*areaplant/2.54)/areafield

x = np.arange(20)/20. + 0.05


transp = df2_early['assCO2'].values
transp = np.array(transp)
y1 = transp/(60*60*24)


transp = df2_heading['assCO2'].values
transp = np.array(transp)
y2 = transp/(60*60*24)


transp = df2_dough['assCO2'].values
transp = np.array(transp)
y3 = transp/(60*60*24)


transp = df2_hard['assCO2'].values
transp = np.array(transp)
y4 = transp/(60*60*24)



transp = df_early['rootmass'].values
transp = np.array(transp)
y1 = transp


transp = df_heading['rootmass'].values
transp = np.array(transp)
y2 = transp


transp = df_dough['rootmass'].values
transp = np.array(transp)
y3 = transp

transp = df3_dough['rootmass'].values
transp = np.array(transp)
y3clm = transp

transp = df5_dough['rootmass'].values
transp = np.array(transp)
y3gday = transp


transp = df_hard['rootmass'].values
transp = np.array(transp)
y4 = transp

transp = df3_hard['rootmass'].values
transp = np.array(transp)
y4clm = transp

transp = df5_hard['rootmass'].values
transp = np.array(transp)
y4gday = transp

# create a color palette
palette = plt.get_cmap('Set1')


#plt.plot(x,y1, marker='', color=palette(1), linewidth=2.4, alpha=0.3, label='Early boot')
#plt.plot(x,y2, marker='', color=palette(2), linewidth=2.4, alpha=0.3, label='Heading')
plt.plot(x,y3, marker='_', color=palette(3), linewidth=2.4, alpha=0.3, label='A$_{n}$')
plt.plot(x,y3clm, marker='x', color=palette(3), linewidth=2.4, alpha=0.3, label='CLM')
plt.plot(x,y3gday, marker='.', color=palette(3), linewidth=2.4, alpha=0.3, label='GDAY')

#plt.plot(x,y4, marker='', color=palette(4), linewidth=2.4, alpha=0.3, label='Hard dough (JULES)')
#plt.plot(x,y4clm, marker='x', color=palette(4), linewidth=2.4, alpha=0.3, label='CLM')
#plt.plot(x,y4gday, marker='.', color=palette(4), linewidth=2.4, alpha=0.3, label='GDAY')
plt.xlim(0,1)
plt.xlabel('Beta')
#plt.ylabel('Transpiration (inches.day$^{-1}$)')
#plt.ylabel(r'CO$_{2}$ Assimilation ($\mu$mol CO$_{2}$.m$^{-2}$.s$^{-1}$)')
plt.ylabel(r'Root biomass (mg)')
plt.title(r'Stage: Dough (day 60)')
#plt.ylabel(r'Yield (mg)')
plt.legend()

#plt.savefig('rootbiom_beta_4stages_resp.png')
plt.show()


sys.exit()



 
# create a color palette
palette = plt.get_cmap('Set1')
 
# multiple line plot
num=0
for column in df1.drop('time', axis=1):
    num+=1
 
    # Find the right spot on the plot
    plt.subplot(2,2, num)
 
    # plot every groups, but discreet
    for v in df1.drop('time', axis=1):
        plt.plot(df1['time'], df1[v], marker='', color='grey', linewidth=0.6, alpha=0.3)
 
    # Plot the lineplot
    plt.plot(df1['time'], df1[column], marker='', color=palette(num), linewidth=2.4, alpha=0.9, label=column)
 
    # Same limits for everybody!
    plt.xlim(0,10)
    plt.ylim(-2,22)
 
    # Not ticks everywhere
    if num in range(7) :
        plt.tick_params(labelbottom='off')
    if num not in [1,4,7] :
        plt.tick_params(labelleft='off')
 
    # Add title
    plt.title(column, loc='left', fontsize=12, fontweight=0, color=palette(num) )
 
# general title
plt.suptitle("How the 9 students improved\nthese past few days?", fontsize=13, fontweight=0, color='black', style='italic', y=1.02)
 
# Axis title
plt.text(0.5, 0.02, 'Time', ha='center', va='center')
plt.text(0.06, 0.5, 'Note', ha='center', va='center', rotation='vertical')

plt.show()
