//
//	10-11.cpp
//		
#include <iostream>
#include <list>
#include <set>

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

list<char> makelist(const char* s) 
{
	list<char> x;
	while(*s != '\0')
		x.push_back(*s++);
		
	return x;
}

int	main()	
{
	list<char> list1 = makelist("C++ Course");
	set<char, less<char> > s;
	list<char>::iterator i;
	
	for (i = list1.begin(); i != list1.end(); ++i)
		 s.insert(*i);
		 
	list<char> list2;
	print("BEFORE:", list1);
	
	set<char, less<char> >::iterator k;
	
	for (k = s.begin(); k != s.end(); ++k)
		list2.push_back(*k);
		
	print("AFTER:", list2);

	return 0;
}


