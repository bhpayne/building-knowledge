//
//	Solution 10-1
//
#include <iostream>
#include <vector>
#include <list>
#include <numeric>

using namespace std;

template <class TYPE1, class TYPE2>
int sum_of_n(TYPE1 & p1, TYPE2 & p2, int n)
{
	typename TYPE1::iterator last1 = p1.begin();
	typename TYPE2::iterator last2 = p2.begin();
	
	for (int i = 0; i < n; i++) {
		last1++;
		last2++;
	}
	
	int sum1 = accumulate(p1.begin(),last1,0);
	int sum2 = accumulate(p2.begin(),last2,0);
	
	cout << "( " << sum1 << " " << sum2 << " ) ";
	
	return sum1 == sum2;
}



int main()
{
    const int SIZE = 5;
    
	int x[SIZE] = {1,2,3,4,5};
	int y[SIZE] = {5,4,3,2,1};

	list <int> L(&x[0], &x[SIZE]);
	vector <int> V(&y[0], &y[SIZE]);

	cout << "First 5 elements of List and Vector have ";
	if (sum_of_n(V,L,5))
		cout << "same sum" << endl;
	else
		cout << "different sum" << endl;

	cout << "First 3 elements of List and Vector have ";
	if (sum_of_n(L,V,3))
		cout << "same sum" << endl;
	else
		cout << "different sum\n";

    return 0;		
}


