//
//	Solution 10-2
//
#include <iostream>
#include <vector>
#include <numeric>

using namespace std;

class Fraction
{
	int n,d;
		
public:
	Fraction(int a = 0, int b = 1) : n(a), d(b) {}
	
	void print() { cout << n << "/" << d << endl; }
	
	friend Fraction operator*(const Fraction & f1, const Fraction & f2);

};

Fraction operator*(const Fraction & f1, const Fraction & f2)
{
		Fraction t;
		
		t.n = f1.n * f2.n;
		t.d = f1.d * f2.d;
		
		return t;
}

template <class TYPE>
class mult 
{
public:
	mult() { cout << "mult constructor" << endl; }
	
	TYPE operator()(TYPE & a, TYPE & b)
	{
		TYPE x = a * b;
		return x;
	}
};

int main()
{
	int x[5] = {2, 3, 5, 7, 11};
	vector<int> v(x, x+5);
	int p = accumulate(v.begin(), v.end(), 1, mult<int>());
	cout << p << endl;

	double y[5] = {2.1, 3.5, 5.3, 7.2, 11.3};
	vector<double> r(y, y+5);
	double q = accumulate(r.begin(), r.end(), 1.0, mult<double>());
	cout << q << endl;

	Fraction z[3] = { Fraction(2,3), Fraction(4,3), Fraction(5,2) };
	vector <Fraction> f(z, z + 3);
	Fraction w = accumulate(f.begin(), f.end(), Fraction(1,1), mult<Fraction>());
	w.print();
	
	return 0;
}

