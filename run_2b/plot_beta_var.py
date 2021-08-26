# libraries and data
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import sys, os
 
file_name_plant_jules = 'jules/plant_jules_{}.txt'
file_name_field_jules = 'jules/field_jules_{}.txt'

file_name_plant_clm = 'clm/plant_clm_{}.txt'
file_name_field_clm = 'clm/field_clm_{}.txt'

file_name_plant_gday = 'gday/plant_gday_{}.txt'
file_name_field_gday = 'gday/field_gday_{}.txt'


df1 = pd.concat([pd.read_csv(file_name_plant_jules.format(i),sep='\t', names=["time", 
              "tt", "plant", "strip", "row", "pos", "species", "weed",
              "age","nrbranches","leafArea","fpar","rfr","biom","yields","leafmass",
               "stemmass", "rootmass","shootrootratio","abovebiom","transpiration"]) 
               for i in range(0, 101)])

df2 = pd.concat([pd.read_csv(file_name_field_jules.format(i),sep='\t', names=["time", 
          "species", "LAI", "nrShoots", "fAbs", "assCO2", "biomAbove", "yield", 
          "harvestIndex","leafArea","fieldRFR"]) for i in range(0, 101)])

df3 = pd.concat([pd.read_csv(file_name_plant_clm.format(i),sep='\t', names=["time", "tt", "plant", "strip", "row", "pos", "species", "weed",
              "age","nrbranches","leafArea","fpar","rfr","biom","yields","leafmass",
               "stemmass", "rootmass","shootrootratio","abovebiom","transpiration"]) for i in range(0, 101)])

df4 = pd.concat([pd.read_csv(file_name_field_clm.format(i),sep='\t', names=["time", "species", "LAI", "nrShoots", "fAbs", "assCO2", "biomAbove", "yield", "harvestIndex","leafArea","fieldRFR"]) for i in range(0, 101)])

df5 = pd.concat([pd.read_csv(file_name_plant_gday.format(i),sep='\t', names=["time", "tt", "plant", "strip", "row", "pos", "species", "weed",
              "age","nrbranches","leafArea","fpar","rfr","biom","yields","leafmass",
               "stemmass", "rootmass","shootrootratio","abovebiom","transpiration"]) for i in range(0, 101)])

df6 = pd.concat([pd.read_csv(file_name_field_gday.format(i),sep='\t', names=["time", "species", "LAI", "nrShoots", "fAbs", "assCO2", "biomAbove", "yield", "harvestIndex","leafArea","fieldRFR"]) for i in range(0, 101)])



# Initialize the figure
# plt.style.use('seaborn-darkgrid')

#plt.plot(df1['age'], df1['transpiration'], marker='', color='grey', linewidth=0.6, alpha=0.3)
#plt.show()

df1_early = df1.loc[df1['age'] == 30]
df1_heading = df1.loc[df1['age'] == 45]
df1_dough = df1.loc[df1['age'] == 59]
df1_hard = df1.loc[df1['age'] == 75]

#print df_early['time'],df_heading['time'],df_dough['time'],df_hard['time']

df2_early = df2.loc[df2['time'] == 31]
df2_heading = df2.loc[df2['time'] == 46]
df2_dough = df2.loc[df2['time'] == 59]
df2_hard = df2.loc[df2['time'] == 76]

#print df2_early['time']



df3_early = df3.loc[df3['age'] == 30]
df3_heading = df3.loc[df3['age'] == 45]
df3_dough = df3.loc[df3['age'] == 59]
df3_hard = df3.loc[df3['age'] == 75]


df4_early = df4.loc[df4['time'] == 31]
df4_heading = df4.loc[df4['time'] == 46]
df4_dough = df4.loc[df4['time'] == 59]
df4_hard = df4.loc[df4['time'] == 76]


df5_early = df5.loc[df5['age'] == 30]
df5_heading = df5.loc[df5['age'] == 45]
df5_dough = df5.loc[df5['age'] == 59]
df5_hard = df5.loc[df5['age'] == 75]


df6_early = df6.loc[df6['time'] == 31]
df6_heading = df6.loc[df6['time'] == 46]
df6_dough = df6.loc[df6['time'] == 59]
df6_hard = df6.loc[df6['time'] == 76]


areaplant = df1.leafArea.values
areaplant = np.array(areaplant)

areafield = 1*1

