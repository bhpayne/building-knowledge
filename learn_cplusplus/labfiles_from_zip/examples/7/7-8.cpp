//
//	7-8.cpp
//
#include <iostream>

using namespace std;

#include "Loan.h"
#include "Mortgage.h"

int main()
{
	Mortgage m("mike", 30, 100000, 7.5);
	
	cout << "MONTH\tPAYMENT\tBALANCE" << endl;
	
	for (int i = 1; i <= 12; i++)
	{
		m.makePayment();
		cout << i	<< "\t" << m.getPayment()
					<< "\t" << m.getBalance()
					<< "\t" << m.getInterest()
					<< "\t" << m.getPrincipal() << endl;
	}
	
	return 0;
}
