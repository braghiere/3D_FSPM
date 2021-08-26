
import numpy as np
import matplotlib.pyplot as plt
import os, sys
from scipy.interpolate import interp2d
from pylab import *
import pandas as pd

filelist=[]
filelist2=[]

#error = []
biomrsd1= []
biomrsd2= []

#ISO
dirname11 = "/home/renato/groimp_efficient/run_2/"
#ISO_beta
dirname12 = "/home/renato/groimp_efficient/run_2c/"
#MONO
dirname21 = "/home/renato/groimp_efficient/run_2d/"
#MONO_beta
dirname22 = "/home/renato/groimp_efficient/run_2a/"
#INTER
dirname31 = "/home/renato/groimp_efficient/run_3/"
#INTER_beta
dirname32 = "/home/renato/groimp_efficient/run_3c/"

list = [94]
#for i in range(60,61):
for i in range(1,61):
#for i in list:
    filelist.append("RSD_2D_MIN3P%s.txt" %i)
    filelist2.append("RSD_2D_%s_2.txt" %i)


#print filelist

for fname in filelist:

 counter = filelist.index(fname)

 fname2 = filelist2[counter]
 #counter = 93
 #ISO
 f11 = open(os.path.join(dirname11,fname),"r")
 #ISO_beta
 f12 = open(os.path.join(dirname12,fname),"r")

 #Mono
 f21 = open(os.path.join(dirname21,fname2),"r")
 #Mono_beta
 f22 = open(os.path.join(dirname22,fname2),"r")

 #Inter
 f31 = open(os.path.join(dirname31,fname2),"r")
 #Mono_beta
 f32 = open(os.path.join(dirname32,fname2),"r")

 #print f
 data11 = f11.readlines()
 data12 = f12.readlines()

 data21 = f21.readlines()
 data22 = f22.readlines()

 data31 = f31.readlines()
 data32 = f32.readlines()

 ivol1 = []
 x1 = []
 z1= []
 RSD11 = []

 ivol2 = []
 x2 = []
 z2= []
 RSD12 = []

 RSD21= []
 RSD22= []

 RSD31= []
 RSD32= []
 
 for i in range(2,len(data11)):
   #print data[i]
   line = data11[i].strip()
   columns = data11[i].split()
   ivol1.append(str(columns[0]))
   x1.append(str(columns[1]))
   z1.append(str(columns[2]))
   RSD11.append(str(columns[3]))

 for i in range(2,len(data12)):
   #print data[i]
   line = data12[i].strip()
   columns = data12[i].split()
   ivol2.append(str(columns[0]))
   x2.append(str(columns[1]))
   z2.append(str(columns[2]))
   RSD12.append(str(columns[3]))

 for i in range(1,len(data21)):
   #print data[i]
   line = data21[i].strip()
   columns = data21[i].split()
   RSD21.append(str(columns[3]))

 for i in range(1,len(data22)):
   #print data[i]
   line = data22[i].strip()
   columns = data22[i].split()
   RSD22.append(str(columns[3]))

 for i in range(1,len(data31)):
   #print data[i]
   line = data31[i].strip()
   columns = data31[i].split()
   RSD31.append(str(columns[3]))

 for i in range(1,len(data32)):
   #print data[i]
   line = data32[i].strip()
   columns = data32[i].split()
   RSD32.append(str(columns[3]))

   
   #print x,z,RSD

 ndata1 = 100
 ndata2 = 100

 x1 = np.linspace(0., 1., ndata1)
 x2 = np.linspace(-1., 0., ndata2)
 z1 = np.linspace(0., 1., ndata1)
 z2 = np.linspace(0., 1., ndata2)
 RSD11 = np.reshape(RSD11, (-1, ndata1))
 RSD12 = np.reshape(RSD12, (-1, ndata1))

 RSD21 = np.reshape(RSD21, (-1, ndata1))
 RSD22 = np.reshape(RSD22, (-1, ndata1))

 RSD31 = np.reshape(RSD31, (-1, ndata1))
 RSD32 = np.reshape(RSD32, (-1, ndata1))

 X1, Y1 = meshgrid(x1, z1)
 X2, Y2 = meshgrid(x2, z2)


 # scipy interp. cubic
 f11 = interp2d(x2, z1, RSD11, kind='cubic')
 f12 = interp2d(x2, z2, RSD12, kind='cubic')

 f21 = interp2d(x2, z1, RSD21, kind='cubic')
 f22 = interp2d(x2, z2, RSD22, kind='cubic')

 f31 = interp2d(x2, z1, RSD31, kind='cubic')
 f32 = interp2d(x2, z2, RSD32, kind='cubic')

 xnew1 = np.arange(0, 1., .0005)
 xnew2 = np.arange(-1., 0., .0005)
 ynew = np.arange(0, 1., .0005)

 data11 = f11(xnew2,ynew)
 data12 = f12(xnew2,ynew)

 data21 = f21(xnew2,ynew)
 data22 = f22(xnew2,ynew)

 data31 = f31(xnew2,ynew)
 data32 = f32(xnew2,ynew)

 Xn1, Yn = np.meshgrid(xnew1, ynew)
 Xn2, Yn = np.meshgrid(xnew2, ynew)



 plt.title('DAY = %d'%(counter+1))
 plt.plot( ynew,np.mean(data11,axis=0), 'k', label='Iso')
 plt.plot( ynew,np.mean(data12,axis=0),  'k--', label='Iso_beta')
 plt.plot( ynew- 0.1,np.mean(data21,axis=0),  'b', label='Mono (plant B)')
 plt.plot( ynew- 0.1,np.mean(data22,axis=0),  'b--', label='Mono_beta (plant B)')
 plt.plot( ynew- 0.1,np.mean(data31,axis=0),  'r', label='Inter')
 plt.plot( ynew- 0.1,np.mean(data32,axis=0),  'r--', label='Inter_beta')


 plt.grid(True)
 plt.xlabel("x (m)", labelpad=20)
 plt.ylabel("Mean root surface density (m$^{-2}$m$^{-3}$)", labelpad=20)
 plt.legend(loc=3)

 plt.tight_layout()
 plt.xlim(0.0,1.)
 plt.ylim(1.,0.0)
 plt.savefig('/home/renato/groimp_efficient/analysis_paper/figures/10_cm/dicot/RSD_horizontal/RSD_horizontal_%02d.png' %(counter+1),dpi=300)
 print 'RSD_horizontal_%02d.png' %(counter+1)
 plt.close("all")
 #plt.show()
sys.exit()




