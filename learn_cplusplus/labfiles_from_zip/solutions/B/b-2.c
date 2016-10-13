//
//	Exercise 2-2
//
//	Write a macro which returns the cube of an expression.
//
#include <stdio.h>
#define CUBE(X) ((X) * (X) * (X))
main()
{
	int x = 3, z = 0;
	printf("Z = %d: X = %d\n", z, x);
	z = CUBE(x);
	printf("AFTER z = CUBE(x): Z = %d: X = %d\n", z, x);
	z = CUBE(x + 1);
	printf("AFTER z = CUBE(x + 1): Z = %d: X = %d\n", z, x);
	z = CUBE(x++);
	printf("AFTER z = CUBE(x++): Z = %d: X = %d\n", z, x);
}
