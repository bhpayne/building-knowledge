//
//	8-21.cpp
//
#include <iostream>
#include <fstream>
#include <stdlib.h>

using namespace std;

int main( )
{
	fstream alpha("letters", ios::in | ios::out | ios::trunc);
	if( ! alpha )
	{
		cerr << "error opening 'letters'" << endl;
		exit(1);
	}
	
    char digit;
    for ( digit = '0'; digit <= '9'; digit++)
		alpha << digit;
		
	cout << "AT POSITION: " << alpha.tellg() << endl;
	
	alpha.seekg(0);
	cout << "AT POSITION: " << alpha.tellg() << endl;
	
	for ( int x = 0; x < 10; x++)
	{
		alpha.get(digit);
		cout << digit;
	}
	cout << endl;
	
	cout << "AT POSITION: " << alpha.tellg() << endl;
	return 0;
}
