//
// Solution for Exercise 7-3
//
#include <iostream>

using namespace std;

#include "Legal.h"

Legal::Legal(string s) : Contractor(s) {}

double Legal::pay()
{
	return 300;
}
void Legal::vacation()
{
	cout << "Legal Vacation" << endl;
}
void Legal::review()
{
	cout << "Legal Review" << endl;
}


