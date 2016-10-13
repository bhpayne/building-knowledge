#include <stdio.h>		/* for printf function */
#include <string.h>		/* for strcpy function */
#include "Record.h"		/* for Record definition */

void print(struct Record param)
{
	printf("%-20s%10.2f%4d\n", param.name, param.pay, param.grade);
}

struct Record initialize( char n[], double p, int g)
{
	struct Record temp;
	strcpy(temp.name, n);
	temp.pay = p;
	temp.grade = g;
	return temp;
}

main()
{
	struct Record e1, e2;
	e1 = initialize("Mike", 1000.00, 12);
	e2 = initialize("Susan", 1100.00, 13);
	print(e1);
	print(e2);
}



