//
//	Solution 4-3
//
#include <iostream>	

using namespace std;

#include "MyString.h"

int main() 
{
	MyString empty;
	MyString text("hello");
	MyString pal("amanaplanacanalpanama");
	
	cout << text.getString() << " is ";
	cout << text.getLength() << " long " << endl;
	
	text.reverse();
	cout << "The reversed string is ";
	cout << text.getString() << endl;
	
	if ( pal.ispal())
	{
		cout << pal.getString() << " is ";
		cout << "a palindrome " << endl;
	}
	
	return 0;
}
