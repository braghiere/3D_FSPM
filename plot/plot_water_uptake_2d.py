
import numpy as np
import matplotlib.pyplot as plt
import os, sys
from scipy.interpolate import interp2d
from pylab import *

filelist=[]

for i in range(1,61):
    filelist.append("/home/renato/groimp_efficient/run_1c/feddes_%s.gsp" %i)

#print filelist

for fname in filelist:

 counter = filelist.index(fname)

 f = open(fname,"r")

 #print f
 data = f.readlines()


 x = []
 y = []
 z= []
 h_w= []
 p_w= []
 s_w= []
 theta_w= []
 transp= []
 evap= []
 
 for i in range(3,len(data)):
   #print data[i]
   line = data[i].strip()
   columns = data[i].split()
   x.append(str(columns[0]))
   y.append(str(columns[1]))
   z.append(str(columns[2]))
   h_w.append(str(columns[3]))
   p_w.append(str(columns[4]))
   s_w.append(str(columns[5]))
   theta_w.append(str(columns[6]))
   transp.append(str(columns[7]))
   evap.append(str(columns[8]))

   #print x,z,RSD

 ndata = 100

 x = np.linspace(0., 1., ndata)
 z = np.linspace(0., 1., ndata)
 transp = np.reshape(transp, (-1, ndata))


 X, Y = meshgrid(x, z)

 # simple fast plot
 #plt.pcolor(X, Y, RSD, vmin=0, vmax=20)
 #plt.colorbar()
 #plt.savefig('images/RSD_%s.png' %counter)
 #plt.close("all")

 output_array = [1,2,3,4,5,6,7,8,9,10,15,20,30,40,50,60]

 # scipy interp. cubic
 f = interp2d(x, z, transp, kind='cubic')
 xnew = np.arange(0, 1.001, .001)
 ynew = np.arange(0, 1.001, .001)
 data1 = f(xnew,ynew)
 Xn, Yn = np.meshgrid(xnew, ynew)
 cs = plt.pcolormesh(Xn, Yn, data1, cmap='jet', vmin=0.0, vmax=1.e-10)
 #cs = plt.pcolormesh(Xn, Yn, data1, cmap='jet', vmin=0.1, vmax=0.3)
 #cs.cmap.set_under('w')
 #plt.pcolormesh(Xn, Yn, data1, cmap='jet', vmin=1.e-13, vmax=1.e-10)
 cbar = plt.colorbar()
 #cbar.ax.set_ylabel('Soil moisture', rotation=270, labelpad=20)
 cbar.ax.set_ylabel('Root water uptake (m$^{-2}$m$^{-3}$)', rotation=270, labelpad=20)

 plt.xlabel("x (m)", labelpad=20)
 plt.ylabel("z (m)", labelpad=20)
 plt.ylim(0.,1.)
 plt.xlim(0.,1.)
 #plt.title('DAY = %d'%output_array[counter])
 plt.title('DAY = %d' %(counter + 1))
 plt.tight_layout()
 plt.savefig('/home/renato/groimp_efficient/run_1c/figures/transp_%02d.png' %(counter + 1),dpi = 300)
 #plt.savefig('/home/renato/groimp_efficient/run_1c/figures/theta_%02d.png' %(counter + 1),dpi = 300)
 #plt.show()
 print 'Figure transp_%02d.png saved sucessfully!' %(counter + 1)
 plt.close("all")


sys.exit()









