//
//	Solution 6-1
//

#ifndef EMPLOYEE_H
#define EMPLOYEE_H

#include "MyDate.h"
#include "MyString.h"

class Employee
{
private:    
	MyDate hiredate;
	MyString name;
	
public:
	Employee(MyString m, MyDate d);
	MyString getName() const;
	MyDate getDate() const;
	void print() const;
};

#endif
