//
//  Solution 7-2
//
#include <iostream>

using namespace std;

#include "Square.h"
#include "MyString.h"

Square::Square(double s, MyString ms) : Shape(ms)
{
	side = s;
}

Square::~Square()
{
   	cout << "Square destructor" << endl;
}

double Square::perimeter()
{
	return side * 4;
}

double Square::area()
{
	return side * side;
}


