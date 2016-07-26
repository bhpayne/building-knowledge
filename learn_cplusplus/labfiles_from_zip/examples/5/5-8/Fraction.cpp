//
//	Fraction.cpp
//
#include <iostream>

using namespace std;

#include "Fraction.h"

Fraction::Fraction(int a, int b)
{
	numer = a;
	denom = b;
}

void Fraction::recip()
{
	int temp;
	temp = numer;
	numer = denom;
	denom = temp;
}

void Fraction::print( )
{
	cout << numer  << "/"  << denom << endl;
}

Fraction Fraction::operator*(const Fraction & p)
{
	Fraction temp;
	temp.numer = p.numer * numer;
	temp.denom = p.denom * denom;
	return temp;
}

Fraction Fraction::operator/(const Fraction & p)
{
	Fraction temp = p;
	temp.recip();
	return *this * temp;
}

Fraction Fraction::operator+(const Fraction & p)
{
	Fraction temp;
	temp.numer = p.numer * denom + p.denom * numer ;
	temp.denom = p.denom * denom;
	return temp;
}

Fraction Fraction::operator-(const Fraction & p)
{
	Fraction temp = p;
	temp.numer *= -1;
	return *this + temp;
}


