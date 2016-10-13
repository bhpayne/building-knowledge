//
//  9-19.cpp
//
#include <iostream>
#include <cstdlib>

using namespace std;

#include "List.h"

int main(int argc, char **argv)
{
    if (argc != 2)
    {
        cerr << "Please specify # of desired elements on the command line" << endl;
        return 1;
    }
    
	int iterations = atoi(argv[1]);
	int i, j;
	List aList;
	
	for ( i = 0; i < iterations; i++)
		aList.insert(i);
		
	for ( i = 0; i < aList.length(); i++)
		j = aList[i];
		
	cout << "Total Reps: " << aList.getReps() << endl;
	
	return 0;
}



