import sys
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import seaborn
import pandas as pd

fig, ax = plt.subplots()
fig.set_tight_layout(True)

# Initialize the figure
plt.style.use('seaborn-darkgrid')

# Query the figure's on-screen size and DPI. Note that when saving the figure to
# a file, we need to provide a DPI for that separately.
print('fig size: {0} DPI, size in inches {1}'.format(
    fig.get_dpi(), fig.get_size_inches()))

df1 = pd.read_csv('/home/renato/groimp_efficient/beta_sensitivity/plant_20.txt',sep='\t', names=["time", "tt", "plant", "strip", "row", "pos", "species", "weed",
              "age","nrbranches","leafArea","fpar","rfr","biom","yields","leafmass",
               "stemmass", "rootmass","shootrootratio","abovebiom","transpiration"])

df2 = pd.read_csv('/home/renato/groimp_efficient/beta_sensitivity/field_20.txt',sep='\t', names=["time", "species", "LAI", "nrShoots", "fAbs", "assCO2", "biomAbove", "yield", "harvestIndex","leafArea","fieldRFR"])


df3 = pd.read_csv('/home/renato/groimp_efficient/beta_sensitivity/plant_clm_20.txt',sep='\t', names=["time", "tt", "plant", "strip", "row", "pos", "species", "weed",
              "age","nrbranches","leafArea","fpar","rfr","biom","yields","leafmass",
               "stemmass", "rootmass","shootrootratio","abovebiom","transpiration"])


df4 = pd.read_csv('/home/renato/groimp_efficient/beta_sensitivity/field_clm_20.txt',sep='\t', names=["time", "species", "LAI", "nrShoots", "fAbs", "assCO2", "biomAbove", "yield", "harvestIndex","leafArea","fieldRFR"])


df5 = pd.read_csv('/home/renato/groimp_efficient/beta_sensitivity/plant_gday_14.txt',sep='\t', names=["time", "tt", "plant", "strip", "row", "pos", "species", "weed",
              "age","nrbranches","leafArea","fpar","rfr","biom","yields","leafmass",
               "stemmass", "rootmass","shootrootratio","abovebiom","transpiration"])


df6 = pd.read_csv('/home/renato/groimp_efficient/beta_sensitivity/field_gday_14.txt',sep='\t', names=["time", "species", "LAI", "nrShoots", "fAbs", "assCO2", "biomAbove", "yield", "harvestIndex","leafArea","fieldRFR"])



time = df1.time.values
time = np.array(time)
x = time/17.02

areaplant1 = df1.leafArea.values
areaplant1 = np.array(areaplant1)

areaplant3 = df3.leafArea.values
areaplant3 = np.array(areaplant3)

areaplant5 = df5.leafArea.values
areaplant5 = np.array(areaplant5)

areafield = 2*2

shootrootratio = df1.transpiration.values
shootrootratio = np.array(shootrootratio)
y = (shootrootratio*10e2*60*60*24*areaplant1/2.54)/areafield

fAbs = df2.fAbs.values
fAbs = np.array(fAbs)
y = (1. - fAbs)/(1.-0.1)

assCO2 = df1.rootmass.values
assCO2 = np.array(assCO2)
#y = (assCO2*10e2*60*60*24*areaplant1/2.54)/areafield
y = assCO2

assCO2 = df3.rootmass.values
assCO2 = np.array(assCO2)
#y1 = (assCO2*10e2*60*60*24*areaplant3/2.54)/areafield
y1 = assCO2

assCO2 = df5.rootmass.values
assCO2 = np.array(assCO2)
#y2 = (assCO2*10e2*60*60*24*areaplant5/2.54)/areafield
y2 = assCO2

#beta = df3.beta.values
#beta = np.array(beta)
#y = beta


# Plot a scatter that persists (isn't redrawn) and the initial line.
#x = np.arange(0, 20, 0.1)
ax.set_xlabel('Time (days)')
ax.set_ylabel(r'Root biomass (mg)')
#ax.set_ylabel(r'CO$_{2}$ Assimilation (mol.CO2.m$^{-2}$.s$^{-1}$)')
#ax.set_ylabel(r'Transpiration (inches.day$^{-1}$)')
#ax.set_ylim(0,1e-6*10e2*60*60*24*0.04/2.54/4)
ax.plot(x, y, 'k-.', linewidth=2,label =r'REFERENCE')
#ax.scatter(x, y1)

line, = ax.plot(x, y, 'r-', linewidth=2, label =r'$\beta$.A')

line1, = ax.plot(x, y1, 'k-', linewidth=2, label = r'$\beta$.V$_{cmax}$')

