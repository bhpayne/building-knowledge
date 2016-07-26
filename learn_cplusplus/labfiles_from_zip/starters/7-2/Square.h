//
//  Starter for Exercise 7-2
//

#ifndef SQUARE_H
#define SQUARE_H

#include "Shape.h"
#include "MyString.h"

class Square : public Shape
{
protected:    
	double side;
	
public:
	Square(double s, MyString ms);
	~Square();
	
	virtual double perimeter();
	virtual double area();
};

#endif


