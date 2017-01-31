#PBS -q batch
#PBS -N sender
#PBS -l nodes=2:ppn=4
#PBS -M js.barbosa10@uniandes.edu.co
#PBS -m abe

module load openmpi/1.8.5
cd $PBS_O_WORKDIR
NPROCS=`wc -l < $PBS_NODEFILE`
mpiexec -v -n $NPROCS ./sender
