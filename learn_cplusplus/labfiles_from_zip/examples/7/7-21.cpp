//
//	7-21.cpp
//
#include <iostream>

using namespace std;

class Loan
{
public:
	Loan()
	{
		cout << "Loan Constructor\n";
	}
	
	virtual int getID() { return 1; }
};

class Mortgage : public Loan
{
public:
	Mortgage()
	{
		cout << "Mortgage Constructor\n";
	}
	
	int getID() { return 2; }
};

class AdjustableRateMortgage : public Mortgage
{
public:
	AdjustableRateMortgage()
	{
		cout << "AdjustableRateMortgage Constructor\n";
	}
	
	int getID() { return 3; }
};

int main()
{
	Loan *ptr = new AdjustableRateMortgage;
	cout << "ID = " << ( ptr->getID() ) << endl;
	return 0;
}
		
