/*

prints the numbers 1 to 10, one number per line
prints the numbers 10 to 1 (counting backwards), one number per line
prints the numbers 1 to 100, 10 numbers per line

Challenge:  Ask the user for the upper limit, whether they want forward or backwards, and how many numbers to print per line.

*/

#include <stdio.h>

int main(){
 
    printf("prints the numbers 1 to 10, one number per line\n");
    for (int indx=1; indx<=10; indx++){
        printf("%d\n",indx);
    }
    
    printf("prints the numbers 10 to 1 (counting backwards), one number per line\n");
    for (int indx=10; indx>=1; indx--){
        printf("%d\n",indx);
    }
    
    printf("prints the numbers 1 to 100, 10 numbers per line\n");
    for (int indx=0; indx<100; indx++){
        if (indx%10==0){
            printf("\n");
        }
        printf("%d,",indx+1);
    }
    printf("\n");
    
    int limit=0, direction=0, perline=0;
    printf("Upper limit: ");
    scanf("%d",&limit);
    printf("forward (0) or backwards (1): ");
    scanf("%d",&direction);
    printf("how many numbers to print per line: ");
    scanf("%d",&perline);
    
    if (direction==0){
        printf("prints the numbers 1 to %d, %d numbers per line\n",limit,perline);

        for (int indx=0; indx<limit; indx++){
            if (indx%perline==0){
                printf("\n");
            }
            printf("%d,",indx+1);
        }
        printf("\n");


    }else{
        printf("prints the numbers %d to 1, %d numbers per line\n",limit,perline);

        for (int indx=limit; indx>0; indx++){
            if (indx%perline==0){
                printf("\n");
            }
            printf("%d,",indx+1);
        }
        printf("\n");
    }
    
}
