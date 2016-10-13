//
//	Starter code for Exercise 3-3
//
#include <iostream>

using namespace std;

struct Fraction 
{
	int numer;
	int denom;
	
	void print( )
	{
		cout << numer  << "/"  << denom;
	}
	
	void recip( ) 
	{
		int temp = numer;
		numer = denom;
		denom = temp;
	}
	
	Fraction mult(const Fraction & p)
	{
		Fraction temp;
		temp.numer = p.numer * numer;
		temp.denom = p.denom * denom;
		return temp;
	}
};



