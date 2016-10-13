//
//      8-5.cpp
//
#include <iostream>

using namespace std;

class Fraction
{
private:    
	int n,d;
	
public:
	Fraction(int a, int b) : n(a), d(b) {}
	
	ostream & operator>>(ostream & os)
	{
		os << n << "/" << d << "\n";
		return os;
	}
};

int main()
{
	Fraction f(2,3);
	f >> cout << 2;
	return 0;
}

