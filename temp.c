#include <stdio.h>
#include <stdlib.h>

main(void)
{
    int i = 1;
    double uniform = 0;
    for(i; i<21; i++)
    {
        uniform = rand()/(double)RAND_MAX;
        printf("%f\n", uniform);
    }
    return 0;
}
