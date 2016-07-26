//
//	8-14.cpp
//
#include <iostream>
#include <limits.h>

using namespace std;

int getAnInt();

int main()
{
	int x;
	x = getAnInt();
	cout << "processing " << x << endl;
	
	return 0;
}

int getAnInt()
{
	int value;
	
	cout << "enter an int: " << flush;
	while(1)
	{
		cin >> value;
		if(cin.good()) {
			cin.ignore(INT_MAX,'\n');
			break;
		}
		cin.clear();
		cin.ignore(INT_MAX,'\n');
		cout << "again: " << flush;
	}
	return value;
}
