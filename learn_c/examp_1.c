#include <stdio.h>

void main(){
  //declare variables
  int nnumber;
  int *ppointer;
  //assign values
  nnumber=15;
  ppointer=&nnumber;
  //print values
  printf("nnumber= %d\n",nnumber);
  //alter value through pointer
  *ppointer=25;
  printf("nnumber now= %d\n",nnumber);
}