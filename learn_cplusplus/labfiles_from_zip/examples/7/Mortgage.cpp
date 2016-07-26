//
//      Mortgage.cpp
//
#include <iostream>
#include <math.h>

using namespace std;

#include "Mortgage.h"

Mortgage::Mortgage(string name, int years, double amt, double rate)
{
	setName(name);
	setYears(years);
	setAmount(amt);
	setRate(rate);
	payment = computePayment();
	balance = amt;
}

void Mortgage::makePayment()
{
	interest  = balance * (1.0/12) * (getRate()/100);
	principal = payment - interest;
	balance = balance - principal;  	
}

double Mortgage::getPayment()
{
	return payment;
}

double Mortgage::getBalance()
{
	return balance;
}

double Mortgage::getPrincipal()
{
		return principal;
}

double Mortgage::getInterest()
{
		return interest;
}

double Mortgage::computePayment()
{
	double j = getRate() / 1200;
	int n = getYears() * 12;
	payment = getAmount() * ( j / (1 - pow( (1 + j), -n) ) );
	cout << "Payment is " << payment << endl;
	return payment;
}


