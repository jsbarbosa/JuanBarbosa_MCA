To log into the machine:
```
ssh fisi3028@clustergate.uniandes.edu.co
```

Information about cpus
```
lscpu; qnodes
```

Queue
```
qstat -q
```

In order to submit a job a bash script is required. Submision is made using `qsub submit_job.sh`
```
#PBS -q batch
#PBS -N test_scheduler
#PBS -l nodes=2:ppn=4
#PBS -M js.barbosa10@uniandes.edu.co
#PBS -m abe

module load openmpi/1.8.5
cd $PBS_O_WORKDIR
NPROCS=`wc -l < $PBS_NODEFILE`
mpiexec -v -n $NPROCS ./mpi_hello_world
```
