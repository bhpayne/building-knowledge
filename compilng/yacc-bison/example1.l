%{
#include "y.tab.h" // file produced by yacc
%}

%%

"print"		{return print;}
"exit"		{return exit_command;}
[a-zA-Z]+	{return exp;}
#[a-zA-Z_ 0-9]+	{return yytext[0];}
[ \t\n]		; // do nothing
.		{ECHO; yyerror ("unexpected char");}

%%

int yywrap (void) {return 1;}


