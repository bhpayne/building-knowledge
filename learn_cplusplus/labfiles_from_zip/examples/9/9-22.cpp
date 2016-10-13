//
//  9-22.cpp
//
#include <iostream>

using namespace std;

#include "List.h"
#include "Iterator.h"

int main()
{
	List myList;
	
	int a = 20;
	int b = 30;
	int c = 40;
	
	myList.insert(a);
	myList.insert(b);
	myList.insert(c);

	Iterator iter(myList);
	
	while (! iter.atEnd())
	{
		cout << *iter << endl;
		++iter;
	}
	
	return 0;
}



