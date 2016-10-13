//
//	Loan.h
//
#include <string>

using namespace std;

class Loan
{	
private:
	string name;
	double amount, rate;
	int years;

public:
	Loan(string, int, double,double);
	Loan(string, int, double);
	Loan(string, int);
	Loan();
	
	string getName(); 	
	double getAmount();
	int getYears(); 
	double getRate();
	
	void setName(string n);
	void setAmount(double  a);
	void setYears(int y);
	void setRate(double r); 
};

