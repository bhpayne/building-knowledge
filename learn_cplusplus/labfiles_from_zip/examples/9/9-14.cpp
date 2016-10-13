//
//	9-14.cpp
//
#include <iostream>
#include <string>
#include <sstream>

using namespace std;

class Fraction
{
private:    
	int n, d;
	
public:
	Fraction(int a = 0, int b = 1) : n(a), d(b) {}
	
	operator double() { return (double) n/d; }
	
	operator string()
	{
		ostringstream output;
		output << n << "/" << d;
		return output.str();
	}
};

int main()
{
	Fraction f(3,7);
	double d = f;
	cout << d << endl;
	
	string data("hello");
	data = (string) f;
	cout << data << endl;
	
	return 0;
}

