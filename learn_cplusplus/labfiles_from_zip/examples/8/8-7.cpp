//
//	8-7.cpp
//
#include <iostream>
#include <cstring>
#include <cstdlib>

using namespace std;

class Fraction
{
private:    
	int n,d;
	
public:
	Fraction(int a, int b) : n(a), d(b) {}
	
	friend ostream & operator<<(ostream & os, const Fraction & f )
	{
		os << f.n << "/" << f.d << endl;
		return os;
	}
	
	friend istream & operator>>(istream & is, Fraction & f )
	{
		char line[100];
		
		is >> line;
        int i;
        for (i = 0; i < strlen(line); i++)
        {
			if (line[i] == '/')
				break;
        }
		line[i] = '\0';
		
		f.n = atoi(line);
		f.d = atoi(line + i + 1);
		
		return is;
	}
};

int main()
{
	Fraction f(2,3);
	cout << "Enter a fraction (n/d): ";
	cin >> f;
	cout << "You entered " << f;
	return 0;
}


