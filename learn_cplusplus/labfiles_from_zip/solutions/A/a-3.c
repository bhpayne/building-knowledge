//
//	Exercise 1-3
//
//	Ask the user to input a few numbers.  Print the sum of the integers
//	between and including those 2 numbers. Make sure that the first number
//	is lower than the second number.
//
#include <stdio.h>
main()
{
	int first, second, sum = 0, i;
	printf("enter the first number: ");
	scanf("%d", &first);
	printf("enter the second number: ");
	scanf("%d", &second);
	while(second < first) {
		printf("ERROR: first number not < second number\n");
		printf("reenter second number ");
		scanf("%d", &second);
	}
	for( i = first; i <=second; i++)
		sum += i;
	printf("The sum of the integers between ");
	printf("%d and %d is %d\n", first, second, sum);
}
