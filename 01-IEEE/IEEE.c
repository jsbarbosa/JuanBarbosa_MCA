#include <stdio.h>
#include <math.h>

int main(void)
{
	unsigned int ref;
    float fixed, temp, step=3;

    int i; 
	
	for (i=-32*step; i<=32*step; i++)
	{
        fixed = pow(10, i/step);
        ref = (*(unsigned int*)&fixed) + 1;
        temp = (*(float*)&ref);
        printf("%.25e \t %.25e\n", fixed, temp-fixed);
	}
	return 0;
}
