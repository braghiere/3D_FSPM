#!/usr/bin/env python

import os

for i in range(60):
   print i

   cmd = "ls -%s -%s"%(i,i+1)
   os.system("grep -vf /home/renato/groimp_efficient/run_1/seg%s.txt /home/renato/groimp_efficient/run_1/seg%s.txt > run1_root_data/seg%s.txt" %(i,i+1,i)) 


