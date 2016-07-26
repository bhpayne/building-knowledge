//
//	Solution for Exercise 5-3
//
#include "IntArray.h"

int main()
{
	IntArray values(10);
	
	values.print();
	
	IntArray items = values;
	items = values;
	
	values = 10;		
	values.print();
	
	values.reset(8);
	values.print();
	
	(++values).print();
	
	values[0] = values[6] = 15;	
	values.print();
	
	return 0;
}


