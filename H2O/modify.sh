#!/bin/bash

WDIR=`pwd`
for i in 200  300  400  500  600  700
do
cd $WDIR/$i
# sed -i "s/--job-name=\$i/--job-name=$i/g" run.slurm
# sed -i "s/ENCUT = \$i/ENCUT = $i/g" INCAR
bash cleanup.sh
sbatch run.slurm
done
