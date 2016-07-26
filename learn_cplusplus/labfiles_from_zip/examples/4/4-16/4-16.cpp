//
//	4-16.cpp
//
#include <iostream>

using namespace std;

#include "Loan.h"

void displayLoan(Loan & loan);

int main()
{
	Loan myLoan;
	
	myLoan.setName("michael");
	myLoan.setYears(30);
	myLoan.setAmount(100000);
	myLoan.setRate(8);
	
	displayLoan(myLoan);
	
	return 0;
}

void displayLoan(Loan & loan)
{
	cout << loan.getName() << " ";
	cout << loan.getAmount() << " ";
	cout << loan.getRate() << " ";
	cout << loan.getYears() << endl;
}

