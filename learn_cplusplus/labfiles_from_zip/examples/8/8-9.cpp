//
//	8-9.cpp
//
#include <iostream>
#include <iomanip>

using namespace std;

int main()
{
	for (int i = 1; i < 20; i += 2)
	{
		cout << setw(5) << setfill('0')
		     << i << " " << setw(5)
		     << i * i << endl;
	}
	
	return 0;
}

