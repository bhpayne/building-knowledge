//
//	Exercise 4-2
//
#include <stdio.h>
void average(int [], int, double *);
main()
{
	double answer;
	int numbers[10] = { 1,2,3,4,5,6,7,8,9,10};
	average(numbers,10, &answer);
	printf("average is %.3f\n", answer);
}
void average(int param[], int amt, double *output)
{
	int i;
	*output = 0.0;
	for ( i = 0; i < amt; i++)
		*output += param[i];
	 *output /= amt;
}
	
