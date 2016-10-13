/*
prints the numbers 1 to 10, one number per line
prints the numbers 10 to 1 (counting backwards), one number per line
prints the numbers 1 to 100, 10 numbers per line 
Challenge:  Ask the user for the upper limit, whether they want forward or backwards, and how many numbers to print per line. 

*/

// gcc morning_warmup_loops_from_Alan.c

#include <stdio.h>

void challengeFunction(int limit, int direction, int perLine);

int main(){
    int i = 1, j = 0;
    int limit = 0, direction = 0, perLine = 0;

/*
    for (i = 1; i <= 10; i++){
        printf("%d\n", i);
    }
    printf("\n\n");

    for (i = 10; i >= 1; i--){
        printf("%d\n", i);
    }
    printf("\n\n");

    for (i = 1; i <= 100; i++){
//        if (j == 10){
//            printf("\n");
//            j = 0;
//        }
        printf("%d ", i);
        if (i % 10 == 0) {
            printf("\n");
        }
    }
    printf("\n\n");

    return 0;
*/

    printf("Enter the number limit\n");
    scanf("%d", &limit);

    printf("Enter the direction (0 for forward, 1 for backwards)\n");
    scanf("%d", &direction);
    
    printf("Enter the amount of numbers to print per line\n");
    scanf("%d", &perLine);
    challengeFunction(limit, direction, perLine);
    return 0;

}

//Direction: 0 for forward and 1 for backwards
//Limit: The number to count up to
//perLine: The amount of numbers to print per line
void challengeFunction(int limit, int direction, int perLine){
    int j = 0;
    int i = 0;

    if (direction == 0){
        for (i = 1; i <= limit; i++){
            if (j == perLine){
                printf("\n");
                j = 0;
            }
            printf("%3d ", i);
            j++;
        }
    } else if (direction == 1){
        for (i = limit; i >= 1; i--){
            if (j == perLine){
                printf("\n");
                j = 0;
            }
            printf("%3d ", i);
            j++;
        }
    }
    printf("\n");

    return;
}
