//
// Solution for Exercise 7-3
//
#include <iostream>

using namespace std;

#include "Accounting.h"

Accounting::Accounting(string s) : Contractor(s) {}

double Accounting::pay()
{
	return 400;
}

void Accounting::vacation()
{
	cout << "Accounting Vacation" << endl;
}

void Accounting::review()
{
	cout << "Accounting Review" << endl;
}
