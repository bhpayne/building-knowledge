//
//	8-6.cpp
//
#include <iostream>

using namespace std;

class Fraction
{
private:    
	int n,d;
	
public:
	Fraction(int a, int b) : n(a), d(b) {}
	
    friend ostream & operator<<(ostream & os, const Fraction & cfr);
};

ostream & operator<<(ostream & os, const Fraction & cfr )
{
        os << cfr.n << "/" << cfr.d << "\n";
        return os;
}

int main()
{
	Fraction f(2,3);
	cout << "fraction is " << f << "\n";
	return 0;
}

