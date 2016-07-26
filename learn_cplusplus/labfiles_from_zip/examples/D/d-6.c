#include <stdio.h>
#define N 5
int total(int * param, int number);
main()
{
	int data[N], result;
	int i = 1;
	int *px;
	for (px = data; px < data + N; px++)
		*px = i++;
	result = total(data, N);
	printf("%d\n", result);
}
int total(int * param, int number)
{
	int sum = 0, i;
	for (i = 0; i < number; i++)
		sum += *param++;
	return sum;
}