areaplant = df1_early['leafArea'].values
areaplant = np.array(areaplant)
transp = df1_early['transpiration'].values
transp = np.array(transp)
y1 = transp*(10e2*60*60*24*areaplant/2.54)/areafield

areaplant = df1_heading['leafArea'].values
areaplant = np.array(areaplant)
transp = df1_heading['transpiration'].values
transp = np.array(transp)
y2 = transp*(10e2*60*60*24*areaplant/2.54)/areafield

areaplant = df1_dough['leafArea'].values
areaplant = np.array(areaplant)
transp = df1_dough['transpiration'].values
transp = np.array(transp)
y3 = transp*(10e2*60*60*24*areaplant/2.54)/areafield

#print y1,y2,y3
#sys.exit()

areaplant = df1_hard['leafArea'].values
areaplant = np.array(areaplant)

transp = df1_hard['transpiration'].values
transp = np.array(transp)
y4 = transp*(10e2*60*60*24*areaplant/2.54)/areafield

#x = np.arange(101)/101. + 0.05
x = np.arange(101)/101. 

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



transp = df1_early['rootmass'].values
transp = np.array(transp)
y1 = transp


transp = df1_heading['rootmass'].values
transp = np.array(transp)
y2 = transp


transp = df1_dough['biom'].values
transp = np.array(transp)
y3 = transp

transp = df2_dough['assCO2'].values
transp = np.array(transp)
y3_b = transp/(60*60*24)

areaplant = df1_dough['leafArea'].values
areaplant = np.array(areaplant)

transp = df1_dough['transpiration'].values
transp = np.array(transp)
y3_c = transp*(10e2*60*60*24*areaplant/2.54)/areafield

transp = df3_dough['biom'].values
transp = np.array(transp)
y3clm = transp

transp = df4_dough['assCO2'].values
transp = np.array(transp)
y3clm_b = transp/(60*60*24)

transp = df3_dough['transpiration'].values
transp = np.array(transp)
y3clm_c = transp*(10e2*60*60*24*areaplant/2.54)/areafield

transp = df5_dough['biom'].values
transp = np.array(transp)
y3gday = transp

transp = df6_dough['assCO2'].values
transp = np.array(transp)
y3gday_b = transp/(60*60*24)

transp = df5_dough['transpiration'].values
transp = np.array(transp)
y3gday_c = transp*(10e2*60*60*24*areaplant/2.54)/areafield


transp = df1_dough['yields'].values
transp = np.array(transp)
y4 = transp

transp = df3_dough['yields'].values
transp = np.array(transp)
y4clm = transp

transp = df5_dough['yields'].values
transp = np.array(transp)
y4gday = transp

# create a color palette
palette = plt.get_cmap('Set1')


#plt.plot(x,y1, marker='', color=palette(1), linewidth=2.4, alpha=0.3, label='Early boot')
#plt.plot(x,y2, marker='', color=palette(2), linewidth=2.4, alpha=0.3, label='Heading')

plt.plot(x,y4, marker='_', color=palette(1), linewidth=2.4, alpha=0.3, label='Scheme 1')
plt.plot(x,y4clm, marker='x', color=palette(2), linewidth=2.4, alpha=0.3, label='Scheme 2')
plt.plot(x,y4gday, marker='.', color=palette(3), linewidth=2.4, alpha=0.3, label='Scheme 3')

#plt.plot(x,y4, marker='', color=palette(4), linewidth=2.4, alpha=0.3, label='Hard dough (JULES)')
#plt.plot(x,y4clm, marker='x', color=palette(4), linewidth=2.4, alpha=0.3, label='CLM')
#plt.plot(x,y4gday, marker='.', color=palette(4), linewidth=2.4, alpha=0.3, label='GDAY')
plt.xlim(0,1)
#plt.ylim(0,1400)
plt.xlabel('Beta')
#plt.ylabel('Transpiration (inches.day$^{-1}$)')
#plt.ylabel(r'CO$_{2}$ Assimilation ($\mu$mol CO$_{2}$.m$^{-2}$.s$^{-1}$)')
#plt.ylabel(r'Shoot-root ratio')
plt.title(r'Stage of development: Dough (day 60)')
plt.ylabel(r'Yield (mg)')
plt.legend()
plt.savefig('/home/renato/groimp_efficient/run_2b/paper_fig/yields_v2.png',dpi=300)
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
