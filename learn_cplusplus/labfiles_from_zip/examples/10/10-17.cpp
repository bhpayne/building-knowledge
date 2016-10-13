//
//      10-17.cpp
//
#include <iostream>
#include <vector>
#include <list>
#include <numeric>

using namespace std;

int mult(int x, int y)
{
	return x * y; 
}

int main()
{
	int x[5] = {2, 3, 5, 7, 11};
	int p;
	
	vector<int> v(x, x + 5);
	p  = accumulate(v.begin(), v.end(), 1, mult);
	cout << p << endl;
	
	list<int> l(x, x + 5);
	p = accumulate(l.begin(), l.end(), 2, mult);
	cout << p << endl;
	
	return 0;
}


