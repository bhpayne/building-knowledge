#include <string.h>
#include <stdio.h>
main ()
{
	char prev[100], line [100];
	strcpy(prev, "");      /* empty string */
	while (gets(line) != NULL)
	{
		if (strcmp(line, prev) != 0)
		{
			printf("%s\n", line);
			strcpy(prev, line);
		}
	}
}
