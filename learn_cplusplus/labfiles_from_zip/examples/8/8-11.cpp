//
//	8-11.cpp
//
#include <iostream>
#include <iomanip>
#include <cstring>

using namespace std;

int main()
{	
	char line[10];

	while(true)
	{
		cin >> setw(10) >> line;
		
		if (strcmp(line, "quit") == 0 )
			break;
			
		cout << line << endl;
	}
	
	return 0;
}
 
