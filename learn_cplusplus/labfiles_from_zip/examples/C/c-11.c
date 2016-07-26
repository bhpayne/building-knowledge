/* 	You can write the code in terms of the
	integers from 1 to 7 where
	1 = Sunday, 2 = Monday, 3 = Tuesday, etc.
*/
main()
{
	int i;
	for (i = 1; i <= 7; i++)
	{
		if ( i == 7 || i == 1)
			printf("not open on Weekends\n");
		else if (i >= 2 && i <= 5)
			printf("open 9AM - 5PM Weekdays\n");
		else
			printf("open 9AM - 9PM on Fridays\n");
	}
}


