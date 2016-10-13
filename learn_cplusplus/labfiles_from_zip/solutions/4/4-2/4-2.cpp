//
//	Solution 4-2
//
#include <iostream>

using namespace std;

#include "MyDate.h"

int main()
{
	MyDate d1(26,2,2001);
	d1.print();

	MyDate d2(26,2);
	d2.print();
	
	MyDate d3(26);
	d3.print();
	
	MyDate d4;
	d4.print();
	
	cout << d4.getDay() << endl;
	cout << d4.getMonth() << endl;
	cout << d4.getYear() << endl;
	
	cout << d4.getDayOfYear() << endl;
	cout << d4.getMonthAsString() << endl;
	
	return 0;
}

