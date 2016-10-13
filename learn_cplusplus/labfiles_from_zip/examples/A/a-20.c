#include <stdio.h>
int multiply(int a, int b)  	/* return type: int */
{				/* name: multiply	*/
	int c;			/* arg list: a, b 	*/
	c = a * b; 
	return c;
}

void print(int param)		/* return type: void */
{				/* name: print		 */
	printf("%d\n", param);	/* arg list: param 	 */
}
main()
{
	int x = 10, y = 20, z;
	z = multiply(x, y);
	print(z);
}


