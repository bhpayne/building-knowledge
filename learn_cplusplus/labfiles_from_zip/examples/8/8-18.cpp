//
//	8-18.cpp
//
#include <iostream>
#include <fstream>

using namespace std;

int main(int argc, char **argv)
{
	int i = 0;
	while( --argc > 0 )	{
		int ct = 0;
		ifstream input(argv[++i]);
		if ( ! input )  {
			cerr << "no such file: "<<argv[i] << endl;
			continue;
		}
		char ch;
		while(input.get(ch)) {
			if(ch == '\n')
				ct++;
		}
		input.close();
		cout << ct << " lines: " << argv[i] << endl;
	}
	
	return 0;
}
