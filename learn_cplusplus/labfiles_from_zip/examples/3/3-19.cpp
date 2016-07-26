//
//	3-19.cpp
//
#include <iostream>
struct Fraction
{
	int n, d;

	Fraction mult(const Fraction & param)
	{
		Fraction temp;
		temp.n = param.n * n;
		temp.d = param.d * d;
		return temp;
	}
	void print()
	{
		std::cout << n << "/" << d << "\n";
	}
};
int main()
{
	Fraction a, b, c;
	a.n = 1;
	a.d = 3;
	b.n = 2;
	b.d = 5;
	c = a.mult(b);
	a.print();
	b.print();
	c.print();
	return 0;
}
