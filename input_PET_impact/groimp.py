#!/home/renato/anaconda2/bin/python

import numpy as np
import matplotlib.pyplot as plt
import os, sys
from scipy.interpolate import interp2d
from pylab import * 
import pandas as pd

counter = 0

while True:

	print "--------------------------------------------------------------------------"  
	print "------------------------ Start GroIMP 1.5 --------------------------------" 

	os.system("java -Xmx2000m -jar /home/renato/Downloads/GroIMP-1.5/core.jar --headless /home/renato/Downloads/FSPM_BASIC-master-transpired/project.gs")

	print "--------------------------------------------------------------------------"  
	print "------------------------ Reading PET from GroIMP 1.5 ---------------------" 

	df1 = pd.read_csv('/home/renato/groimp/transp.txt',header=0, names=['transpiration'])
	PET = df1.transpiration.values

	PET = np.array(PET)

	print "--------------------------------------------------------------------------"  
	print "--------------- Writing feddes.soi for Min3pArchiSImple ------------------" 

	df2 = pd.read_csv('/home/renato/groimp/input/feddes.soi',sep='\t',names=['time','ET','canopy_int','solar_ratio','scale_tree_growth','rub1','rub2','rub3'])

	df2.to_csv('/home/renato/groimp/input/feddes_original.soi',sep='\t', index=False, header=None)

	ET = df2.ET.values
	ET = np.array(ET)

	i = len(PET)

	#old_err_state = np.seterr(divide='ignore', invalid='ignore')
	#ignored_states = np.seterr(**old_err_state)

	beta = np.zeros(i)

	try:
    	   np.divide(ET[:i],PET,beta)
	except ZeroDivisionError:
    	   pass



	beta[beta > 1] = 1.0

	data = np.array([df2.time[:i].values,
                 PET[:i],
                 df2.canopy_int[:i].values,
                 df2.solar_ratio[:i].values,
                 df2.scale_tree_growth[:i].values]).T

	df3 = pd.DataFrame(data)

	df3.to_csv('/home/renato/groimp/input/feddes.soi',sep='\t', index=False, header=None )

	print "--------------------------------------------------------------------------"  
	print "--------------- Writing biomrac.txt for Min3pArchiSImple -----------------" 
	print "--------------------- from GroIMP1.5 ArchiSImple -------------------------" 

	os.system("cp /home/renato/groimp/input/biomrac.txt /home/renato/groimp/input/biomrac_ori.txt")

	df4 = pd.read_csv('/home/renato/groimp/root.txt',names=['rootbiom'],header = 0)

	data = np.array([df4.rootbiom.values/1000]).T

	df5 = pd.DataFrame(data)

	df5.to_csv('/home/renato/groimp/input/biomrac.txt',sep='\t', index=False, header=None )


	print "--------------------------------------------------------------------------"  
	print "------------------------- Start Min3pArchiSImple -------------------------" 
	print "--------------------------------------------------------------------------" 

	os.system("cd /home/renato/groimp/input")
	os.system("/home/renato/Desktop/Min3pArchi91/bin/main.exe")

	print "--------------------------------------------------------------------------"  
	print "------------------------- Calculating root water -------------------------" 
	print "------------------------- uptake from Min3pArchi -------------------------" 

	ET = []

	for count in range(0,i):
 
 	   df1 = pd.read_csv('feddes_%s.gsp' %count,
      	         delim_whitespace=True,skiprows=3,header=None,
                 names=["x", "y", "z", "h_w", "p_w", "s_w", "theta_w", "transp", "evap"])


 	   RSD = df1['transp'].values
	   RSD_sum = np.array(RSD).astype(np.float)

           ET.append(sum(RSD_sum))

        data = np.array(ET).T

        df3 = pd.DataFrame(data)

        df3.to_csv('/home/renato/groimp/ET_min3p.txt',sep='\t', index=False, header=None )

        beta = np.zeros(i)

        try:
           np.divide(ET,PET,beta)
        except ZeroDivisionError:
           pass

        data = np.array(beta).T

        df3 = pd.DataFrame(data)

        df3.to_csv('/home/renato/groimp/beta_0.xls',sep=',', index=False, header=None )

        

        print data

        df3.to_csv('/home/renato/groimp/beta_0_%s.xls' %(counter),sep=',', index=False, header=None )


        print "--------------------------------------------------------------------------"  
	print "------------------------- Printing -------------------------" 
	
        f = open('feddes_20.gsp',"r")

        #print f
        dataf = f.readlines()

        x = []
 	y = []
 	z= []
 	h_w= []
 	p_w= []
 	s_w= []
 	theta_w= []
 	transp= []
 	evap= []
 
 	for i in range(3,len(dataf)):
   	 #print data[i]
   	 line = dataf[i].strip()
   	 columns = dataf[i].split()
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

 	ndata = 50

 	x = np.linspace(0., 2., ndata)
 	z = np.linspace(0., 2., ndata)
 	transp = np.reshape(transp, (-1, ndata))

 	X, Y = meshgrid(x, z)

	 
 	# scipy interp. cubic
 	f = interp2d(x, z, transp, kind='cubic')
 	xnew = np.arange(0, 2, .01)
 	ynew = np.arange(0, 2, .01)
 	data1 = f(xnew,ynew)
 	Xn, Yn = np.meshgrid(xnew, ynew)
 	plt.pcolormesh(Xn, Yn, data1, cmap='jet', vmin=0, vmax=1e-9)
 	cbar = plt.colorbar()
 	cbar.ax.set_ylabel('Root water uptake (m$^{-2}$m$^{-3}$)', rotation=270, labelpad=20)
 	plt.xlabel("x (m)", labelpad=20)
 	plt.ylabel("z (m)", labelpad=20)
 	#plt.title('DAY = %d'%output_array[counter])
 	plt.title('DAY = 20 - Figure %s' %(counter))
 	plt.tight_layout()
 	plt.savefig('../figures/transp_20_%s.png' %(counter))
 	print 'Figure transp_%s.png saved sucessfully!' %(counter)
        plt.close("all")

        counter = counter + 1

        if np.any(data > 0.9):
            break





