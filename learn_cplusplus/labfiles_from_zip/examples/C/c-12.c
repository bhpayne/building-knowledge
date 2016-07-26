#include <stdio.h>
enum Days
{
	Sun, Mon, Tues, Wed, Thurs, Fri, Sat
};
main()
{
	enum Days i;
	for (i = Sun; i <= Sat; i++)
	{
		if ( i == Sat || i == Sun)
			printf("not open on Weekends\n");
		else if (i >= Mon && i <= Thurs)
			printf("open 9AM - 5PM Weekdays\n");
		else
			printf("open 9AM - 9PM on Fridays\n");
	}
}



