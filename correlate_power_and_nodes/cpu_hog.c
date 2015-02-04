#include <time.h>
#include <stdio.h>
#include <stdlib.h>

/*********
 * Ben Payne
 * from
 * http://stackoverflow.com/questions/4019121/run-an-infinite-loop-for-a-while-in-c
 * http://stackoverflow.com/questions/5157337/c-reading-command-line-parameters
 */

/*
 The arguments to main are:
 int argc - the number of arguments passed into your program when it was run. It is at least 1.
 char **argv - this is a pointer-to-char *. It can alternatively be this: char *argv[], which means 'array of char *'. This is an array of C-style-string pointers.
 */
int main(int argc, char **argv){
//    printf("I got here");

    if ( argc < 2 ){ // expecting a single command line argument
        printf("expecting 1 argument, number of seconds to run, and got %d arguments\n",argc-1);
        return 0;
//    }else{
//        printf("got %d argument\n",argc-1);
    }
    int delay_time = strtol(argv[1],NULL,10);
//    printf("time delay is %d\n",delay_time);
    
    // set the end time to the current time plus <input> seconds
    time_t endTime = time(NULL) + delay_time;

//    printf("while %lld < %lld\n", (long long) time(NULL), (long long) endTime);
    
    int asdf;
    while (time(NULL) < endTime){
        asdf=1+1; // do work here
//        printf("while %lld < %lld\n", (long long) time(NULL), (long long) endTime);
    }
}

