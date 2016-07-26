//
//	7-14.cpp
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
	
	int getID() { return 1; }
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
	AdjustableRateMortgage arm;
	
	return 0;
}
		
