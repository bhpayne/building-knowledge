//
//  9-18.cpp
//
#include <iostream>

using namespace std;

#include "List.h"

int main()
{
    List aList;

    int a = 20;
    int b = 30;
    int c = 40;
    int d = 50;

    aList.insert(a);
    aList.insert(b);
    aList.insert(c);
    aList.insert(d);
		
	for (int i = 0; i < aList.length(); i++)
		cout << aList[i] << endl;
		
	return 0;
}



