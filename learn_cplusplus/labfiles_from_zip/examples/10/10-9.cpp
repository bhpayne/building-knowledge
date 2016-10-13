//
//	10-9.cpp
//
#include <iostream>
#include <algorithm>
#include <vector>

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

vector<char> vec(const char* s)
{
	vector<char> x;
	while (*s != '\0')
		 x.push_back(*s++);
	return x;
}

int main()
{
	vector<char> v = vec("Advanced C++");
	
	reverse(v.begin( ), v.end());
	
	print("VECTOR:", v);
	
	return 0;
}
