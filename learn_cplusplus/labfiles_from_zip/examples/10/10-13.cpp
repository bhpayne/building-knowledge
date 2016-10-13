//
//	10-13.cpp
//
#include <iostream>
#include <vector>
#include <list>
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
    const int SIZE = 6;
    
	int x[SIZE] = {2, 4, 6, 8, 10, 12};
	
	vector<int> v(&x[0], &x[SIZE]);
	print("VECTOR:", v);

	int y[SIZE] = {1, 3, 5, 7, 9, 11};
	
	list<int> l(&y[0], &y[SIZE]);
	print("LIST:", l);

	int val;
	while(1)
	{
		cout << "Enter a value (0 to exit) ";
		cin >> val;
		if ( val == 0 )
			break;
			
		vector<int>::iterator where;
		where = find(v.begin(), v.end(), val);
		if (where != v.end()) 
			cout << "found " << val << " in vector" << endl;
			
		list<int>::iterator place;
		place = find(l.begin(), l.end(), val);
		if (place != l.end())	
			cout << "found " << val << " in list" << endl;
	}
	
	return 0;
}


