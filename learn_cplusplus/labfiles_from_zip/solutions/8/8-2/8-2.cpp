//
//	Solution 8-2
//
#include <iostream>
#include <fstream>
#include <cstring>
#include <cstdlib>

using namespace std;

int main()
{
	cout << "enter filename ";
	char fn[100];
	cin >> fn;

	ifstream in(fn);
	if ( ! in)
	{
		cerr << "can't open " << fn << endl;
		exit(1);
	}

	cout << "enter number ";
	int number;
	cin >> number;

	ofstream out("longer", ios::trunc);
	if ( ! out)
	{
		cerr << "can't open longer" << endl;
		exit(2);
	}
	
	char line[100];
	int ln = 1;
	
	while(in.getline(line, 100))
	{
		if ( strlen(line) > number ) {
			out << ln << "\t" << line << endl;
			cout << ln << "\t" << line << endl;
		}
		ln++;
	}
	
	return 0;
}


