
import numpy as np
import matplotlib.pyplot as plt
import os, sys
from scipy.interpolate import interp2d
from pylab import *

filelist=[]

#error = []
biomrsd1= []
biomrsd2= []
biomrsd3= []

dirname2 = "/home/renato/groimp_efficient/run_3/"
dirname1 = "/home/renato/groimp_efficient/run_3/"

list = [94]

for i in range(1,61):
#for i in list:
    filelist.append("water_%s.gsp" %i)

#print filelist

for fname in filelist:

 counter = filelist.index(fname)
 #counter = 93

 f1 = open(os.path.join(dirname1,fname),"r")
 f2 = open(os.path.join(dirname2,fname),"r")

 #print f
 data1 = f1.readlines()
 data2 = f2.readlines()


 x1 = []
 y1 = []
 z1 = []
 h_w1 = []
 p_w1 = []
 s_w1 = []
 theta_w1 = []
 transp1 = []
 evap1 = []
 transp12 = []
 transp1tot = []

 x2 = []
 y2 = []
 z2 = []
 h_w2 = []
 p_w2 = []
 s_w2 = []
 theta_w2 = []
 transp2 = []
 evap2 = []
 transp22 = []
 transp2tot = []
 
 for i in range(3,len(data1)):
   #print data[i]
   line = data1[i].strip()
   columns = data1[i].split()
   x1.append(str(columns[0]))
   y1.append(str(columns[1]))
   z1.append(str(columns[2]))
   h_w1.append(str(columns[3]))
   p_w1.append(str(columns[4]))
   s_w1.append(str(columns[5]))
   theta_w1.append(str(columns[6]))
   transp1.append(str(columns[7]))
   evap1.append(str(columns[8]))
   transp12.append(str(columns[9]))
   transp1tot.append(str(columns[10]))

 for i in range(3,len(data2)):
   #print data[i]
   line = data2[i].strip()
   columns = data2[i].split()
   x2.append(str(columns[0]))
   y2.append(str(columns[1]))
   z2.append(str(columns[2]))
   h_w2.append(str(columns[3]))
   p_w2.append(str(columns[4]))
   s_w2.append(str(columns[5]))
   theta_w2.append(str(columns[6]))
   transp2.append(str(columns[7]))
   evap2.append(str(columns[8]))
   transp22.append(str(columns[9]))
   transp2tot.append(str(columns[10]))
   #print x,z,RSD

 ndata1 = 100
 ndata2 = 100

 x1 = np.linspace(0., 1., ndata1)
 x2 = np.linspace(-1., 0., ndata2)
 z1 = np.linspace(0., 1., ndata1)
 z2 = np.linspace(0., 1., ndata2)

 transp1 = np.reshape(theta_w1, (-1, ndata1))

 transp2 = np.reshape(theta_w2, (-1, ndata2))


 X1, Y1 = meshgrid(x1, z1)
 X2, Y2 = meshgrid(x2, z2)

 # simple fast plot
 #plt.pcolor(X, Y, RSD, vmin=0, vmax=20)
 #plt.colorbar()
 #plt.savefig('images/RSD_%s.png' %counter)
 #plt.close("all")

 output_array = [1,2,3,4,5,6,7,8,9,10,15,20,30,40,50,60]

 # scipy interp. cubic
 f1 = interp2d(x1, z1, transp1, kind='cubic')
 f2 = interp2d(x2, z2, transp2, kind='cubic')
 xnew1 = np.arange(0, 1., .01)
 xnew2 = np.arange(-1., 0., .01)
 ynew = np.arange(0, 1., .01)
 data1 = f1(xnew1,ynew)
 data2 = f2(xnew2,ynew)
 Xn1, Yn = np.meshgrid(xnew1, ynew)
 Xn2, Yn = np.meshgrid(xnew2, ynew)
 cs = plt.pcolormesh(Xn1, Yn, data1, cmap='jet', vmin=min(data1.min(),data2.min()), vmax=max(data1.max(),data2.max()))
 cs = plt.pcolormesh(Xn2, Yn, data2, cmap='jet', vmin=min(data1.min(),data2.min()), vmax=max(data1.max(),data2.max()))
 cs = plt.pcolormesh(Xn1, Yn, data1, cmap='jet', vmin=0.15, vmax=0.25)
 cs = plt.pcolormesh(Xn2, Yn, data2, cmap='jet', vmin=0.15, vmax=0.25)
 #cs = plt.pcolormesh(Xn1, Yn, data1, cmap='jet', vmin=0., vmax=1.e-11)
 #cs = plt.pcolormesh(Xn2, Yn, data2, cmap='jet', vmin=0., vmax=1.e-11)

 cbar = plt.colorbar()
 cbar.ax.set_ylabel('Soil moisture availability', rotation=270, labelpad=20)
 #cbar.ax.set_ylabel('Root water uptake (m$^{-2}$m$^{-3}$)', rotation=270, labelpad=20)

 #plt.xlabel("x (m)", labelpad=20)
 plt.ylabel("z (m)", labelpad=20)
 xname = [-0.5,0.5]
 labels = ['Without Beta','With Beta']
 plt.xticks(xname,labels)
 plt.ylim(0.,1.)
 plt.xlim(-1.,1.)
 #plt.title('DAY = %d'%output_array[counter])
 plt.title('DAY = %d' %(counter + 1))
 plt.tight_layout()
 #plt.savefig('/home/renato/groimp_efficient/run_1c/paper_fig/transp_%02d.png' %(counter + 1),dpi = 300)
 plt.savefig('/home/renato/groimp_efficient/run_3/figures/thetaw_new/theta_%02d.png' %(counter + 1))
 #plt.show()
 print 'Figure transp_%02d.png saved sucessfully!' %(counter + 1)
 plt.close("all")

 #error.append(np.sum(RSD))
 biomrsd1.append(np.sum(np.array(transp1).astype(np.float)))
 biomrsd2.append(np.sum(np.array(transp12).astype(np.float)))
 #biomrsd3.append(np.sum(np.array(transp1tot).astype(np.float)))

biomrsd1 = np.array(biomrsd1)/(ndata1*ndata1)
biomrsd2 = np.array(biomrsd2)/(ndata2*ndata2)
#biomrsd3 = np.array(biomrsd3)/(ndata2*ndata2)

plt.plot(biomrsd1,label='Monocot')
plt.plot(biomrsd2,label='Dicot')
plt.plot(biomrsd3,label='Total')

plt.xlabel("Time (days)", labelpad=20)
plt.ylabel("Integrated soil moisture availability", labelpad=20)
#plt.ylabel("Integrated root water uptake (m$^{-2}$m$^{-3}$)", labelpad=20)
# plt.title('DAY = 94')
plt.ylim(0.15,0.25)
plt.legend()
plt.title('Two plants')
plt.tight_layout()
plt.savefig('/home/renato/groimp_efficient/run_3/figures/thetaw_new/theta_total.png')
plt.show()

sys.exit()












