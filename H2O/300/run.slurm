#!/bin/bash
#SBATCH --job-name=300       # create a short name for your job
#SBATCH --nodes=1                # node count
#SBATCH --ntasks-per-node=1      # total number of tasks per node
#SBATCH --cpus-per-task=1        # cpu-cores per task (>1 if multi-threaded tasks)
#SBATCH --mem-per-cpu=4G         # memory per cpu-core (4G is default)
#SBATCH --time=01:30:00          # total run time limit (HH:MM:SS)


export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK
export PATH=$PATH:/scratch/gpfs/yp0007/software/vasp/vasp.6.3.2/bin

module purge
module load intel/19.1/64/19.1.1.217
module load intel-mpi/intel/2019.7/64

srun vasp_gam