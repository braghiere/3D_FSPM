
import numpy as np
import matplotlib.pyplot as plt
import os, sys
from scipy.interpolate import interp2d
from pylab import *

filelist=[]

for i in range(1,61):
    filelist.append("/home/renato/groimp_efficient/run_1c/RSD_2D_MIN3P%s.txt" %i)

#print filelist

for fname in filelist:

 counter = filelist.index(fname)

 f = open(fname,"r")

 #print f
 data = f.readlines()

 ivol = []
 x = []
 z= []
 RSD= []
 
 for i in range(2,len(data)):
   #print data[i]
   line = data[i].strip()
   columns = data[i].split()
   ivol.append(str(columns[0]))
   x.append(str(columns[1]))
   z.append(str(columns[2]))
   RSD.append(str(columns[3]))
   
   #print x,z,RSD

 ndata = 100

 x = np.linspace(0., 1., ndata)
 z = np.linspace(0., 1., ndata)
 RSD = np.reshape(RSD, (-1, ndata))

 X, Y = meshgrid(x, z)

 # simple fast plot
 #plt.pcolor(X, Y, RSD, vmin=0, vmax=20)
 #plt.colorbar()
 #plt.savefig('images/RSD_%s.png' %counter)
 #plt.close("all")

 # scipy interp. cubic
 f = interp2d(x, z, RSD, kind='cubic')
 xnew = np.arange(0, 1., .001)
 ynew = np.arange(0, 1., .001)
 data1 = f(xnew,ynew)
 Xn, Yn = np.meshgrid(xnew, ynew)
 cs = plt.pcolormesh(Xn, Yn, data1, cmap='BrBG', vmin=1.e-2, vmax=10)
 #plt.pcolormesh(Xn, Yn, data1, cmap='BrBG')
 cbar = plt.colorbar()
 cs.cmap.set_under('w')
 cbar.ax.set_ylabel('Root surface density (m$^{-2}$m$^{-3}$)', rotation=270, labelpad=20)
 plt.xlabel("x (m)", labelpad=20)
 plt.ylabel("z (m)", labelpad=20)
 # plt.title('DAY = 94')
 plt.title('DAY = %d'%(counter+1))
 plt.tight_layout()
 plt.savefig('/home/renato/groimp_efficient/run_1c/figures/RSD_%s.png' %(counter+1),dpi=300)
 print 'Figure RSD_%s.png saved sucessfully!' %(counter+1)
 #plt.show()
 plt.close("all")


sys.exit()









