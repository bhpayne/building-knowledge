//
//  Iterator.cpp
//

#include "Iterator.h"

Iterator::Iterator(const List & aList) : currentItem(aList.head) {}

int Iterator::operator*()
{
    return currentItem -> data; 
}

Iterator Iterator::operator++() 
{
	if (currentItem)
	{
		currentItem = currentItem -> next;
	}

	return *this;
}


