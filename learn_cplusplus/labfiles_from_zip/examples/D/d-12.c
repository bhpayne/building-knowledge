#include <stdio.h>
#define MAX 100
main()
{
	char line[MAX];
	int length;
	gets(line);
	length = strlen(line);
	printf("length of %s", line);
	printf(" is %d\n", length);
}
int strlen(char *s)			/* s -> line 	 	*/
{
	int ct = 0;
	while(*s != '\0') {		/* end of string	*/
		s++;			/* no, add 1 to s	*/
		ct++;			/* add 1 to ct		*/
	}
	return (ct);
}


