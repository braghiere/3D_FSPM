
import numpy as np
import matplotlib.pyplot as plt
import os, sys
from scipy.interpolate import interp2d
from pylab import *
import pandas as pd

filelist=[]
filelist1=[]
filelist2=[]

#error = []
biomrsd1= []
biomrsd2= []


dirname1 = "/home/renato/groimp_efficient/run_2/"
dirname2 = "/home/renato/groimp_efficient/run_2c/"

dirname3 = "/home/renato/groimp_efficient/run_2a/"

dirname12 = "/home/renato/groimp_efficient/run_3/"
dirname22 = "/home/renato/groimp_efficient/run_3c/"

list = [94]
#for i in range(60,61):
for i in range(1,61):
#for i in list:
    filelist.append("RSD_2D_MIN3P%s.txt" %i)
    filelist1.append("RSD_2D_%s.txt" %i)
    filelist2.append("RSD_2D_%s_2.txt" %i)

#print filelist

for fname in filelist:

 counter = filelist.index(fname)

 fname1 = filelist1[counter]
 fname2 = filelist2[counter]

 #counter = 93
 #ISO
 f1 = open(os.path.join(dirname1,fname),"r")
 #ISO_beta
 f2 = open(os.path.join(dirname2,fname),"r")
 #Inter
 f12 = open(os.path.join(dirname12,fname2),"r")
 #Inter_beta
 f22 = open(os.path.join(dirname22,fname2),"r")

 f3 = open(os.path.join(dirname3,fname1),"r")
 f31 = open(os.path.join(dirname3,fname2),"r")


 #print f
 data1 = f1.readlines()
 data2 = f2.readlines()

 data12 = f12.readlines()
 data22 = f22.readlines()

 data3 = f3.readlines()
 data31 = f31.readlines()

 ivol1 = []
 x1 = []
 z1= []
 RSD1 = []

 ivol2 = []
 x2 = []
 z2= []
 RSD2 = []

 RSD12= []
 RSD22= []

 RSD3= []
 RSD31= []
 
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

 for i in range(1,len(data12)):
   #print data[i]
   line = data12[i].strip()
   columns = data12[i].split()
   RSD12.append(str(columns[3]))


 for i in range(1,len(data22)):
   #print data[i]
   line = data22[i].strip()
   columns = data22[i].split()
   RSD22.append(str(columns[3]))

 for i in range(1,len(data3)):
   #print data[i]
   line = data3[i].strip()
   columns = data3[i].split()
   RSD3.append(str(columns[3]))

 for i in range(1,len(data31)):
   #print data31[i]
   line = data31[i].strip()
   columns = data31[i].split()
   RSD31.append(str(columns[3]))

 print len(RSD3),len(RSD31)
 print RSD3[0],RSD31[0]
   
   #print x,z,RSD

 ndata1 = 100
 ndata2 = 100

 x1 = np.linspace(0., 1., ndata1)
 x2 = np.linspace(-1., 0., ndata2)
 z1 = np.linspace(0., 1., ndata1)
 z2 = np.linspace(0., 1., ndata2)

 RSD1 = np.reshape(RSD1, (-1, ndata1))
 RSD2 = np.reshape(RSD2, (-1, ndata2))

 RSD12 = np.reshape(RSD12, (-1, ndata1))
 RSD22 = np.reshape(RSD22, (-1, ndata1))

 RSD3 = np.reshape(RSD3, (-1, ndata1))
 RSD31 = np.reshape(RSD31, (-1, ndata1))

 X1, Y1 = meshgrid(x1, z1)
 X2, Y2 = meshgrid(x2, z2)


 # scipy interp. cubic
 f1 = interp2d(x1, z1, RSD1, kind='linear')
 f2 = interp2d(x2, z2, RSD2, kind='linear')

 f12 = interp2d(x1, z1, RSD12, kind='linear')
 f22 = interp2d(x2, z2, RSD22, kind='linear')

 f3 = interp2d(x1, z1, RSD3, kind='linear')
 f31 = interp2d(x2, z2, RSD31, kind='linear')

 xnew1 = np.arange(0, 1., .01)
 xnew2 = np.arange(-1., 0., .01)
 ynew = np.arange(0, 1., .01)

 data1 = f1(xnew1,ynew)
 data2 = f2(xnew2,ynew)
 data12 = f12(xnew1,ynew)
 data22 = f22(xnew2,ynew)

 data3 = f3(xnew1,ynew)
 data31 = f31(xnew2,ynew)

 Xn1, Yn = np.meshgrid(xnew1, ynew)
 Xn2, Yn = np.meshgrid(xnew2, ynew)



 plt.title('DAY = %d'%(counter+1))
 plt.semilogx(np.sum(data1,axis=1), ynew, 'k', label='Iso')
 plt.semilogx(np.sum(data2,axis=1), ynew, 'k--', label='Iso_beta')
 plt.semilogx(np.sum(data3,axis=1), ynew, 'b--', label='Mono_beta (A)')
 plt.semilogx(np.sum(data31,axis=1), ynew, 'b-.', label='Mono_beta (B)')
 plt.semilogx(np.sum(data12,axis=1), ynew, 'r', label='Inter')
 plt.semilogx(np.sum(data22,axis=1), ynew, 'r--', label='Inter_beta')


 plt.grid(True)
 plt.ylabel("z (m)", labelpad=20)
 plt.xlabel("Total root surface density (m$^{-2}$m$^{-3}$)", labelpad=20)
 plt.legend()
 plt.tight_layout()
 plt.xlim(0.01,1000.)
 plt.ylim(0.,1.0)
 plt.savefig('/home/renato/groimp_efficient/run_2c/paper_fig/RSD_vertical/RSD_vertical_%02d.png' %(counter+1),dpi=300)
 print 'RSD_vertical_%02d.png' %(counter+1)
 plt.close("all")
 #plt.show()
sys.exit()




