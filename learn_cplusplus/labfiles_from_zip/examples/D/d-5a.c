#include <stdio.h>
void change_wrong(int a);
main()
{
	int a = 10;
	printf("Before call: %d\n", a);
	change_wrong(a);
	printf("After call: %d\n", a);
}
void change_wrong(int param)
{
	param = param + 1;
	printf("Inside function: %d\n", param);
}



