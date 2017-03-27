/*
 * montecarlo.c
 * 
 * Copyright 2017 juan <juan@lenovo>
 * 
 * This program is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 2 of the License, or
 * (at your option) any later version.
 * 
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 * 
 * You should have received a copy of the GNU General Public License
 * along with this program; if not, write to the Free Software
 * Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
 * MA 02110-1301, USA.
 * 
 * 
 */

#include <mpi.h>
#include <time.h>
#include <stdio.h>
#include <stdlib.h>
#include <assert.h>
#include <math.h>

int generator(int num_elements){
    float x, y, r;
    int count = 0, i = 0;
    for (i; i < num_elements; i++)
    {
        x = drand48();
        y = drand48();
        r = pow(pow(x, 2) + pow(y, 2), 0.5);
        if (r < 1)
        {
            count = count + 1;
        }
    }
    return count;
}

int main(int argc, char** argv) 
{
    int rank, size;
    
    MPI_Init(NULL, NULL);
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    MPI_Comm_size(MPI_COMM_WORLD, &size);
    
    srand48(time(NULL) + rank);

    int num_elements_per_proc = atoi(argv[1]);
    int each = generator(num_elements_per_proc);
    int *all = (int*)malloc(sizeof(int)*size);
    assert(all != NULL);
    
    float denom = size*num_elements_per_proc;
    
    MPI_Gather(&each, 1, MPI_INT, all, 1, MPI_INT, 0,MPI_COMM_WORLD);
    if (rank == 0)
    {
        int sum = 0, i;
        for(i = 0; i < size; i++)
        {
            sum = sum + all[i];
        }
        
        printf("%f\n", 4*sum/denom);
    }    
    MPI_Barrier(MPI_COMM_WORLD);
    MPI_Finalize();
}

