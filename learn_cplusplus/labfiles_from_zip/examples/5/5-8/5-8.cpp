//
//	5-8.cpp
//

#include "Fraction.h"

int main()
{
	Fraction a(2,3), b(5,2), c(4,3), d(1,2);
	
  	c = (a - b) * (c + d);
	c.print();
	
	return 0;
}
