//
//	Loan.h
//
#include <string>

using namespace std;

struct Loan
{	
private:
	string name;
	double amount, rate;
	int years;
	
public:
	string getName(); 	
	double getAmount();
	int getYears(); 
	double getRate();
	
	void setName(string n);
	void setAmount(double  a);
	void setYears(int y);
	void setRate(double r);
};

