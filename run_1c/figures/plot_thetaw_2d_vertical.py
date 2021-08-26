
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


dirname1 = "/home/renato/groimp_efficient/run_1/"
dirname2 = "/home/renato/groimp_efficient/run_1c/"

dirname12 = "/home/renato/groimp_efficient/run_3/"
dirname22 = "/home/renato/groimp_efficient/run_3c/"

list = [94]
#for i in range(60,61):
for i in range(1,61):
#for i in list:
    filelist.append("feddes_%s.gsp" %i)
    filelist2.append("water_%s.gsp" %i)

#print filelist

for fname in filelist:

 counter = filelist.index(fname)

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

 #print f
 data1 = f1.readlines()
 data2 = f2.readlines()

 data12 = f12.readlines()
 data22 = f22.readlines()

 x1 = []
 y1 = []
 z1 = []
 h_w1 = []
 p_w1 = []
 s_w1 = []
 theta_w1 = []
 transp1 = []
 evap1 = []

 x2 = []
 y2 = []
 z2 = []
 h_w2 = []
 p_w2 = []
 s_w2 = []
 theta_w2 = []
 transp2 = []
 evap2 = []

 x12 = []
 y12 = []
 z12 = []
 h_w12 = []
 p_w12 = []
 s_w12 = []
 theta_w12 = []
 transp12 = []
 evap12 = []
 transp122 = []
 transp1tot = []

 x22 = []
 y22 = []
 z22 = []
 h_w22 = []
 p_w22 = []
 s_w22 = []
 theta_w22 = []
 transp22 = []
 evap22 = []
 transp222 = []
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

 for i in range(3,len(data12)):
   #print data[i]
   line = data12[i].strip()
   columns = data12[i].split()
   x12.append(str(columns[0]))
   y12.append(str(columns[1]))
   z12.append(str(columns[2]))
   h_w12.append(str(columns[3]))
   p_w12.append(str(columns[4]))
   s_w12.append(str(columns[5]))
   theta_w12.append(str(columns[6]))
   transp12.append(str(columns[7]))
   evap12.append(str(columns[8]))
   transp122.append(str(columns[9]))
   transp1tot.append(str(columns[10]))

 for i in range(3,len(data22)):
   #print data[i]
   line = data22[i].strip()
   columns = data22[i].split()
   x22.append(str(columns[0]))
   y22.append(str(columns[1]))
   z22.append(str(columns[2]))
   h_w22.append(str(columns[3]))
   p_w22.append(str(columns[4]))
   s_w22.append(str(columns[5]))
   theta_w22.append(str(columns[6]))
   transp22.append(str(columns[7]))
   evap22.append(str(columns[8]))
   transp222.append(str(columns[9]))
   transp2tot.append(str(columns[10]))
   
   #print x,z,RSD

 ndata1 = 100
 ndata2 = 100

 x1 = np.linspace(0., 1., ndata1)
 x2 = np.linspace(-1., 0., ndata2)
 z1 = np.linspace(0., 1., ndata1)
 z2 = np.linspace(0., 1., ndata2)

 theta_w1 = np.reshape(theta_w1, (-1, ndata1))
 theta_w12 = np.reshape(theta_w12, (-1, ndata1))


 theta_w2 = np.reshape(theta_w2, (-1, ndata2))
 theta_w22 = np.reshape(theta_w22, (-1, ndata2))


 X1, Y1 = meshgrid(x1, z1)
 X2, Y2 = meshgrid(x2, z2)


 # scipy interp. cubic
 f1 = interp2d(x1, z1, theta_w1, kind='cubic')
 f2 = interp2d(x2, z2, theta_w2, kind='cubic')

 f12 = interp2d(x1, z1, theta_w12, kind='cubic')
 f22 = interp2d(x2, z2, theta_w22, kind='cubic')

 xnew1 = np.arange(0, 1., .001)
 xnew2 = np.arange(-1., 0., .001)
 ynew = np.arange(0, 1., .001)
 data1 = f1(xnew1,ynew)
 data2 = f2(xnew2,ynew)
 data12 = f12(xnew1,ynew)
 data22 = f22(xnew2,ynew)

 Xn1, Yn = np.meshgrid(xnew1, ynew)
 Xn2, Yn = np.meshgrid(xnew2, ynew)



 plt.title('DAY = %d'%(counter+1))
 plt.plot(np.mean(data1,axis=0), ynew, 'k', label='Iso')
 plt.plot(np.mean(data2,axis=0), ynew, 'r', label='Iso_beta')
 plt.plot(np.mean(data12,axis=0), ynew, 'k--', label='Inter')
 plt.plot(np.mean(data22,axis=0), ynew, 'r--', label='Inter_beta')

 plt.ylabel("z (m)", labelpad=20)
 plt.xlabel("Soil moisture availability", labelpad=20)
 plt.legend()
 plt.tight_layout()
 plt.xlim(0,1.0)
 plt.ylim(0.,1.0)
 plt.savefig('/home/renato/groimp_efficient/run_1c/paper_fig/theta_vertical/theta_vertical_%02d.png' %(counter+1),dpi=300)
 print 'theta_vertical_%02d.png' %(counter+1)
 plt.close("all")
 #plt.show()
sys.exit()




