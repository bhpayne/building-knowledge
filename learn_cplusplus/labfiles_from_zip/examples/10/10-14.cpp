//
//	10-14.cpp
//
#include <iostream>
#include <vector>
#include <list>
#include <deque>
#include <algorithm>

using namespace std;

template <class TYPE>
void print(const char * title, TYPE & data)
{
	cout << title << " " ;
	typename TYPE::iterator it = data.begin();
	for (; it != data.end(); it++)
		cout << *it << " ";
	cout << endl;
}

int main()
{
    const int SIZE1 = 3;
    const int SIZE2 = 3;
    
	int x[SIZE1] = {5, 6, 10};
	int y[SIZE2] = {5, 7, 9};
	
	vector<int> result(SIZE1 + SIZE2);
	vector<int> v(&x[0], &x[SIZE1]);
	
	print("VECTOR: ", v);
	
	list<int> l(&y[0], &y[SIZE2]);
	print("LIST: ", l);
	
	merge(v.begin(), v.end(), l.begin(), l.end(), result.begin());
	print("VECTOR", result);

	return 0;
}
