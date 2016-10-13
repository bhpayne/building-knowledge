//
//	10-10.cpp
//
#include <iostream>
#include <algorithm>
#include <list>

using namespace std;

list<char> makelist(const char* s)
{
	list<char> x;
	while (*s != '\0')
		x.push_back(*s++);
	return x;
}

int main()
{
	list<char> list1 = makelist("instructor");
	
	list<char>::iterator lsi = list1.begin();
	
	reverse(list1.begin(), list1.end());
	
	while(lsi != list1.end())
		cout << *lsi++ << endl;
		
	return 0;
}


