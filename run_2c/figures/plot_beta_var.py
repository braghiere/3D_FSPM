# libraries and data
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import sys, os

file_name_plant = '/home/renato/groimp_efficient/run_1/plant_rew.txt'
file_name_field = '/home/renato/groimp_efficient/run_1/field_rew.txt'

 
file_name_plant_jules = 'jules/plant_{}.txt'
file_name_field_jules = 'jules/field_{}.txt'

file_name_plant_clm = 'clm/plant_{}.txt'
file_name_field_clm = 'clm/field_{}.txt'

file_name_plant_gday = 'gday/plant_{}.txt'
file_name_field_gday = 'gday/field_{}.txt'


dfa = pd.read_csv(file_name_plant,sep='\t', names=["time", 
              "tt", "plant", "strip", "row", "pos", "species", "weed",
              "age","age(days)","nrbranches","leafArea","fpar","rfr","biom","yields","leafmass",
               "stemmass", "rootmass","shootrootratio","abovebiom","transpiration"])

xa = dfa['age(days)'].values
xa = np.array(xa)


dfb = pd.read_csv(file_name_field,sep='\t', names=["time", 
          "species", "LAI", "nrShoots", "fAbs", "assCO2", "biomAbove", "yield", 
          "harvestIndex","leafArea","fieldRFR"])

xa = dfa['age(days)'].values
xa = np.array(xa)

areaplant = dfa['leafArea'].values
areaplant = np.array(areaplant)

areafield = 1*1

transp = dfa['transpiration'].values
transp = np.array(transp)
ya = transp*(10e2*60*60*24*areaplant/2.54)/areafield
ya = transp*(10e2*60*60*24/2.54)/areafield


#ya = transp


df1 = pd.concat([pd.read_csv(file_name_plant_jules.format(i),sep='\t', names=["time", 
              "tt", "plant", "strip", "row", "pos", "species", "weed",
              "age","nrbranches","leafArea","fpar","rfr","biom","yields","leafmass",
               "stemmass", "rootmass","shootrootratio","abovebiom","transpiration"]) 
               for i in range(94, 95)])

df2 = pd.concat([pd.read_csv(file_name_field_jules.format(i),sep='\t', names=["time", 
          "species", "LAI", "nrShoots", "fAbs", "assCO2", "biomAbove", "yield", 
          "harvestIndex","leafArea","fieldRFR"]) for i in range(94, 95)])

df3 = pd.concat([pd.read_csv(file_name_plant_clm.format(i),sep='\t', names=["time", 
              "tt", "plant", "strip", "row", "pos", "species", "weed",
              "age","nrbranches","leafArea","fpar","rfr","biom","yields","leafmass",
               "stemmass", "rootmass","shootrootratio","abovebiom","transpiration"]) for i in range(60, 61)])

df4 = pd.concat([pd.read_csv(file_name_field_clm.format(i),sep='\t', names=["time", "species", "LAI", "nrShoots", "fAbs", "assCO2", "biomAbove", "yield", "harvestIndex","leafArea","fieldRFR"]) for i in range(60, 61)])

df5 = pd.concat([pd.read_csv(file_name_plant_gday.format(i),sep='\t',  names=["time", 
              "tt", "plant", "strip", "row", "pos", "species", "weed",
              "age","nrbranches","leafArea","fpar","rfr","biom","yields","leafmass",
               "stemmass", "rootmass","shootrootratio","abovebiom","transpiration"]) for i in range(60, 61)])

df6 = pd.concat([pd.read_csv(file_name_field_gday.format(i),sep='\t', names=["time", "species", "LAI", "nrShoots", "fAbs", "assCO2", "biomAbove", "yield", "harvestIndex","leafArea","fieldRFR"]) for i in range(60, 61)])



# Initialize the figure
plt.style.use('seaborn-darkgrid')

#plt.plot(df1['age'], df1['transpiration'], marker='', color='grey', linewidth=0.6, alpha=0.3)
#plt.show()


areaplant = df1.leafArea.values
areaplant = np.array(areaplant)



areaplant = df1['leafArea'].values
areaplant = np.array(areaplant)

