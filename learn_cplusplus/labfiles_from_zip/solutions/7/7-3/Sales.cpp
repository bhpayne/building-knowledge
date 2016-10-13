//
// Solution for Exercise 7-3
//
#include <iostream>

using namespace std;

#include "Sales.h"

Sales::Sales(string s) : Employee(s) {}

double Sales::pay()
{
	return 100;
}

void Sales::vacation()
{
	cout << "Sales Vacation" << endl;
}

double Sales::pension()
{
	return 1000;
}

void Sales::bonus( )
{
	cout << "Sales Bonus" << endl;
}


