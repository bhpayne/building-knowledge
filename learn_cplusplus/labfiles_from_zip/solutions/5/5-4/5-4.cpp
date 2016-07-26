//
//	Solution for Exercise 5-4
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
	
	IntArray data(10);
	data.reset(7);
	values = values + data;
	values.print();
	
	return 0;
}


