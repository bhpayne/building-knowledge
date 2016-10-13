//
//	4-40.cpp
//
#include <iostream>
#include <string>

using namespace std;

class ID
{
private:
	static int id;
	int number;
	string name;
	
public:
	ID(string val)
	{
		name = val;
		number = id++;
	}
	
	static int nextID()
	{
		return id;
	}
	
	int getID()
	{
		return number;
	}
	
	string getName()
	{
		return name;
	}
};

int ID::id = 1;

int main()
{
	ID employees[] = {ID("mike"), ID("sue"), ID("erin") };
	
	for (int i = 0; i < 3; i++)
	{
		cout << employees[i].getName() << ": ";
		cout << employees[i].getID() << endl;
	}
	cout << "next ID is: " << ID::nextID() << endl;
	
	return 0;
}
	
