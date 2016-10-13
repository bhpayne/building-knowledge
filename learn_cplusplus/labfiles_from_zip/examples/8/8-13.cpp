//
//	8-13.cpp
//
#include <iostream>
#include <iomanip>

using namespace std;

int main()
{
	char c[10];
	
	while( cin >> c && ! cin.eof() ) 
	{
		cout << c << endl;
	}
	cout << "end of program" << endl;
	
	return 0;
}
