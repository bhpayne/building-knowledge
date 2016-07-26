//
//	5-19.cpp
//

#include "IntArray.h"

int main()
{
	IntArray values(10);
	values.print();
	
	IntArray items = values;
	items = values;
	
	return 0;
}
