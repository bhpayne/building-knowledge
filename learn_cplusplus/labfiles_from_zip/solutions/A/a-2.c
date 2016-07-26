//
//	Exercise 1-2
//
//	Ask the user to input a few numbers.  Print the sum of the integers
//	between and including those 2 numbers.
//
#include <stdio.h>
main()
{
	int first, second, sum = 0, i;

	printf("enter the first number: ");
	scanf("%d", &first);
	printf("enter the second number: ");
	scanf("%d", &second);
	for( i = first; i <= second; i++)
		sum += i;
	printf("The sum of the integers between ");
	printf("%d and %d is %d\n", first, second, sum);
}
