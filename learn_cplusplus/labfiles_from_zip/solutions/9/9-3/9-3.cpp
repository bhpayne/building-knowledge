//
//	Solution 9-3
//
#include <iostream>
#include <string>
#include <cmath>
#include <cstring>
#include <cstdlib>

using namespace std;

class ArgsException
{
private:    
	string reason;
	
public:
	ArgsException(string s)
	{
		reason = s;
	}
	string getReason()
	{
		return reason;
	}
};

class NonIntegerException
{
private:    
	string data;
	int arg;
	
public:
	NonIntegerException(string s, int a)
	{
		data = s;
		arg = a;
	}
	int whichArg()
	{
		return arg;
	}
	string getBadData()
	{
		return data;
	}
};

void check(char * p, int whicharg)
{
	int i;
	for (i = 0; i < strlen(p); i++)
	{
		if (p[i] < '0' || p[i] > '9')
			throw NonIntegerException(p,whicharg);
	}
}

int main(int argc, char **argv)
{
	try {
		if ( argc != 3)
			throw ArgsException("arg count incorrect");
			
		check(argv[1], 1);
		check(argv[2], 2);
		
		int base = atoi(argv[1]);
		int expo = atoi(argv[2]);
		
		cout << pow( base, expo ) << endl;
	}
	catch(ArgsException ae)
	{
		cout << ae.getReason() << endl;
	}
	catch(NonIntegerException nie)
	{
		cout << " arg " << nie.whichArg()
		     << " (" << nie.getBadData()
		     << ") not numeric" << endl;
	}
	
	return 0;
}


