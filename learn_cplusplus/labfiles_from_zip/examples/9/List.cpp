//
//  List.cpp
//
#include <iostream>
#include <stdlib.h>

using namespace std;

#include "List.h"

List::List() : head(0), tail(0), howmany(0), reps(0)
{
	cout << "List Constructor" << endl;
}

List::~List()
{
	Item *scan = head;
	Item *deleted;
	
	while( scan != 0 )
	{
		deleted = scan;
		scan = scan -> next;
		delete deleted;
	}
}

int List::operator[](int position) const
{
	Item * ptr;
	
	for ( ptr = head; position > 0; position--)
	{
		reps++;
		ptr = ptr -> next;
	}
	
	return ptr -> data;
}

void List::insert(int newElement)
{
	Item *newItem = new Item(newElement);
	if (newItem == 0) {
	    cerr << "Memory allocation failed in List::insert" << endl;
	    exit(1);
	}

	if ( head == 0)
		head = tail = newItem;
	else
	{
		newItem -> next = head;
		head = newItem;
	}
	howmany++;
}


