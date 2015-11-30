#include <stdio.h>

int *ppointer;

void somefunc()
{
    int nnumber;
    //assign values
    nnumber=25;
    ppointer=&nnumber;
    
}
void main(){
    //declare variables
    somefunc();
    printf("value of pointer=%d\n", *ppointer);
}