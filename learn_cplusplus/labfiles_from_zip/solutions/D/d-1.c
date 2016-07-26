//
//	Exercise 4-1
//
#include <stdio.h>
double average(int [], int);
main()
{
	double answer;
	int numbers[10] = { 1,2,3,4,5,6,7,8,9,10};
	answer = average(numbers,10);
	printf("average is %.3f\n", answer);
}
double average(int param[], int amt)
{
	double sum = 0.0;
	int i;
	for ( i = 0; i < amt; i++)
		sum += param[i];
	return sum/amt;
}
