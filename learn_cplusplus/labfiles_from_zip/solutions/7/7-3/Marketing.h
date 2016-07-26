//
// Solution for Exercise 7-3
//

#ifndef MARKETING_H
#define MARKETING_H

#include "Employee.h"

class Marketing: public Employee
{
public:
	Marketing(string s);
	
	virtual double pay();
	virtual void vacation();
	virtual double pension();
	virtual void bonus();
};

#endif