line2, = ax.plot(x, y2, 'b-', linewidth=2, label = r'$\beta$.V$_{cmax}$ & $\beta$.J$_{max}$')

ax.legend()

def update(i):
    #label = 'timestep {0}'.format(i)
    label = 'Beta {0}'.format(i/20.)

    print(label)
    df1 = pd.read_csv('/home/renato/groimp_efficient/beta_sensitivity/plant_%s.txt'%i,sep='\t', names=["time", "tt", "plant", "strip", "row", "pos", "species", "weed",
              "age","nrbranches","leafArea","fpar","rfr","biom","yields","leafmass",
               "stemmass", "rootmass","shootrootratio","abovebiom","transpiration"])

    df2 = pd.read_csv('/home/renato/groimp_efficient/beta_sensitivity/field_%s.txt'%i,sep='\t', names=["time", "species", "LAI", "nrShoots", "fAbs", "assCO2", "biomAbove", "yield", "harvestIndex","leafArea","fieldRFR"])


    df3 = pd.read_csv('/home/renato/groimp_efficient/beta_sensitivity/plant_clm_%s.txt'%i,sep='\t', names=["time", "tt", "plant", "strip", "row", "pos", "species", "weed",
              "age","nrbranches","leafArea","fpar","rfr","biom","yields","leafmass",
               "stemmass", "rootmass","shootrootratio","abovebiom","transpiration"])

    df4 = pd.read_csv('/home/renato/groimp_efficient/beta_sensitivity/field_clm_%s.txt'%i,sep='\t', names=["time", "species", "LAI", "nrShoots", "fAbs", "assCO2", "biomAbove", "yield", "harvestIndex","leafArea","fieldRFR"])

    df5 = pd.read_csv('/home/renato/groimp_efficient/beta_sensitivity/plant_gday_%s.txt'%i,sep='\t', names=["time", "tt", "plant", "strip", "row", "pos", "species", "weed",
              "age","nrbranches","leafArea","fpar","rfr","biom","yields","leafmass",
               "stemmass", "rootmass","shootrootratio","abovebiom","transpiration"])

    df6 = pd.read_csv('/home/renato/groimp_efficient/beta_sensitivity/field_gday_%s.txt'%i,sep='\t', names=["time", "species", "LAI", "nrShoots", "fAbs", "assCO2", "biomAbove", "yield", "harvestIndex","leafArea","fieldRFR"])




    time = df1.time.values
    time = np.array(time)
    x = time    


    areaplant1 = df1.leafArea.values
    areaplant1 = np.array(areaplant1)

    areaplant3 = df1.leafArea.values
    areaplant3 = np.array(areaplant3)

    areaplant5 = df1.leafArea.values
    areaplant5 = np.array(areaplant5)


    areafield = 2*2

    biomAbove = df1.transpiration.values
    biomAbove = np.array(biomAbove)
    y = (biomAbove*10e2*60*60*24*areaplant1/2.54)/areafield

    assCO2 = df2.fAbs.values
    assCO2 = np.array(assCO2)  
    y = (1. - assCO2)/(1.-0.1)

    assCO2 = df1.rootmass.values
    assCO2 = np.array(assCO2)  
    #y = (assCO2*10e2*60*60*24*areaplant1/2.54)/areafield
    y = assCO2

    assCO2 = df3.rootmass.values
    assCO2 = np.array(assCO2)
    #y1 = (assCO2*10e2*60*60*24*areaplant3/2.54)/areafield
    y1 = assCO2

    assCO2 = df5.rootmass.values
    assCO2 = np.array(assCO2)
    #y2 = (assCO2*10e2*60*60*24*areaplant5/2.54)/areafield
    y2 = assCO2

    #beta = df3.beta.values
    #beta = np.array(beta)
    #y = beta

    # Update the line and the axes (with a new xlabel). Return a tuple of
    # "artists" that have to be redrawn for this frame.
    line.set_ydata(y)
    line1.set_ydata(y1)
    line2.set_ydata(y2)
    #ax.set_xlabel(label)
    ax.set_title(label)
    ax.legend()
    return line, line1, line2, ax

if __name__ == '__main__':
    # FuncAnimation will call the 'update' function for each frame; here
    # animating over 10 frames, with an interval of 200ms between frames.
    anim = FuncAnimation(fig, update, frames=np.arange(1, 21), interval=500)
    if len(sys.argv) > 1 and sys.argv[1] == 'save':
        anim.save('rootmass_3_methods.gif', dpi=80, writer='imagemagick')
    else:
        # plt.show() will just loop the animation forever.
        plt.show()
