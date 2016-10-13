//
//  Point.cpp
//
#include <iostream>

using namespace std;

#include "Point.h"

Point::Point(int x, int y) : xc(x), yc(y) {}

Point::Point(const Point & p) : xc(p.xc), yc(p.yc)
{
	cout << "Point Copy Constructor" << endl;
}

Point & Point::operator=(const Point &)
{
	cout << "Point Assignment Operator" << endl;
	return *this;
}

void Point::print( ) const
{
	cout << xc << "," << yc << endl;
}

