#include <stdio.h>
main()
{
	int hm;
	char book[20];
	double price;

	printf("enter a number ");
	scanf("%d", &hm);
	printf("enter a title ");
	scanf("%s", book);
	printf("enter a price ");
	scanf("%lf", &price);
	printf("%d %s's cost $%.2f\n", hm, book, hm * price);
}



