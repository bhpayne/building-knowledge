//
//  Solution 7-2
//
#include <iostream>

using namespace std;

#include "Shape.h"
#include "MyString.h"

Shape::Shape(MyString s)
{
	shapename = s;
}

Shape::~Shape()
{
	cout << "Shape Destructor\n";
}

const char * Shape::getName()
{
	return shapename.getString();
}


