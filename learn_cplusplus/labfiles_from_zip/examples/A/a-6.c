#include <stdio.h>
main()
{

	int base = 2;		/* define and init */
	int exponent = 5;	/* define and init */
	int result = 1;		/* define and init */
	int i;

	for(i = 0; i < exponent; i++)
		result *= base;

	/*
		printf is a function which displays
		things on the standard output.  Each item
		to be displayed must have a format
		specifier such as %d for integers, or %f
		for decimal numbers
	*/

	printf("%d to the %d power is %d\n",
			base,    exponent,   result);

	return 0;

}
