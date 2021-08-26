
import numpy as np
import matplotlib.pyplot as plt
import os, sys
from scipy.interpolate import interp2d
from pylab import *

filelist1=[]
filelist2=[]
filelist3=[]

element =[]

biomrsd1= []
biomrsd2= []
biomrsd3= []

dirname = "/home/renato/groimp_efficient/run_3c/"

for i in range(1,61):
    element.append(i)
#print filelist

for fnumber in element:

 counter = element.index(fnumber)


 f1 = open(os.path.join(dirname,"RSD_2D_%s.txt" %fnumber),"r")
 f2 = open(os.path.join(dirname,"RSD_2D_%s_2.txt" %fnumber),"r")
 f3 = open(os.path.join(dirname,"RSD_tot_2D_MIN3P%s.txt" %fnumber),"r")

 #print f
 data1 = f1.readlines()
 data2 = f2.readlines()
 data3 = f3.readlines()

 ivol = []
 x1 = []
 z1= []
 x2 = []
 z2= []
 x3 = []
 z3= []
 RSD1= []
 RSD2= []
 RSD3= []
 
 for i in range(1,len(data1)):
   #print data[i]
   line = data1[i].strip()
   columns = data1[i].split()
   ivol.append(str(columns[0]))
   x1.append(str(columns[1]))
   z1.append(str(columns[2]))
   RSD1.append(str(columns[3]))


 for i in range(1,len(data2)):
   #print data[i]
   line = data2[i].strip()
   columns = data2[i].split()
   ivol.append(str(columns[0]))
   x2.append(str(columns[1]))
   z2.append(str(columns[2]))
   RSD2.append(str(columns[3]))

 for i in range(2,len(data3)):
   #print data[i]
   line = data3[i].strip()
   columns = data3[i].split()
   ivol.append(str(columns[0]))
   x3.append(str(columns[1]))
   z3.append(str(columns[2]))
   RSD3.append(str(columns[3]))
   
   #print x,z,RSD
 ndata = 100

 x = np.linspace(0., 1., ndata)
 z = np.linspace(0., 1., ndata)
 RSD1 = np.reshape(RSD1, (-1, ndata))
 RSD2 = np.reshape(RSD2, (-1, ndata))
 RSD3 = np.reshape(RSD3, (-1, ndata))

 X, Y = meshgrid(x, z)

 # simple fast plot
 #plt.pcolor(X, Y, RSD, vmin=0, vmax=20)
 #plt.colorbar()
 #plt.savefig('images/RSD_%s.png' %counter)
 #plt.close("all")

 # scipy interp. cubic
 f = interp2d(x, z, RSD3, kind='cubic')
 xnew = np.arange(0, 1., .0005)
 ynew = np.arange(0, 1., .0005)
 data1 = f(xnew,ynew)
 Xn, Yn = np.meshgrid(xnew, ynew)
 cs = plt.pcolormesh(Xn, Yn, data1, cmap='BrBG', vmin=1.e-2, vmax=5)
 cs.cmap.set_under('w')
 cbar = plt.colorbar()
 cbar.ax.set_ylabel('Root surface density (m$^{-2}$m$^{-3}$)', rotation=270, labelpad=20)
 plt.ylim(0.,1.0)
 plt.xlim(0.,1.0)
 plt.xlabel("x (m)", labelpad=20)
 plt.ylabel("z (m)", labelpad=20)
 plt.title('DAY = %d'%(counter+1))
 plt.grid()
 plt.tight_layout()
 plt.savefig('/home/renato/groimp_efficient/run_3c/figures/RSD/run_3c_RSD_%02d.png' %(counter+1),dpi=300)
 print 'Figure RSD_%s.png saved sucessfully!' %(counter+1)
 plt.close("all")

 #error.append(np.sum(RSD))
 biomrsd1.append(np.sum(np.array(RSD1).astype(np.float)))
 biomrsd2.append(np.sum(np.array(RSD2).astype(np.float)))
 biomrsd3.append(np.sum(np.array(RSD3).astype(np.float)))

plt.plot(biomrsd1,label='Monocot')
plt.plot(biomrsd2,label='Dicot')
plt.plot(biomrsd3,label='Total')

plt.xlabel("Time (days)", labelpad=20)
plt.ylabel("Integrated root surface density (m$^{-2}$m$^{-3}$)", labelpad=20)
# plt.title('DAY = 94')
plt.legend()
plt.title('Two roots')
plt.tight_layout()
plt.savefig('RSD/RSD_total.png')
#plt.show()

sys.exit()










