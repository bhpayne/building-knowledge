#define SIZE 5
main()
{
	int x[SIZE] = { 1,2,3,4,5 };
	int i, end, temp;
	printf("print array elements\n");
	for (i = 0; i < SIZE; i++)
		printf("%d ", x[i]);
	printf("\nadd 5 to each element\n");
	for (i = 0; i < SIZE; i++)
		x[i] = x[i] + 5;
	printf("print them again\n");
	for (i = 0; i < SIZE; i++)
		printf("%d ", x[i]);
}



