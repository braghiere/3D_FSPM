import numpy as np
import matplotlib.pyplot as plt
import os, sys
from scipy.interpolate import interp2d
from pylab import *
import pandas as pd

filelist=[]

error = []
biomrsd1= []
biomrsd2= []

for i in range(1,95):
  
 df1 = pd.read_csv('/home/renato/groimp_efficient/input/feddes_%s.gsp'%i,skiprows=3,
                   delim_whitespace=True,names=["x", "y", "z", "h_w", "p_w", "s_w", "theta_w", "transp", "evap"])

 df2 = pd.read_csv('/home/renato/groimp_efficient/input/biomrac_3000/feddes_%s.gsp' %i,skiprows=3,
                   delim_whitespace=True,names=["x", "y", "z", "h_w", "p_w", "s_w", "theta_w", "transp", "evap"])


 x = np.array(df1['x'].values)
 z = np.array(df1['z'].values)
 RSD1 = np.array(df1['theta_w'].values)

 RSD2 = np.array(df2['theta_w'].values)

 RSD = RSD2 - RSD1

 ndata = 50

 x = np.linspace(0., 2., ndata)
 z = np.linspace(0., 2., ndata)
 RSD = np.reshape(RSD, (-1, ndata))

 X, Y = meshgrid(x, z)

 # simple fast plot
 #plt.pcolor(X, Y, RSD, vmin=0, vmax=20)
 #plt.colorbar()
 #plt.savefig('images/RSD_%s.png' %counter)
 #plt.close("all")

 #output_array = [1,2,3,4,5,6,7,8,9,10,15,20,30,40,50,60]

 # scipy interp. cubic
 f = interp2d(x, z, RSD, kind='cubic')
 xnew = np.arange(0, 2, .01)
 ynew = np.arange(0, 2, .01)
 data1 = f(xnew,ynew)
 Xn, Yn = np.meshgrid(xnew, ynew)
 #plt.pcolormesh(Xn, Yn, data1, cmap='RdBu_r', vmin=-0.025, vmax=0.025)
 plt.pcolormesh(Xn, Yn, data1, cmap='RdBu_r', vmin=-1e-4, vmax=1e-4)
 #plt.pcolormesh(Xn, Yn, data1, cmap='jet', vmin=-RSD1.min(), vmax=RSD1.max())
 cbar = plt.colorbar()
 #cbar.ax.set_ylabel('Difference Root density (m$^{-2}$m$^{-3}$)', rotation=270, labelpad=20)
 #cbar.ax.set_ylabel('Root water uptake (m$^{-2}$m$^{-3}$)', rotation=270, labelpad=20)
 cbar.ax.set_ylabel('Difference soil moisture content', rotation=270, labelpad=20)
 plt.xlabel("x (m)", labelpad=20)
 plt.ylabel("z (m)", labelpad=20)
 plt.title('DAY = %d'%(i))
 plt.tight_layout()
 plt.savefig('/home/renato/groimp_efficient/figures/anom_theta_%02d.png' %(i))
 #plt.show()
 print np.sum(RSD)
 print 'Figure transp_%s.png saved sucessfully!' %(i)
 plt.close("all")

 error.append(np.sum(RSD))
 biomrsd1.append(np.sum(RSD1))
 biomrsd2.append(np.sum(RSD2))

plt.plot(biomrsd1,label='Limited Root biomass')
plt.plot(biomrsd2,label='Not limited Root biomass')
plt.legend()
plt.show()


sys.exit()









 
