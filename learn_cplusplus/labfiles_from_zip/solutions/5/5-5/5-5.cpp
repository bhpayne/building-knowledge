//
//	Solution 5-5
//
#include <iostream>

using namespace std;

#include "MyString.h"

int main() 
{
	MyString empty;
	MyString text("hello");
	
	cout << "longest: " << MyString::getLongest() << endl;
	
	MyString pal("amanaplanacanalpanama");
	
	cout << "longest: " << MyString::getLongest() << endl;
	cout << "count is " << MyString::getCount() << endl;
	
	cout << text.getString() << " is ";
	cout << text.getLength() << " long " << endl;
	
	text.reverse();
	
	cout << "The reversed string is ";
	cout << text.getString() << endl;
	
	if ( pal.ispal()) {
		cout << pal.getString() << " is ";
		cout << "a palindrome " << endl;
	}

	text = pal;
	MyString another(text);
	
	return 0;
}
