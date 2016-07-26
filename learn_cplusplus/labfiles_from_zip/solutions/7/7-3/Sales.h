//
// Solution for Exercise 7-3
//

#ifndef SALES_H
#define SALES_H

#include "Employee.h"

class Sales : public Employee
{
public:
	Sales(string s);
	
	virtual double pay();
	virtual void vacation();
	virtual double pension();
	virtual void bonus();
};

#endif

