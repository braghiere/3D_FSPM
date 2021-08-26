#!/bin/bash  
echo "--------------------------------------------------------------------------"  
echo "------------------------ Start GroIMP 1.5 --------------------------------" 

#java -Xmx2000m -jar /home/renato/Downloads/GroIMP-1.5/core.jar --headless --degub=INFO  /home/renato/Downloads/FSPM_BASIC-master-transpired/project.gs  

echo "--------------------------------------------------------------------------"  
echo "------------------------ Reading PET from GroIMP 1.5 ---------------------" 
 
filename_transp_groimp="/home/renato/groimp/transp.txt"

index=0
{
read
while IFS=, read -r line 
do
        PET[$index]=`echo ${line} | sed -e 's/[eE]+*/\\*10\\^/'`
        #PET[$index]=${line/[eE]+*/*10^}
	index=$(($index+1))
done
} < $filename_transp_groimp

echo "MY PET ARRAY is: ${PET[*]}"
echo "Total days in the file: ${index}"

day=$index

echo $day

echo "--------------------------------------------------------------------------"  
echo "--------------- Writing feddes.soi for Min3pArchiSImple ------------------" 

filename_et_min3p="/home/renato/groimp/input/feddes.soi"

index=0

while read day     ET     CI     SR     STR 
do
        ET[$index]=`echo ${ET} | sed -e 's/[eE]+*/\\*10\\^/'`
        #ET[$index]=${ET/[eE]+*/*10^}
        ET[$index]="($(sed 's/[eE]+\{0,1\}/*10^/g' <<<"$ET"))"
	index=$(($index+1))

done < $filename_et_min3p

echo "MY ET ARRAY is: ${ET[*]}"
echo "Total days in the file: ${index}"

echo "--------------------------------------------------------------------------"  
echo "--------------- Writing beta file for groimp -----------------------------" 

echo "the value of day is : $day"

startvalue=0
stopvalue=60


beta=$(for ((i=$startvalue;i<=stopvalue;++i)); do
          a=`echo ${ET[i]} | bc -l`
          b=`echo ${PET[i]} | bc -l`
          c=`echo $a/$b | bc -l`


          if (( $(bc <<< "$c <= 1") ))
          then
             echo "$c" | bc -l
          elif (( $(bc <<< "$c > 1") ))
          then
             echo "1.0" | bc -l
          else 
             echo "0.0" | bc -l
          fi

      done)

  echo "MY beta ARRAY is: ${beta[*]}"







