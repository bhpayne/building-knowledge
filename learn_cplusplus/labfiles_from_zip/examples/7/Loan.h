//
//	Loan.h
//
#ifndef LOAN_H
#define LOAN_H

#include <iostream>
#include <string>

using namespace std;

class Loan
{	
private:
	string name;
	double amount, rate;
	int years;
	
public:
	Loan(string n, int yrs, double amt, double r);
	Loan(string n, int yrs, double amt);
	Loan(string n, int yrs);
	
        //
        //  Remove the comment marker for the default Loan constructor
        //  in order to compile any class that is derived from
        //  Loan and that does not use a member initialization list
	    
    //  Loan() { }
	
	string getName(); 	
	double getAmount();
	int getYears(); 
	double getRate();
	
	void setName(string n);
	void setAmount(double  a);
	void setYears(int y);
	void setRate(double r);
};

#endif

