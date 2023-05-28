%{
void yyerror (char *s);
#include <stdio.h>
#include <stdlib.h>

%}

%start line
%token exit_command
%token print
%token exp
%%

/* descriptions of expected inputs	corresponding actions (in C) */

line	: exit_command ';'	{exit(EXIT_SUCCESS);}
	| exp ';'		{;}
	| print exp ';'		{printf("printing %d\n", $2);}
	| line print exp ';'	{printf("printing %d\n", $3);}
	| line exit_command ';'	{exit(EXIT_SUCCESS);}
	;

%%  /* C code */

int main (void) {
  return yyparse();
}

void yyerror (char *s) {fprintf (stderr, "%s\n", s);}