transp = df1['transpiration'].values
transp = np.array(transp)
y1 = transp*(10e2*60*60*24*areaplant/2.54)/areafield

areaplant = df3['leafArea'].values
areaplant = np.array(areaplant)

transp = df3['transpiration'].values
transp = np.array(transp)
y2 = transp*(10e2*60*60*24*areaplant/2.54)/areafield

areaplant = df3['leafArea'].values
areaplant = np.array(areaplant)

transp = df3['transpiration'].values
transp = np.array(transp)
y3 = transp*(10e2*60*60*24*areaplant/2.54)/areafield

#print y1,y2,y3
#sys.exit()

areaplant = df1['leafArea'].values
areaplant = np.array(areaplant)

transp = df1['transpiration'].values
transp = np.array(transp)
y6 = transp*(10e2*60*60*24*areaplant/2.54)/areafield
y6 = transp*(10e2*60*60*24/2.54)/areafield
#x = np.arange(101)/101. + 0.05
#x = np.arange(101)/101. 
x = df1['time'].values
x94 = np.array(x)

x = df3['time'].values
x = np.array(x)

transp = df2['assCO2'].values
transp = np.array(transp)
y1 = transp/(60*60*24)


transp = df2['assCO2'].values
transp = np.array(transp)
y2 = transp/(60*60*24)


transp = df2['assCO2'].values
transp = np.array(transp)
y3 = transp/(60*60*24)


transp = df2['assCO2'].values
transp = np.array(transp)
y4 = transp/(60*60*24)




transp = df1['rootmass'].values
transp = np.array(transp)
y1 = transp


transp = df1['rootmass'].values
transp = np.array(transp)
y2 = transp


transp = df1['biom'].values
transp = np.array(transp)
y3 = transp

transp = df3['rootmass'].values
transp = np.array(transp)
y3clm = transp

transp = df5['rootmass'].values
transp = np.array(transp)
y3gday = transp


transp = df2['assCO2'].values
transp = np.array(transp)
y4 = transp/(60*60*24)

transp = df3['rootmass'].values
transp = np.array(transp)
y4clm = transp

#transp = df5_hard['rootmass'].values
#transp = np.array(transp)
#y4gday = transp

# create a color palette
palette = plt.get_cmap('Set1')

print len(xa)
print len(y6)

#plt.plot(x,y1, marker='', color=palette(1), linewidth=2.4, alpha=0.3, label='Early boot')
#plt.plot(x,y2, marker='', color=palette(2), linewidth=2.4, alpha=0.3, label='Heading')
plt.plot(xa,ya, marker='_', color=palette(4), linewidth=2.4, alpha=0.3, label='No limitation')
plt.plot(xa,y6, marker='_', color=palette(1), linewidth=2.4, alpha=0.3, label='Beta factor')
#plt.plot(x,y3clm, marker='x', color=palette(2), linewidth=2.4, alpha=0.3, label='Scheme 2')
#plt.plot(x,y3gday, marker='.', color=palette(3), linewidth=2.4, alpha=0.3, label='Scheme 3')

#plt.plot(x,y4, marker='', color=palette(4), linewidth=2.4, alpha=0.3, label='Hard dough (JULES)')
#plt.plot(x,y4clm, marker='x', color=palette(4), linewidth=2.4, alpha=0.3, label='CLM')
#plt.plot(x,y4gday, marker='.', color=palette(4), linewidth=2.4, alpha=0.3, label='GDAY')
plt.xlim(min(xa),max(xa))
#plt.ylim(min(ya),max(ya))
plt.xlabel('Time (days)')
plt.ylabel('Transpiration (inches.day$^{-1}$)')
#plt.ylabel(r'CO$_{2}$ Assimilation ($\mu$mol CO$_{2}$.m$^{-2}$.s$^{-1}$)')
#plt.ylabel(r'Shoot-root ratio')
#plt.title(r'Stage: Dough (day 60)')
#plt.ylabel(r'Plant biomass (mg)')
plt.legend()
print y4,ya
#plt.savefig('rootbiom_beta_4stages_resp.png')
plt.savefig('/home/renato/groimp_efficient/run_1c/paper_fig/transp3.png',dpi=300)
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
