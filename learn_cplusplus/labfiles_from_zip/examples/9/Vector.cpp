//
//  Vector.cpp
//

#include "Vector.h"
#include "SizeException.h"
#include "RangeException.h"

Vector::Vector(int sz, int max)
{
	size = sz;
	maxValue = max;
	
	p = new int[size];	
}

int Vector::getValue(int pos)
{
	if (pos >= size || pos < 0)
		throw RangeException(pos, "getValue: range error");
		
	return p[pos];
}

void Vector::setValue(int pos, int value)
{
	if (pos >= size || pos < 0)
		throw RangeException(pos, "setValue: range error");
		
	if (value > maxValue)
		throw SizeException(value, "setValue: value is too big");
		
	p[pos] = value;
}



