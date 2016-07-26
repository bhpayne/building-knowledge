//
//	Solution for Exercise 5-1
//
#include <iostream>

using namespace std;

#include "Fraction.h"

int main()
{
	Fraction a(2,3), b(5,6), c;
	
	a.print();
	b.print();
	
	cout << "MULT" << endl;
	c = a * b;
	c.print();
	
	cout << "DIVIDE" << endl;
	c = a / b;
	c.print();
	
	cout << "ADD" << endl;
	c = a + b;
	c.print();

	cout << "SUBTRACT" << endl;
	c = a - b;
	c.print();
	
	return 0;
}

