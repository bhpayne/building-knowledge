//
//	Mortgage.h
//
#ifndef MORTGAGE_H
#define MORTGAGE_H

#include <string>

using namespace std;

#include "Loan.h"

class Mortgage : public Loan
{	
private:
	double payment;
	double balance;
	double principal;
	double interest;
	double computePayment();
	
public:
	Mortgage(string name, int years, double amt, double rate);
	
	double getPayment();
	void makePayment();
	double getBalance();
	double getPrincipal();
	double getInterest();
};

#endif
