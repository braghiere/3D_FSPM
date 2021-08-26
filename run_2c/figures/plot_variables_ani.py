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

df1 = pd.read_csv('/home/renato/groimp_efficient/run_1c/jules/plant_94.txt',sep='\t', names=["time", "tt", "plant", "strip", "row", "pos", "species", "weed",
              "age","nrbranches","leafArea","fpar","rfr","biom","yields","leafmass",
               "stemmass", "rootmass","shootrootratio","abovebiom","transpiration"])

df2 = pd.read_csv('/home/renato/groimp_efficient/run_1c/jules/field_94.txt',sep='\t', names=["time", "species", "LAI", "nrShoots", "fAbs", "assCO2", "biomAbove", "yield", "harvestIndex","leafArea","fieldRFR"])

df3 = pd.read_csv('/home/renato/groimp_efficient/run_1c/jules/beta_1_94.txt',sep='\t',names=['beta'])

df4 = pd.read_csv('/home/renato/groimp_efficient/run_1c/jules/RWU_94.txt',sep='\t',names=['RWU'])


time = df1.time.values
time = np.array(time)
x = time    

transpiration = df1.transpiration.values
transpiration = np.array(transpiration)
y1 = transpiration

RWU = df4.RWU.values
RWU = np.array(RWU)
y2 = RWU

#beta = df3.beta.values
#beta = np.array(beta)
#y = beta


# Plot a scatter that persists (isn't redrawn) and the initial line.
#x = np.arange(0, 20, 0.1)
ax.set_xlabel('Time')
ax.set_ylabel('Evapotranspiration (m.s-1)')
ax.set_ylim(0,2.e-7)
#ax.set_ylim(y1.min(),y1.max())
ax.scatter(x, y1)
ax.scatter(x, y2)

line1, = ax.plot(x, y1, 'r-', linewidth=2, label=r'PET_{0}')
line2, = ax.plot(x, y2, 'b-', linewidth=2, label=r'ET_{0}')
ax.legend()
def update(i):
    label = 'timestep {0}'.format(i)
    print(label)
    df1 = pd.read_csv('/home/renato/groimp_efficient/run_1c/jules/plant_%s.txt'%i,sep='\t', names=["time", "tt", "plant", "strip", "row", "pos", "species", "weed",
              "age","nrbranches","leafArea","fpar","rfr","biom","yields","leafmass",
               "stemmass", "rootmass","shootrootratio","abovebiom","transpiration"])

    df2 = pd.read_csv('/home/renato/groimp_efficient/run_1c/jules/field_%s.txt'%i,sep='\t', names=["time", "species", "LAI", "nrShoots", "fAbs", "assCO2", "biomAbove", "yield", "harvestIndex","leafArea","fieldRFR"])

    df3 = pd.read_csv('/home/renato/groimp_efficient/run_1c/jules/beta_1_%s.txt'%i,sep='\t',names=['beta'])

    df4 = pd.read_csv('/home/renato/groimp_efficient/run_1c/jules/RWU_%s.txt'%i,sep='\t',names=['RWU'])



    time = df1.time.values
    time = np.array(time)
    x = time    

    transpiration = df1.transpiration.values
    transpiration = np.array(transpiration)
    y1 = transpiration

    RWU = df4.RWU.values
    RWU = np.array(RWU)  
    y2 = RWU


    # Update the line and the axes (with a new xlabel). Return a tuple of
    # "artists" that have to be redrawn for this frame.
    line1.set_ydata(y1)
    line2.set_ydata(y2)
    #ax.set_xlabel(label)
    ax.set_title(label)
    return line1,line2, ax

if __name__ == '__main__':
    # FuncAnimation will call the 'update' function for each frame; here
    # animating over 10 frames, with an interval of 200ms between frames.
    anim = FuncAnimation(fig, update, frames=np.arange(1, 95), interval=500)
    if len(sys.argv) > 1 and sys.argv[1] == 'save':
        anim.save('assco2.gif', dpi=300, writer='imagemagick')
    else:
        # plt.show() will just loop the animation forever.
        plt.show()
