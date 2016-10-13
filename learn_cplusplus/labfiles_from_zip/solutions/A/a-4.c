//
//	Exercise 1-4
//
//	Write a function which produces the sum of the squares of the
//	2 integers handed to the function.
//
int sum_of_squares(int side1, int side2);
#include <stdio.h>
main()
{
	int first, second, result;
	printf("enter the first number: ");
	scanf("%d", &first);
	printf("enter the second number: ");
	scanf("%d", &second);
	result = sum_of_squares(first, second);
	printf("Sum of %d squared and %d squared is %d\n",
		      first,         second,         result);
}
int sum_of_squares(int left, int right)
{
	int result;
	return left * left + right * right;
}
