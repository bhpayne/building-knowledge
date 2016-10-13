//
//  Starter for Exercise 7-2
//

#ifndef SHAPE_H
#define SHAPE_H

#include "MyString.h"

class Shape
{
protected:
	MyString shapename;
	
public:
	Shape(MyString s);
	virtual ~Shape();
	
	virtual double perimeter() = 0;
	virtual double area() = 0;
	
	const char *getName();
};

#endif

