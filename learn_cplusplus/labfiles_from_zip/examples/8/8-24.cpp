//
//	8-24.cpp
//
#include <iostream>
#include <fstream>
#include <stdlib.h>

using namespace std;

class Fraction
{
private:    
	int n, d;
	
public:
	Fraction(int a, int b) : n(a), d(b) {}
	
	friend ostream & operator<<(ostream & os, const Fraction & cfr)
	{
		os << cfr.n << "/" << cfr.d << endl;
		return os;
	}
};

void writeit(Fraction & fr, fstream & stream)
{
	cout << "writing " << fr << endl;
	stream.write((char *) &fr, sizeof(Fraction));
}

int main()
{
	fstream f("ratios", ios::in | ios::out | ios::trunc);
	if ( ! f)  {
		cerr << "error opening ratios" << endl;
		exit(0);
	}
	
	Fraction x(2,3);
	Fraction y(3,4);
	Fraction z(5,6);
	
	writeit(x,f);
	writeit(y,f);
	writeit(z,f);
	
	f.seekg(0);
	for (int i = 0; i < 3; i++) {
		cout << "At pos " << f.tellg() << " "; 
		f.read((char *) &x, sizeof(Fraction));
		cout << x;
	}
	
	return 0;
}


