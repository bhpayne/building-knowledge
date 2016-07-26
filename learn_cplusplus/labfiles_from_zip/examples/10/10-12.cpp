//
//	10-12.cpp
//
#include <iostream>
#include <string>
#include <map>

using namespace std;

int main()
{
	string name;
	double val;
	map <string, double, less<string> > accounts;
	
	while(1)
	{
		cout << "enter name ";
		cin >> name;
		if (name == "quit")
			break;
			
		cout << "enter amount ";
		cin >> val;
		accounts[name] = accounts[name] + val;
	}

	map<string,double,less<string> >::iterator i;

 	for(i = accounts.begin(); i != accounts.end(); i++)
 	{
		cout << (*i).first << " " << (*i).second; 
		cout << endl;
	}
	
	return 0;
}


