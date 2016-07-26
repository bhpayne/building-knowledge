//
//	Solution 9-1
//
#include <iostream>

using namespace std;

template <class T>
T minimum(const T & v1, const T & v2)
{
	T temp =  v1 < v2 ? v1 : v2;
	return temp;
}

class Fraction
{
private:    
	int n, d;
	
public:
	Fraction(int a = 0, int b = 1) : n(a), d(b) {}
	
	friend bool operator<(const Fraction & f1, const Fraction & f2)
	{
		double fr1 = (double) f1.n/f1.d;
		double fr2 = (double) f2.n/f2.d;
		return fr1 < fr2;
	}
	
	friend ostream & operator<<(ostream & os, const Fraction & f)
	{
		os << f.n << "/" << f.d << endl;
		return os;
	}
};

int main()
{
	int x = 10, y = 15;
	cout << minimum(x,y) << endl;

	double a = 10.5, b = 25.6;
	cout << minimum(a,b) << endl;

	char let1 = 'a', let2 = 'b';
	cout << minimum(let1,let2) << endl;

	Fraction f1(2,3), f2(3,4);
	cout << minimum(f1, f2) << endl;

	return 0;
}


