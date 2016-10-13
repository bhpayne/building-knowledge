//
//	IntArray.cpp
//
#include <iostream>

using namespace std;

#include "IntArray.h"

// Constructor
IntArray::IntArray(int size)
{
	howmany = size;
	data = new int[howmany];
	for (int i = 0; i < howmany; i++)
		data[i] = 0;
}

// Copy constructor
IntArray::IntArray(const IntArray & car)
{
	howmany = car.howmany;
	data = new int[howmany];
	for (int i = 0; i < howmany; i++)
		data[i] = car.data[i];
}

// Assignment Operator
IntArray & IntArray::operator=(const IntArray & car)
{
	if ( this != &car )
	{
		delete [] data;
		howmany = car.howmany;
		data = new int[howmany];
		for (int i = 0; i < howmany; i++)
			data[i] = car.data[i];
	}
	return *this;
}

// Destructor
IntArray::~IntArray()
{
	delete [] data;
}
	
void IntArray::print()
{
	for (int i = 0; i< howmany; i++)
		cout << data[i] << " ";
	cout << endl;
}



