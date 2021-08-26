#! /home/renato/anaconda2/bin/ python

from __future__ import print_function, absolute_import, division

import _min3p
import f90wrap.runtime
import logging
import os
import sys
import time
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
#from goto import goto, comefrom, label

class Goto(Exception): 
      pass  # declare a label

import ctypes 
from struct import *
lib = ctypes.cdll.LoadLibrary('/home/renato/Desktop/Min3pArchi91_reconstruc/ArchiSimple/_ArchiSimple.so')

import min3p


def main():

    pet = []

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
          for igb in range(0, min3p.gen.ngb):
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

    if (min3p.gen.varsat_flow and min3p.gen.transient_flow and
        min3p.gen.mass_balance_vs):
        min3p.msysvs()


    #compute initial system mass - reactive transport

    if (min3p.gen.mass_balance_rt):
        min3p.msysrt()



    #transient simulation for variably saturated flow and 
    #reactive transport
    if ((min3p.gen.varsat_flow and min3p.gen.transient_flow) or 
         min3p.gen.reactive_transport):
         #timeloop.f in python 
         #reactive transport    
         r0 = 0.0
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
            zero_r8(min3p.gen.qwater,min3p.gen.nn,1,1) 
            #zero_r4(min3p.gen.qwater,min3p.gen.nn,1,1)

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
         go_to = 0
         while (min3p.gen.time < (min3p.gen.tfinal-tiny_time)):
               min3p.gen.mtime = min3p.gen.mtime + 1

               #variable time stepping

               if (min3p.gen.mtime == 1 and (not min3p.gen.restart_sim)): 

	         if (min3p.gen.varsat_flow and min3p.gen.reactive_transport):
                    #initialize iupsg variable 
                    #(updated after each N-R iteration, in reactran)
                    
                    iupsg = []
	            for i1 in range(0,gen.njavs):
	               iupsg.append('a')

               elif (min3p.gen.mtime > 1 or min3p.gen.restart_sim):

                     #assign new time step for global simulation
                     #flow and reactive transport

                     if (min3p.gen.varsat_flow and min3p.gen.reactive_transport):
                        if (min3p.gen.transient_flow and
                            min3p.gen.variably_saturated):
                              min3p.gen.delt = min(min3p.gen.delt_vs,
                                               min3p.gen.delt_rt)
                        else:
                              min3p.gen.delt = min3p.gen.delt_rt  

                       #flow only

                     elif (min3p.gen.varsat_flow and (not 
                           min3p.gen.reactive_transport)):
                          if (min3p.gen.transient_flow and 
                              min3p.gen.variably_saturated):
                             min3p.gen.delt = min3p.gen.delt_vs  
                          else:
                             min3p.gen.delt = min3p.gen.delt   

                       #reactive transport only

                     elif ((not min3p.gen.varsat_flow) and 
                          (min3p.gen.reactive_transport)):
                            min3p.gen.delt = min3p.gen.delt_rt  


                     #adjust time step to target read times for transient
                     #boundary conditions
                     #for variably saturated flow

                     if (min3p.gen.update_bcvs):
	               if ((min3p.gen.time + min3p.gen.delt) > 
                          (min3p.gen.time_bcvs*min3p.gen.time_factor)):

	                  min3p.gen.delt = min3p.gen.time_bcvs*min3p.gen.time_factor 
                          -(min3p.gen.time)

	                  min3p.gen.delt = max(min3p.gen.delt, min3p.gen.deltmin)
                          #print('first max/ delt = ',gen.delt )

                     #adjust time step to target read times for updating soil
                     # specific  parameters

                     if (min3p.biol.root_uptake):
	               if ((min3p.gen.time+min3p.gen.delt) > 
                          (min3p.biol.time_soi*min3p.gen.time_factor)):
	                  min3p.gen.delt = min3p.biol.time_soi*min3p.gen.time_factor
                          -min3p.gen.time

	                  min3p.gen.delt = max(min3p.gen.delt,min3p.gen.deltmin)
                          #print('second max/ delt = ',gen.delt )      

               #maximum number of iterations exceeded, time step guess was poor,
               #reduce time step size 

               #goto .onethousand
               #while go_to == 0:
               #while go_to == 1:
               while True:

                while True:

                   if go_to == 1:

                     #label .ninehundredninetynine

                     min3p.gen.time = min3p.gen.time - min3p.gen.delt
                     min3p.gen.mtime_f = min3p.gen.mtime_f + 1
                     min3p.gen.reduce_timestep = False
                     min3p.gen.delt = rhalf*min3p.gen.delt  #additional time step reduction        
                     go_to = 0

                   #else:
                   #label .onethousand

                   if (min3p.gen.delt < (min3p.gen.deltmin - tiny)):

                      sys.exit(" Error message")
 

                   min3p.gen.time = min3p.gen.time + min3p.gen.delt   


                   if (min3p.gen.time > (min3p.gen.igstime + tiny_time)):
                      min3p.gen.delt = min3p.gen.delt + min3p.gen.igstime - min3p.gen.time

                      min3p.gen.time = min3p.gen.igstime
                    
                      #print('third max/ delt = ',gen.delt ) 
                   #make sure solution time will be consistent with target
                   # read times for source chemistry

                   if (min3p.gen.transient_source):
                      if (min3p.gen.time > (min3p.gen.tsrc[min3p.gen.itsrc]+tiny_time)):
                         min3p.gen.delt = min3p.gen.delt + min3p.gen.tsrc[gen.itsrc] - min3p.gen.time    
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
  
                   elif (min3p.gen.idetail_vs == 0 and min3p.gen.transient_flow
                       or min3p.gen.idetail_rt == 0):

	                if ((min3p.gen.skip > 0) and 
                          (min3p.gen.nskip < min3p.gen.skip)):
                          #skip this time step
                          min3p.gen.nskip = gen.nskip + 1
                        else:  
                          min3p.gen.nskip = 0
		          #write(ilog,'(a,i9,2x,a,1pe10.3,1x,a,1x,a,1pe10.3,1x,a)') 
                          #& 'timestep:',mtime,'time:',time_io,time_unit,
                          #& 'delt:',delt_io,time_unit

                   #write run specific information to screen

                   if (min3p.gen.skip > 0 and min3p.gen.nskip < min3p.gen.skip):
                    #skip this time step
                    #empty = 0
                    pass
                   else: 
 	            #print(' timestep:',gen.mtime,'time:',gen.time_io,
                    #      gen.l_time_unit,'delt:',gen.delt_io,gen.l_time_unit)
                    print(" timestep: %i time: %.3e %i delt: %.3e %i" 
                         % (min3p.gen.mtime,min3p.gen.time_io,min3p.gen.l_time_unit,
                              min3p.gen.delt_io,min3p.gen.l_time_unit))

                   if (min3p.gen.varsat_flow and min3p.gen.transient_flow):
                      min3p.tranflow()
                      #convergence failure 
                      #restart newton iteration with reduced timestep

                      if (min3p.gen.reduce_timestep): 
                         print(' You will have to use GOTO 1 ')
                         go_to = 1
                         break 
                         #goto .ninehundredninetynine
                         #goto(25114)
                         #break
                      #else:
                      #   go_to = 0


                   #reactive transport
                   if (min3p.gen.reactive_transport):
                      min3p.reactran()

                    #convergence failure - restart newton iteration 
                    #with reduced timestep

                      if (min3p.gen.reduce_timestep):
                       #goto .ninehundredninetynine
                       go_to = 1
                       print(' You will have to use GOTO 2 ')
                       break
                       #goto(25114)
                      #else:
                      # go_to = 0


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
                        print(' write contour data, T = ', min3p.gen.time_io,
                              min3p.gen.l_time_unit)
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
                          if (min3p.gen.transient_flow or 
                              min3p.gen.reactive_transport):
                             for igb in range (0,min3p.gen.ngb):
                                #assign unit numbers for output of transient data
                                tranunit[igb]
                                ivol = min3p.gen.ngb_vol[igb]

                                #temperature corrections for debye-huckel, 
                                #equilibrium and rate constants
                                if (min3p.chem.temp_field):
                                   min3p.tcorr(min3p.gen.tkel[ivol])

                                #write transient data to output file
                                if (min3p.gen.transient_flow):  	            
	                           min3p.tprfvs[ivol]

                                if (min3p.gen.reactive_transport):
                                   if (min3p.chem.ng == 0 and min3p.chem.nm != 0):
                                      # FG, 3, quick fix to enable simulation 
                                      # with no gas species explicitly considered
                                      # ('gases' in DB2 = 0)
                                      min3p.tprfrtlcg0(totcnew[1][ivol],cnew[1][ivol],
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
                                   elif (min3p.chem.nm == 0 and min3p.chem.ng != 0): 
                                        #!! FG, 4 April 08 quick fix to enable
                                        # simulation without reacting mineral
                                        # ('mineral' in DB2 = 0)
                                        min3p.tprfrtlcm0(totcnew[1][ivol],cnew[1][ivol],
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
				        min3p.tprfrtlc(totcnew[1][ivol],cnew[1][ivol],
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

                          min3p.gen.igb_step = 0

                   #prepare for next time step
                   min3p.nexttime()
                   #write temp file for restart option - added 20070130
                   min3p.restart_w()

                   #update boundary conditions for variably saturated flow
                   if (min3p.gen.update_bcvs):
                    min3p.updtbcvs()

                   #!FG nov 2017 : mise a jour densite racinaire 
                   #(this call has been moved from above)
                   if (min3p.biol.inside_rld or min3p.biol.coupled_archi_rld): 
	              #updtrootdensity()


                    #rewriting updtrootdensity() in Python
                    tiny_updtroot = 1.e-10
                    if(min3p.biol.file_rlddata):
                      #!FGG,Jan 2014 headings written in the rlddata file, only once
                      #write(irlddata,'(2a)')'variables = "time","x", "y", "z", "rld"'
                      file_rlddata = open("feddes.rlddata", 'w')
                      file_rlddata.write('variables = "time","x", "y", "z", "rld"\n')
                      #!LLab 3,Jan 2014
                      min3p.biol.file_rlddata = False
                      #!make sure headings are written only once

                    if(min3p.biol.inside_rld):
                       if (min3p.gen.time_io > (min3p.biol.time_rld-tiny_updtroot)):
                           #!LLab 30, Dec 2013---- update root each day  
                           for ivol in range(49,100):
                              #! moitie sup du profil dans transp.dat
                              min3p.biol.rld[ivol] = min3p.biol.rld[ivol]*1.2 
                              #! 20% d'augmentation tous les jours
                        
                              #!LLab 3, Jan 2014 Write update times 
                              #and updated rld values in .rlddata file    
             
                           for ivol in range(0,gen.nn):
                               #biol.irlddata.write(biol.time_rld,gen.xg[ivol],
                               #                    gen.yg[ivol],gen.zg[ivol],
                               #                    biol.rld[ivol])
                               file_rlddata.write(min3p.biol.time_rld,
                                                min3p.gen.xg[ivol],
                                                min3p.gen.yg[ivol],
                                                min3p.gen.zg[ivol],
                                                min3p.biol.rld[ivol])
              
                 
                           print('RLD inside updated')
                  
                           min3p.biol.time_rld = min3p.biol.time_rld + 1.0 

                    #!! COUPLAGE :
                    if(min3p.biol.coupled_archi_rld): 
                      if (min3p.biol.maillage_rld_coupled): 
                         #!spatial discretization info passed to Archissimple 
                         #after the first time increment
                         min3p.biol.maillage_rld_coupled = False

                      if (min3p.gen.time_io > (min3p.biol.time_rld - tiny_updtroot)): 
                         min3p.biol.compt_rld_coupled = min3p.biol.compt_rld_coupled + 1
                         #! CB COUPLAGE 
                         delt_MIN3P = min3p.gen.time_io - min3p.gen.time_io_prec 
                         # ! CB calcul du pas de temps d une journee 
                         #pour mettre ds Compute Archi
                         print(' TIME MIN3P = ', min3p.gen.time_io,
                             ' DELTA T MIN3P = ', delt_MIN3P)  


                         j = int(min3p.gen.time_io) - 1

                         if(j == 0):
                            beta = np.ones(int(min3p.gen.tfinal))
                            data = np.array([beta]).T
                            df4 = pd.DataFrame(data)

                            df4.to_excel("/home/renato/groimp_efficient/run_1/beta_1.xls",
                                       index=False, header=False)

                            print ("----------------------------------------",
                                 "----------------------------------")
                            print ("--------------- Writing feddes.soi for", 
                                 "Min3pArchiSImple ------------------") 

                            df2 = pd.read_csv('/home/renato/groimp_efficient/run_1/feddes.soi',sep='\t',names=['time','ET','canopy_int','solar_ratio','scale_tree_growth'])

                            print ("----------------------------------",
                              "----------------------------------------"  )
                            print ("------------------------ Start GroIMP 1.5 -----",
                              "---------------------------")

                            os.system("java -Xmx2000m -jar /home/renato/Downloads/GroIMP-1.5/core.jar --headless /home/renato/Downloads/FSPM_BASIC-run_1/project.gs")

                            df1 = pd.read_csv('/home/renato/groimp_efficient/run_1/transp.txt',header=0, names=['transpiration'])

                            PET = df1.transpiration.values

                            PET = np.array(PET)

                            ET = PET

        
                            #ET = np.empty(int(min3p.gen.tfinal))
                            #ET.fill(2.0E-8)
                            i = len(ET)
    

                            df1 = pd.read_csv('/home/renato/groimp_efficient/run_1/root.txt',
                                          header=0, names=['rootbiom'])
                            root = df1.rootbiom.values

                            root = np.array(root)

                            rootbiom = root*10.E-3*0.1
                            #rootbiom = np.empty(int(min3p.gen.tfinal))
                            #rootbiom.fill(3000)


                         print ("----------------------------------",
                              "----------------------------------------"  )
                         print ("------------------------ Start GroIMP 1.5 -----",
                              "---------------------------")

                         os.system("java -Xmx2000m -jar /home/renato/Downloads/GroIMP-1.5/core.jar --headless /home/renato/Downloads/FSPM_BASIC-run_1/project.gs")

                         print ("---------------------------------",
                              "-----------------------------------------")
                         print ("------------------------ Reading PET from GroIMP 1.5",
                              "---------------------")

                         df1 = pd.read_csv('/home/renato/groimp_efficient/run_1/transp.txt',header=0, names=['transpiration'])

                         PET = df1.transpiration.values

                         PET = np.array(PET)

                         ET[j] = PET[j]

                         
                         time_soi_var = df2.time.values
                         canopy_int_var = df2.canopy_int.values
                         solar_ratio_var = df2.solar_ratio.values
                         scale_tree_growth_var = df2.scale_tree_growth.values

                         min3p.biol.pet = PET[j]*(60*60*24)
                         min3p.biol.time_soi = time_soi_var[j]
                         #min3p.biol.pet = PET[j]
                         min3p.biol.canopy_int = canopy_int_var[j]
                         min3p.biol.solar_ratio = solar_ratio_var[j]
                         min3p.biol.scale_tree_growth = scale_tree_growth_var[j]

                         print(min3p.biol.time_soi,min3p.biol.pet,
                               min3p.biol.canopy_int,min3p.biol.solar_ratio,
                               min3p.biol.scale_tree_growth)
                         print ("-------------------------------------",
                              "-------------------------------------")  
                         print ("------------------------ Writing update of feddes.soi",
                              "--------------------")
  
                         data = np.array([df2.time[:i].values,
                                ET[:i],
                                df2.canopy_int[:i].values,
                                df2.solar_ratio[:i].values,
                                df2.scale_tree_growth[:i].values]).T


                         df3 = pd.DataFrame(data)

                         df3 = pd.DataFrame({'col1':time_soi_var[:i],
                                             'col2':ET[:i],
                                             'col3':canopy_int_var[:i],
                                             'col4':solar_ratio_var[:i],
                                             'col5':scale_tree_growth_var[:i]})


                         df3.to_csv('/home/renato/groimp_efficient/run_1/feddes.soi', sep='\t', index=False, header=None )

                         df3.to_csv('/home/renato/groimp_efficient/run_1/feddes_original_%s.soi' %int(min3p.gen.time_io),sep='\t', index=False, header=None)

                         print ("--------------------------------------",
                      "------------------------------------")
                         print ("------------------- Reading RootBiom from GroIMP 1.5 ",
                        "---------------------") 

                         df1 = pd.read_csv('/home/renato/groimp_efficient/run_1/root.txt',
                                          header=0, names=['rootbiom'])
                         root = df1.rootbiom.values

                         root = np.array(root)

                         rootbiom = root*10.E-3*0.1

                         print ("----------------------------------",
                      "----------------------------------------")  
                         print ("---------------------- Writing update of biomrac.txt",
                      "---------------------") 
  
                         data = np.array([rootbiom[:i]]).T

                         df4 = pd.DataFrame(data)


                         df4.to_csv('/home/renato/groimp_efficient/run_1/biomrac.txt', sep='\t',index=False, header=None)
                         df4.to_csv('/home/renato/groimp_efficient/run_1/biomrac_%s.txt' %int(min3p.gen.time_io), sep='\t', index=False, header=None)



                         x_g = np.zeros(min3p.gen.nn, dtype = np.float32,order='F')
                         y_g = np.zeros(min3p.gen.nn, dtype = np.float32,order='F')
                         z_g = np.zeros(min3p.gen.nn, dtype = np.float32,order='F')
                         humidity = np.zeros(min3p.gen.nn, dtype = np.float32,order='F')

                         for ivol in range(0,min3p.gen.nn):   
                            x_g[ivol]=min3p.gen.xg.item(ivol)
                            y_g[ivol]=min3p.gen.yg.item(ivol)
                            z_g[ivol]=min3p.gen.zg.item(ivol)
                            humidity[ivol]=min3p.gen.pornew.item(ivol)*min3p.gen.sanew.item(ivol)

                         #! CB : parce que nzz=1 ds transp-updrld
                         # -1 because first element in Fortran is 1
                         # but in Python is 0
                         z_max = min3p.gen.zmax[min3p.gen.nzz-1]
                         x_max = min3p.gen.xmax[min3p.gen.nxx-1]
                         nv_z = min3p.gen.nvz
                         nv_x = min3p.gen.nvx  

                  
                         if(min3p.gen.nvx > 1):
                           flag=2  #! if 1< control volume in x -> 2D
                         else:
                           flag=1 #! if 1 control volume in x -> 1D 

                         #!------------ COUPLAGE 1D --------------
                         if(flag == 1):
                           print(' ')
                           print(' COUPLAGE 1D')
                           print(' ')
                           
                           RSD_archi = np.zeros(min3p.gen.nvz+1)
                           RSD_bonsens = np.zeros(min3p.gen.nvz+1)
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


                           lib.COMPUTE(flag, min3p.gen.time_io, delt_MIN3P, z_max, 
                                     nv_z, x_max, nv_x, RSD_archi,min3p.gen.tfinal,
                                     x_g, y_g, z_g, humidity)

                           for ivol in range(0,min3p.gen.nn):
                              RSD_bonsens[min3p.gen.nn-ivol+1]=RSD_archi[ivol]
  
                           for ivol in range(0,gen.nn): 
                              min3p.biol.rld[ivol]=RSD_bonsens[ivol]

                           #ecriture fichier RSD pour verif :
                           ii = min3p.gen.time_io
                           if(min3p.gen.time_io < 10):
                              #write (file_name, '("RSD_1D_MIN3P", I1,".txt")' ) ii
                              file_name = open("RSD_1D_MIN3P%s.txt" % ii, 'w')
                           else:
                              #write (file_name, '("RSD_1D_MIN3P", I2,".txt")' ) ii
                              file_name = open("RSD_1D_MIN3P%s.txt" % ii, 'w')
                           if(min3p.gen.time_io >= 100):
                              file_name = open("RSD_1D_MIN3P%s.txt" % ii, 'w')
                              #write (file_name, '("RSD_1D_MIN3P", I3,".txt")' ) ii
                           #open(1111,file=file_name)
                           file_name.write('variables = "ivol", "z", "RSD"\n')
                           file_name.write('zone t = "RSD, T = %f days i = %d,' 
                       'j = %d, k = %d, f=point' 
                           % min3p.gen.time_io,min3p.gen.nvx,min3p.gen.nvz,
                           min3p.gen.nvy)
                           for ivol in range (0,min3p.gen.nn):
                              file_name.write(ivol,' ',min3p.gen.zg[ivol],' ',
                                                     min3p.biol.rld[ivol])

                           file_name.close()

                         else:                      
                           print(' ')
                           print(' COUPLAGE 2D')
                           print(' ')
                           
                           RSD_archi = np.zeros((min3p.gen.nvz*min3p.gen.nvz)+1)
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


                           lib.COMPUTE(flag,
                                     min3p.gen.time_io,
                                     delt_MIN3P,
                                     z_max, 
                                     nv_z, 
                                     x_max, 
                                     nv_x, 
                                     RSD_archi.ctypes.data,
                                     int(min3p.gen.tfinal),
                                     x_g.ctypes.data,
                                     y_g.ctypes.data,
                                     z_g.ctypes.data,
                                     humidity.ctypes.data)
                         

                           for ivol in range(0,min3p.gen.nn): 
                              min3p.biol.rld[ivol] = RSD_archi.item(ivol)
                          
                           min3p.biol.rld[min3p.gen.nn-1] = 0 
                           #Au coin du domaine on met RSD = 0 sinon 
                           #on a une valeur garbage de 1

                           #ecriture fichier RSD pour verif :
                           ii = min3p.gen.time_io
                           if(min3p.gen.time_io < 10):
                              #write (file_name, '("RSD_1D_MIN3P", I1,".txt")' ) ii
                              file_name = open("RSD_2D_MIN3P%d.txt" % ii, 'w')
                           else:
                              #write (file_name, '("RSD_1D_MIN3P", I2,".txt")' ) ii
                              file_name = open("RSD_2D_MIN3P%d.txt" % ii, 'w')
                           if(min3p.gen.time_io >= 100):
                              file_name = open("RSD_2D_MIN3P%d.txt" % ii, 'w')
                            

                           file_name.write('variables = "ivol", "x", "z", "RSD"\n')
                           file_name.write('zone t = "RSD, T = %f days i = %d, j = %d, k = %d, f=point\n' % (min3p.gen.time_io,min3p.gen.nvx,min3p.gen.nvz,min3p.gen.nvy))
                           for ivol in range (0,min3p.gen.nn):
                           
                              file_name.write("%d %f %f %f\n" % (ivol,x_g.item(ivol),
                                            z_g.item(ivol),RSD_archi.item(ivol)))

                           file_name.close()

                           print ("--------------------------------------",
                                "------------------------------------")  
                           print ("------------------------- Calculating root water",
                                "-------------------------") 
                           print ("------------------------- uptake from Min3pArchi",
                                "-------------------------") 

                           df0 = pd.read_csv('feddes_%s.gsp'  %int(min3p.gen.time_io),
                               delim_whitespace=True,skiprows=3,header=None,
                               names=["x", "y", "z", "h_w", "p_w", "s_w", "theta_w",
                                      "transp", "evap"])

                           transp = df0['transp'].values
                           transp_sum = np.sum(np.array(transp).astype(np.float))

                           ET[j] = transp_sum

                           data = np.array([ET]).T

                           df8 = pd.DataFrame(data)

                           df8.to_csv('/home/renato/groimp_efficient/run_1/RWU_%s.txt' %int(min3p.gen.time_io),
                             sep='\t', index=False, header=None )

                           # Calculating Beta and garanteeing not greater than 1, 
                           # negative, or zero
                           if((PET[j] >= ET[j]) and (PET[j] > 0.0) 
                              and (ET[j] > 0.0)):
                              beta[j] = ET[j]/PET[j]
                           else:
                              beta[j] = 1.0

                           # Avoiding beta smaller than 0.2 because 
                           # it could kill the plant 
                           if(beta[j] <= 0.2): 
                              beta[j] = 0.2
                           else:
                              pass



                           os.system("rm /home/renato/groimp_efficient/run_1/beta_1.xls")

                           data = np.array([beta]).T

                           df4 = pd.DataFrame(data)
                           df4.to_excel("/home/renato/groimp_efficient/run_1/beta_1.xls",
                               index=False, header=False)

                           df4.to_csv('/home/renato/groimp_efficient/run_1/beta_1_%s.txt' %int(min3p.gen.time_io),
                             sep='\t', index=False, header=None)



                           print ("-------------------------------------------",
                           "-------------------------------") 
                           print ("------------------------ Copying GroIMP 1.5 files",
                           "-------------------------------")


                           df0 = pd.read_csv('/home/renato/groimp_efficient/run_1/field.txt',
                       delim_whitespace=True,skiprows=1,header=None,
                       names=["time", "species", "LAI", "nrShoots", "fAbs",
                              "assCO2", "biomAbove", "yield", "harvestIndex",
                              "leafArea","fieldRFR"])

                           df0.to_csv('/home/renato/groimp_efficient/run_1/field_%s.txt' %int(min3p.gen.time_io), sep='\t', index=False, header=None)

                           df0 = pd.read_csv('/home/renato/groimp_efficient/run_1/plant.txt',
                        delim_whitespace=True,skiprows=1,header=None,
                        names=["time", "tt", "plant", "strip", "row", "pos",
                               "species", "weed","age","nrbranches","leafArea",
                               "fpar","rfr","biom","yield","leafmass","stemmass",
                               "rootmass","shootrootratio","abovebiom",
                               "transpiration"])

                           df0.to_csv('/home/renato/groimp_efficient/run_1/plant_%s.txt' %int(min3p.gen.time_io), sep='\t', index=False, header=None)

                           print ('PET =',min3p.biol.pet)
                           pet.append(min3p.biol.pet)

                         min3p.gen.time_io_prec = min3p.gen.time_io 
                         #! CB pour calcul pas de temps delt_MIN3P 
                         #a mettre ds Compute_archi
                   
                         for ivol in range(0,min3p.gen.nn):
                             file_rlddata.write("%f %f %f %f %f\n" %
                                           (min3p.biol.time_rld,
                                           x_g.item(ivol),y_g.item(ivol),
                                           z_g.item(ivol),min3p.biol.rld.item(ivol)))

                     
                         if (min3p.biol.compt_rld_coupled >= 2): 
                            pass
                            empty = 0
          
                         min3p.biol.time_rld=min3p.biol.time_rld + 1.0   

                    #!END COUPLAGE 
                    for ivol in range(0,min3p.gen.nn):
                       min3p.biol.rldbck[ivol] = min3p.biol.rld[ivol]
             
                    sumrld = 0.0
                    for ivol in range(0,min3p.gen.nn):
                       sumrld = sumrld + min3p.biol.rldbck[ivol]

                    if (sumrld == 0):
                       min3p.biol.rootdensitynill= True
                    else:
                       min3p.biol.rootdensitynill= False
                    break                  
                    print('HERE')    
                    print('GOTO = ',go_to)   
                if (go_to == 1):
                   continue
                else:
                   break 
               #  update etp and canopy dependent parameters
               if (min3p.biol.root_uptake or min3p.gen.pure_evap):
 	           min3p.updtetp()
                   #sys.exit()
                   pass

               #  update temperature field
               if (min3p.chem.temp_field):
                   min3p.readtemp()
                   if (min3p.chem.update_temp):
                       min3p.intpolt()

               # update cputime
               cpuint_old = min3p.gen.cpuint
               min3p.gen.cpuint = time.time()
               if (min3p.gen.cpuint < cpuint_old):
                   min3p.gen.csec = min3p.gen.csec + min3p.gen.cpuint 
                   - cpuint_old + r86400
               else:
                   min3p.gen.csec = min3p.gen.csec + min3p.gen.cpuint - cpuint_old
       




    #cputime and statistics to screen and generic output file

    if (min3p.gen.varsat_flow or min3p.gen.reactive_transport):
        min3p.rstatgs(min3p.gen.ilog)
        min3p.rstatgs(min3p.gen.igen)
        empty = 0
 
    print('  ***************** normal exit ******************')
    #write(ilog,'(72a)')('-',i=1,72)
    #write(ilog,'(/a//)')
    # &'         ***************** normal exit ******************'
    # write(igen,'(72a)')('-',i=1,72)
    # write(igen,'(/a//)')
    #&'         ***************** normal exit ******************'

    #  close I/O files (global system)
   
    min3p.clsgfls()

      
    #CB WRITE AND CLOSE FILE ARCHISIMPLE :
    lib.END_ARCHI()

    

    sys.exit()



if __name__ == "__main__":
    main()
