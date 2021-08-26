import sys
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import seaborn
import pandas as pd

fig, ax = plt.subplots()
fig.set_tight_layout(True)

# Query the figure's on-screen size and DPI. Note that when saving the figure to
# a file, we need to provide a DPI for that separately.
print('fig size: {0} DPI, size in inches {1}'.format(
    fig.get_dpi(), fig.get_size_inches()))

df1 = pd.read_csv('/home/renato/groimp_efficient/output_94steps_no_respiration_effect/plant_20.txt',sep='\t', names=["time", "tt", "plant", "strip", "row", "pos", "species", "weed",
              "age","nrbranches","leafArea","fpar","rfr","biom","yields","leafmass",
               "stemmass", "rootmass","shootrootratio","abovebiom","transpiration"])

df2 = pd.read_csv('/home/renato/groimp_efficient/output_94steps_no_respiration_effect/field_20.txt',sep='\t', names=["time", "species", "LAI", "nrShoots", "fAbs", "assCO2", "biomAbove", "yield", "harvestIndex","leafArea","fieldRFR"])

df3 = pd.read_csv('/home/renato/groimp_efficient/output_94steps_biom_feedback/plant_1.txt',sep='\t', names=["time", "tt", "plant", "strip", "row", "pos", "species", "weed",
              "age","nrbranches","leafArea","fpar","rfr","biom","yields","leafmass",
               "stemmass", "rootmass","shootrootratio","abovebiom","transpiration"])

df4 = pd.read_csv('/home/renato/groimp_efficient/output_94steps_biom_feedback/plant_2.txt',sep='\t', names=["time", "tt", "plant", "strip", "row", "pos", "species", "weed",
              "age","nrbranches","leafArea","fpar","rfr","biom","yields","leafmass",
               "stemmass", "rootmass","shootrootratio","abovebiom","transpiration"])



time = df1.time.values
time = np.array(time)
x = time    

areaplant = df1.leafArea.values
areaplant = np.array(areaplant)

areafield = 2*2

shootrootratio = df1.rootmass.values
shootrootratio = np.array(shootrootratio)
#y = (shootrootratio*10e2*60*60*24*areaplant/2.54)/areafield
y = shootrootratio

transp1 = df3.rootmass.values
transp1 = np.array(transp1)
y1 = transp1

#transp2 = df4.transpiration.values
#transp2 = np.array(transp2)
#y2 = transp2


#fAbs = df2.fAbs.values
#fAbs = np.array(fAbs)
#y = (1. - fAbs)/(1.-0.1)



#beta = df3.beta.values
#beta = np.array(beta)
#y = beta


# Plot a scatter that persists (isn't redrawn) and the initial line.
#x = np.arange(0, 20, 0.1)
ax.set_xlabel('Time')
#ax.set_ylabel(r'CO$_{2}$ Assimilation')
#ax.set_ylabel(r'Transpiration (m.s$^{-1}$)')
ax.set_ylabel(r'Root biomass (mg)')
#ax.set_ylim(0,1e-6*10e2*60*60*24*0.04/2.54/4)
#ax.set_ylim(0,1e-7)
#ax.set_ylim(0,2)
ax.scatter(x, y, label = 'No water limitation')
#ax.scatter(x, y1, label = 'No limitation sec')
#ax.plot(x, y2, 'g-',label = 'Limitation once')


line, = ax.plot(x, y, 'r-', linewidth=2,label = 'No effect on Rd')
line1, = ax.plot(x, y1, 'b-', linewidth=2,label = 'Beta effect on Rd')

def update(i):
    label = 'timestep {0}'.format(i)
    #label = 'Beta {0}'.format(i/20.)

    print(label)
    df1 = pd.read_csv('/home/renato/groimp_efficient/output_94steps_no_respiration_effect/plant_%s.txt'%i,sep='\t', names=["time", "tt", "plant", "strip", "row", "pos", "species", "weed",
              "age","nrbranches","leafArea","fpar","rfr","biom","yields","leafmass",
               "stemmass", "rootmass","shootrootratio","abovebiom","transpiration"])

    df2 = pd.read_csv('/home/renato/groimp_efficient/output_94steps_no_respiration_effect/field_%s.txt'%i,sep='\t', names=["time", "species", "LAI", "nrShoots", "fAbs", "assCO2", "biomAbove", "yield", "harvestIndex","leafArea","fieldRFR"])

    df3 = pd.read_csv('/home/renato/groimp_efficient/output_94steps_biom_feedback/plant_%s.txt'%i,sep='\t', names=["time", "tt", "plant", "strip", "row", "pos", "species", "weed",
              "age","nrbranches","leafArea","fpar","rfr","biom","yields","leafmass",
               "stemmass", "rootmass","shootrootratio","abovebiom","transpiration"])

    df4 = pd.read_csv('/home/renato/groimp_efficient/output_94steps_biom_feedback/field_%s.txt'%i,sep='\t', names=["time", "species", "LAI", "nrShoots", "fAbs", "assCO2", "biomAbove", "yield", "harvestIndex","leafArea","fieldRFR"])

    time = df1.time.values
    time = np.array(time)
    x = time    


    areaplant = df1.leafArea.values
    areaplant = np.array(areaplant)

    areafield = 2*2

    biomAbove = df1.rootmass.values
    biomAbove = np.array(biomAbove)
    #y = (biomAbove*10e2*60*60*24*areaplant/2.54)/areafield
    y = biomAbove

    transp1 = df3.rootmass.values
    transp1 = np.array(transp1)
    y1 = transp1

    #assCO2 = df2.fAbs.values
    #assCO2 = np.array(assCO2)  
    #y = (1. - assCO2)/(1.-0.1)


    #beta = df3.beta.values
    #beta = np.array(beta)
    #y = beta

    # Update the line and the axes (with a new xlabel). Return a tuple of
    # "artists" that have to be redrawn for this frame.
    line.set_ydata(y)
    line1.set_ydata(y1)
    #ax.set_xlabel(label)
    ax.set_title(label)
    ax.legend()
    return line,line1, ax

if __name__ == '__main__':
    # FuncAnimation will call the 'update' function for each frame; here
    # animating over 10 frames, with an interval of 200ms between frames.
    anim = FuncAnimation(fig, update, frames=np.arange(1, 94), interval=500)
    if len(sys.argv) > 1 and sys.argv[1] == 'save':
        anim.save('rootmass_comp.gif', dpi=80, writer='imagemagick')
    else:
        # plt.show() will just loop the animation forever.
        plt.show()
