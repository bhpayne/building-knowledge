%{
#include "example2.h"
%}
%%
","		return COMMA;
":"		return COLON;
"("		return right_paran;
")"		return left_paran;
"=="		return equals;
"0"		return ZERO;
"1"		return ONE;
a[0-9]+		return bit;
am[0-9]+	return passed_bit;
#.*		return COMMENT; // everything after #
"VAR"		return VARIABLE;
"MACRO"		return KEYWORD_MACRO;
"BEGIN"         return KEYWORD_BEGIN;
"input"         return KEYWORD_input;
"output"        return KEYWORD_output;
"END"           return KEYWORD_END;
"if"		return KEYWORD_if;
"@newtime"	return DIRECTIVE_newtime;
"@ec"		return DIRECTIVE_ec;
"@assert"	return DIRECTIVE_assert;
"h"		return had;
"cx"		return cnot;
"x"		return not;
[a-zA-Z][a-zA-Z_0-9]+      return name; // this must come after all other keywords
[ \t\n]		; //do nothing with empty lines
.		printf("unexpected input\n");
%%

int yywrap(void)
{
    return 1;
}
