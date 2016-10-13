//
//	10-18.cpp
//
#include <iostream>
#include <vector>
#include <numeric>

using namespace std;

class mult 
{
public:
	mult() { cout << "mult constructor" << endl; }
	
	int operator()(int a, int b)
	{
		int x = a * b;
		cout << "mult() " << x << endl;
		return x;
	}
};

int main()
{
	int x[5] = {2, 3, 5, 7, 11};
	vector<int> v(x, x + 5);
	
	int p = accumulate(v.begin(), v.end(), 1, mult());
	
	cout << p << endl;
	
	return 0;
}
