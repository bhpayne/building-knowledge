#include <stdio.h>		/* for printf function */
#include <string.h>		/* for strcpy function */
#include "Record.h"		/* for Record definition */

void print(struct Record param)
{
	printf("%-20s%10.2f%4d\n", param.name, param.pay, param.grade);
}
main()
{
	struct Record e1, e2;
	strcpy(e1.name, "Mike");
	e1.pay = 1000.00;
	e1.grade = 12;
	strcpy(e2.name, "Susan");
	e2.pay = 1100.00;
	e2.grade = 13;

	print(e1);   		/* invoke print: pass e1 */
	print(e2);		/* invoke print: pass e2 */
}



