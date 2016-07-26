//
//	10-15.cpp
//
#include <iostream>
#include <vector>
#include <list>
#include <numeric>

using namespace std;


int main()
{
    const int SIZE = 5;
    
	int x[SIZE] = {2, 3, 5, 7, 11};
	
	vector<int> V(&x[0], &x[SIZE]);
	int sum;
	sum = accumulate(V.begin(), V.end(), 0);
    cout << sum << endl;

	double y[SIZE] = {2.1, 3.1, 5.2, 7.2, 11.1 };
	
	list<double> l(&y[0], &y[SIZE]);
	double total;
	total = accumulate(l.begin(), l.end(), 0.0);
	cout << total << endl;

	cout << accumulate(x, x + SIZE, 0) << endl;

	list<int> ell(&x[0], &x[SIZE]);
	cout << accumulate(ell.begin(), ell.end(), 0.0) << endl;

	return 0;
}


