//
//      Loan.cpp
//
#include <string>

using namespace std;

#include "Loan.h"

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

