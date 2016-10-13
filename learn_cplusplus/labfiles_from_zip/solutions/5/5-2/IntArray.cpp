//
//	Solution for Exercise 5-2
//
#include <iostream>

using namespace std;

#include "IntArray.h"

IntArray::IntArray(int size)
{
	howmany = size;
	data = new int[howmany];
	int i;
	for (i = 0; i < howmany; i++)
		data[i] = 0;
}

IntArray::IntArray(const IntArray & car)
{
	helper(car);
}

IntArray::~IntArray()
{
	delete [] data;
}

IntArray & IntArray::operator=(const IntArray & car)
{
	if ( this != &car )
	{
		delete [] data;
		helper(car);	
	}
	return *this;
}

void IntArray::print()
{
	int i;
	
	for (i = 0; i< howmany; i++)
		cout << data[i] << " ";
		
	cout << endl;
}

void IntArray::helper(const IntArray & car)
{
	howmany = car.howmany;
	data = new int[howmany];
	for (int i = 0; i < howmany; i++)
		data[i] = car.data[i];
}

