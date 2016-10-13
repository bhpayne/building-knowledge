//
//	Solution 3-3
//
#include <iostream>

using namespace std;

struct Fraction {
	int numer;
	int denom;
	
	void initialize(int a, int b)
	{
		numer = a;
		denom = b;
	}
	
	void print() {
		cout << numer << "/" << denom << endl;
	}
	
	void recip() {
		int temp;
		temp = numer;
		numer = denom;
		denom = temp;
	}

	
	Fraction add(const Fraction & x)
	{
		Fraction temp;
		temp.numer = numer * x.denom + denom * x.numer;
		temp.denom = denom * x.denom;
		return temp;
	}
	
	Fraction mult(const Fraction & p)
	{
		struct Fraction temp;
		temp.numer = p.numer * numer;
		temp.denom = p.denom * denom;
		return temp;
	}
	
	Fraction divide(const Fraction & x)
	{
		Fraction temp = x;
		temp.recip();
		Fraction temp2;
		temp2.numer = numer;
		temp2.denom = denom;
		return temp2.mult(temp);
	}
};

main()
{
	Fraction a, b, c;
	
	a.initialize(2,3);
	b.initialize(3,4);
	
	a.print();
	b.print();
	
	cout << "ADD\n";
	c = a.add(b);
	c.print();
	
	cout << "DIVIDE\n";
	c = a.divide(b);
	c.print();
	
	return 0;
}
