
import numpy as np
import matplotlib.pyplot as plt
import os, sys
from scipy.interpolate import interp2d
from pylab import *

filelist=[]

#error = []
biomrsd1= []
biomrsd2= []


dirname2 = "/home/renato/groimp_efficient/run_2/"
dirname1 = "/home/renato/groimp_efficient/run_2c/"

list = [94]

for i in range(1,61):
#for i in list:
    filelist.append("RSD_2D_MIN3P%s.txt" %i)


#print filelist

for fname in filelist:

 counter = filelist.index(fname)
 #counter = 93

 f1 = open(os.path.join(dirname1,fname),"r")
 f2 = open(os.path.join(dirname2,fname),"r")

 #print f
 data1 = f1.readlines()
 data2 = f2.readlines()

 ivol1 = []
 x1 = []
 z1= []
 RSD1 = []

 ivol2 = []
 x2 = []
 z2= []
 RSD2 = []
 
 for i in range(2,len(data1)):
   #print data[i]
   line = data1[i].strip()
   columns = data1[i].split()
   ivol1.append(str(columns[0]))
   x1.append(str(columns[1]))
   z1.append(str(columns[2]))
   RSD1.append(str(columns[3]))

 for i in range(2,len(data2)):
   #print data[i]
   line = data2[i].strip()
   columns = data2[i].split()
   ivol2.append(str(columns[0]))
   x2.append(str(columns[1]))
   z2.append(str(columns[2]))
   RSD2.append(str(columns[3]))
   
   #print x,z,RSD

 ndata1 = 100
 ndata2 = 100

 x1 = np.linspace(0., 1., ndata1)
 x2 = np.linspace(-1., 0., ndata2)
 z1 = np.linspace(0., 1., ndata1)
 z2 = np.linspace(0., 1., ndata2)
 RSD1 = np.reshape(RSD1, (-1, ndata1))
 RSD2 = np.reshape(RSD2, (-1, ndata2))

 X1, Y1 = meshgrid(x1, z1)
 X2, Y2 = meshgrid(x2, z2)

 # scipy interp. cubic
 f1 = interp2d(x1, z1, RSD1, kind='cubic')
 f2 = interp2d(x2, z2, RSD2, kind='cubic')
 xnew1 = np.arange(0, 1., .0005)
 xnew2 = np.arange(-1., 0., .0005)
 ynew = np.arange(0, 1., .0005)
 data1 = f1(xnew1,ynew)
 data2 = f2(xnew2,ynew)
 Xn1, Yn = np.meshgrid(xnew1, ynew)
 Xn2, Yn = np.meshgrid(xnew2, ynew)
 cs = plt.pcolormesh(Xn1, Yn, data1, cmap='BrBG', vmin=1.e-2, vmax=5)
 cs = plt.pcolormesh(Xn2, Yn, data2, cmap='BrBG', vmin=1.e-2, vmax=5)
 #plt.pcolormesh(Xn, Yn, data1, cmap='BrBG')
 cbar = plt.colorbar()
 cs.cmap.set_under('w')
 cbar.ax.set_ylabel('Root surface density (m$^{-2}$m$^{-3}$)', rotation=270, labelpad=20)
 plt.ylim(0,1.0)
 #plt.xlabel("x (m)", labelpad=20)
 plt.ylabel("z (m)", labelpad=20)
 xname = [-0.5,0.5]
 plt.axvline(x=0.0,color='k')
 labels = ['Without Beta','With Beta']
 plt.xticks(xname,labels)
 # plt.title('DAY = 94')
 plt.title('DAY = %d'%(counter+1))
 plt.tight_layout()
 plt.savefig('/home/renato/groimp_efficient/run_2c/paper_fig/RSD/RSD_%02d.png' %(counter+1), dpi=300)
 print 'Figure RSD_%s.png saved sucessfully!' %(counter+1)
 #plt.show()
 plt.close("all")

 #error.append(np.sum(RSD))
 biomrsd1.append(np.sum(np.array(RSD1).astype(np.float)))
 biomrsd2.append(np.sum(np.array(RSD2).astype(np.float)))

plt.plot(biomrsd1,'r--',label='With Beta')
plt.plot(biomrsd2,'r-',label='Without Beta')


plt.xlabel("Time (days)", labelpad=20)
plt.ylabel("Integrated root surface density (m$^{-2}$m$^{-3}$)", labelpad=20)
# plt.title('DAY = 94')
plt.legend()
plt.title('Dicot')
plt.tight_layout()
plt.savefig('/home/renato/groimp_efficient/run_2c/paper_fig/RSD/RSD_total.png')
#plt.show()

sys.exit()









