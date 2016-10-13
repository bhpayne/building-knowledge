//
//	Solution 3-4
//
#include <iostream>
#include <string>
#include <stdlib.h>

using namespace std;

struct Pair
{
	string first;
	string second;
	bool   same;
	
	void setFirst(string p1)
	{
		first = p1;
	}
	
	void setSecond(string p1)
	{
		second = p1;
		same = false;
		if (first == second)
			same = true;
	}
	
	string getFirst()
	{
		return first;
	}
	
	string getSecond()
	{
		return second;
	}
	
	bool areTheSame()
	{
		return same;
	}
};


int main(int argc, char ** argv)
{
	if (argc != 3)
		exit(0);
		
    Pair aPair;
    
	aPair.setFirst(argv[1]);
	aPair.setSecond(argv[2]);
	
	cout << aPair.getFirst() << "\n";
	cout << aPair.getSecond() << "\n";
	
	if (aPair.areTheSame())
		cout << "are the same\n";
		
	return 0;
}

