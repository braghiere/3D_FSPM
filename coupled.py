from __future__ import print_function, absolute_import, division

import matplotlib.pyplot as plt
import numpy as np
import _min3p 
import f90wrap.runtime
import logging
import os
import sys
import time
from goto import goto, comefrom, label

import ctypes 
from struct import *

lib = ctypes.cdll.LoadLibrary('/home/renato/Desktop/Min3pArchi91_reconstruc/ArchiSimple/_ArchiSimple.so')

import min3p_ofi_time as min3p

def main():

    min3p.gen.show_module = True
    min3p.gen.analyt_deriv_rt = False

    #welcome the user and read problem read prefix name

    min3p.welcome() 

    #open problem specific input file, generic output file
    #and scratch file for temporary data storage
 
    min3p.opngfls()

    #initialize global control parameters
 
    min3p.initcpgs()

    #define constants for global use
 
    min3p.constnts()

    #initialize variably saturated flow and/or reactive transport simulation 
    #or initialize equilibrium or reaction path simulation

    min3p.initprob()

    #equilibrium or reaction path simulation

    if (not min3p.gen.reactive_transport and min3p.gen.geo_chemistry):
	min3p.batreac()

    #reset problem size for reaction-transport problem

    if (min3p.gen.reactive_transport):
	min3p.setsize(min3p.gen.redox_equil_rt)
	if (min3p.chem.nm > 0):
           min3p.chem.finite_minerals = True

    #open files for postprocessing 
 
    if (min3p.gen.varsat_flow or min3p.gen.reactive_transport):
	min3p.opnpgfls()
    #write initial contour data to output file
    #and define next output time
      
    if (min3p.gen.varsat_flow or min3p.gen.reactive_transport):
        min3p.gen.initial_condition = True
        min3p.gen.igstime = 0
        if (min3p.gen.gs_output):
          if (min3p.gen.varsat_flow):
            min3p.outputvs()
          if (min3p.gen.reactive_transport):
            min3p.outputrt()
          min3p.gen.igstime = 1
          min3p.gen.initial_condition = False

    #write initial condition of transient data to output file
 
    if (min3p.gen.reactive_transport):
        if (min3p.gen.gb_output):
          for igb in range(1, min3p.gen.ngb + 1):
          #assign unit numbers for output of transient data
            min3p.tranunit(igb)

            ivol = min3p.gen.ngb_vol(igb)

              #FG, 3, April 08 quick fix to enable simulation 
              #with no gas species explicitly considered
            if (min3p.chem.ng == 0 and min3p.chem.nm != 0): 

             #FG, 3, new subroutine without gaz related arrays and the unit number
                min3p.tprfrtlcg0(totcnew(1,ivol),cnew(1,ivol),cx(1,ivol), 
                        gamma(1,ivol),gamma(nc-1,ivol),
                        cmnew(1,ivol),
                        cec_g(ivol),distcoff_rt(1,ivol),
                        area(1,ivol),phi(1,ivol),phiold(1,ivol),
                        sionnew(ivol),tkel(ivol),hhead(ivol),
                        zg(ivol),time_io,delt,sanew(ivol),
                        pornew(ivol),igbt,igbc,igbm,igbgr,igbi,
                        igbb,igbs,igbv,igbd,igbx,prefix,l_prfx,
                        tec_header,ivol,0,zone_name,l_zone_name,
                        update_porosity)
            
	    elif (min3p.chem.nm == 0 and min3p.chem.ng != 0):
                  #FG, 4, April 08 quick fix to enable simulation 
                  #without reacting mineral

             #FG, 4, new subroutine without reacting mineral 
             #related arrays and unit numbers
                min3p.tprfrtlcm0(totcnew(1,ivol),cnew(1,ivol),cx(1,ivol), 
                        gamma(1,ivol),gamma(nc-1,ivol),
                        gnew(1,ivol),cec_g(ivol),distcoff_rt(1,ivol),
                        sionnew(ivol),tkel(ivol),hhead(ivol),
                        zg(ivol),time_io,delt,sanew(ivol),
                        pornew(ivol),igbt,igbc,igbm,igbg,igbgr,igbi,
                        igbb,igbx,prefix,l_prfx,
                        tec_header,ivol,0,zone_name,l_zone_name,
                        update_porosity)

            elif (min3p.chem.nm == 0 and min3p.chem.ng != 0):
             #FG, 4,  required if no mineral and no gaz specified, 
             #in order to warn user that it won't work as it
             print('warning: the simulation will fail since no mineral AND no gas specified')
	     sys.exit("Error message")

            else: 
             #FG, 3, 4 if neither ng = 0 nor nm = 0  (initial subroutine)  
                min3p.tprfrtlc(totcnew(1,ivol),cnew(1,ivol),cx(1,ivol),
                         gamma(1,ivol),gamma(nc-1,ivol),cmnew(1,ivol),
                         gnew(1,ivol),cec_g(ivol),distcoff_rt(1,ivol),
                         area(1,ivol),phi(1,ivol),phiold(1,ivol),
                         sionnew(ivol),tkel(ivol),hhead(ivol),
                         zg(ivol),time_io,delt,sanew(ivol),
                         pornew(ivol),igbt,igbc,igbm,igbg,igbgr,igbi,
                         igbb,igbs,igbv,igbd,igbx,prefix,l_prfx,
                         tec_header,ivol,0,zone_name,l_zone_name,
                         update_porosity)

    if (min3p.gen.varsat_flow):
        #initialize iteration parameters for variably saturated flow
        min3p.gen.ittot_vs = 0
        min3p.gen.itseep_tot = 0
        min3p.gen.itsolvtot_vs = 0

        # CB initialize Archisimple: 
        sR = lib.INIT_ARCHI()
        #print('sR=',sR)

        #  pause
        #  steady state flow
        if (min3p.gen.steady_flow):
          min3p.stedflow()


    #compute initial system mass - variably saturated flow
    #transient conditions

    if (min3p.gen.varsat_flow and min3p.gen.transient_flow and min3p.gen.mass_balance_vs):
        min3p.msysvs()


    #compute initial system mass - reactive transport

    if (min3p.gen.mass_balance_rt):
        min3p.msysrt()


    #transient simulation for variably saturated flow and 
    #reactive transport
    if ((min3p.gen.varsat_flow and min3p.gen.transient_flow) or min3p.gen.reactive_transport):
         #timeloop.f in python 
         #reactive transport    
         r0 = 0.
         rhalf = 0.5
         r86400 = 8.64e4
         tiny_time = 1.e-10
         tiny = 1.0e-300
 
         #initialize time stepping and iteration parameters for 
         #reactive transport
         min3p.gen.mtime = 0
         min3p.gen.reduce_timestep = 0
         min3p.gen.mtime_f = 0
         min3p.gen.igb_step = 0
	 min3p.gen.csec = 0 

         #initialize chemical water source/sink term 
	 if (min3p.gen.chemical_water):
            min3p.zero_r8(min3p.gen.qwater,min3p.gen.nn,1,1) 

         #initialize skip variable
	 min3p.gen.nskip = 0

         #c_restart added 20070130
	 min3p.gen.rsrt_cnt = r0

         if (min3p.gen.restart_sim):
	    min3p.restart_r()
	    min3p.gen.time = min3p.gen.time_io*min3p.gen.time_factor
	    min3p.gen.restart_sim= False

         if (min3p.gen.reactive_transport):
            min3p.gen.ittot_rt = 0
            min3p.gen.itsolvtot_rt = 0
            if (min3p.gen.update_activity_rt == 'no_update'):
                min3p.gen.update_activity = 'no_update'
            elif (min3p.gen.update_activity_rt == 'time_lagged'):
                min3p.gen.update_activity = 'time_lagged'
            elif (min3p.gen.update_activity_rt == 'double_update'):
                min3p.gen.update_activity = 'double_update'

         print(' enter timeloop')
         print(' ----------------------------------------------------------------')
         #write(ilog,'(a)')'enter timeloop'
         #write(ilog,'(72a)')('-',i=1,72)
         
         #time loop
         #exit time loop based upon final solution time 
         while (min3p.gen.time < (min3p.gen.tfinal-tiny_time)):
               min3p.gen.mtime = min3p.gen.mtime + 1

               #variable time stepping

               if (min3p.gen.mtime == 1 and (not min3p.gen.restart_sim)): 

	         if (min3p.gen.varsat_flow and min3p.gen.reactive_transport):
                    #initialize iupsg variable 
                    #(updated after each N-R iteration, in reactran)
                    
                    iupsg = []
	            for i1 in range(1,min3p.gen.njavs):
	               iupsg.append('a')

               elif (min3p.gen.mtime > 1 or min3p.gen.restart_sim):

                     #assign new time step for global simulation
                     #flow and reactive transport

                     if (min3p.gen.varsat_flow and min3p.gen.reactive_transport):
                        if (min3p.gen.transient_flow and min3p.gen.variably_saturated):
                              min3p.gen.delt = min(min3p.gen.delt_vs,min3p.gen.delt_rt)
                        else:
                              min3p.gen.delt = min3p.gen.delt_rt  

                       #flow only

                     elif (min3p.gen.varsat_flow and (not min3p.gen.reactive_transport)):
                          if (min3p.gen.transient_flow and min3p.gen.variably_saturated):
                             min3p.gen.delt = min3p.gen.delt_vs  
                          else:
                             min3p.gen.delt = min3p.gen.delt   

                       #reactive transport only

                     elif ((not min3p.gen.varsat_flow) and (min3p.gen.reactive_transport)):
                            min3p.gen.delt = min3p.gen.delt_rt  


                     #adjust time step to target read times for transient
                     #boundary conditions
                     #for variably saturated flow

                     if (min3p.gen.update_bcvs):
	               if ((min3p.gen.time + min3p.gen.delt) > (min3p.gen.time_bcvs*min3p.gen.time_factor)):
	                  min3p.gen.delt = min3p.gen.time_bcvs*min3p.gen.time_factor-gen.time
	                  min3p.gen.delt = max(min3p.gen.delt, min3p.gen.deltmin)
                          #print('first max/ delt = ',gen.delt )

                     #adjust time step to target read times for updating soil
                     # specific  parameters

                     if (min3p.biol.root_uptake):
	               if ((min3p.gen.time+min3p.gen.delt) > (min3p.biol.time_soi*min3p.gen.time_factor)):
	                  min3p.gen.delt = min3p.gen.time_soi*min3p.gen.time_factor-min3p.gen.time
	                  min3p.gen.delt = max(min3p.gen.delt,min3p.gen.deltmin)
                          #print('second max/ delt = ',gen.delt )      

               #maximum number of iterations exceeded, time step guess was poor,
               #reduce time step size 

               goto .onethousand

               label .ninehundredninetynine

               min3p.gen.time = min3p.gen.time - min3p.gen.delt
               min3p.gen.mtime_f = min3p.gen.mtime_f + 1
               min3p.gen.reduce_timestep = False
               #gen.reduce_timestep = 0
               min3p.gen.delt = rhalf*min3p.gen.delt  #additional time step reduction

               label .onethousand

               if (min3p.gen.delt < (min3p.gen.deltmin - tiny)):

                  #write(ilog,'(72a)')('-',i=1,72)
                  #write(ilog,'(a)')'failure in timeloop'
                  #write(ilog,'(a)')'no further time step reduction possible'
                  #write(ilog,'(a)')'bye now ...'
                  #write(ilog,'(72a)')('-',i=1,72)
                  #write(ilog,'(72a)')('-',i=1,72)
                  #write(igen,'(a)')'failure in timeloop'
                  #write(igen,'(a)')'no further time step reduction possible'
                  #write(igen,'(a)')'bye now ...'
                  #write(ilog,'(72a)')('-',i=1,72)
                  sys.exit(" Error message")
                  #break

               min3p.gen.time = min3p.gen.time + min3p.gen.delt   

               #make sure solution will be computed at specified output times

               #print('time = ',gen.time, 'gs_tout(igstime) =', gen.gs_tout[gen.igstime],'igstime=',gen.igstime)       
               #if (gen.time > (gen.gs_tout[gen.igstime] + tiny_time)):
               #     gen.delt = gen.delt + gen.gs_tout[gen.igstime] - gen.time
               #     gen.time = gen.gs_tout[gen.igstime]
               # SOLVING PROBLEM WITH INCORRECT GS_TOUT
               if (min3p.gen.time > (min3p.gen.igstime + tiny_time)):
                    min3p.gen.delt = min3p.gen.delt + min3p.gen.igstime - min3p.gen.time
                    min3p.gen.time = min3p.gen.igstime
                    
                    #print('third max/ delt = ',gen.delt ) 
               #make sure solution time will be consistent with target
               # read times for source chemistry

               if (min3p.gen.transient_source):
                  if (min3p.gen.time > (min3p.gen.tsrc[min3p.gen.itsrc]+tiny_time)):
                     min3p.gen.delt = min3p.gen.delt + min3p.gen.tsrc[min3p.gen.itsrc] - min3p.gen.time    
                     min3p.gen.time = min3p.gen.tsrc[min3p.gen.itsrc]
                     #print('fourth max/ delt = ',gen.delt ) 

               #  convert current solution time and time step to I/O units

               min3p.gen.time_io = min3p.gen.time/min3p.gen.time_factor
               min3p.gen.delt_io = min3p.gen.delt/min3p.gen.time_factor

               #  write run specific information to log file

               if (min3p.gen.idetail_vs > 0 and min3p.gen.transient_flow or 
                   min3p.gen.idetail_rt > 0):
                   if (min3p.gen.skip > 0 and min3p.gen.nskip < min3p.gen.skip):
                      min3p.gen.nskip = min3p.gen.nskip + 1

                   else:
                      min3p.gen.nskip = 0
		      #write(ilog,'(/72a)')('-',i=1,72)
                      #write(ilog,'(a,i6,2x,a,1pe10.3,1x,a,1x,a,1pe10.3,1x,a)') 
                      #&'timestep:',mtime,'time:',time_io,time_unit,
                      #&'delt:',delt_io,time_unit
                      #write(ilog,'(72a/)')('-',i=1,72)

               elif (gen.idetail_vs == 0 and gen.transient_flow
                     or gen.idetail_rt == 0):

	            if ((gen.skip > 0) and (gen.nskip < gen.skip)):
                        #skip this time step
                        gen.nskip = gen.nskip + 1
                    else:  
                        gen.nskip = 0
		        #write(ilog,'(a,i9,2x,a,1pe10.3,1x,a,1x,a,1pe10.3,1x,a)') 
                        #& 'timestep:',mtime,'time:',time_io,time_unit,
                        #& 'delt:',delt_io,time_unit

               #write run specific information to screen

               if (min3p.gen.skip > 0 and min3p.gen.nskip < min3p.gen.skip):
                  #skip this time step
                  empty = 0
               else: 
 	          #print(' timestep:',gen.mtime,'time:',gen.time_io,
                  #      gen.l_time_unit,'delt:',gen.delt_io,gen.l_time_unit)
                  print(" timestep: %i time: %.3e %i delt: %.3e %i" 
                         % (min3p.gen.mtime,min3p.gen.time_io,min3p.gen.l_time_unit,min3p.gen.delt_io,
                           min3p.gen.l_time_unit))

               if (min3p.gen.varsat_flow and min3p.gen.transient_flow):
                    min3p.tranflow()
                    #convergence failure 
                    #restart newton iteration with reduced timestep

                    if (min3p.gen.reduce_timestep): 
                       print(' You will have to use GOTO 1 ')
                       goto .ninehundredninetynine
                       #goto(25114)

               #reactive transport
               if (min3p.gen.reactive_transport):
                  min3p.reactran()

                  #convergence failure - restart newton iteration 
                  #with reduced timestep

                  if (min3p.gen.reduce_timestep):
                   goto .ninehundredninetynine
                   print(' You will have to use GOTO 2 ')
                   #goto(25114)

               # mass balance for variably saturated flow
               if (min3p.gen.varsat_flow and min3p.gen.mass_balance_vs):
                   min3p.mbalvs()

               # write magnitude of current time step to file
               if (min3p.gen.idetail_vs > 0 and min3p.gen.transient_flow or
                   min3p.gen.idetail_rt > 0):
                   if (min3p.gen.mtime == 1):
	                #write(idelt,'(3a)') 'title = "dataset ',prefix(:l_prfx),'"'
                        #write(idelt,'(3a)') 'variables = "time", "delta t"'
                        #write(idelt,'(2a)') 'zone t = "time step data", f=point'
                        empty = 0
                   #write(idelt,'(2(1pe13.5))') time_io,delt_io
  
               #write contour data to output file at specified output times
               if (min3p.gen.gs_output):
                 #if (gen.time >= (gen.gs_tout[gen.igstime]-tiny_time)):
                 if (min3p.gen.time >= (min3p.gen.igstime-tiny_time)):
                    #report to screen
                    print(' ')
                    print(' write contour data, T = ', min3p.gen.time_io, min3p.gen.l_time_unit)
                    print(' -------------------------------'
                          '-------------------------------')

                    if (min3p.gen.varsat_flow and min3p.gen.transient_flow):
                       min3p.outputvs()
                    if (min3p.gen.reactive_transport):
                       min3p.outputrt()
                    min3p.gen.igstime = min3p.gen.igstime + 1.0
 
               #write transient data to output file
               #every ngb_step time step and after completion of solution
               if (min3p.gen.gb_output):
                  min3p.gen.igb_step = min3p.gen.igb_step + 1
                  if (min3p.gen.igb_step == min3p.gen.ngb_step 
                      or min3p.gen.time > (min3p.gen.tfinal-tiny_time)):
                      if (min3p.gen.transient_flow or min3p.gen.reactive_transport):
                         for igb in range (1,min3p.gen.ngb):
                            #assign unit numbers for output of transient data
                            min3p.tranunit[igb]
                            ivol = min3p.gen.ngb_vol[igb]

                            #temperature corrections for debye-huckel, 
                            #equilibrium and rate constants
                            if (chem.temp_field):
                               tcorr(gen.tkel[ivol])

                            #write transient data to output file
                            if (gen.transient_flow):		  	            
	                       tprfvs[ivol]

                            if (gen.reactive_transport):
                               if (chem.ng == 0 and chem.nm != 0):
                                    # FG, 3, quick fix to enable simulation 
                                    # with no gas species explicitly considered
                                    # ('gases' in DB2 = 0)
                                    tprfrtlcg0(totcnew[1][ivol],cnew[1][ivol],
                                              cx[1][ivol],gamma[1][ivol],
                                              gamma[chem.nc+1][ivol],cmnew[1][ivol],
                                              cec_g[ivol],
                                              distcoff_rt[1][ivol],area[1][ivol],
                                              phi[1][ivol],phiold[1][ivol],
                                              sionnew[ivol],tkel[ivol],hhead[ivol],
                                              zg[ivol],time_io,delt,sanew[ivol],
                                              pornew[ivol],igbt,igbc,igbm,igbgr,
                                              igbi,igbb,igbs,igbv,igbd,igbx,prefix,
                                              l_prfx,tec_header,ivol,mtime,
                                              zone_name,l_zone_name,update_porosity)
                               elif (chem.nm == 0 and chem.ng != 0): 
                                      #!! FG, 4 April 08 quick fix to enable
                                      # simulation without reacting mineral
                                      # ('mineral' in DB2 = 0)
                                      tprfrtlcm0(totcnew[1][ivol],cnew[1][ivol],
                                                 cx[1][ivol],gamma[1][ivol],
                                                 gamma[chem.nc+1][ivol],
                                                 gnew[1][ivol],cec_g[ivol],
                                                 distcoff_rt[1][ivol],
                                                 sionnew[ivol],tkel[ivol],
                                                 hhead[ivol],
                                                 zg[ivol],time_io,delt,sanew[ivol],
                                                 pornew[ivol],igbt,igbc,
                                                 igbm,igbg,igbgr,
                                                 igbi,igbb,igbx,prefix,
                                                 l_prfx,tec_header,ivol,
                                                 mtime,zone_name,
                                                 l_zone_name,update_porosity)
  			       else: 
				      tprfrtlc(totcnew[1][ivol],cnew[1][ivol],
                                               cx[1][ivol],gamma[1][ivol],
                                              gamma[chem.nc+1][ivol],cmnew[1][ivol],
                                               gnew[1][ivol],cec_g(ivol),
                                               distcoff_rt[1][ivol],area[1][ivol],
                                               phi[1][ivol],phiold[1][ivol],
                                               sionnew[ivol],tkel[ivol],hhead[ivol],
                                               zg[ivol],time_io,delt,sanew[ivol],
                                               pornew[ivol],igbt,igbc,
                                               igbm,igbg,igbgr,
                                               igbi,igbb,igbs,igbv,
                                               igbd,igbx,prefix,
                                               l_prfx,tec_header,ivol,
                                               mtime,zone_name,
                                               l_zone_name,update_porosity)

                      gen.igb_step = 0

               #prepare for next time step
               nexttime()
               #write temp file for restart option - added 20070130
               restart_w()

               #update boundary conditions for variably saturated flow
               if (gen.update_bcvs):
                  updtbcvs()

               #!FG nov 2017 : mise a jour densite racinaire 
               #(this call has been moved from above)
               if (biol.inside_rld or biol.coupled_archi_rld): 
	          #updtrootdensity()
                  #rewriting updtrootdensity() in Python
                  tiny_updtroot = 1.e-10
                  if(biol.file_rlddata):
                    #!FGG,Jan 2014 headings written in the rlddata file, only once
                    #write(irlddata,'(2a)')'variables = "time","x", "y", "z", "rld"'
                    #biol.irlddata.write('variables = "time","x", "y", "z", "rld"')
                    #!LLab 3,Jan 2014
                    biol.file_rlddata = False
                    #!make sure headings are written only once

                  if(biol.inside_rld):
                     if (gen.time_io > (biol.time_rld-tiny_updtroot)):
                         #!LLab 30, Dec 2013---- update root each day  
                         for ivol in range(50,100):
                            #! moitie sup du profil dans transp.dat
                            biol.rld[ivol] = biol.rld[ivol]*1.2 
                            #! 20% d'augmentation tous les jours
                        
                            #!LLab 3, Jan 2014 Write update times 
                            #and updated rld values in .rlddata file    
             
                         for ivol in range(0,gen.nn):
                             biol.irlddata.write(biol.time_rld,gen.xg[ivol],
                                                 gen.yg[ivol],gen.zg[ivol],
                                                 biol.rld[ivol])
              
                 
                         print('RLD inside updated')
                  
                         biol.time_rld = biol.time_rld + 1.0 

                  #!! COUPLAGE :
                  if(biol.coupled_archi_rld): 
                    if (biol.maillage_rld_coupled): 
                       #!spatial discretization info passed to Archissimple 
                       #after the first time increment
                       biol.maillage_rld_coupled = False

                    if (gen.time_io > (biol.time_rld - tiny_updtroot)): 
                       biol.compt_rld_coupled = biol.compt_rld_coupled + 1
                       #! CB COUPLAGE 
                       delt_MIN3P = gen.time_io - gen.time_io_prec 
                       # ! CB calcul du pas de temps d une journee 
                       #pour mettre ds Compute Archi
                       print(' TIME MIN3P = ', gen.time_io,
                             ' DELTA T MIN3P = ', delt_MIN3P)   
                       #allocate(x_g(nn))
                       #allocate(y_g(nn))
                       #allocate(z_g(nn))
                       #allocate(humidity(nn))

                       #x_g = []
                       #y_g = []
                       #z_g = []
                       #humidity = []

                       x_g = np.zeros(gen.nn, dtype = np.float32)
                       y_g = np.zeros(gen.nn, dtype = np.float32)
                       z_g = np.zeros(gen.nn, dtype = np.float32)
                       humidity = np.zeros(gen.nn, dtype = np.float32)

                       for ivol in range(0,gen.nn):   
                          x_g[ivol]=gen.xg.item(ivol)
                          y_g[ivol]=gen.yg.item(ivol)
                          z_g[ivol]=gen.zg.item(ivol)
                          humidity[ivol]=gen.pornew.item(ivol)*gen.sanew.item(ivol)
                          if(humidity[ivol] > 10. or humidity[ivol] < 0.01):
                            humidity[ivol] = 3.0
                          print(humidity[ivol])
                       x_g = np.asarray(x_g, dtype=np.float32)
                       y_g = np.asarray(y_g, dtype=np.float32)
                       z_g = np.asarray(z_g, dtype=np.float32)
                       humidity = np.asarray(humidity, dtype=np.float32)


                       #! CB : parce que nzz=1 ds transp-updrld
                       # -1 because first element in Fortran is 1
                       # but in Python is 0
                       z_max = gen.zmax[gen.nzz-1]
                       x_max = gen.xmax[gen.nxx-1]
                       z_max = 2
                       x_max = 2
                       nv_z = gen.nvz
                       nv_x = gen.nvx  

                       #THIS IS NOT AN UNIVERSAL SOLUTION AND IT HAS TO BE 
                       #IMPROVED 
                       
                       x_g = np.tile(np.linspace(0,2,num=50,dtype = np.float32),50)  
                       z_g = np.repeat(np.linspace(0,2,num=50,dtype = np.float32),50)
                       y_g = np.zeros(2500,dtype = np.float32)

                       gen.x_g = x_g
                       gen.z_g = z_g
                       gen.y_g = y_g
                       gen.zmax[gen.nzz-1] = z_max
                       gen.xmax[gen.nzz-1] = x_max
   
                       if(gen.nvx > 1):
                         flag=2  #! if 1< control volume in x -> 2D
                       else:
                         flag=1 #! if 1 control volume in x -> 1D 

                       #!------------ COUPLAGE 1D --------------
                       if(flag == 1):
                         print(' ')
                         print(' COUPLAGE 1D')
                         print(' ')
                           
                         RSD_archi = np.zeros(gen.nvz+1)
                         RSD_bonsens = np.zeros(gen.nvz+1)
                         RSD_archi = np.asarray(RSD_archi, dtype=np.float64)

                         lib.COMPUTE.argtypes = [ctypes.c_int, 
                                                 ctypes.c_float,
                                                 ctypes.c_float,
                                                 ctypes.c_int,
                                                 ctypes.c_int,
                                                 ctypes.c_int,
                                                 ctypes.c_int,
                                                 ctypes.c_void_p,
                                                 ctypes.c_int,
                                                 ctypes.c_void_p,
                                                 ctypes.c_void_p,
                                                 ctypes.c_void_p,
                                                 ctypes.c_void_p] 

                         lib.COMPUTE.restype = None


                         lib.COMPUTE(flag, gen.time_io, delt_MIN3P, z_max, 
                                     nv_z, x_max, nv_x, RSD_archi,gen.tfinal,
                                     x_g, y_g, z_g, humidity)

                         for ivol in range(1,gen.nn):
                            RSD_bonsens[gen.nn-ivol+1]=RSD_archi[ivol]

                         for ivol in range(1,gen.nn): 
                            biol.rld[ivol]=RSD_bonsens[ivol]

                         #ecriture fichier RSD pour verif :
                         ii = gen.time_io
                         if(gen.time_io < 10):
                            #write (file_name, '("RSD_1D_MIN3P", I1,".txt")' ) ii
                            file_name = open("RSD_1D_MIN3P%s.txt" % ii, 'w')
                         else:
                            #write (file_name, '("RSD_1D_MIN3P", I2,".txt")' ) ii
                            file_name = open("RSD_1D_MIN3P%s.txt" % ii, 'w')
                         if(gen.time_io >= 100):
                            file_name = open("RSD_1D_MIN3P%s.txt" % ii, 'w')
                            #write (file_name, '("RSD_1D_MIN3P", I3,".txt")' ) ii
                         #open(1111,file=file_name)
                         file_name.write('variables = "ivol", "z", "RSD"\n')
                         #write(1111,*) 'variables = "ivol", "z", "RSD"' 
                         #!FG to make tecplot readable files
                         #!FG to make tecplot readable files
                         #write(1111,'(a,1pe10.3,1x,a,3(a,i5),a)') 
                         #'zone t = "RSD, T = ',time_io,time_unit(:l_time_unit),
                         # '", i =',nvx,', j =',nvz,', k =',nvy,',  f=point'
                         #file_name.write('zone t = "RSD, T = ',gen.time_io,
                         #            gen.l_time_unit,'", i =',gen.nvx,', j =',
                         #            gen.nvz,', k =',gen.nvy,',  f=point')
                         file_name.write('zone t = "RSD, T = %f days i = %d,' 
                       'j = %d, k = %d, f=point' % gen.time_io,gen.nvx,gen.nvz,gen.nvy)
                         for ivol in range (1,gen.nn):
                            file_name.write(ivol,' ',gen.zg[ivol],' ',
                                                     biol.rld[ivol])
                         #    write(1111,'(I8, a, f9.5, a, f9.5)') ivol,' ', 
                         #         zg(ivol),' ', rld(ivol) 
                         #    !FG I8 instead of I4 to allow printing of ivol>9999
         
                         #close(1111)
                         file_name.close()

                       else:                      
                         print(' ')
                         print(' COUPLAGE 2D')
                         print(' ')
                           
                         RSD_archi = np.zeros((gen.nvz*gen.nvz)+1)
                         RSD_archi = np.asarray(RSD_archi, dtype=np.float64)

                         lib.COMPUTE.argtypes = [ctypes.c_int, 
                                                 ctypes.c_float,
                                                 ctypes.c_float,
                                                 ctypes.c_int,
                                                 ctypes.c_int,
                                                 ctypes.c_int,
                                                 ctypes.c_int,
                                                 ctypes.c_void_p,
                                                 ctypes.c_int,
                                                 ctypes.c_void_p,
                                                 ctypes.c_void_p,
                                                 ctypes.c_void_p,
                                                 ctypes.c_void_p] 
                         lib.COMPUTE.restype = None



                         #print ('passing address x_g: %0x' % x_g.ctypes.data)
                         #print ('passing address RSD_archi: %0x' % RSD_archi.ctypes.data)           
                         

                         lib.COMPUTE(flag,
                                     gen.time_io,
                                     delt_MIN3P,
                                     z_max, 
                                     nv_z, 
                                     x_max, 
                                     nv_x, 
                                     RSD_archi.ctypes.data,
                                     int(gen.tfinal),
                                     x_g.ctypes.data,
                                     y_g.ctypes.data,
                                     z_g.ctypes.data,
                                     humidity.ctypes.data)
                         

                         for ivol in range(0,gen.nn): 
                            #biol.rld[ivol] = RSD_archi[ivol]
                            biol.rld[ivol] = RSD_archi.item(ivol)
                            #print(ivol)
                            #biol.rld.append(RSD_archi[ivol])
                
                         biol.rld[gen.nn-1] = 0 
                         #Au coin du domaine on met RSD = 0 sinon 
                         #on a une valeur garbage de 1

                         #ecriture fichier RSD pour verif :
                         ii = gen.time_io
                         if(gen.time_io < 10):
                            #write (file_name, '("RSD_1D_MIN3P", I1,".txt")' ) ii
                            file_name = open("RSD_2D_MIN3P%d.txt" % ii, 'w')
                         else:
                            #write (file_name, '("RSD_1D_MIN3P", I2,".txt")' ) ii
                            file_name = open("RSD_2D_MIN3P%d.txt" % ii, 'w')
                         if(gen.time_io >= 100):
                            file_name = open("RSD_2D_MIN3P%d.txt" % ii, 'w')
                            #write (file_name, '("RSD_1D_MIN3P", I3,".txt")' ) ii
                         #open(1111,file=file_name)

                         file_name.write('variables = "ivol", "x", "z", "RSD"\n')
                         #file_name.write('zone t = "RSD, T = ',gen.time_io,
                         #            gen.l_time_unit,'", i =',gen.nvx,', j =',
                         #            gen.nvz,', k =',gen.nvy,',  f=point')
                         file_name.write('zone t = "RSD, T = %f days i = %d, j = %d, k = %d, f=point\n' % (gen.time_io,gen.nvx,gen.nvz,gen.nvy))
                         for ivol in range (0,gen.nn):
                            #file_name.write("%d %f %f %f\n" % (ivol,gen.xg[ivol],
                            #                gen.zg[ivol],biol.rld[ivol]))
                            file_name.write("%d %f %f %f\n" % (ivol,x_g.item(ivol),
                                            z_g.item(ivol),RSD_archi.item(ivol)))

                         #    write(1111,'(I8, a, f9.5, a, f9.5)') ivol,' ', 
                         #         zg(ivol),' ', rld(ivol) 
                         #    !FG I8 instead of I4 to allow printing of ivol>9999
         
                         #close(1111)
                         file_name.close()

                       gen.time_io_prec = gen.time_io 
                       #! CB pour calcul pas de temps delt_MIN3P 
                       #a mettre ds Compute_archi
                   
                       for ivol in range(1,gen.nn):
                           #write(irlddata,'(6e15.7)') time_rld,xg(ivol),
                           #      yg(ivol),zg(ivol),rld(ivol) 
                           #biol.irlddata.write(biol.time_rld,gen.xg[ivol],
                           #                    gen.yg[ivol],gen.zg[ivol],
                           #                    biol.rld[ivol])
                           empty = 0

                       if (biol.compt_rld_coupled >= 2): 
                          #! CB   write(*,*) 'Soil moisture passed'
                          empty = 0
          
                       biol.time_rld=biol.time_rld + 1.0   
                  
                  #!END COUPLAGE 
                  for ivol in range(0,gen.nn-1):
                     biol.rldbck[ivol] = biol.rld[ivol]
             
                  sumrld = 0.0
                  for ivol in range(0,gen.nn-1):
                     sumrld = sumrld + biol.rldbck[ivol]

                  if (sumrld == 0):
                     biol.rootdensitynill= True
                  else:
                     biol.rootdensitynill= False


  
               #  update etp and canopy dependent parameters
               if (biol.root_uptake or gen.pure_evap):
 	           updtetp()

               #  update temperature field
               if (chem.temp_field):
                   readtemp()
                   if (chem.update_temp):
                       intpolt()

               # update cputime
               cpuint_old = gen.cpuint
               gen.cpuint = time.time()
               if (gen.cpuint < cpuint_old):
                   gen.csec = gen.csec + gen.cpuint - cpuint_old + r86400
               else:
                   gen.csec = gen.csec + gen.cpuint - cpuint_old
       
  

         #print (' NO PROBLEMS WHATSOEVER. KEEP GOING...')



    #cputime and statistics to screen and generic output file

    if (gen.varsat_flow or gen.reactive_transport):
        rstatgs(gen.ilog)
        rstatgs(gen.igen)
        empty = 0
 
    print('  ***************** normal exit ******************')
    #write(ilog,'(72a)')('-',i=1,72)
    #write(ilog,'(/a//)')
    # &'         ***************** normal exit ******************'
    # write(igen,'(72a)')('-',i=1,72)
    # write(igen,'(/a//)')
    #&'         ***************** normal exit ******************'

    #  close I/O files (global system)
   
    clsgfls()

      
    #CB WRITE AND CLOSE FILE ARCHISIMPLE :
    lib.END_ARCHI()
    
 

    sys.exit()



if __name__ == "__main__":
    main()

