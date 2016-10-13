//
//      LoanFunctions.cpp
//
#include <string>

using namespace std;

#include "Loan.h"

Loan::Loan(string n, int yrs, double amt, double r)
{		
	name = n;
	years = yrs;
	amount = amt;
	rate = r;
}

Loan::Loan(string n, int yrs, double amt)
{
	name = n;
	years = yrs;
	amount = amt;
	rate = 7.5; 
}

Loan::Loan(string n, int yrs)
{	
	name = n;
	years = yrs;
	amount = 100000;
	rate = 7.5;
}

string Loan::getName()  
{ 
	return name; 
}

double Loan::getAmount()
{ 
	return amount; 
}

int Loan::getYears() 
{ 
	return years; 
}

double Loan::getRate() 
{ 
	return rate; 
}

void Loan::setName(string n)
{ 
	name = n;
}

void Loan::setAmount(double  a)
{ 
	amount = a; 
}

void Loan::setYears(int y)
{ 
	years = y;
}

void Loan::setRate(double r)
{
	rate = r; 
}

