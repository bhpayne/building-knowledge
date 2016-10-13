#include <math.h>
#include <stdio.h>
#include <stdlib.h>

/* if use cc compiler must use -lm option */

main()
{
	char buffer[100];
	double n1, n2, n3;
	printf("enter a base ");
	gets(buffer);
	n1 = atof(buffer);
	printf("enter an exponent ");
	gets(buffer);
	n2 = atof(buffer);
	n3 = pow(n1, n2);
	printf("%f raised to the %f is %f\n", n1, n2, n3);
}



