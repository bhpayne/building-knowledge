//
//  Solution 7-2
//

#ifndef CIRCLE_H
#define CIRCLE_H

#include "Shape.h"
#include "MyString.h"

class Circle : public Shape
{	
protected:
	double radius;
	
public:
	Circle(double radius, MyString s);
	~Circle();
	
	virtual double perimeter();
	virtual double area();
};

#endif

