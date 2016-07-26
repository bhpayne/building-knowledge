#include <stdio.h>
int multiply(int factor1, int factor2);
void print(int number);
main()
{
	int x = 10, y = 20, z;
	z = multiply(x, y);
	print(z);
}

int multiply(int a, int b)
{
	int c;
	c = a * b;
	return c;
}

void print(int param)
{
	printf("%d\n", param);
}


