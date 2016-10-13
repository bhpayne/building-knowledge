//
//	Solution 8-1
//
#include <iostream>			
	
using namespace std;

#include "MyString.h"

int main()
{
	MyString stu1, stu2;
	
	cout << "enter two strings ";
	cin >> stu1 >> stu2;

	cout << "You entered " << stu1 << " and " << stu2 << endl;

	if ( stu1 == stu2 )
		cout << stu1 << " == " << stu2 << endl;

	return 0;
}


