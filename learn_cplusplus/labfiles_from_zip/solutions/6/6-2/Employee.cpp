//
//	From Solution 6-1
//
#include <iostream>

using namespace std;

#include "Employee.h"

Employee::Employee(MyString m, MyDate d)
: hiredate(d), name(m)
{
}

MyString Employee::getName() const
{
	return name;
}

MyDate Employee::getDate() const
{
	return hiredate;
}

void Employee::print() const
{
	hiredate.print();
	cout << name.getString() << endl;
}



