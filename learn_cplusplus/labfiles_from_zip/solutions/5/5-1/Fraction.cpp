//
//	Solution for Exercise 5-1
//
#include <iostream>

using namespace std;

#include "Fraction.h"

Fraction::Fraction(int n, int d)
{
	numer = n;
	denom = d;
}

void Fraction::recip()
{
	int temp;
	
	temp = numer;
	numer = denom;
	denom = temp;
}

void Fraction::print()
{
	cout << numer << "/" << denom << endl;
}

Fraction operator*(const Fraction & p1, const Fraction & p2)
{
	Fraction temp;
	
	temp.numer = p1.numer * p2.numer;
	temp.denom = p1.denom * p2.denom;
	return temp;
}

Fraction operator/(const Fraction & p1, const Fraction & p2)
{
	Fraction temp = p2;
	
	temp.recip();
	return temp * p1;
}

Fraction operator+(const Fraction & p1, const Fraction & p2)
{
	Fraction temp;
	temp.numer = p1.numer * p2.denom + p2.numer * p1.denom;
	temp.denom = p1.denom * p2.denom;
	return temp;
}

Fraction operator-(const Fraction & p1, const Fraction & p2)
{
	Fraction temp;
	temp.numer = p1.numer * p2.denom - p2.numer * p1.denom;
	temp.denom = p1.denom * p2.denom;
	return temp;
}
