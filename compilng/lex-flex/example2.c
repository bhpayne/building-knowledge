#include <stdio.h>
#include "example2.h"

extern int yylex();
extern int yylineno;
extern char* yytext;

char *names[] = {NULL, "bit", "BEGIN_COMMENT", "KEYWORD_MACRO", "KEYWORD_BEGIN", "KEYWORD_END", "KEYWORD_input", "KEYWORD_output", "KEYWORD_if", "DIRECTIVE_newtime", "DIRECTIVE_ec", "DIRECTIVE_assert", "had", "cnot", "not", "name", "COMMA","COLON","right_paran","left_paran","equals"};

int main(void)
{
  int name_token, value_token;
  name_token = yylex(); // return first valid token
  while(name_token) {
    printf("%d\n", name_token);
    // get next token
    name_token = yylex();
  }
  return 0;
}




