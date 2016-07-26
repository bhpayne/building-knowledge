//
//  Solution 7-2
//

#include <iostream>

using namespace std;

#include "Shape.h"
#include "Circle.h"
#include "Square.h"

int main()
{
    const int SIZE = 4;
    
	Circle  c1(5.0,  "Circle 1");
	Square 	s1(5.0,  "Square 1");
	Circle 	c2(10.0, "Circle 2");
	Square 	s2(10.0, "Square 2");
	
	Shape	*ptrs[SIZE] = { &c1, &s1, &c2, &s2 };

	cout << "AREAS" << endl;
	int i;
	for (i = 0; i < SIZE; i++)
		cout << ptrs[i] -> area() << endl;

	cout << "PERIMETERS" << endl;
	for (i = 0; i < SIZE; i++)
		cout << ptrs[i] -> perimeter() << endl;

	cout << "NAMES" << endl; 
	for (i = 0; i < SIZE; i++)
		cout << ptrs[i] -> getName() << endl;

	return 0;
}

