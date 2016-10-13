//
// Solution for Exercise 7-3
//
#include <iostream>

using namespace std;

#include "Marketing.h"

Marketing::Marketing(string s) : Employee(s) {}

double Marketing::pay()
{
	return 200;
}

void Marketing::vacation()
{
	cout << "Marketing Vacation" << endl;
}

double Marketing::pension()
{
	return 2000;
}

void Marketing::bonus( )
{
	cout << "Marketing Bonus" << endl;
}


