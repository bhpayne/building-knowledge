//
//  Line.cpp
//
#include <iostream>

using namespace std;

#include "Line.h"

Line::Line(const Point & a1, const Point & a2) : p1(a1) , p2(a2) { }

Line::Line(const Line & clr) : p1(clr.p1), p2(clr.p2)
{
	cout << "Line Copy Constructor" << endl;
}

Line & Line::operator=(const Line & clr)
{
	cout << "Line Assignment Operator" << endl;
	
	p1 = clr.p1;
	p2 = clr.p2;
	
	return *this;
}

void Line::print( ) const
{
	p1.print();
	p2.print();
}

