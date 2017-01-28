#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main(void)
{
    // DISCLAIMER added N, lambda, min, max, min_dist, max_dist, random. Previously it only printed uniform.

    int i = 1, N = 10000000; 
    double uniform = 0;

    double lambda = 3, min = 1, max = 20, min_dist, max_dist, random; //new
    
    min_dist = exp(-max/lambda); //new
    max_dist = exp(-min/lambda); //new

    for(i; i<N; i++)
    {
        uniform = rand()/(double)RAND_MAX;
        random = (max_dist-min_dist+1)*uniform + min_dist; //new
        uniform = -lambda*log(random); //new
        if (uniform >= 1) //new
        {
            printf("%f\n", uniform);
        }
    }
    return 0;
}
