//
//	3-31.cpp
//
#include <iostream>
#include <string>
using namespace std;
int main()
{
	string simple("must include");
	cout << simple << "\n"; 
	simple.append(" string");
	cout << simple << "\n";
	cout << simple.length() << "\n";
	cout << simple[0] << "\n";
	string phrase;
	phrase = simple;
	phrase.append(" to work. ");
	cout << simple << "\n";
	cout << phrase << "\n";
	return 0;
}


