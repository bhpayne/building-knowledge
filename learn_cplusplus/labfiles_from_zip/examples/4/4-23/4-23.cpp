//
//	4-23.cpp
//

#include <iostream>

using namespace std;

#include "Loan.h"

int main()
{
	Loan myLoan1("michael", 30, 100000, 8.0);
	cout << myLoan1.getName() << " ";
	cout << myLoan1.getAmount() << " ";
	cout << myLoan1.getRate() << " ";
	cout << myLoan1.getYears() << endl;

	Loan myLoan2("susan", 20, 75000);
	cout << myLoan2.getName() << " ";
	cout << myLoan2.getAmount() << " ";
	cout << myLoan2.getRate() << " ";
	cout << myLoan2.getYears() << endl;

	Loan myLoan3("erin", 10);
	cout << myLoan3.getName() << " ";
	cout << myLoan3.getAmount() << " ";
	cout << myLoan3.getRate() << " ";
	cout << myLoan3.getYears() << endl;

	Loan myLoan4;
	cout << myLoan4.getName() << " ";
	cout << myLoan4.getAmount() << " ";
	cout << myLoan4.getRate() << " ";
	cout << myLoan4.getYears() << endl;
	
	return 0;
}

