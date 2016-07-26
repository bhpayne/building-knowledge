//
//  Solution 7-2
//
#include <iostream>

using namespace std;

#include "Circle.h"
#include "MyString.h"

Circle::Circle(double r, MyString s) : Shape(s)
{
	radius = r;
}

Circle::~Circle()
{
	cout << "Circle destructor" << endl;
}

double Circle::perimeter()
{
	return 2 * 3.14159 * radius;
}

double Circle::area()
{
	return 3.14159 * radius * radius;
}

