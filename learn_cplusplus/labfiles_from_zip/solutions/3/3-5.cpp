//
//	Solution 3-5
//
#include <iostream>
#include <cmath>
#include <cstdlib>

using namespace std;
struct Mortgage
{
	double amount;
	double rate;
	int years;
	double payment;
	double balance;
	double principal;
	double interest;

	void setValues(int yrs, double amt, double intRate)
	{
		years = yrs;
		amount = balance = amt;
		rate = intRate;
		payment = computePayment();
		
	}
	double computePayment()
	{
		double j = rate / 1200;
		int n = years * 12;
		payment = amount * ( j / (1 - pow( (1 + j), -n) ) );
		return payment;
	}
	void makePayment()
	{	
		interest  = balance * (1.0/12) * (rate/100);
		principal = payment - interest;
		balance = balance - principal;  
	}
	double getBalance()
	{
		return balance;
	}
	double getInterest()
	{
		return interest;
	}
	double getPrincipal()
	{
		return principal;
	} 
	double getPayment()
	{
		return payment;
	}
};
int main()
{
	Mortgage m;
	m.setValues(30, 100000, 7.5);
	char line[10];
	cout << "enter months ";
	cin >> line;
	int months = atoi(line);
	double payment = m.getPayment();
	for (int i = 1; i <= months; i++)
	{
		m.makePayment();
		cout 	<< i << "\t"
			<< payment << "\t" 
			<< m.getPrincipal() << "\t"
			<< m.getInterest() << "\t"
			<< m.getBalance() << "\n";
	}
	return 0;
}

