yacc -d example1.y 
lex example1.l
gcc lex.yy.c y.tab.c -o runme
