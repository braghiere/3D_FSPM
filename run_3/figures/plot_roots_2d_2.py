
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

biomrsd12= []
biomrsd22= []
biomrsd32= []

dirname1 = "/home/renato/groimp_efficient/run_3/"
dirname2 = "/home/renato/groimp_efficient/run_3c/"

for i in range(1,61):
    element.append(i)
#print filelist

for fnumber in element:

 counter = element.index(fnumber)


 f1 = open(os.path.join(dirname1,"RSD_2D_%s.txt" %fnumber),"r")
 f2 = open(os.path.join(dirname1,"RSD_2D_%s_2.txt" %fnumber),"r")
 f3 = open(os.path.join(dirname1,"RSD_tot_2D_MIN3P%s.txt" %fnumber),"r")

 f12 = open(os.path.join(dirname2,"RSD_2D_%s.txt" %fnumber),"r")
 f22 = open(os.path.join(dirname2,"RSD_2D_%s_2.txt" %fnumber),"r")
 f32 = open(os.path.join(dirname2,"RSD_tot_2D_MIN3P%s.txt" %fnumber),"r")



 #print f
 data1 = f1.readlines()
 data2 = f2.readlines()
 data3 = f3.readlines()

 data12 = f12.readlines()
 data22 = f22.readlines()
 data32 = f32.readlines()


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

 RSD12= []
 RSD22= []
 RSD32= []
 
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

 for i in range(2,len(data12)):
   #print data[i]
   line = data12[i].strip()
   columns = data12[i].split()
   RSD12.append(str(columns[3]))

 for i in range(2,len(data22)):
   #print data[i]
   line = data22[i].strip()
   columns = data22[i].split()
   RSD22.append(str(columns[3]))

 for i in range(2,len(data32)):
   #print data[i]
   line = data32[i].strip()
   columns = data32[i].split()
   RSD32.append(str(columns[3]))
   
   #print x,z,RSD
 ndata = 100

 x = np.linspace(0., 1., ndata)
 x_2 = np.linspace(-1., 0., ndata)
 z = np.linspace(0., 1., ndata)
 RSD1 = np.reshape(RSD1, (-1, ndata))
 RSD2 = np.reshape(RSD2, (-1, ndata))
 RSD3 = np.reshape(RSD3, (-1, ndata))

 RSD32 = np.reshape(RSD32, (-1, ndata))

 X, Y = meshgrid(x, z)
 X2, Y = meshgrid(x_2, z)

 # simple fast plot
 #plt.pcolor(X, Y, RSD, vmin=0, vmax=20)
 #plt.colorbar()
 #plt.savefig('images/RSD_%s.png' %counter)
 #plt.close("all")

 # scipy interp. cubic
 f = interp2d(x, z, RSD3, kind='cubic')
 f2 = interp2d(x_2, z, RSD32, kind='cubic')
 xnew = np.arange(0, 1., .0005)
 xnew2 = np.arange(-1, 0., .0005)
 ynew = np.arange(0, 1., .0005)
 data1 = f(xnew,ynew)
 data2 = f2(xnew2,ynew)
 Xn, Yn = np.meshgrid(xnew, ynew)
 Xn2, Yn = np.meshgrid(xnew2, ynew)
 cs = plt.pcolormesh(Xn, Yn, data1, cmap='BrBG', vmin=1.e-2, vmax=5)
 cs = plt.pcolormesh(Xn2, Yn, data2, cmap='BrBG', vmin=1.e-2, vmax=5)
 cs.cmap.set_under('w')
 cbar = plt.colorbar()
 cbar.ax.set_ylabel('Root surface density (m$^{-2}$m$^{-3}$)', rotation=270, labelpad=20)
 xname = [-0.5,0.5]
 labels = ['Without Beta','With Beta']
 plt.xticks(xname,labels)
 plt.xlim(-1.,1.)
 plt.ylim(0.,1.0)
 plt.axvline(x=0.0,color='k')
 plt.xlabel("x (m)", labelpad=20)
 plt.ylabel("z (m)", labelpad=20)
 plt.title('DAY = %d'%(counter+1))
 plt.tight_layout()
 plt.savefig('RSD/RSD_%s.png' %(counter+1), dpi =300)
 #plt.show()
 print 'Figure RSD_%s.png saved sucessfully!' %(counter+1)
 plt.close("all")

 #error.append(np.sum(RSD))
 biomrsd1.append(np.sum(np.array(RSD1).astype(np.float)))
 biomrsd2.append(np.sum(np.array(RSD2).astype(np.float)))
 biomrsd3.append(np.sum(np.array(RSD3).astype(np.float)))

 biomrsd12.append(np.sum(np.array(RSD12).astype(np.float)))
 biomrsd22.append(np.sum(np.array(RSD22).astype(np.float)))
 biomrsd32.append(np.sum(np.array(RSD32).astype(np.float)))

 print ' run_3: monocot =', biomrsd1[counter]
 print ' run_3c: monocot =', biomrsd12[counter]

plt.plot(biomrsd1,'b-',label='Monocot')
plt.plot(biomrsd2,'r-',label='Dicot')
plt.plot(biomrsd3,'k-',label='Total')

plt.plot(biomrsd12,'b--',label='Monocot')
plt.plot(biomrsd22,'r--',label='Dicot')
plt.plot(biomrsd32,'k--',label='Total')

plt.xlabel("Time (days)", labelpad=20)
plt.ylabel("Integrated root surface density (m$^{-2}$m$^{-3}$)", labelpad=20)
# plt.title('DAY = 94')
plt.legend()
plt.title('Two roots')
plt.tight_layout()
plt.savefig('RSD/RSD_total.png')
#plt.show()

sys.exit()










