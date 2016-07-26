//
//	9-7.cpp
//
#include <iostream>

using namespace std;

#include "Stack.cpp"

class Fraction
{
private:    
	int n, d;
	
public:
	Fraction(int a = 0, int b = 1) : n(a), d(b) {}
	
	friend ostream & operator<<(ostream & os, const Fraction & cfr)
	{
		os << cfr.n << "/" << cfr.d << endl;
		return os;
	}
};

int main( )
{
	//
	// Stack of int's
	//
	Stack <int> ints(100);
	int i;
	
	for ( i = 0; i < 5; i++)
	{	
		ints.push(i);
	}
	
	while( ! ints.isEmpty())
		cout << ints.pop() << endl;
		
	cout << endl;
	
	//
	// Stack of Fractions
	//
	Stack <Fraction> fractions(100);
	
	for ( i = 0; i < 5; i++)
	{	
		Fraction f(i, i+1);
		fractions.push(f);
	}
	
	while( ! fractions.isEmpty())
		cout << fractions.pop();
		
	cout << endl;
	
	//
	// Stack of string's
	//
	Stack <string> words(100);
	string aWord;
	
	cout << "Enter Words: ctrl-d to quit ";
	while ( cin >> aWord) 
	{
		words.push(aWord);
	}
	
	while( ! words.isEmpty())
		cout << words.pop() << endl;
	
	return 0;
}

