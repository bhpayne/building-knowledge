//
// Solution 7-1
//
#include <iostream>

using namespace std;

#include "Point.h"

Point::Point(int a, int b) : n(a), d(b) {}

int Point::getX()
{
    return n;
}

int Point::getY()
{
    return d;
}

void Point::print()
{
	cout << n << "," << d;
}


